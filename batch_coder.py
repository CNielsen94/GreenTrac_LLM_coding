import os
import sys
import json
import time
import re
import argparse
from pathlib import Path
from typing import Dict, Any, Optional, List
import concurrent.futures

# --- Third-party libraries ---
try:
    import google.generativeai as genai
    from google.api_core.exceptions import ResourceExhausted
    from tenacity import retry, stop_after_attempt, wait_exponential
    from dotenv import load_dotenv
    from tqdm import tqdm
except ImportError as e:
    print(f"Error: A required library is missing. {e}")
    print("Please install all required libraries from requirements.txt (including tqdm):")
    print("pip install -r requirements.txt")
    sys.exit(1)

# --- CONFIGURATION ---
MODEL_NAME = "gemini-2.5-pro"
PROMPTS_DIR = Path("prompts")
INPUT_DIR = Path("inputs/markdown")
OUTPUT_DIR = Path("results")
MAX_PARALLEL_WORKERS = 10 # Tune this value (e.g., 5-15) to balance speed and API rate limits

# --- UTILITY FUNCTIONS ---
def deep_merge(dict1: Dict, dict2: Dict) -> Dict:
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            dict1[key] = deep_merge(dict1[key], value)
        else:
            dict1[key] = value
    return dict1

def extract_json_from_response(response_text: str) -> Optional[Dict[str, Any]]:
    if not response_text:
        return None
    match = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", response_text)
    if not match:
        match = re.search(r"(\{[\s\S]*?\})", response_text)
    if match:
        json_string = match.group(1)
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return None
    return None

# --- API CALL & WORKER LOGIC ---

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=2, max=60),
    retry=lambda retry_state: isinstance(retry_state.outcome.exception(), ResourceExhausted),
    before_sleep=lambda retry_state: print(
        f"\nAPI rate limit hit for a worker. Retrying in {retry_state.next_action.sleep:.2f}s..."
    )
)
def call_gemini_with_retry(model_client: genai.GenerativeModel, prompt: str) -> str:
    response = model_client.generate_content(prompt)
    try:
        return response.text
    except ValueError:
        if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
             # Log that a specific call was blocked, but don't crash.
            print(f"\nWarning: API call blocked for safety reason: {response.prompt_feedback.block_reason}")
        return ""

def process_single_document_prompt(doc_path: Path, prompt_path: Path, model_client: genai.GenerativeModel) -> Optional[Dict]:
    """
    Worker function: processes one document against one prompt.
    This is the target for our parallel execution.
    """
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt_template = f.read()
        with open(doc_path, 'r', encoding='utf-8') as f:
            document_text = f.read()
            
        final_prompt = prompt_template.replace("{{DOCUMENT_TEXT}}", document_text)
        response_text = call_gemini_with_retry(model_client, final_prompt)
        return extract_json_from_response(response_text)
    except Exception as e:
        print(f"\nError processing {doc_path.name} with {prompt_path.name}: {e}")
        return None

def find_all_prompts(start_dir: Path) -> List[Path]:
    """Recursively finds all .txt prompt files in a directory, sorted."""
    prompt_files = []
    for entry in sorted(start_dir.iterdir()):
        if entry.is_dir():
            prompt_files.extend(find_all_prompts(entry))
        elif entry.is_file() and entry.suffix == '.txt':
            prompt_files.append(entry)
    return prompt_files

# --- MAIN EXECUTION ---

def main():
    parser = argparse.ArgumentParser(description="A parallel CLI for the Qualitative Coding Pipeline.")
    parser.add_argument(
        "-f", "--file", 
        type=str, 
        default=None, 
        help="Process a single specific markdown file from the input directory."
    )
    parser.add_argument(
        "--run-first-prompt",
        action="store_true",
        help="Only run the very first prompt (e.g., 01_submission_metadata.txt) for a quick test."
    )
    args = parser.parse_args()

    # --- Load API Key and Configure Gemini ---
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ FATAL ERROR: GOOGLE_API_KEY not found.")
        sys.exit(1)
        
    try:
        genai.configure(api_key=api_key)
        model_client = genai.GenerativeModel(MODEL_NAME)
        print(f"✅ Successfully configured Gemini with model: {MODEL_NAME}")
    except Exception as e:
        print(f"❌ FATAL ERROR: Failed to configure Google Gemini AI: {e}")
        sys.exit(1)

    # --- Verify directories and find files ---
    if not PROMPTS_DIR.is_dir() or not INPUT_DIR.is_dir():
        print(f"❌ FATAL ERROR: Ensure '{PROMPTS_DIR}' and '{INPUT_DIR}' directories exist.")
        sys.exit(1)
    OUTPUT_DIR.mkdir(exist_ok=True)

    markdown_files = []
    if args.file:
        target_file = INPUT_DIR / args.file
        if not target_file.is_file():
            print(f"❌ FATAL ERROR: Specified file '{args.file}' not found in '{INPUT_DIR}'.")
            sys.exit(1)
        markdown_files.append(target_file)
    else:
        markdown_files = sorted(list(INPUT_DIR.glob('*.md')))
        
    if not markdown_files:
        print(f"🤷 No markdown files found to process.")
        return

    # --- Find all prompts ---
    all_prompt_files = find_all_prompts(PROMPTS_DIR)
    if args.run_first_prompt:
        print("🚀 --run-first-prompt flag detected. Processing only the first prompt.")
        all_prompt_files = all_prompt_files[:1]

    print(f"✅ Found {len(markdown_files)} document(s) and {len(all_prompt_files)} prompt(s) to process.")
    
    # --- Main Processing Loop (Prompt by Prompt) ---
    all_results = {doc.stem: {} for doc in markdown_files}
    start_time = time.time()

    for prompt_path in all_prompt_files:
        relative_prompt_path = prompt_path.relative_to(PROMPTS_DIR)
        print(f"\nProcessing prompt: {relative_prompt_path}")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_PARALLEL_WORKERS) as executor:
            future_to_doc = {
                executor.submit(process_single_document_prompt, doc_path, prompt_path, model_client): doc_path
                for doc_path in markdown_files
            }
            
            progress = tqdm(concurrent.futures.as_completed(future_to_doc), total=len(markdown_files), desc="Documents")
            for future in progress:
                doc_path = future_to_doc[future]
                try:
                    result = future.result()
                    if result:
                        doc_stem = doc_path.stem
                        
                        path_parts = relative_prompt_path.parts
                        current_level = all_results[doc_stem]
                        
                        # --- 🐞 THE FIX IS HERE 🐞 ---
                        # The original code used path_parts[:-1], which created the redundant nesting.
                        # By using path_parts[:-2], we build the path only to the parent directory,
                        # allowing deep_merge to correctly place the LLM's dictionary.
                        path_to_build = path_parts[:-2] if len(path_parts) > 1 else []
                        
                        for part in path_to_build:
                            part_key = part.lstrip("0123456789_")
                            current_level = current_level.setdefault(part_key, {})
                        
                        deep_merge(current_level, result)
                        
                except Exception as exc:
                    print(f"\n{doc_path.name} generated an exception: {exc}")

    total_duration = time.time() - start_time
    print(f"\n{'='*60}\n✅ All processing complete in {total_duration:.2f} seconds.\n{'='*60}")
    
    # --- Save all results ---
    for doc_stem, data in all_results.items():
        output_filename = f"{doc_stem}_coded.json"
        results_path = OUTPUT_DIR / output_filename
        with open(results_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"📄 Final results for '{doc_stem}' saved to: {results_path}")
# 📝 Disagreement Analysis
This report was generated using Gemin-2.5-pro. The model was provided the following:
1. **Code name:** (for example Objectives - End plastic pollution) and it's subcodes (```mentioned with timeframe```, ```mentioned, no timeframe``` and ```not mentioned```
2. **Code prompt:** The specific prompt provided to the coding system for the given code. These prompts contain the individual code definitions used.
3. **'Golden' definition:** The original codebook definition for the given code (this one is currently only applied to the C9 codes, but will be applied to the rest later)
4. **Disagreement instances:** All instances of disagreement from disagreement_report.md for the respective code.

## 1. High-Level Overview
This report summarizes the root-cause analysis of disagreements between an LLM's qualitative coding and an expert human's "golden standard." The analysis reveals a clear and consistent meta-pattern: the primary driver of disagreement is not a failure of the LLM to follow instructions, but rather a fundamental mismatch between the simplified, literal prompts given to the LLM and the complex, nuanced, and context-dependent cognitive model of the human expert.

In almost every case, the LLM performed its given task with high fidelity. However, the tasks themselves were often flawed hypotheses about the expert's true coding process. The disagreements, therefore, are not failures but invaluable data points that successfully reverse-engineer the expert's unstated rules. The overwhelming primary culprit is Prompt Ambiguity, not in the sense of unclear wording, but in the prompt's failure to accurately model the expert's sophisticated logic.

#### 2. **Key Themes of Disagreement & Primary Failure Patterns**

The analysis revealed three dominant themes of prompt failure, each leading to systematic disagreements.

#### **Theme 1: The "Substance" Filter (Keyword Mention vs. Substantive Proposal)**

The most common failure pattern occurred when the LLM was prompted to find any mention of a concept, while the expert was only coding for substantive, concrete policy proposals. The LLM correctly found keywords, but lacked the instruction to evaluate the author's intent.

Core Issue: Prompts instructed the LLM to perform simple keyword detection, while the expert was performing nuanced proposal evaluation.

Prime Examples:

Ban & Moratorium: The LLM correctly found the word "ban" in a document arguing against it (Japan) and "moratoriums" in a general list of options (HAC). The expert correctly excluded these because they were not concrete proposals for a ban or moratorium.

Mandatory action plan: The LLM correctly found the phrase "national action plans" within a pre-written template question (Tonga) or in a hypothetical statement (Kuwait). The expert correctly ignored these as they were not substantive, country-authored proposals.

##### **Theme 2: The "Mutual Exclusivity" Filter (Conceptual Conflation & Codebook Architecture)**

This was the most critical and insightful failure pattern. The expert operates within a highly structured, hierarchical codebook where categories are mutually exclusive. The LLM, given a series of flat, isolated prompts, was unable to respect these boundaries, leading to systematic miscategorization.

Core Issue: Prompts for general codes were so broad that they conceptually overlapped with other, more specific codes in the system, violating the principle of mutual exclusivity.

Prime Examples:

Knowledge sharing (Parent vs. Child): The expert's definition revealed that this is a parent category with specific child codes like "technology transfer" and "capacity building." The LLM was incorrectly prompted to code for the parent category, causing it to flag any mention of a child category, which the expert correctly assigned to the more specific code.

Economic Instruments (Tax incentive, Subsidy, Penalty): The LLM was given overly broad prompts for each, causing it to conflate them. It coded "fees" and "levies" under Tax incentive when the expert assigned them to Penalty, and it coded general "financial assistance" under Subsidy when the expert reserved that code for specific market-altering instruments.

Information and guidance: This prompt was so broad it became a "catch-all," causing the LLM to incorrectly code concepts that belonged in more specific categories like Harmonization, Expert group, and Education programs.

##### **Theme 3: The "Level of Abstraction" Filter (General Concept vs. Formal Mechanism)**

This pattern occurred when the expert was looking for a specific, high-level, formal mechanism, while the prompt instructed the LLM to find any general mention of the related low-level concept.

Core Issue: A mismatch in the required level of abstraction between the prompt and the expert's true definition.

Prime Examples:

Performance standard: The expert's definition included formal frameworks like "ESM" and "BAT." The LLM, prompted to find any "requirement," flagged general goals like "products must be recyclable" (Kuwait), which did not meet the expert's high-level, formal-framework standard.

Harmonization: The expert's example referenced the formal "Harmonized System" for trade. The LLM, prompted to find any effort to "align" or "make consistent," flagged general statements like "we should align our plans," which the expert correctly excluded.

Just transition: The expert's definition was titled "Legal recognition – just transition," indicating a search for formal legal mechanisms. The LLM, prompted to find general "social impact," incorrectly flagged social support programs that lacked this legalistic core.

3. Unified Recommendation for Prompt Engineering
The consistent theme is that simple, keyword-based prompts are insufficient for replicating expert-level qualitative analysis. The path to alignment requires re-engineering the prompts to mirror the expert's cognitive process, making their tacit, unwritten knowledge explicit.

Prioritize a Structured, Mutually Exclusive Codebook: The entire system of prompts must be designed with an "awareness" of the other codes. For hierarchical structures (like Knowledge sharing), prompts for parent categories must be written as residual categories, explicitly instructing the LLM to first check for a fit in a more specific child category.

Incorporate Contextual Filters and Negative Constraints: Prompts must move beyond simple "look for X" instructions. They need to be framed as multi-step, conditional logic:

Add a "Substance" Filter: "Code as 'Mentioned' ONLY IF the text makes a substantive proposal for a new measure..."

Add Negative Constraints: "You MUST NOT code for..." This is the most powerful tool for enforcing mutual exclusivity and preventing conceptual bleed. For example, the Information and guidance prompt must explicitly exclude concepts belonging to Harmonization or Expert group.

Match the Level of Abstraction: Analyze the golden standard's examples to determine the correct level of abstraction. If the expert is looking for formal, named systems (like "ESM"), the prompt must instruct the LLM to prioritize those and ignore general, aspirational statements.

#### **(Objectives - End plastic pollution)**

##### **Analysis for Code: Objectives - End plastic pollution**

1. Prompt/Instruction Analysis

The original code prompt is clear, specific, and well-structured. It provides an explicit list of keywords (e.g., "ending, eliminating, addressing, tackling, combating, preventing, or stopping") to define what constitutes a "mention." It also gives a clear, unambiguous definition for what qualifies as a "timeframe." The instructions leave little room for subjective interpretation and are designed for precise application.

2. Disagreement Pattern Analysis

A stark and consistent pattern emerged across all disagreements. The LLM meticulously followed the prompt's broad definition, correctly identifying instances where terms like "addressing plastic pollution" (e.g., Argentina, China) or "combating plastic pollution" (e.g., Gabon, Bangladesh) were used. It then accurately determined whether a specific timeframe was present or absent.

Conversely, the human coder (NVIVO) appears to have operated under a much narrower, unstated definition, systematically failing to code for the broader terms explicitly listed in the prompt. The human code seems to only register very direct phrases like "end plastic pollution." This results in two major patterns:

The LLM correctly codes "Mentioned, no time frame" (C) for dozens of countries, while the human coder incorrectly codes "Not mentioned" (D).

The LLM correctly codes "Mentioned with time frame" (B) when a date is present (e.g., Cook Islands, Switzerland), while the human coder either misses the timeframe or misses the mention entirely.

3. Primary Culprit Determination

Primary Culprit: Potential Human Coder Error

4. Detailed Rationale

The evidence overwhelmingly suggests that the LLM adhered to the provided instructions more faithfully than the human coder. The "gold standard" data appears to be inconsistent with the codebook (the prompt). For example, in the cases of Argentina, Bahrain, China, and nearly twenty others, the LLM correctly identified phrases like "addressing plastic pollution" and "tackling plastic pollution" — which are explicitly included in the prompt's definition — and coded "Mentioned, no time frame." The human coder marked these as "Not mentioned," directly contradicting the instructions. Furthermore, for countries like the Cook Islands and Switzerland, the LLM correctly identified both the mention of the objective and the specific "by 2040" timeframe, while the human coder failed to capture this. The LLM's reasoning and citations are consistently sound and directly support its decisions based on a literal interpretation of the prompt, indicating the human coding, not the LLM's logic, is the source of the disagreement.

5. Recommendation for Improvement

The prompt itself is effective and does not need significant changes. The primary issue lies in the alignment between the human-coded "gold standard" and the codebook.

Recommendation: The human-coded data should be audited and re-coded with strict adherence to the existing prompt's definitions. The coder must be instructed to apply the full list of keywords ("addressing," "tackling," etc.) provided in the mentioned definition. This will create a more reliable and consistent evaluation dataset for future LLM performance assessment. If the intent was for a narrower definition, the prompt must be revised to reflect that by removing the broader synonyms.

#### **(Objectives - Reduce production)**

##### **Analysis for Code: Objectives - Reduce production**

1. Prompt/Instruction Analysis

The prompt is very clear and effective. It successfully establishes a two-tiered coding system: first, identifying any mention of reducing production (mentioned), and second, determining if that mention includes a specific, quantitative target (specification_provided). The inclusion of keywords and the explicit instruction to differentiate production reduction from waste reduction provide strong guidance and minimize ambiguity.

2. Disagreement Pattern Analysis

The disagreements show a highly consistent and systematic pattern.

General Mentions: In the vast majority of cases (e.g., Australia, Canada, Japan, United Kingdom), the LLM correctly identifies general statements like "restrain the production," "eliminate or restrict... products," or "keep plastic production within sustainable levels." It correctly codes these as "Mentioned, no specification" (G). The human coder, however, appears to have missed these mentions entirely, leading to a large number of incorrect "Not mentioned" (H) codes.

Specific Mentions: When a specific, quantifiable target is present, the LLM correctly identifies it. For instance, in Nepal (ban on production of bags < 40 microns), Monaco (footnote mentioning a 3% annual decrease), and Azerbaijan ("almost zero level"), the LLM correctly codes "Mentioned with specification" (F). The human coder missed these specifications.

In short, the LLM consistently outperforms the human coder in both identifying relevant text and correctly applying the distinction between a general mention and a specific one, based on a strict interpretation of the prompt.

3. Primary Culprit Determination

Primary Culprit: Potential Human Coder Error

4. Detailed Rationale

The evidence strongly indicates that the human coder did not consistently apply the definitions provided in the prompt. The LLM, by contrast, followed the instructions with high fidelity. For dozens of countries, the LLM correctly identified mentions of controlling or reducing production and coded them as "Mentioned, no specification," while the human gold standard incorrectly coded them as "Not mentioned." The case of Australia, where the LLM cited "Restrain the production of unnecessary primary plastics," is a perfect example of this pattern. Furthermore, the LLM demonstrated a superior ability to detect specific quantitative targets, as seen in the Monaco case, where it correctly extracted a "3 percent annually" decrease from a footnote—a detail the human coder missed. The LLM's reasoning and citations are consistently robust and directly aligned with the prompt, making the human coding the clear source of the discrepancies.

5. Recommendation for Improvement

The prompt is well-designed and does not require major changes. The core issue is the quality and consistency of the human-coded "gold standard" data.

Recommendation: The human-coded dataset should be audited against the codebook provided in the prompt. The human coder should be instructed to re-evaluate the documents, paying close attention to the full list of keywords for "mentioned" and the strict definition of a quantitative "specification." This will ensure the gold standard accurately reflects the coding instructions and provides a reliable benchmark for evaluating the LLM. A minor clarification could be added to the prompt to specify whether statements rejecting the objective (as seen in the Russia example) should be included or excluded, for example: "Look for statements proposing or supporting the reduction of plastic production..."

#### **(Objectives - Benefits of plastic)**

[ ] J : Mentioned

[ ] K : Not mentioned

##### **Analysis for Code: Objectives - Benefits of plastic**

1. Prompt/Instruction Analysis

The prompt provided to the LLM defines this code with broad and inclusive criteria. It specifically directs the model to look for both explicit "positive contributions" and implicit "acknowledgments of... utility, or necessity," such as references to "essential uses." This is a reasonable and clearly articulated definition. However, given that the human coder may have been working from a more refined or narrower codebook, this very breadth is a likely source of systematic disagreement if the human's instructions were more restrictive.

2. Disagreement Pattern Analysis

The analysis reveals a pattern of complete and systematic disagreement between the two coding outputs. For every instance, the LLM identified evidence that matched its broad instructions, while the human coder did not. The LLM consistently captured both explicit statements (e.g., EU: "plastic plays an important role") and logical, implicit acknowledgements (e.g., Canada: focusing on "unnecessary" plastics implies some are "necessary"). This suggests the LLM correctly followed its instructions, and the human coder likely followed a different, more restrictive set of instructions that defined this code more narrowly, leading to the divergent results.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is not within the text of the LLM's prompt itself, but in its application for a comparative analysis against a human using a different, more refined codebook. The core issue is a definitional mismatch between the two sets of instructions.)

4. Detailed Rationale

The primary reason for the disagreement appears to be a definitional mismatch between the prompt given to the LLM and the refined codebook used by the human analyst. The LLM's prompt encouraged a broad interpretation, leading it to correctly identify implicit acknowledgements of plastic's utility. For example, it interpreted phrases like "necessary plastic products" (Tunisia) or the need for "specific exemptions" (Cook Islands) as valid instances, which is a reasonable application of its instructions. The human coder's results, showing zero instances, suggest their codebook contained a much stricter definition, possibly requiring a direct and explicit statement of a specific benefit while excluding the implicit acknowledgements the LLM was instructed to find. Therefore, the disagreement is not the result of an error by either the LLM or the human, but rather a systemic issue stemming from the two operating under different rule sets.

5. Recommendation for Improvement

To ensure meaningful comparison and improve inter-rater reliability between the LLM and human coders, their instructions must be precisely aligned.

Recommendation: For future evaluations, the LLM's prompt should be updated to perfectly mirror the nuances and specific criteria present in the refined human codebook. For this specific code, the prompt could be revised to specify whether only explicit statements of benefits should be included and provide clear inclusion/exclusion criteria for implicit acknowledgements. This alignment is critical for generating comparable data and accurately assessing the LLM's performance against the established human standard.

#### **(objectives - Protect human health)**

[ ] M : Mentioned

[ ] N : Not mentioned

##### **Analysis for Code: objectives - Protect human health**

1. Prompt/Instruction Analysis

The prompt instructs the LLM to code for any mention of "preserving, protecting, safeguarding, or addressing risks to human health." While clear on its own, its effectiveness must be judged by its ability to replicate the golden standard. The results indicate that the golden standard employs a much more specific, unstated rule that this "refined" prompt fails to capture. The prompt's definition is demonstrably too broad and does not contain the necessary nuance or exclusion criteria used by the human expert.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, which reveals a fundamental flaw in the prompt's logic. The LLM, correctly following its instructions, consistently found direct mentions of "human health" or "public health" and coded "Mentioned." The golden standard, however, is consistently "Not mentioned." This shows that the refined prompt, despite iterative tuning, is still causing the LLM to systematically identify text that the golden standard deems irrelevant for this code. The disagreement isn't random; it's a predictable error generated by a faulty prompt.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: In this context, "ambiguity" means the prompt is an inaccurate or incomplete model of the golden standard's complex logic, leading the LLM to misapply the code according to the true, unwritten rules.)

4. Detailed Rationale

The core issue is that the "refined" prompt is not yet an accurate operationalization of the golden standard. The prompt's simple instruction to find any mention of "human health" is a poor fit for the expert's nuanced task. For example, the golden standard might require that protecting human health be stated as a primary, formal objective of the proposed treaty, not just as a background concern or justification.

The LLM, following its faulty (i.e., overly simplistic) instructions, correctly flags documents like Palestine's ("protect the public health") and Ghana's ("health catastrophe"). However, the golden standard shows these do not meet the higher, more specific threshold required for a positive code. The prompt is the culprit because it lacks the crucial context and exclusion criteria needed for the LLM to replicate the expert's judgment. It is telling the LLM to catch small fish when the expert is only looking for whales.

5. Recommendation for Improvement

The prompt needs to be further refined to integrate the implicit logic of the golden standard. The goal is to make the human expert's tacit knowledge explicit for the LLM.

Recommendation:

Analyze the False Positives: Use the instances the LLM incorrectly coded (e.g., Armenia, Ghana, Palestine) as a training set. Work with the human expert to understand why these direct mentions do not qualify.

Extract the Core Logic: The expert's logic is likely more complex, such as "Only code if health is mentioned in the official 'Objectives' section of the document," or "Only code if a specific health-protection mechanism is proposed."

Rewrite the Prompt with Explicit Constraints: Revise the prompt to include this logic. For example:

"Code as 'Mentioned' ONLY IF protecting human health is listed as a formal, numbered, or bulleted objective of the proposed instrument. Do NOT code if it is only mentioned as a general impact, a justification in the preamble, or a background concern."

This more constrained prompt has a much higher chance of successfully replicating the golden standard.

#### **(Objectives - Protect biodiversity)**

[ ] P : Mentioned

[ ] Q : Not mentioned

##### Analysis for Code: Objectives - Protect biodiversity

1. Prompt/Instruction Analysis

The prompt given to the LLM defines the code with very broad and inclusive criteria. It instructs the model to look for the term "biodiversity" but also for wide-ranging proxies like "ecosystem protection," "protecting wildlife," or even vague "similar environmental preservation goals." The subsequent disagreements demonstrate that this broad definition is a poor model of the golden standard, which operates under much more specific and restrictive criteria that the prompt fails to specify.

2. Disagreement Pattern Analysis

The analysis reveals a pattern of total disagreement, indicating the prompt is fundamentally misaligned with the golden standard. The LLM, correctly following its overly broad instructions, identified a mention in every case. It correctly flagged documents that explicitly mention "biodiversity" (Ghana, Bangladesh) and strong proxies like protecting "animal health" (Burkina Faso).

Since the golden standard is "Not mentioned" for all of these instances—including those with a direct keyword match—it proves that the expert's coding rule is far more nuanced than the one provided to the LLM. The prompt is causing the LLM to make systematic errors relative to the ground truth.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here refers to the prompt's failure to accurately model and specify the complex, nuanced rules of the golden standard, thereby giving the LLM an incomplete and misleading set of instructions for the task.)

4. Detailed Rationale

The root cause of the disagreement is that the "refined" prompt is not a valid representation of the expert coder's logic. The prompt's wide net (instructing the LLM to code for general "environmental preservation goals") is in direct conflict with the expert's much narrower approach.

The most telling evidence is the case of Bangladesh, where the text explicitly mentions minimizing adverse impacts on "biodiversity." The LLM, following its prompt, correctly coded this. However, the golden standard is "Not mentioned." This proves that the expert's true rule is not a simple keyword search. The rule is likely more sophisticated, perhaps requiring that "biodiversity protection" be listed as a standalone, primary, and formal objective of the treaty, not just mentioned as an impacted area. The current prompt lacks this crucial situational context, making it impossible for the LLM to replicate the expert's result.

5. Recommendation for Improvement

The prompt must be significantly revised to encode the tacit knowledge and specific rules of the human expert. The goal is to move from a broad, keyword-based instruction to a narrow, context-aware one.

Recommendation:

Deduce the Expert's Rule: Analyze the "false positives" (like Bangladesh and Ghana) to determine why the expert excluded them. The rule is likely contextual (e.g., "must be in a formal list of objectives") rather than semantic.

Rewrite the Prompt with High Specificity: The new prompt must incorporate this contextual rule. It should explicitly tell the LLM what not to code. For example:

"Look for the explicit term 'biodiversity' or 'wildlife conservation'. Code as 'Mentioned' ONLY IF it is listed as a formal, numbered, or bulleted objective of the proposed instrument. You MUST NOT code if the term is mentioned as part of a general discussion of environmental impacts, justifications, or in the preamble."

This revised, more constrained prompt would stand a much better chance of aligning with the golden standard.

#### **(Objectives - Lifecycle approach)**

[ ] S : Mentioned

[ ] T : Not mentioned

[ ] U : Partial mention

##### Analysis for Code: Objectives - Lifecycle approach

1. Prompt/Instruction Analysis

The prompt instructs the LLM to perform what is essentially a keyword search for "lifecycle" and its synonyms, and then to classify the coverage. The instruction is simple and direct. However, the consistent disagreement with the golden standard reveals that this simplicity is its core flaw. The prompt lacks the necessary conditional logic to distinguish between a superficial mention of the term and a substantive, detailed application of the lifecycle concept, a distinction the human expert clearly makes.

2. Disagreement Pattern Analysis

A very clear and telling pattern emerges from the disagreements: the LLM consistently identifies the presence of the phrase "full life cycle," while the human expert assesses the substance of the argument.

Many of the LLM's "false positives" (Azerbaijan, Bahrain, Nigeria, Russia, etc.) occur because it flags a boilerplate question from the submission template that all countries were responding to. The LLM correctly finds the phrase "full life cycle" in the question, but the golden standard indicates that simply including the question without providing a substantive answer does not count.

In other cases (China, Bosnia and Herzegovina), the LLM identifies a discussion of the lifecycle, but the expert coder has deemed it "Not mentioned" or "Partial." This suggests the expert is applying a higher standard, likely requiring that the document not only mention the concept but also detail binding obligations across all stages (upstream, midstream, and downstream) to qualify as a full mention.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity lies in the prompt's failure to model the expert's nuanced, multi-step logic. It gives a simple instruction for a complex task, leading the LLM to predictable and systematic errors.)

4. Detailed Rationale

The core problem is that the prompt is an inaccurate hypothesis of the expert's true coding process. The expert isn't just asking, "Is the word 'lifecycle' here?" They are asking, "Does this document, in its own unique text, commit to a comprehensive and detailed set of policies that cover the entire plastic lifecycle?" The prompt completely fails to capture this sophisticated, two-part logic.

This is most evident in the numerous cases where the LLM flags the boilerplate question. For example, in Azerbaijan's submission, the LLM cites the template question containing "full life cycle," and the expert correctly codes this as only a "Partial mention," because the country did not substantively elaborate on the concept in its own response. The LLM's prompt lacks the instruction to differentiate between template text and the respondent's original contribution. The current prompt is setting the LLM up for failure by giving it an overly simplistic rule for a nuanced task.

5. Recommendation for Improvement

The prompt needs to be fundamentally re-engineered to incorporate the expert's multi-step, conditional logic. It must move beyond keyword detection to substantive analysis.

Recommendation:
Rewrite the prompt to include a chain of instructions that mirrors the expert's decision-making process. This could be structured as follows:

Initial Search: "First, search for the explicit phrases 'life cycle,' 'lifecycle,' or 'cradle-to-grave'."

Boilerplate Check: "Crucially, you must verify if the found text is part of a pre-written template question. If it is, and the country's unique response does not elaborate further on the lifecycle concept, code as 'Partial mention'."

Substance Check: "If the phrase appears in the country's original text, you must then verify that the surrounding text provides specific details or obligations for all three stages: upstream (production/design), midstream (use/consumption), and downstream (waste management/disposal). If all three stages are substantively addressed, code as 'Mentioned.' If only one or two stages are detailed, code as 'Partial mention'."

By making the expert's tacit knowledge explicit in this way, the prompt will guide the LLM to replicate the golden standard with much higher accuracy.

#### **(Value chain)**

[ ] AD : 1. Upstream

[ ] AG : 2. Midstream

[ ] AO : 3. Downstream

[ ] AS : 4. Cross value chain

##### Analysis for Code: Value chain

1. Prompt/Instruction Analysis

The core strategy here was to deconstruct a single, complex conceptual code ("Value chain") into a series of discrete, granular sub-codes (feedstock, production, design, etc.), each with its own simple prompt. The hypothesis was that by having the LLM execute these simple tasks, the aggregated results would replicate the expert's holistic judgment.

The disagreement data shows this hypothesis to be fundamentally flawed. The strategy has created two distinct, systematic problems:

Over-sensitivity (False Positives): For the Upstream, Midstream, and Downstream categories, the simple, context-free prompts caused the LLM to flag any passing mention of a concept, a task it performed well but which did not align with the expert's need for substantive policy proposals.

Conceptual Blind Spots (False Negatives): For the Cross-value chain category, the breakdown was incomplete. The LLM was only prompted on two sub-topics, while the expert's golden standard clearly includes several others, leading the LLM to miss the majority of relevant information.

2. Disagreement Pattern Analysis

Two clear, opposing patterns of error emerged:

Pattern 1: Over-coding in Upstream, Midstream, and Downstream
The LLM consistently identified mentions of value chain stages that the golden standard ignores. A deep dive into the LLM's justifications (e.g., AOSIS, Argentina, Canada) shows it was correctly following its simple instructions to find any text related to "feedstock," "production," or "design." However, the expert coder is clearly operating on a higher-level principle: a simple mention is not enough to warrant a code. The golden standard requires the document to propose a substantive core obligation or a specific control measure related to that stage. The LLM's prompts lack this critical requirement for substance, leading it to flag many low-value mentions.

Pattern 2: Under-coding in Cross-value chain
The LLM failed to identify any instances of this code, while the golden standard has a high count. This is a catastrophic failure of the prompting architecture. The LLM was only prompted to look for "emissions" and "microplastic leakage." The expert's definition of "Cross-value chain" is demonstrably broader, likely including concepts like financing mechanisms, Extended Producer Responsibility (EPR), public awareness campaigns, and technology transfer—topics the LLM was never asked to look for. It couldn't find what it wasn't told to find.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is architectural. The strategy of breaking a holistic concept into a series of isolated, simple prompts is an inaccurate model of the expert's integrated reasoning process. The failure is not in any single prompt's wording but in the overall design.)

4. Detailed Rationale

The core issue is a definitional and structural mismatch between the LLM's task and the expert's task. The expert applies a single, complex lens, asking, "Does this document propose meaningful interventions at any stage of the value chain?" The LLM, by contrast, was forced to apply a dozen simple, disconnected lenses, asking, "Is the word 'design' here? Is the word 'feedstock' here?"

This architectural flaw explains both error patterns. For Upstream/Midstream/Downstream, the LLM flags any mention of a stage because its prompts lack the crucial qualifier of "substantive policy proposal." For "Cross value chain," the LLM finds nothing because the prompt architecture failed to provide it with a complete list of relevant sub-topics. The prompts are a flawed and incomplete map of the expert's mental model, making it impossible for the LLM to successfully navigate the task.

5. Recommendation for Improvement

The entire prompting architecture for this code needs to be rethought. The attempt to simplify the task by breaking it down has stripped it of the necessary context and complexity.

Recommendation:
The granular, multi-prompt approach for this code should be abandoned. It has proven to be an ineffective model of the expert's task. Instead, it should be replaced with a single, holistic prompt that more closely mirrors the expert's cognitive process.

A more effective prompt would:

Provide All Definitions at Once: Give the LLM the definitions for all value chain stages (Upstream, Midstream, Downstream, and a complete list for Cross-value chain) in a single context window.

Introduce a Rule of Substance: The core instruction must be elevated from simple detection to substantive evaluation. For example:

"Your task is to identify which stages of the plastic value chain are addressed with substantive policy proposals, core obligations, or specific control measures. A simple passing mention of a stage (e.g., 'we must consider the full lifecycle, from production to waste') is not sufficient. The document must propose a concrete action for that stage. Based on this rule, analyze the document and list all stages for which such substantive measures are proposed."

This single, more sophisticated prompt would empower the LLM to perform a level of analysis much closer to the golden standard, moving beyond keyword matching to genuine conceptual evaluation.

## C9 - Types of measure


### [ ] AX : Economic

#### [ ] AY : Deposit systems

##### Analysis for Code: C9 - Deposit systems

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT provided to the LLM and the GOLDEN_DEFINITION are very closely aligned. Both define the code as a system where a consumer receives a refund for returning an item, using near-identical language ("deposit-return schemes," "refund of a deposit upon return"). The LLM's prompt is slightly more descriptive with examples like "bottle bills," but it does not conflict with the golden standard. The prompt, therefore, appears to be an accurate and effective model of the explicit rules in the golden codebook.

2. Disagreement Pattern Analysis

Unlike previous examples, this code shows two distinct and opposing patterns of disagreement:

LLM False Positives: In a majority of cases (Monaco, Palau, Philippines, Switzerland), the LLM correctly identified explicit text like "deposit return schemes" or "Container Deposit Law." The golden standard, however, coded these as "Not mentioned." In another case (Nigeria), the LLM made a reasonable semantic inference, equating a "buy-back model" with a deposit system, which the golden standard did not accept.

LLM False Negatives: In two instances (Oman, Sierra Leone), the LLM failed to find any mention, while the golden standard correctly identified that the measure was present.

This dual-error pattern suggests that this code, despite its simple definition, is surprisingly difficult to apply with perfect consistency for both the LLM and the human expert.

3. Primary Culprit Determination

Primary Culprit: Inherent Subjectivity / Grey Area

(Note: This is chosen because errors are present on both sides. However, the analysis reveals that the most significant and frequent disagreements stem from apparent inconsistencies in the golden standard, leaning the problem towards Potential Human Coder Error.)

4. Detailed Rationale

The complexity of this case stems from two separate issues. First, the LLM made a logical leap in the Nigeria case, assuming a "buy-back model" is functionally identical to a deposit system. The golden standard's stricter interpretation is reasonable, as a buy-back model might not involve an initial deposit. This highlights a subtle grey area that the prompt's definition doesn't resolve.

Second, and more significantly, there are several cases (Monaco, Palau, Philippines) where the LLM correctly identified explicit, undeniable keywords like "deposit return schemes," yet the golden standard is marked as "Not mentioned." These instances appear to be clear inconsistencies or errors in the golden standard data. While the LLM also has clear misses (Oman, Sierra Leone), the fact that the human-coded ground truth contains multiple apparent errors on straightforward cases is the most impactful source of disagreement. The combination of these factors indicates a task with hidden complexities and potential inconsistencies in the benchmark data itself.

5. Recommendation for Improvement

Because errors are present in both the LLM's output and the golden standard, a two-pronged approach is necessary to improve alignment.

Recommendation:

Audit and Clarify the Golden Standard: The primary action should be to review the golden standard for consistency. The instances where explicit mentions of "deposit return schemes" were coded as "Not mentioned" need to be audited. This process will either correct errors in the benchmark data or reveal a highly specific, unstated rule (e.g., "the scheme must be described as already implemented, not just proposed") that must then be explicitly added to the codebook.

Refine the Prompt for Edge Cases: To address the LLM's errors, the prompt should be updated based on the audit's findings.

To fix the false positive in the Nigeria case, the prompt should explicitly state whether semantic equivalents like "buy-back model" should be included or excluded.

To fix the false negatives in Oman and Sierra Leone, the texts from those documents should be analyzed to understand what keywords or concepts the LLM missed, and those terms should be added to the prompt's definition.

#### [ ] AZ : Penalty
##### Analysis for Code: C9 - Penalty

1. Prompt/Instruction Analysis

At first glance, the ORIGINAL_CODE_PROMPT given to the LLM and the GOLDEN_DEFINITION appear to be well-aligned. Both are broad and include key terms like "polluter-pays schemes" and other punitive financial measures. The LLM's prompt is actually more detailed, explicitly listing "taxes" and "fees."

However, the subsequent 100% disagreement rate proves that this surface-level similarity is misleading. The GOLDEN_DEFINITION, despite its simple wording, is clearly being applied by the human expert with a crucial, unstated contextual rule that the LLM's prompt completely fails to capture. The prompt, while textually similar, is an inaccurate and incomplete model of the expert's actual application of the code.

2. Disagreement Pattern Analysis

The pattern is one of total, systematic disagreement, with the LLM producing a high volume of false positives. In every single instance, the LLM correctly identified text that matched the literal definition in its prompt. For example, it found explicit mentions of:

"penalties" and "Polluter Pay schemes" (Palau)

"Plastic Taxes" and "polluter pays principle" (Nigeria)

"Punitive measures" and "levies and taxes" (Papa New Guinea)

The golden standard, however, is "Not mentioned" in all these cases. This is not a random error; it is a predictable failure caused by the prompt's lack of a critical piece of contextual logic. The LLM is perfectly executing a flawed instruction.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is not in the prompt's wording itself, which is clear, but in its failure to model the expert's sophisticated, context-dependent application of the golden standard. It is missing a crucial "if/then" condition.)

4. Detailed Rationale

The core of the disagreement lies in a sophisticated distinction the expert is making that the prompt does not account for: the difference between (a) national-level economic instruments used as domestic policy and (b) international punitive measures for a country's failure to comply with the treaty itself.

The LLM's prompt, which includes broad terms like "taxes" and "fees," instructs it to find any mention of the former. The expert, however, appears to be coding exclusively for the latter. The submission from Palau is the most damning evidence: the text explicitly calls for the treaty to have "defined... penalties." The LLM correctly identifies this. The expert's "Not mentioned" code strongly implies that their true definition of a penalty is a formal, detailed compliance mechanism within the treaty, not just a call for one. Similarly, the China submission explicitly states the international compliance mechanism should be "non-punitive," highlighting that this distinction is present in the source texts themselves, and the expert is correctly keying into it. The LLM's prompt is simply not equipped to understand this crucial context.

5. Recommendation for Improvement

The prompt must be re-engineered to explicitly teach the LLM the expert's nuanced distinction. It needs to move from a simple keyword search to a context-aware evaluation.

Recommendation:
The current prompt should be discarded and replaced with a more constrained, conditional one that makes the expert's tacit knowledge explicit.

Example of a Revised Prompt:

"Your task is to identify if the document proposes punitive measures for non-compliance with the international treaty itself.

Code as 'Mentioned' ONLY IF the text describes a formal mechanism with penalties, fines, or sanctions that would apply to a Party for failing to meet its obligations under the legally binding instrument.

You MUST NOT code for general proposals of national-level economic instruments, such as domestic taxes, levies, fees, or polluter-pays schemes, which are listed as policy options for countries to implement themselves."

This revised prompt forces the LLM to perform the same sophisticated contextual analysis as the human expert, dramatically increasing the likelihood of alignment with the golden standard.

#### [ ] BA : Public procurement

##### Analysis for Code: C9 - Public procurement

1. Prompt/Instruction Analysis

This is a classic case of a definitional mismatch between the LLM's instructions and the expert's true goal.

The ORIGINAL_CODE_PROMPT is literal and mechanistic. It instructs the LLM to look for the tool: "government or public sector purchasing requirements."

The GOLDEN_DEFINITION is conceptual and purpose-driven. It defines the code by its goal: "Measures that propose creating a market for new technology and practice."

The LLM's prompt is a flawed simplification. It mistakenly assumes that any mention of the tool ("public procurement") automatically implies the specific goal the expert is looking for ("market creation").

2. Disagreement Pattern Analysis

The single disagreement instance powerfully illustrates the flaw in the prompt's logic. The LLM, correctly following its literal instructions, identified the exact phrase "public procurement" in the EU's submission and coded "Mentioned."

The expert coder, applying their conceptual rule, correctly identified that this phrase, while present, was not used in a context that explicitly proposed "creating a market for new technology." The mention was generic. This shows that the prompt is systematically generating false positives by failing to check for the required purpose or context.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is not in the prompt's wording, which is clear, but in its status as an inaccurate and incomplete model of the expert's conceptual rule. It focuses on the 'how' instead of the required 'why'.)

4. Detailed Rationale

The root cause of this disagreement is that the prompt trained the LLM to find a specific tool, while the expert is looking for a specific job to be done. The EU's submission mentions the tool ("public procurement") but does not explicitly state it will be used for the expert's required job ("creating a market for new technology").

The LLM's coding is a perfect execution of a faulty instruction. The golden standard's Not mentioned code is also perfectly correct according to its more sophisticated, purpose-driven rule. The failure lies entirely in the prompt's oversimplified definition, which lacks the essential conceptual nuance of the golden standard. It is a classic example of confusing the method with the objective.

5. Recommendation for Improvement

The prompt must be re-engineered to teach the LLM the expert's conceptual rule, moving it from simple keyword detection to purpose-driven analysis.

Recommendation:
The prompt should be rewritten to prioritize the goal over the mechanism. The definition from the golden standard should be the core of the instruction.

Example of a Revised Prompt:

"Your task is to identify measures that aim to create a market for new, sustainable technologies or practices by using government purchasing power.

Code as 'Mentioned' if the text explicitly links public purchasing policies to this goal. Look for phrases like 'green public procurement,' 'preferential purchasing for innovative products,' or 'using procurement to foster a market for alternatives.'

You MUST NOT code a general mention of 'public procurement' on its own unless it is clearly and directly connected to the purpose of market creation for new technologies."

This revised prompt forces the LLM to look for the same conceptual connection as the expert, which will dramatically improve its alignment with the golden standard.

#### [ ] BB : R&D funding

##### Analysis for Code: C9 - R&D funding

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION are, on a literal level, almost identical. Both define the code as "funding" or "investment" in research and development. The example in the golden definition ("Increase investment in new materials...") is a perfect match for the kinds of phrases the LLM was instructed to find.

However, the disagreement data reveals that this textual similarity is deceptive. The expert is applying a powerful, unstated contextual filter that is completely absent from both the written golden definition and the LLM's prompt. The prompt, while appearing accurate, is a critically incomplete model because it lacks this essential piece of the expert's logic.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, with the LLM registering a 100% false positive rate across 38 instances. The LLM systematically and correctly identified explicit keywords and phrases that match its instructions, such as:

"Invest in research and innovation" (African Group)

"Support research on safe plastic alternatives" (Australia)

"mobilize... financial resources to support relevant research, development, and innovation (R&D&I) projects" (Uruguay)

The fact that the golden standard is "Not mentioned" for every single one of these direct hits proves that the expert's rule is not based on keywords alone. The LLM is flawlessly executing a prompt that is fundamentally misaligned with the expert's true task.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is not in the clarity of the prompt's language but in its failure to specify the crucial context in which a mention must appear to be considered valid according to the golden standard.)

4. Detailed Rationale

The core of the disagreement lies in the expert's sophisticated distinction between a binding core obligation and a supporting or voluntary measure. The expert appears to be coding exclusively for instances where R&D funding is proposed as a direct, mandatory action within the treaty's core framework.

The LLM, by contrast, was given a context-free instruction to find any mention of R&D funding anywhere in the document. As a result, it correctly flagged dozens of instances where R&D funding was mentioned as part of "Means of Implementation" (Uruguay), "Scientific & technical cooperation" (Armenia), or as a "voluntary approach" (China). The expert correctly identifies these as conceptually different from a core obligation and therefore does not apply the code.

The prompt is the culprit because it fails to provide the LLM with this essential piece of situational knowledge. It asks the LLM to identify what is mentioned, while the expert is evaluating both what is mentioned and how it is framed within the proposed policy structure.

5. Recommendation for Improvement

The prompt must be re-engineered to teach the LLM the expert's contextual rule. The goal is to move the LLM's task from simple keyword detection to a more nuanced, policy-aware classification.

Recommendation:
The current prompt should be replaced with a more constrained one that explicitly encodes the expert's logic. This can be achieved by adding a clear, negative constraint.

Example of a Revised Prompt:

"Your task is to identify if the document proposes R&D funding as a direct, binding core obligation.

Code as 'Mentioned' ONLY IF the text describes a mandatory requirement for Parties to fund or invest in research and development.

You MUST NOT code if R&D funding is mentioned only in the context of:

Supporting activities like 'Means of Implementation.'

General 'Scientific and Technical Cooperation.'

'Voluntary' or 'optional' measures for countries to consider.

Potential uses for a separate financial mechanism."

This revised prompt forces the LLM to perform the same contextual filtering as the expert, which is the critical step needed to align its output with the golden standard.

#### [ ] BC : Subsidy

##### Analysis for Code: C9 - Subsidy

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION are, on the surface, almost identical. Both use broad, inclusive language, listing terms like "subsidies," "grants," "reward systems," and "financial incentives." Crucially, the example provided in the GOLDEN_DEFINITION ("removal of... subsidies") is also explicitly covered in the LLM's prompt.

Based on the text alone, the prompt appears to be an excellent and faithful model of the golden standard's written rules. However, the subsequent 100% disagreement rate proves that the expert's application of the rule is governed by a powerful, unstated context that is completely missing from both the written definition and the LLM's instructions.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, resulting in a 100% false positive rate for the LLM across 44 instances. The LLM systematically and correctly identified explicit keywords from its prompt that were also present in the golden definition. For instance, it correctly flagged:

The exact keyword "subsidies" (or its removal) in Ecuador, HAC, Libya, Monaco, Norway, and Peru.

Explicit mentions of "grants" in the African Group and Nigeria.

Widespread mentions of "financial incentives" and "financial support."

The golden standard, however, is "Not mentioned" in every single case. This includes instances that are a perfect match for the GOLDEN_DEFINITION's own text and its provided example. This proves conclusively that the disagreement is not random but is the result of a fundamental, conceptual mismatch between the prompt and the expert's actual coding practice.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is not in the prompt's wording but in its profound failure to model the expert's unwritten, context-dependent rules. It is an accurate reflection of an inaccurate definition.)

4. Detailed Rationale

The core of the disagreement lies in a critical, high-level distinction the expert is making that is invisible to the LLM. The expert is conceptually separating (a) general financial mechanisms for implementation (like funding for developing countries) from (b) specific economic instruments designed to alter domestic market behavior.

The LLM's prompt, with its broad inclusion of "financial support" and "grants," instructs it to capture all instances of (a). The expert, however, appears to be coding those under a different conceptual category (e.g., "Means of Implementation") and is reserving the "Subsidy" code exclusively for instances of (b).

The most powerful evidence for this is the Ecuador submission. The text calls for the "removal of... subsidies that support the expansion of plastics production"—a perfect, verbatim match for the example in the GOLDEN_DEFINITION. The fact that the expert coded this as "Not mentioned" is definitive proof that a hidden rule is at play. The expert's true definition is not what is written; it is something far more specific and contextual. The prompt, by mirroring the flawed written definition, has perfectly engineered the LLM's failure.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's sophisticated, conceptual distinction. This requires adding explicit negative constraints to filter out the types of financial support that the expert codes elsewhere.

Recommendation:
The current prompt should be entirely replaced. The new prompt must operationalize the expert's distinction between general financial aid and a specific market-altering instrument.

Example of a Revised Prompt:

"Your task is to identify if the document proposes specific subsidies, grants, or reward systems as a direct economic instrument to alter domestic market behavior.

Code as 'Mentioned' ONLY IF the text describes a specific program, such as grants for recycling facilities or incentives for using biodegradable alternatives. The removal of subsidies on fossil fuels also qualifies.

You MUST NOT code for general financial mechanisms related to the treaty's implementation. Explicitly exclude:

General 'financial assistance,' 'financial support,' or 'financial resources' for developing countries.

Funding for 'capacity-building' or 'technology transfer.'

The creation of general multilateral or trust funds."

This revised, context-aware prompt has a much higher probability of replicating the expert's nuanced judgment and aligning with the golden standard.

#### [ ] BD : Tax incentive
##### Analysis for Code: C9 - Tax incentive

1. Prompt/Instruction Analysis

This case reveals a critical flaw in the ORIGINAL_CODE_PROMPT's design. The prompt given to the LLM is exceptionally broad, instructing it to look for "any tax-related measures" and "similar fiscal measures." This encourages the LLM to group various economic tools under one umbrella.

In stark contrast, the GOLDEN_DEFINITION, while short, is far more specific in its application. The example ("taxes... for consumption reduction") and the disagreements that follow demonstrate that the expert is applying a very narrow definition, looking only for measures explicitly and literally labeled as a "tax." The LLM's prompt is a flawed hypothesis because its broadness fundamentally misrepresents the expert's highly specific and compartmentalized mental model.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, with the LLM producing a 100% false positive rate. The LLM, correctly following its overly broad instructions, identified a wide range of terms that it was told to consider "similar fiscal measures." For example, it flagged:

General "fiscal measures" (Burkina Faso, Guinea)

"Incentives" and "disincentives" (Kuwait, Uganda)

The "elimination of subsidies" (Cook Islands, Rwanda)

"Charges and levies" (Moldova)

The golden standard, however, is "Not mentioned" in all these cases. This proves that the expert is making a sharp conceptual distinction between a direct "tax" and these other economic instruments, which they likely code under different categories (like "Penalty" or "Subsidy"). The LLM's prompt is causing it to conflate these distinct concepts.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is that the prompt's definition is far too general and fails to model the expert's narrow, specific, and unwritten rule for what constitutes a "Tax incentive" versus other, separate fiscal measures.)

4. Detailed Rationale

The root cause of the disagreement is that the expert's codebook is highly structured, with separate, mutually exclusive codes for "Tax," "Subsidy," and "Penalty." The LLM's prompt for "Tax incentive" is so broad that it bleeds into these other categories, instructing the LLM to code things that the expert would classify elsewhere.

For instance, in the Cook Islands submission, the LLM flagged the "eliminate subsidies" text. While this is a fiscal measure, the expert likely reserves this for the "Subsidy" code. Similarly, in the Moldova case, the LLM flagged "charges and levies," which the expert likely codes under "Penalty." The expert's true definition for this specific code is not "any fiscal measure" but "only a tax." The prompt is the culprit because it fails to provide this crucial negative constraint, leading the LLM to systematically miscategorize the data according to the expert's more granular framework.

5. Recommendation for Improvement

The prompt must be significantly constrained to align with the expert's narrow and specific application of this code. The goal is to teach the LLM to isolate "taxes" from all other fiscal measures.

Recommendation:
The prompt should be rewritten to be highly specific and include explicit exclusions.

Example of a Revised Prompt:

"Your task is to identify measures that explicitly involve a tax.

Code as 'Mentioned' ONLY IF the text uses the specific word 'tax,' 'taxes,' 'taxation,' 'tariff,' or 'duty.' This can include measures like a 'virgin plastic tax,' 'tax on single-use items,' or 'tax breaks' for certain behaviors.

You MUST NOT code for other, more general fiscal terms, even if they are related. Explicitly exclude:

General terms like 'fiscal measures.'

'Incentives' or 'disincentives.'

'Levies,' 'fees,' or 'charges.'

The 'removal of subsidies.'"

This revised prompt forces the LLM to adhere to the expert's narrow, compartmentalized definition, preventing it from conflating distinct economic instruments and dramatically increasing the likelihood of alignment.

#### [ ] BE : Trading system
##### Analysis for Code: C9 - Trading system

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT provided to the LLM is demonstrably flawed because it is conceptually over-broad. It conflates several distinct economic tools by instructing the LLM to look for "emissions trading, plastic credits, tariffs, cap-and-trade systems, or similar trading mechanisms." While these are all market-based instruments, the expert's coding scheme, as revealed by the disagreements, treats them as separate categories.

The GOLDEN_DEFINITION is also broad in its text ("Any measure on the economic side of plastic trade, such as tariffs"), but its application by the expert is clearly much narrower. The prompt's failure is that it takes the broad text at face value and does not account for the expert's highly compartmentalized application of the rules.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, resulting in a 100% false positive rate for the LLM. This systemic failure stems directly from the prompt's flawed, overly broad definition. The LLM, correctly following its instructions, flagged a wide variety of fiscal measures that the expert clearly categorizes elsewhere:

Correctly Identified Keywords: The LLM found explicit mentions of "tariffs" (Ecuador, HAC, Monaco, Peru) and "plastic credits" (Cambodia, Indonesia), which are perfect matches for the prompt.

Conflation with Other Codes: The LLM also coded mentions of "taxes" and "levies" (China, Micronesia), which the expert likely places under the "Tax incentive" or "Penalty" codes.

Broad Interpretation: The LLM flagged general terms like "market-based instruments" (Australia), which the expert does not consider specific enough for this code.

The most telling piece of evidence is the Palestine submission. The GOLDEN_DEFINITION uses Palestine's mention of a "tariff" as the canonical example for this code. However, in the actual disagreement data, the expert's golden standard for Palestine is "Not mentioned." This contradiction strongly suggests either an inconsistency in the golden standard itself or the presence of an unwritten, highly specific contextual rule that even overrides a perfect keyword match.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is that the prompt's definition is too general and fails to model the expert's highly specific, unwritten rules for what distinguishes a "Trading system" from a "Tax" or a "Penalty.")

4. Detailed Rationale

The root cause of the disagreement is that the expert's mental model contains sharp, mutually exclusive boundaries between different economic instruments, while the LLM's prompt encourages it to blur those lines. The expert's framework appears to be:

Tax incentive: A domestic tax.

Penalty: A domestic fee or levy for non-compliance.

Trading system: A mechanism related to international trade (tariffs) or a formal cap-and-trade/credit system.

The LLM's prompt fails because it lumps "tariffs" in with "similar trading mechanisms," leading it to incorrectly classify domestic taxes and fees under this code. The prompt is teaching the LLM a flawed conceptual model. Even when the LLM finds a perfect keyword like "tariff" (as in the Palestine or Peru cases), the disagreement persists, indicating the expert's rule is even more nuanced than just the keyword. The prompt is the culprit because it is a poor approximation of the expert's complex and compartmentalized logic.

5. Recommendation for Improvement

The prompt must be significantly narrowed and rewritten to teach the LLM the expert's specific, bounded definition. It must explicitly differentiate this code from the "Tax" and "Penalty" codes.

Recommendation:
The prompt should be revised to focus exclusively on international trade mechanisms and formal credit/cap-and-trade systems, while actively excluding domestic fiscal tools.

Example of a Revised Prompt:

"Your task is to identify measures related to international trade or formal credit/trading systems.

Code as 'Mentioned' ONLY IF the text proposes one of the following:

Trade Measures: Such as 'tariffs,' 'import/export duties,' 'trade restrictions,' or 'trade-related measures' between countries.

Credit/Trading Systems: Such as 'plastic credits,' 'carbon credits,' 'cap-and-trade' systems, or tradable 'production permits.'

You MUST NOT code for general domestic fiscal measures. Explicitly exclude:

General 'taxes' or 'taxation.'

'Levies,' 'fees,' or 'charges.'"

This revised prompt provides the sharp conceptual boundaries that the LLM needs to replicate the expert's highly structured coding scheme. It would also be beneficial to review the golden standard for consistency, particularly regarding the Palestine case.

### [ ] BF : Regulatory

#### [ ] BG : Ban
##### Analysis for Code: C9 - Ban

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION are, on the surface, perfectly aligned. Both provide a broad, inclusive definition, instructing the coder to look for "bans," "phase-outs," or "eliminations." The texts are nearly identical.

However, the consistent pattern of disagreement reveals that the expert is applying this definition with a very specific, unstated contextual filter that is completely absent from the LLM's instructions. The prompt, while textually accurate, is a flawed hypothesis because it fails to capture the expert's crucial, implicit rule for application.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, with the LLM producing a 100% false positive rate. The LLM systematically and correctly found explicit keywords and strong semantic equivalents that match its instructions. For example, it identified:

Direct mentions of "banning" or "prohibit" (Uganda).

Direct mentions of "eliminating" or "elimination" (Armenia, Mauritius, Qatar).

The term "phase-out" (Ghana).

A discussion about a "blanket ban" (Japan).

Strong semantic equivalents like reducing production to "almost zero level" (Azerbaijan).

The golden standard, however, is "Not mentioned" in every single case. This proves that the expert's rule is not a simple keyword search. The LLM is perfectly executing a prompt that is fundamentally misaligned with the expert's true, more sophisticated task.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is not that the prompt is unclear, but that it is an inaccurate and incomplete model of the expert's nuanced, context-dependent logic. It lacks a critical qualifying condition.)

4. Detailed Rationale

The core of the disagreement lies in the expert's distinction between a discussion of a concept and a formal policy proposal. The expert appears to be coding exclusively for instances where a country puts forward a concrete, binding ban as a core obligation of the treaty.

The LLM, lacking this instruction, correctly flags any mention of the concept. The Japan submission is the clearest example of this failure: the text discusses "blanket bans" only to argue against them. The expert correctly identifies this is not a proposal for a ban and codes "Not mentioned." The LLM, simply looking for the keyword, codes "Mentioned." Similarly, in Ghana, the text mentions that a fee could "complement phase-out obligations," which acknowledges that phase-outs are a type of policy but does not propose a new one. The expert's more nuanced reading correctly excludes this, while the LLM's simpler instruction does not. The prompt is the culprit because it fails to teach the LLM to differentiate between a mention and a proposal.

5. Recommendation for Improvement

The prompt must be re-engineered to explicitly encode the expert's contextual rule. It must move the LLM from simple keyword detection to evaluating the author's intent.

Recommendation:
The prompt should be rewritten to include a clear, primary condition: the text must be a concrete proposal.

Example of a Revised Prompt:

"Your task is to identify if the document makes a clear proposal for a specific and binding ban, prohibition, phase-out, or elimination of a plastic product, material, or additive as a core obligation of the treaty.

Code as 'Mentioned' ONLY IF the text is actively advocating for a ban to be included in the instrument.

You MUST NOT code if the text:

Only discusses the concept of a ban in general terms.

Mentions a ban to argue against it.

Refers to bans as a complementary or existing measure without proposing a new one.

Uses vague terms like 'reducing' without a clear goal of total elimination or phase-out."

This revised prompt equips the LLM with the same critical filter the expert is using, which is essential for aligning its output with the golden standard.

#### [ ] BH : EPR
##### Analysis for Code: C9 - EPR (Extended Producer Responsibility)

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION are textually well-aligned. Both define EPR as making producers responsible for the post-consumer stage of their products, with the golden standard's example reinforcing this by mentioning the transfer of environmental costs to producers. The LLM's prompt is a faithful and reasonable interpretation of the written golden standard.

However, the mixed pattern of disagreements—numerous false positives from the LLM and a critical false negative—proves that the expert's actual application of this code involves unwritten rules and a level of subjectivity that neither the written definition nor the LLM's prompt successfully captures.

2. Disagreement Pattern Analysis

The disagreements for this code are complex and occur in both directions, which is highly informative:

LLM False Positives (Systematic Over-generalization): In most cases (Australia, Ghana, Micronesia), the LLM correctly identified broad, related concepts like the "polluter-pays principle" or a global fee on polymer producers. While EPR is an application of the polluter-pays principle, the expert is clearly making a sharp distinction between the general principle and a specific EPR scheme. The LLM's prompt fails to teach it this distinction. In other cases (Canada, Russia), the LLM found the exact keywords "extended producer responsibility," yet the expert still disagreed, indicating a requirement for more substantive detail than a simple mention.

LLM False Negative (Conceptual Contradiction): The Nepal case is the most critical piece of evidence. The LLM correctly reasoned that since the "take-back" responsibility was on consumers and guides—not producers—it did not qualify as EPR. The expert, however, coded this as "Mentioned." This implies the expert's working definition of EPR includes take-back schemes regardless of who is responsible, a definition that contradicts the explicit "Producer" part of the concept.

3. Primary Culprit Determination

Primary Culprit: Inherent Subjectivity / Grey Area

(Note: This is chosen because errors and inconsistencies are evident in both the LLM's interpretation and, more importantly, in the application of the golden standard itself. The boundaries of the code are not being applied consistently or intuitively.)

4. Detailed Rationale

This is a classic "grey area" problem where the simple definition of a code breaks down in practice. The LLM's false positives stem from a reasonable but incorrect assumption that related concepts (like "polluter pays") are interchangeable with EPR. The prompt's failure to draw a sharp line around the specific mechanism of EPR is a key issue.

However, the more significant problem is the inconsistency revealed by the Nepal case. If the golden standard includes a non-producer take-back scheme under the "EPR" label, it suggests the expert's application of the code is either highly subjective or inconsistent with the code's own name and standard definition. At the same time, the expert ignores perfect keyword matches in the Canada and Russia cases. This combination—ignoring perfect matches while including a contradictory one—means there is no single, clear rule that can be reliably followed. The definition's boundaries are fluid and subjective, leading to errors on both sides.

5. Recommendation for Improvement

To resolve this, both the golden standard's application and the LLM's prompt need clarification and alignment. The goal is to establish a single, consistent, and unambiguous rule.

Recommendation:

Audit the Golden Standard for a Consistent Rule: The first step must be a conceptual audit of the golden standard. A decision is required:

Does "EPR" absolutely require the producer to be responsible? If yes, the Nepal case should be reviewed as a potential human coding error. If no, the GOLDEN_DEFINITION itself must be rewritten to reflect this broader scope (e.g., "Includes any formal take-back scheme").

Why were explicit "EPR" mentions (Canada, Russia) excluded? The expert's unstated rule (e.g., "must be a substantive proposal, not just a mention in a list") must be extracted and written down.

Engineer a Highly Specific, Bounded Prompt: Based on the results of the audit, the prompt must be rewritten with sharp, explicit boundaries.

Example of a Revised Prompt (assuming the audit confirms EPR requires producer responsibility):

"Your task is to identify specific Extended Producer Responsibility (EPR) schemes where the original producer or importer is made financially or operationally responsible for the post-consumer stage of their products.

Code as 'Mentioned' ONLY IF this direct link to the producer is stated.

You MUST NOT code for:

General mentions of the 'polluter-pays principle.'

General fees, levies, or taxes on the supply chain.

Take-back schemes where the responsibility is on consumers or government."

This process of auditing the expert's logic and then encoding that precise logic into the prompt is the only way to resolve this type of complex, subjective disagreement.

#### [ ] BI : Legal recognition - Just transition
##### Analysis for Code: C9 - just-transition

1. Prompt/Instruction Analysis

This is a textbook case of a critical conceptual mismatch between the prompt and the golden standard.

The ORIGINAL_CODE_PROMPT provided to the LLM defines "just transition" in broad, social terms: "provisions addressing the social impact of the transition, particularly for vulnerable groups."

The GOLDEN_DEFINITION, starting with its very title ("Legal recognition – just transition"), defines the concept in narrow, legal terms: "The recognition of the legal rights of certain actors."

The LLM's prompt is a fundamentally flawed hypothesis. It incorrectly assumes that any mention of social support for vulnerable groups is equivalent to the expert's much higher and more specific standard of formal legal recognition.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, with the LLM producing a 100% false positive rate. This systemic error is a direct and predictable result of the flawed prompt. The LLM, correctly following its instructions, systematically identified dozens of instances that fit its broad, social-impact definition. For example:

It flagged mentions of including the "informal waste sector" (AOSIS, New Zealand).

It flagged proposals for "job transition programs" and creating "green jobs" (Burkina Faso, Cambodia).

It flagged general support for "affected communities" (African Group, Sierra Leone).

The golden standard, however, is "Not mentioned" in every single case. This proves that the expert is correctly ignoring these social measures because they do not meet the specific threshold of proposing "legal recognition" or "legal rights." The LLM is perfectly executing an instruction that asks the wrong question.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is profound. The prompt is not merely imprecise; it targets an entirely different concept (social impact) than the one the golden standard is actually measuring (legal rights).)

4. Detailed Rationale

The root cause of this total disagreement is that the prompt sent the LLM on a completely different mission than the one the expert was on. The GOLDEN_DEFINITION's title, "Legal recognition – just transition," is the smoking gun. The expert is not looking for general help for waste pickers; they are looking for proposals to formally grant them legal status, rights to the materials they collect, or formal integration into municipal waste systems.

The LLM's "false positives" are all perfect examples of this distinction. The Sri Lanka submission, which proposes to "Develop waste pickers in to entrepreneurs" and ensure their "occupational health and safety," is a social and economic support measure. It is not, however, a proposal to grant them legal rights. The expert correctly excludes it. The LLM, bound by its flawed "social impact" prompt, incorrectly includes it. The prompt is the culprit because it completely misses the legalistic core of the expert's definition.

5. Recommendation for Improvement

The prompt must be fundamentally rewritten to abandon the broad social definition and adopt the narrow legal one from the golden standard. The key is to shift the LLM's focus from "helping" to "legalizing."

Recommendation:
The current prompt should be discarded entirely. The new prompt must be built around the concept of "legal rights" and "formal recognition."

Example of a Revised Prompt:

"Your task is to identify proposals for the formal legal recognition or the granting of legal rights to vulnerable groups within the plastic value chain, particularly the informal waste sector.

Code as 'Mentioned' ONLY IF the text explicitly proposes measures like:

Integrating waste pickers into formal waste management systems.

Granting legal rights to waste pickers over the materials they collect.

Establishing a formal legal status for the informal recycling sector.

You MUST NOT code for general social or economic support measures. Explicitly exclude mentions of:

General 'social impacts' or 'socio-economic development.'

'Job creation,' 'training programs,' or ensuring 'health and safety.'

General 'inclusion' of vulnerable groups without a specific proposal for formal or legal integration."

This revised, legally-focused prompt is essential for teaching the LLM to replicate the expert's highly specific and nuanced judgment.

#### [ ] BJ : Mandatory action plan
##### Analysis for Code: C9 - Mandatory action plan

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION are, on the surface, well-aligned. Both point to "National Action Plans (NAPs)" as the core concept. The LLM's prompt even includes the key term "required," seemingly capturing the essence of the "Mandatory" title.

However, the consistent pattern of disagreement proves that the expert is applying a much more sophisticated filter than the prompt provides. The prompt correctly identifies the subject (NAPs) but completely fails to specify the required context (a substantive proposal vs. a passing mention), making it an inaccurate and incomplete model of the expert's logic.

2. Disagreement Pattern Analysis

The pattern is one of consistent false positives from the LLM. In all three cases, the LLM correctly identified the exact phrase "national action plan(s)." The golden standard, however, is "Not mentioned." This indicates that the expert's rule is not a simple keyword search. The disagreement stems from the context in which the keyword appears:

Tonga: The LLM flagged the term within a pre-written template question. The expert correctly ignored this, as it's not a substantive proposal from the country itself.

Kuwait: The LLM flagged a hypothetical statement: "A treaty may require... a national action plan." The expert correctly identified this as a discussion of a possibility, not a concrete proposal.

Malaysia: The LLM flagged a reference to NAPs as a place to incorporate findings. Again, the expert correctly identified this as a reference to NAPs, not a proposal for mandatory NAPs.

The LLM is performing perfect keyword detection, while the expert is performing nuanced intent analysis.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is that the prompt fails to model the expert's crucial distinction between a substantive proposal and a superficial mention of the concept, leading the LLM to over-code.)

4. Detailed Rationale

The core of the disagreement is that the expert's true definition for this code is not just "Does the text mention NAPs?" but rather, "Does the text, in its own original contribution, put forward a firm proposal for mandatory NAPs to be a core obligation of this treaty?"

The LLM's prompt lacks this critical, multi-part condition. It gives the LLM a simple hammer ("find 'NAPs'"), but the expert is using a surgical tool. The Tonga case is the most definitive evidence. Flagging text from a template question is a classic failure mode for a simple keyword-based approach. The expert's "Not mentioned" code proves they are correctly filtering for substantive, country-authored proposals. The prompt is the culprit because it failed to provide the LLM with this essential "ignore template text" and "evaluate intent" logic.

5. Recommendation for Improvement

The prompt must be re-engineered to explicitly teach the LLM the expert's contextual rules. The goal is to elevate the LLM's task from keyword searching to proposal evaluation.

Recommendation:
The prompt needs to be rewritten with clear, hierarchical conditions and explicit negative constraints.

Example of a Revised Prompt:

"Your task is to determine if the document makes a substantive and direct proposal for mandatory National Action Plans (NAPs) to be a core, required component of the treaty.

Code as 'Mentioned' ONLY IF the country, in its own text, advocates for this requirement.

You MUST NOT code if the mention of 'National Action Plan' occurs in one of the following contexts:

It is part of a pre-written template question that the country is answering.

It is a hypothetical or general statement about what a treaty could or may include.

It simply refers to NAPs as an existing concept without proposing their mandatory inclusion in this specific instrument."

This revised prompt directly encodes the expert's unstated rules, forcing the LLM to perform the same level of contextual analysis and dramatically increasing the likelihood of alignment.


### [ ] BK : Mandatory certification
#### Analysis for Code: C9 - Mandatory certification

1. Prompt/Instruction Analysis

This case reveals a subtle but powerful conceptual mismatch between the LLM's instructions and the expert's application of the code.

The ORIGINAL_CODE_PROMPT is conceptually broad. It instructs the LLM to look for "mandatory... certification, approval schemes, or verification systems." This encourages the LLM to treat these related-but-distinct concepts as interchangeable.

The GOLDEN_DEFINITION is conceptually narrow. While its text is simple ("Require the adoption of certification measures"), its application, as revealed by the disagreements, is highly specific. The expert is looking for the formal, explicit proposal of a "certification scheme" itself, not its component parts or related concepts.

The LLM's prompt is a flawed hypothesis because it conflates the formal process of certification with the standards and labels that are merely inputs or outputs of that process.

2. Disagreement Pattern Analysis

The pattern is one of overwhelmingly systematic false positives from the LLM, with one false negative. The LLM, correctly following its broad instructions, consistently flagged mentions of concepts it was told were equivalent to certification. The expert, applying a narrower rule, correctly excluded them. This created several distinct error types:

Conflating Standards with Certification: In many cases (AOSIS, Australia, EU, HAC), the LLM flagged proposals for "standards," "criteria," or "harmonized systems." The expert's coding shows a clear distinction: setting a standard is a prerequisite for certification, but it is not the certification process itself.

Conflating Labeling with Certification: The LLM also flagged mentions of "labeling" or "eco-labeling" (Cambodia, Korea, USA). The expert correctly identifies that a label is often the result of a certification process, not the process itself.

Conflating Approval with Certification: The LLM flagged "licensing and permits" (Bosnia and Herzegovina) and "approval process" (Oman). While related, the expert treats these as separate regulatory instruments.

Missing the "Mandatory" Constraint: In the Sierra Leone case, the LLM flagged "voluntary certification schemes," missing the crucial "Mandatory" aspect of the code's title and intent.

One False Negative: The LLM missed the instance in the Micronesia submission, which indicates that while the prompt is too broad, it may also be missing a specific keyword that the expert found.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is conceptual. The prompt fails to model the expert's sharp, unwritten distinctions between a formal 'certification scheme' and its related-but-separate components like standards, labels, and permits.)

4. Detailed Rationale

The root cause of this widespread disagreement is that the expert's mental model is highly structured and compartmentalized, while the LLM's prompt is broad and conflationary. The expert's framework appears to treat "Standards," "Labeling," and "Certification" as three distinct codes. The LLM's prompt for this one code incorrectly absorbs all three.

The EU submission is a perfect example. The text proposes "standards" for biodegradable plastics and "product passports" or "labelling" for transparency. The LLM, following its instructions to find "verification systems," correctly identifies these. The expert's "Not mentioned" code proves they are applying a much narrower filter, looking only for the explicit proposal of a formal "certification scheme." The prompt is the culprit because it fails to teach the LLM these critical boundaries.

5. Recommendation for Improvement

The prompt must be significantly narrowed to align with the expert's specific and bounded definition. It needs to be taught to isolate the formal process of certification from its inputs and outputs.

Recommendation:
The prompt should be rewritten to be highly specific, prioritizing the core concept and explicitly excluding related-but-distinct terms.

Example of a Revised Prompt:

"Your task is to identify proposals for a formal, mandatory certification scheme or system.

Code as 'Mentioned' ONLY IF the text uses explicit phrases like 'certification scheme,' 'certification system,' or proposes a formal process where a third party verifies and certifies compliance with a set of standards.

You MUST NOT code for the individual components that are merely related to certification. Explicitly exclude standalone mentions of:

The creation of 'standards,' 'criteria,' or 'definitions.'

Requirements for 'labeling,' 'eco-labeling,' or 'marking.'

'Permits' or 'licenses.'

'Voluntary' certification schemes."

This revised prompt provides the sharp conceptual boundaries the LLM needs to replicate the expert's highly structured coding framework.

#### [ ] BL : Mandatory infrastructure
##### Analysis for Code: C9 - Mandatory infrastructure

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT provided to the LLM and the GOLDEN_DEFINITION are, on a literal level, well-aligned. Both use the key concept of "requiring" or making "mandatory" the establishment of infrastructure. The golden standard's example ("Establish the infrastructure for separate waste collection") is a direct, imperative command that seems to fit the prompt's search for "required infrastructure development."

However, the subsequent 100% disagreement rate across 45 instances is definitive proof that this textual similarity is an illusion. The expert is applying the word "require" with a very specific, narrow, and legalistic meaning that is completely absent from the LLM's prompt. The prompt, by using "required" in a more general, common-sense way, fails to capture the expert's nuanced, high-threshold rule.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, with the LLM producing a 100% false positive rate. This systematic error is a direct result of the prompt's flawed definition of "required." The LLM, correctly following its instructions, flagged a wide spectrum of text that it interpreted as a requirement, including:

Direct Proposals to Build: The LLM found explicit proposals, such as China's call to "Establish a complete system covering collection, recycling and disposal" and the EU's proposal for "Obligations for Parties... to take measures to develop an environmentally sound waste management system (infrastructures)."

Statements of Necessity: The LLM flagged text stating that infrastructure is a prerequisite for success, such as Australia's note that success is "dependent on communities having access to... waste management services."

Calls for Investment: The LLM identified calls for "investment in" infrastructure (Azerbaijan, Saudi Arabia).

Creation of Systemic Infrastructure: The LLM flagged proposals for non-physical systems like a "network of technical centres" (Brazil) or a "global knowledge hub" (Thailand).

The golden standard, by being "Not mentioned" in every single one of these cases, proves that the expert's definition of "mandatory infrastructure" is something far more specific than any of these.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is profound and conceptual. The prompt fails to define its key term—"mandatory" or "required"—in the same narrow, legalistic way that the expert applies it, leading to a complete breakdown in communication.)

4. Detailed Rationale

The core of this massive disagreement lies in the interpretation of the word "mandatory." The LLM was prompted to interpret "mandatory" or "required" in its common-sense meaning: "is this infrastructure described as necessary for success?" The expert, however, is clearly using a much stricter, legalistic interpretation: "Does this text propose a specific, legally binding obligation within the treaty that mandates all Parties to establish a certain type of physical infrastructure?"

The most powerful evidence for this is the EU's submission. The text explicitly mentions "Obligations for Parties" to "develop... infrastructures." This is a seemingly perfect match for both the LLM's prompt and the golden definition. The fact that the expert coded this as "Not mentioned" is the smoking gun. It proves that even this language does not meet their incredibly high threshold. The expert's true rule is something more than just a proposal for an obligation; the specifics are unstated but clearly very restrictive. The LLM's prompt, by lacking this high-level, context-aware filter, is guaranteed to fail.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's extremely narrow and specific definition of "mandatory." It must be taught to ignore general needs, calls for investment, and even general proposals for obligations.

Recommendation:
The prompt should be rewritten to be highly restrictive and focused on the legalistic nature of a binding treaty provision.

Example of a Revised Prompt:

"Your task is to identify if the document proposes a specific and legally binding obligation for all Parties to establish physical waste management infrastructure.

Code as 'Mentioned' ONLY IF the text uses explicit, mandatory language to require the creation of physical systems like collection points, sorting facilities, or recycling plants as a formal part of the treaty's core rules.

You MUST NOT code if the text:

Simply states that infrastructure is needed, necessary, or dependent for success.

Calls for investment in infrastructure.

Proposes the creation of non-physical or digital infrastructure like knowledge hubs, databases, or technical centers.

Discusses infrastructure in the context of general 'Means of Implementation' or financial support without making it a standalone, binding obligation for all Parties."

This revised prompt provides the sharp, legalistic focus that is essential for the LLM to begin to replicate the expert's highly refined and specific coding practice.

#### [ ] BM : Mandatory labelling
##### 1. Prompt/Instruction Analysis

This case reveals a critical conceptual flaw in the ORIGINAL_CODE_PROMPT. The prompt given to the LLM is overly broad and conflationary, instructing it to look for "required product labels, marking, or information disclosure." It treats these three related but distinct concepts as interchangeable.

The GOLDEN_DEFINITION, by contrast, is much more focused. Its definition ("Require specific labelling of information") and its example (“ensure the appropriate labelling of plastic products”) strongly suggest the expert is looking for the specific, formal act of applying a physical label to a product. The LLM's prompt is a flawed hypothesis because it incorrectly assumes that any form of information transparency is equivalent to a mandatory labelling scheme.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, resulting in a 100% false positive rate for the LLM. This systemic error is a direct and predictable result of the prompt's flawed, over-broad definition. The LLM, correctly following its instructions, flagged a wide variety of measures that the expert clearly categorizes elsewhere:

Direct Keyword Hits (Ignored by Expert): The LLM found numerous explicit mentions of "labelling" or "eco-labelling" (AOSIS, Canada, Korea, Peru, Singapore). The expert's "Not mentioned" code for all of these proves that their rule is not a simple keyword search; it requires a specific context or level of substance that these mentions lack (e.g., they are mentioned in a list of options or as a voluntary measure).

Conflation with Broader Concepts: The LLM's prompt explicitly told it to code for "information disclosure" and "marking." As a result, it correctly flagged:

Mentions of "marking" (HAC, Palau, UK).

Mentions of general "information disclosure," "transparency," or "tracking" (Guinea, Kenya, Oman, Tanzania).
The expert's coding demonstrates a sharp, unwritten distinction: a requirement for transparency in a supply chain is not the same as a mandatory physical product label.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is conceptual. The prompt fails to model the expert's sharp, unwritten distinctions between a formal 'labelling scheme' and its related-but-separate components like information disclosure, transparency, and marking.)

4. Detailed Rationale

The root cause of this total disagreement is that the expert's mental model is highly structured, while the LLM's prompt is conceptually messy. The expert appears to have separate internal categories for a "Mandatory Labelling Scheme," "Transparency/Information Disclosure," and perhaps even "Standards." The LLM's prompt for this one code incorrectly absorbs all of these distinct ideas.

The submission from Kenya is a perfect example. The text proposes the "right to know (transparency)" and "tracking the ingredients... throughout the supply chain." The LLM, correctly following its instruction to find "information disclosure," flagged this. The expert's "Not mentioned" code proves they are applying a much narrower filter, looking only for proposals related to a physical label applied to the final product. The prompt is the culprit because it fails to teach the LLM these critical conceptual boundaries.

5. Recommendation for Improvement

The prompt must be significantly narrowed and rewritten to teach the LLM the expert's specific, bounded definition. It must explicitly differentiate a formal labelling scheme from general transparency requirements.

Recommendation:
The prompt should be revised to focus exclusively on the act of applying a physical label and should actively exclude the broader, related concepts.

Example of a Revised Prompt:

"Your task is to identify proposals for a formal, mandatory product labelling scheme.

Code as 'Mentioned' ONLY IF the text explicitly proposes a required system for applying a physical label or eco-label to a product to disclose information to consumers or waste managers.

You MUST NOT code for other, more general transparency measures. Explicitly exclude standalone mentions of:

General principles like the 'right to know' or 'transparency.'

Requirements for 'information disclosure' in the value chain (e.g., in databases).

'Tracking' or 'marking' of materials or fishing gear.

The creation of 'standards' or 'criteria' for products."

This revised prompt provides the sharp conceptual boundaries that the LLM needs to replicate the expert's highly structured and specific coding framework.

#### [ ] BN : Mandatory reports
##### 1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION appear reasonably aligned at a surface level. Both mention "reporting on the implementation of measures." However, there is a critical, subtle difference that becomes the root cause of all disagreements:

The LLM's prompt is exceptionally broad, instructing it to find any form of "data submission, disclosure requirements, or information sharing."

The Golden Definition's example provides the crucial hidden context. It highlights reporting as a tool to "...shed light on the extent to which Parties are... complying with their obligations."

The LLM's prompt is a flawed hypothesis because it fails to capture this essential purpose. It instructs the model to find any instance of information transfer, while the expert is looking for a specific, formal process: reporting for the purpose of verifying compliance with the treaty.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, with the LLM producing a 100% false positive rate. This systemic error is a direct and predictable result of the prompt's conceptual flaw. The LLM, correctly following its overly broad instructions, flagged a variety of text that the expert correctly identifies as not meeting their higher, more specific standard:

Conflating Transparency with Reporting: In several cases (Armenia, Nigeria, HAC), the LLM flagged proposals for "transparency requirements on chemicals" or "disclosure of information on... composition." The expert correctly distinguishes that a transparency requirement on a product is conceptually different from a national report on treaty implementation.

Conflating Data Submission with Reporting: In other cases (Azerbaijan, Yemen), the LLM flagged calls to "create a database" or "compile statistics." The expert correctly identifies that providing raw data is not the same as submitting a formal progress report.

Ignoring Context (Boilerplate Trap): In many instances (Malaysia, Palestine, Saudi Arabia, Uganda), the LLM flagged text that was simply part of the pre-written template question ("How to ensure... efficient national reporting?"). The expert correctly ignores these, as they are not substantive proposals.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is conceptual and profound. The prompt fails to model the expert's unwritten but critical distinction between general information sharing and formal compliance reporting, leading to a complete misinterpretation of the task.)

4. Detailed Rationale

The core of this disagreement is that the expert's mental model for this code is hierarchical and purpose-driven, while the LLM's prompt is flat and keyword-based. The expert is not just asking, "Is reporting mentioned?" They are asking, "Is a formal, mandatory national reporting system being proposed for the specific purpose of monitoring and verifying a country's compliance with its treaty obligations?"

The prompt's failure to include this multi-part, purpose-driven logic is its fatal flaw. The HAC submission is a perfect example. The text calls for parties to "report on the quantities and type of plastic polymers produced." This is a report, but its purpose is data collection. The expert's "Not mentioned" code proves they are reserving this code exclusively for reports on the implementation of and compliance with measures. The LLM, lacking this crucial distinction, cannot possibly replicate the expert's judgment.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's sophisticated, purpose-driven logic. It needs to be given the same cognitive toolkit as the human expert.

Recommendation:
The current prompt should be replaced with a highly constrained, multi-conditional one that makes the expert's tacit knowledge explicit.

Example of a Revised Prompt:

"Your task is to identify if the document proposes a formal, mandatory national reporting system for the purpose of monitoring compliance with the treaty's obligations.

Code as 'Mentioned' ONLY IF the text describes a required national report detailing a country's progress in implementing the treaty's rules and measures.

You MUST NOT code for other, more general forms of information sharing. Explicitly exclude the following:

Proposals for general transparency or information disclosure on products (e.g., chemical composition).

Requirements to submit raw data or statistics to a database.

Mentions of reporting that appear only in a pre-written template question."

This revised prompt elevates the LLM's task from simple keyword matching to the same level of conceptual and contextual analysis that the human expert is performing, which is the necessary step to achieve alignment.

#### [ ] BO : Moratorium
##### Analysis for Code: C9 - Moratorium

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT provided to the LLM and the GOLDEN_DEFINITION are, on a literal level, almost identical. Both define a moratorium as a temporary ban or a "ban for a specific period." Critically, the GOLDEN_DEFINITION's own example is a text that simply lists the word "moratoriums."

This setup creates a logical trap. The prompt is a faithful and accurate model of the written golden standard, including its example. However, the disagreement data proves that the expert's application of this rule is governed by unstated contextual filters that are completely missing from the LLM's instructions.

2. Disagreement Pattern Analysis

Two distinct and revealing patterns of disagreement have emerged:

Keyword Match vs. Substantive Proposal: In the African Group and HAC submissions, the LLM correctly identified the exact keyword "moratoriums" from its prompt. In both cases, the word appeared in a general list of potential policy options. The expert's "Not mentioned" code reveals a higher-level rule: a simple mention in a list of examples is not sufficient to qualify as a substantive proposal.

Conceptual Conflation: In the Philippines case, the LLM made a semantic leap, equating the term "phase-out" with a "moratorium." While both are time-based, a "phase-out" is a gradual but permanent elimination, whereas a moratorium is a temporary pause. The expert is correctly distinguishing between these two distinct regulatory instruments, a nuance the LLM failed to grasp.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is twofold. First, the prompt fails to model the expert's unwritten rule about "substantive proposals." Second, it is not specific enough to prevent the LLM from conflating "moratorium" with the distinct concept of "phase-out.")

4. Detailed Rationale

The core issue is that the LLM's prompt, while textually accurate to the written definition, is a poor model of the expert's actual, more sophisticated cognitive process. The expert is not simply searching for a keyword; they are evaluating the author's intent and the substance of the proposal.

The disagreements with the African Group and HAC prove this. The LLM found the exact word that the golden standard's own example uses, and yet it was wrong. This shows the expert's true rule is something like, "Does the document substantively propose a moratorium as a core measure?" The LLM's prompt lacks this critical filter.

Furthermore, the Philippines case demonstrates that the prompt's definition isn't sharp enough. It allowed the LLM to make a plausible but incorrect logical inference, blurring the lines between a temporary halt (moratorium) and a gradual stop (phase-out). The prompt is the culprit because it fails to provide both the contextual and the semantic boundaries that the expert is clearly and correctly applying.

5. Recommendation for Improvement

The prompt must be re-engineered to encode the expert's two key unstated rules: the requirement for a substantive proposal and the sharp distinction from a "phase-out."

Recommendation:
The prompt needs to be rewritten with both a primary condition and a clear negative constraint.

Example of a Revised Prompt:

"Your task is to identify if the document makes a substantive proposal for a moratorium, which is a temporary ban, pause, or suspension of a specific activity.

Code as 'Mentioned' ONLY IF the document is actively advocating for a moratorium to be included in the instrument. A simple mention of the word 'moratorium' in a general list of potential policy options is not sufficient.

You MUST NOT code for 'phase-outs' or 'phase-downs,' as these are gradual but permanent eliminations and are considered a different type of measure."

This revised prompt provides the LLM with the necessary conceptual toolkit to move beyond simple keyword matching and begin to replicate the expert's nuanced, context-aware judgment.

#### [ ] BP : Performance standard
##### Analysis for Code: C9 - Performance standard

1. Prompt/Instruction Analysis

This is a classic case of a prompt being both too broad and conceptually misaligned with the expert's task.

The ORIGINAL_CODE_PROMPT is overly general, instructing the LLM to look for any mention of "standards, specifications, criteria, requirements, or regulations." This casts an extremely wide net, essentially asking the LLM to find any proposed rule for a product.

The GOLDEN_DEFINITION provides the critical, unstated context. While its text is also broad, it explicitly includes high-level, formal frameworks like "Environmentally Sound Management (ESM), best available techniques (BAT), and best environmental practices (BEP)."

The LLM's prompt is a flawed operationalization of the golden standard. It correctly identifies the general topic but completely misses the expert's focus on formal, structured, and often technical regulatory frameworks over simple desired product characteristics.

2. Disagreement Pattern Analysis

The pattern is one of overwhelmingly systematic false positives from the LLM, coupled with at least one critical false negative (Yemen). The LLM, correctly following its broad instructions, consistently flagged text that mentioned a desired outcome or a general rule. The expert, applying a higher-level filter, correctly excluded them. This created several distinct error types:

Conflating Goals with Standards: In the Kuwait case, the LLM flagged "Plastic products must be reusable, recyclable or compostable." This is a desired outcome or goal, but the expert's coding demonstrates it does not qualify as a formal performance standard in itself.

Conflating Principles with Standards: In the Korea case, the LLM flagged "Applying eco-design principles." The expert correctly distinguishes between a guiding principle and a specific, measurable standard.

Conflating General Mentions with Substantive Proposals: In several cases (Malaysia, Mauritius, Morocco), the LLM flagged the general word "standards." The expert's disagreement shows they are looking for a proposal for a specific standard or framework, not just a passing mention of the concept.

The single false negative (Yemen) indicates that the LLM's prompt is also incomplete and may be missing a keyword or concept that the expert's more holistic understanding captures.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is conceptual and deeply rooted. The prompt fails to model the expert's crucial distinction between a general product requirement and a formal, technical, or named regulatory framework like ESM or BAT.)

4. Detailed Rationale

The core of this disagreement is that the expert's definition of "Performance Standard" is at a much higher level of abstraction than what the LLM was prompted to find. The expert is not looking for any rule; they are looking for formal, named, or highly structured technical frameworks and regulations. The inclusion of "ESM, BAT, and BEP" in their definition is the most powerful clue. These are not simple product criteria; they are comprehensive management and technical systems.

The LLM's "false positives" are all perfect examples of this mismatch. The Nigeria submission calls for a "Mandatory circularity application to design out waste." The LLM sees this as a "design criteria." The expert, however, likely sees this as a general principle and is looking for a more concrete, technical proposal, like "Parties must adhere to ISO 14001 standards for circular design." The prompt is the culprit because it teaches the LLM to operate at a low level of abstraction (finding any "requirement") while the expert is working at a high level (finding "formal frameworks").

5. Recommendation for Improvement

The prompt needs to be fundamentally re-engineered to elevate the LLM's task from finding simple rules to identifying formal, structured frameworks. It must be taught to recognize and prioritize the expert's preferred level of abstraction.

Recommendation:
The prompt should be rewritten to prioritize formal frameworks and explicitly exclude general goals or principles.

Example of a Revised Prompt:

"Your task is to identify proposals for formal, technical, or named performance standards and regulatory frameworks.

Code as 'Mentioned' ONLY IF the text proposes or references a specific, structured system. Prioritize mentions of established frameworks like 'Environmentally Sound Management (ESM),' 'best available techniques (BAT),' and 'best environmental practices (BEP).' Also include concrete proposals for new, binding technical standards or regulations.

You MUST NOT code for general or aspirational statements. Explicitly exclude standalone mentions of:

General product goals (e.g., 'products must be recyclable').

Guiding principles (e.g., 'applying eco-design principles').

The general words 'standards' or 'criteria' without a specific, formal proposal attached."

This revised prompt provides the LLM with the necessary conceptual filters to differentiate between a simple goal and a formal performance standard, which is the key to aligning with the expert's nuanced judgment.

#### [ ] BQ : Requirements & surveillance in trade systems
##### Analysis for Code: C9 - Requirements & surveillance in trade systems

1. Prompt/Instruction Analysis

This is a classic case of a prompt's definition being both too broad and conceptually overlapping with other codes in the expert's framework.

The ORIGINAL_CODE_PROMPT instructs the LLM to look for any measure "affecting international trade," including "import/export restrictions."

The GOLDEN_DEFINITION is deceptively simple ("Any measure on the economic side of plastic trade"), but the disagreements prove that its application is highly specific and, crucially, mutually exclusive from other codes like "Ban" or "Tax incentive."

The LLM's prompt is a flawed hypothesis because it fails to account for this critical principle of mutual exclusivity. It instructs the LLM to code for concepts that the expert, following a more structured codebook, correctly assigns elsewhere.

2. Disagreement Pattern Analysis

The pattern is one of overwhelmingly systematic false positives from the LLM, with one false negative. The LLM, correctly following its broad instructions, consistently flagged text that the expert correctly categorized under different, more specific codes. This created two clear error patterns:

Conflation with the "Ban" Code: In numerous cases (Guinea, Nepal, Palau, Tunisia, Uganda), the LLM flagged mentions of "import/export bans" or "prohibitions." The expert's "Not mentioned" code for all of these proves they are correctly and systematically assigning these concepts only to the more specific "Ban" code, even though they are trade-related.

Conflation with General Topic Mentions: In other cases (Bangladesh, Brazil, Russia), the LLM flagged general discussions of "transboundary movement" or "international trade." The expert correctly ignores these, as they are not proposals for a specific regulatory measure but are simply mentions of the topic area.

The single false negative (Korea) indicates that the LLM's prompt may also be missing a specific keyword that the expert's more holistic understanding captures.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is architectural. The prompt fails to model the expert's structured, mutually exclusive codebook, leading the LLM to systematically miscategorize data by placing specific measures (like bans) into a general category where they don't belong.)

4. Detailed Rationale

The root of this disagreement is that the expert is operating within a structured hierarchy of codes, while the LLM was given a flat, context-free instruction. The expert's logic is clear: if a measure is a "Ban," it goes in the "Ban" bucket, even if it's an import ban. This prevents double-coding and maintains the integrity of each specific code.

The LLM's prompt, which explicitly includes "import/export restrictions," directly contradicts this unwritten but crucial structural rule. The Nepal submission is a perfect example. The text mentions an "import... ban." The LLM, correctly following its prompt, codes it here. The expert, correctly following their structured methodology, codes it under "Ban" and leaves this code blank. The prompt is the culprit because it is not "aware" of the other codes in the system and therefore cannot respect the necessary boundaries between them.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's rule of mutual exclusivity. It needs to be taught not just what to look for, but also what to ignore because it belongs in a different category.

Recommendation:
The prompt should be rewritten to be much more specific, focusing on trade measures that are not bans or simple tariffs, and it must include explicit negative constraints.

Example of a Revised Prompt:

"Your task is to identify proposals for specific requirements, surveillance, or notification systems governing the international trade of plastic, excluding simple bans or taxes.

Code as 'Mentioned' ONLY IF the text proposes a specific regulatory mechanism for trade, such as:

Notification requirements for transboundary shipments (like under the Basel Convention).

Quotas on imports or exports.

Tracking systems for internationally traded plastics.

Restrictions on trade with non-parties to the treaty.

You MUST NOT code for measures that are more specifically defined by other codes. Explicitly exclude:

Any mention of a 'ban,' 'prohibition,' or 'restriction' on imports or exports (these belong to the 'Ban' code).

Any mention of 'tariffs' or general 'taxes' on trade (these belong to other economic codes)."

This revised prompt provides the LLM with the necessary conceptual boundaries to navigate the expert's complex codebook and correctly distinguish this code from its neighbors.

#### [ ] BR : Quota
NEED TO FIGURE OUT THIS ONE - NOT 100% WHICH CODE THIS CORRESPONDS TO.

### [ ] BS : Soft

#### [ ] BT : Assessment, monitoring and evaluation
##### Analysis for Code: C9 - Assessment, monitoring and evaluation

1. Prompt/Instruction Analysis

At first glance, the ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION appear to be in perfect harmony. Both use extremely broad language, instructing the model to find "all mentions of the need for assessment, monitoring, and evaluation." The LLM's prompt, which looks for systems to "track, observe, measure, assess, or evaluate," is a faithful and logical interpretation of this written rule.

However, the 100% disagreement rate proves that this textual alignment is a mirage. The expert is clearly applying a powerful, unstated structural rule that is completely absent from the LLM's instructions. The prompt, while a perfect reflection of the (flawed) written definition, is a failed hypothesis because it does not account for the expert's structured, multi-code framework.

2. Disagreement Pattern Analysis

The pattern is one of total disagreement, with the LLM producing a 100% false positive rate. This systematic error is a direct and predictable consequence of the prompt's conceptual overlap with another code in the expert's system: "Mandatory reports."

The LLM, correctly following its broad instructions, consistently flagged text that explicitly mentioned its keywords. For example:

"M&E and reporting to track and report the progress" (Cambodia)

"national reporting... to track the progress" (Bahrain)

"Measurement, Reporting and Verification" and "Assessment Panels" (Mauritius)

The expert's "Not mentioned" code for all of these proves that they are systematically and correctly assigning any measure related to formal reporting on policy implementation and effectiveness to the "Mandatory reports" code, leaving this code for a different, more general purpose.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is architectural and conceptual. The prompt fails to model the expert's mutually exclusive codebook, causing it to systematically miscategorize data by placing formal reporting mechanisms into this more general "monitoring" bucket where they don't belong.)

4. Detailed Rationale

The root cause of this total disagreement is that the expert is operating with at least two distinct, non-overlapping codes, while the LLM was only given instructions for one, overly broad version. The expert's framework is clearly structured:

Code A (Mandatory reports): This is for the formal, structured process of national reporting to a central body to track and verify compliance with treaty obligations.

Code B (This Code - Assessment, monitoring, and evaluation): This is for the more general activity of scientific monitoring, research, and assessment of plastic pollution in the environment, separate from the formal compliance reporting process.

The LLM's prompt for Code B is so broad that it completely subsumes Code A. It explicitly asks the LLM to find systems that "track... or evaluate... policy effectiveness"—the exact definition of the "Mandatory reports" code. The Mauritius submission, with its explicit mention of "Measurement, Reporting and Verification," is the smoking gun. The LLM correctly identified this as a monitoring activity. The expert correctly identified it as a formal reporting mechanism and, following their structured methodology, assigned it to the "Mandatory reports" code, leaving this one blank. The prompt is the culprit because it is not "aware" of the other codes in the system and therefore cannot respect the necessary boundaries.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's crucial rule of mutual exclusivity. It must be taught to differentiate the activity of scientific monitoring from the act of compliance reporting.

Recommendation:
The prompt needs to be rewritten with a sharp, primary focus on scientific and environmental assessment, while including an explicit negative constraint to exclude compliance reporting.

Example of a Revised Prompt:

"Your task is to identify proposals for the general scientific assessment, research, and monitoring of plastic pollution itself, its environmental sources, or its impacts.

Code as 'Mentioned' ONLY IF the text proposes activities like 'marine litter surveys,' 'monitoring plastic flows in rivers,' or 'assessing the impacts on ecosystems.'

You MUST NOT code for any system related to formal national reporting on policy implementation or compliance. Explicitly exclude any mention of:

'National reports' or 'reporting requirements.'

Systems to 'track the progress' or 'evaluate the effectiveness' of the treaty's implementation.

'M&E,' 'MRV,' or 'Verification Mechanisms' related to compliance."

This revised, highly constrained prompt provides the LLM with the necessary conceptual boundaries to navigate the expert's complex codebook and correctly distinguish this code from its neighbors.

#### [ ] BV : Education programs and awareness raising
##### Analysis for Code: C9 - Education programs and awareness raising

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT provided to the LLM and the GOLDEN_DEFINITION are, on the surface, well-aligned. Both define the code broadly, focusing on "awareness-raising campaigns" and "public education initiatives" aimed at the "general public."

However, the pattern of disagreements reveals two critical, unstated rules in the expert's application that are completely absent from the LLM's prompt. This makes the prompt, while textually similar, a flawed and incomplete model of the expert's true, more sophisticated coding process. It correctly identifies the general topic but misses crucial boundaries and contextual filters.

2. Disagreement Pattern Analysis

The disagreements provided show a consistent pattern of false positives from the LLM, which stem from two distinct types of error:

Conceptual Conflation: In several cases (HAC, Philippines, Uruguay), the LLM correctly identified mentions of "information disclosure" or "labelling" and, following its broad prompt, interpreted this as a form of "consumer education." The expert's "Not mentioned" code for these instances proves they are correctly applying a rule of mutual exclusivity, reserving these concepts for the "Mandatory labelling" code. The LLM's prompt for this code lacks the necessary negative constraint to respect that boundary.

Lack of a "Substantive Proposal" Filter: In many other cases (Burkina Faso, Ghana, Kuwait, Palau, Russia), the LLM correctly found explicit keywords like "education program," "raise public awareness," or "awareness-raising campaigns." The expert's disagreement reveals they are applying a higher-level filter: they are not just looking for a mention of the concept, but for a substantive, forward-looking proposal for a measure to be included in the treaty. The LLM's prompt lacks this critical distinction between a general mention and a concrete proposal.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is twofold and systemic. The prompt fails to model the expert's mutually exclusive codebook structure, and it fails to specify the required level of substance, leading the LLM to make predictable, logical errors.)

4. Detailed Rationale

The core issue is that the LLM's prompt is a "flat" instruction for a task that exists within a "deep," structured system. The expert's mental model contains sharp boundaries and hierarchies that the prompt does not reflect.

The HAC submission perfectly illustrates the first error type. The text proposes "disclosure of information on... composition... through marking or labelling." For the expert, this clearly belongs to the "Mandatory labelling" code. For the LLM, whose prompt lacks the instruction to exclude labelling, it's a reasonable, logical—but incorrect—fit for "consumer education."

The Ghana submission illustrates the second error. The text mentions "education" as a potential recipient of funds from a proposed fee. The expert correctly identifies that the primary subject here is a funding mechanism, not a proposal for an education program. The LLM, simply keying on the word "education," misses this crucial contextual distinction. The prompt is the culprit because it fails to provide the LLM with the two critical filters the expert is using: (1) "Is this concept better suited for another code?" and (2) "Is this a substantive proposal or just a passing mention?"

5. Recommendation for Improvement

The prompt must be re-engineered to explicitly teach the LLM the expert's unwritten rules. It needs to be given the same conceptual toolkit, including both the rule of substance and the rule of mutual exclusivity.

Recommendation:
The prompt should be rewritten to be more constrained, focusing on substantive proposals and actively excluding concepts that belong to other codes.

Example of a Revised Prompt:

"Your task is to identify if the document makes a substantive proposal for a public education program or awareness-raising campaign as a distinct measure.

Code as 'Mentioned' ONLY IF the text is actively advocating for a specific program, initiative, or campaign aimed at the general public or consumers.

You MUST NOT code for related but distinct concepts that belong to other categories. Explicitly exclude:

Any measure related to 'product labelling,' 'marking,' or 'information disclosure' on products.

General statements where education or awareness is mentioned as a potential beneficiary of a funding mechanism, but is not the primary measure being proposed."

This revised prompt provides the sharp conceptual boundaries necessary for the LLM to navigate the expert's complex codebook and align with the golden standard.

#### [ ] BW : Expert group
##### Analysis for Code: C9 - Expert group

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION are, on a literal level, in perfect agreement. Both instruct the model to find the establishment of "scientific committees," "technical panels," or other "expert bodies" designed to assist in implementing the treaty. The golden standard's example ("a scientific advisory function") reinforces this focus.

Based on the text alone, the prompt appears to be a well-constructed and faithful model of the written golden standard. However, the consistent pattern of disagreements proves that the expert's application of this rule is governed by a crucial, unstated distinction that is completely absent from the LLM's instructions.

2. Disagreement Pattern Analysis

The disagreements provided show a strong and systematic pattern of false positives from the LLM, with one false negative. This reveals a critical conceptual flaw in the prompt's design:

Systematic False Positives (Conflating "Advisory" with "Implementation"): In the vast majority of cases (Cook Islands, Indonesia, Iran, Korea, Libya, etc.), the LLM correctly identified explicit proposals for various committees and subsidiary bodies. It found mentions of "Compliance Committee," "Implementation Committee," "Executive Committee," and "standing committees for financing, technology development, and transfer." The expert's "Not mentioned" code for all of these proves they are applying a sharp, unstated rule: they are distinguishing between (a) scientific/technical advisory bodies and (b) operational implementation or compliance bodies. The expert appears to be reserving this code exclusively for the former, while the LLM's broad prompt instructs it to capture both.

One False Negative: The LLM missed the instance in the Azerbaijan submission, which indicates that while the prompt is too broad conceptually, it may also be missing a specific keyword or phrase that the expert's more holistic understanding captures.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is conceptual and critical. The prompt fails to model the expert's sharp, unwritten distinction between advisory/scientific expert groups and operational/compliance committees, leading the LLM to systematically miscategorize the data.)

4. Detailed Rationale

The core of this disagreement is that the expert's codebook is highly structured and compartmentalized, while the LLM's prompt for this single code is overly broad and conflationary. The expert is not just asking, "Is a committee mentioned?" They are asking, "Is a scientific or technical advisory committee mentioned?" and correctly assigning implementation/compliance committees to a different, more appropriate code.

The submission from Indonesia is a perfect example. The text proposes a "Compliance Committee" and "Subsidiary bodies." The LLM, correctly following its broad prompt, flags this. The expert, correctly following their structured and mutually exclusive codebook, recognizes that a "Compliance Committee" is a distinct regulatory instrument and does not belong under the "Expert group" code. The prompt is the culprit because it is not "aware" of the other codes in the expert's system and therefore cannot respect the necessary conceptual boundaries between them. It has taught the LLM a flawed and overly simplistic model of the expert's task.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's crucial conceptual distinction. It needs to be given the same set of boundaries that the expert is using to maintain a clean, structured dataset.

Recommendation:
The prompt should be rewritten to be much more specific, focusing exclusively on advisory/scientific bodies and actively excluding operational or compliance-focused committees.

Example of a Revised Prompt:

"Your task is to identify proposals for scientific, technical, or socio-economic advisory bodies designed to provide expert guidance and assessment.

Code as 'Mentioned' ONLY IF the text proposes a group whose primary function is advisory, assessment, or scientific review. Look for terms like 'scientific advisory committee,' 'technical panel,' or 'assessment body.'

You MUST NOT code for committees whose primary function is operational or related to compliance. Explicitly exclude:

'Compliance Committees.'

'Implementation Committees.'

'Executive Committees.'

Committees focused solely on 'financing' or the administration of funds."

This revised, highly constrained prompt provides the LLM with the necessary conceptual toolkit to navigate the expert's complex codebook and correctly distinguish this code from its neighbors.

#### [ ] BX : Harmonization
##### Analysis for Code: C9 - Harmonization

1. Prompt/Instruction Analysis

The ORIGINAL_CODE_PROMPT provided to the LLM and the GOLDEN_DEFINITION are, on a literal reading, well-aligned. Both use broad, inclusive language, instructing the model to find any effort to "standardize, align, or make consistent" systems and practices.

However, the consistent pattern of disagreements proves that this textual similarity is a red herring. The expert is applying this definition with a powerful, unstated filter that is completely absent from the LLM's instructions. The prompt, while a faithful reflection of the written rule, is a critically flawed hypothesis because it fails to capture the expert's much more specific and high-threshold application of that rule.

2. Disagreement Pattern Analysis

The disagreements provided show a strong and systematic pattern of false positives from the LLM, with one critical false negative. This dual-error pattern is highly informative:

Systematic False Positives: In the vast majority of cases, the LLM correctly identified explicit keywords that match its instructions. It found the exact word "harmonized" in numerous submissions (AOSIS, Armenia, New Zealand, Thailand, etc.) and strong semantic equivalents like "standardized" or "common format" in many others (Bosnia and Herzegovina, China, Korea). The expert's "Not mentioned" code for all of these proves their rule is not a simple keyword search. They are clearly looking for something more specific than a general call for alignment.

One False Negative: The LLM missed the instance in the Brazil submission. This is a crucial piece of data. It demonstrates that while the LLM's prompt is far too broad (causing it to over-code), it is also incomplete, as it failed to capture the specific signal that the expert correctly identified in that document.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is profound and conceptual. The prompt fails to model the expert's unwritten but critical distinction between a general desire for consistency and a proposal for a specific, formal harmonization system or mechanism.)

4. Detailed Rationale

The core of this disagreement is that the expert is not coding for the concept of harmonization in general; they appear to be coding for proposals of specific, formal harmonization systems. The GOLDEN_DEFINITION's own example is the most telling clue: it references the "Harmonized System of Designation and Coding of Goods"—a specific, existing, formal international framework for trade.

The LLM, lacking this crucial context, correctly flags any generic call to "align plans" or create "common definitions." The expert correctly ignores these as they do not rise to the level of proposing a formal system. The prompt is the culprit because it teaches the LLM to identify the general goal (consistency) rather than the specific mechanism (a formal system) that the expert is actually looking for. It's a classic case of mismatch in the level of abstraction.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's sophisticated, high-level distinction. It must be taught to ignore general calls for standards and focus only on proposals for specific, formal systems.

Recommendation:
The prompt should be rewritten to be highly restrictive, prioritizing formal systems and explicitly excluding the general statements that are currently causing false positives.

Example of a Revised Prompt:

"Your task is to identify proposals for specific, formal, or named international systems of harmonization.

Code as 'Mentioned' ONLY IF the text proposes or references a concrete mechanism, such as the 'Harmonized System' for trade classification, or a new, formally named global system for reporting or standards.

You MUST NOT code for general or aspirational statements about the need for consistency. Explicitly exclude standalone mentions of:

The general need for 'standards,' 'common criteria,' or 'common definitions.'

The goal of having 'aligned plans' or 'comparable data.'

The general word 'harmonized' unless it is tied to a specific, named system or framework."

This revised, highly constrained prompt provides the LLM with the necessary conceptual filter to differentiate between a general goal and a specific, formal mechanism, which is the key to aligning with the expert's nuanced judgment.

#### [ ] BY : Information and guidance
##### Analysis for Code: C9 - Information and guidance

1. Prompt/Instruction Analysis

At first glance, the ORIGINAL_CODE_PROMPT and the GOLDEN_DEFINITION seem perfectly aligned. Both use broad, inclusive language, instructing the model to find any mention of "guidelines," "best practices," or "informational resources."

However, the consistent pattern of disagreements proves that this textual similarity is a trap. The expert is clearly applying a powerful, unstated structural rule that is completely absent from the LLM's instructions. The prompt, while a faithful reflection of the written rule, is a critically flawed hypothesis because it fails to account for the expert's highly structured, multi-code framework where categories must be mutually exclusive.

2. Disagreement Pattern Analysis

The disagreements provided show a strong and systematic pattern of false positives from the LLM. This error is not random; it's a predictable consequence of the prompt's conceptual overlap with several other codes in the expert's system:

Conflation with "Harmonization": In the African Group case, the LLM flagged "harmonized definitions, formats and methodologies." The expert correctly identifies this as belonging to the "Harmonization" code, not here.

Conflation with "Expert group": In the AOSIS case, the LLM flagged text about "Subsidiary bodies" providing "guidance" and "reports." The expert correctly assigns the creation of the body to the "Expert group" code.

Conflation with "Education programs": In the Argentina case, the LLM flagged "information, awareness and training campaigns for the public," which the expert correctly assigns to the "Education" code.

Lack of a "Substantive Proposal" Filter: In many other cases (Bahrain, Bosnia, China), the LLM flagged general mentions of "best practices" or "sharing information." The expert's disagreement reveals they are looking for a concrete proposal to create a formal guidance document or toolkit, not just a general activity of information exchange. The GOLDEN_DEFINITION's own example ("develop and adopt guidelines") strongly supports this interpretation.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is architectural and conceptual. The prompt fails to model the expert's mutually exclusive codebook, causing it to systematically miscategorize data by placing concepts that belong to other, more specific codes into this general bucket.)

4. Detailed Rationale

The root cause of this disagreement is that the expert is operating within a structured, hierarchical codebook, while the LLM was given a flat, context-free instruction for this code. The expert's logic is clear and correct from a data integrity perspective: if a measure is a proposal to create a standard, it goes in "Harmonization"; if it's a proposal to create an expert body, it goes in "Expert group." This prevents double-counting and maintains the conceptual purity of each code.

The LLM's prompt for "Information and guidance" is so broad that it becomes a catch-all, instructing the model to code for concepts that are more precisely defined elsewhere. The prompt is not "aware" of the other codes in the system and therefore cannot respect the necessary boundaries between them. The African Group submission is a perfect example: the mention of "harmonized definitions" is a textbook case for the "Harmonization" code. The LLM's prompt, by including "guidelines" without excluding "harmonization," forces an error.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's crucial rule of mutual exclusivity. It needs to be taught not just what to look for, but also what to ignore because it belongs in a different, more specific category.

Recommendation:
The prompt should be rewritten to be much more specific, focusing on the creation of formal documents and actively excluding concepts that belong to other codes.

Example of a Revised Prompt:

"Your task is to identify proposals for the creation of formal but non-binding guidance documents, toolkits, or collections of best practices.

Code as 'Mentioned' ONLY IF the text is actively proposing the development of a specific informational resource to assist with implementation.

You MUST NOT code for related but distinct concepts that are covered by other codes. Explicitly exclude the following:

Proposals for 'standards,' 'harmonized definitions,' or 'common methodologies' (these belong to 'Harmonization').

Proposals to create 'expert groups,' 'committees,' or 'advisory panels' (these belong to 'Expert group').

Proposals for 'public awareness campaigns' or 'school programs' (these belong to 'Education')."

This revised, highly constrained prompt provides the LLM with the necessary conceptual boundaries to navigate the expert's complex codebook, respect the principle of mutual exclusivity, and dramatically increase its alignment with the golden standard.

#### [ ] BZ : Knowledge sharing
##### Analysis for Code: C9 - Knowledge sharing

1. Prompt/Instruction Analysis

This is a superb example of a subtle but profound mismatch between the LLM's instructions and the expert's true coding framework.

The ORIGINAL_CODE_PROMPT is conceptually flat and broad. It instructs the LLM to look for any mechanism related to exchanging information, including best practices and technology transfer.

The GOLDEN_DEFINITION provides the critical, unstated context in its very title: "Knowledge-sharing (subcategories: data registry, capacity-building, technology transfer, and joint research projects)."

This seemingly minor parenthetical is the key to the entire analysis. It reveals that the expert's codebook is hierarchical and structured. "Knowledge-sharing" is not a single, flat code; it is a high-level parent category, and the items listed are its specific, individual children codes. The LLM's prompt is a flawed hypothesis because it incorrectly treats this parent category as a simple, catch-all code.

2. Disagreement Pattern Analysis

The disagreements provided show a strong and systematic pattern of false positives from the LLM. This error is not random; it's a predictable consequence of the prompt's failure to understand the expert's hierarchical system. In every instance provided, the LLM correctly identified explicit keywords that the GOLDEN_DEFINITION itself lists as subcategories. For example:

It correctly flagged "technology transfer" and "capacity building" in the African Group and China submissions.

It correctly flagged "best practices" in the AOSIS submission.

It correctly flagged the creation of a "hub... for data and information" (a proxy for a data registry) in the AOSIS case.

The expert's "Not mentioned" code for all of these instances proves they are correctly applying a rule of mutual exclusivity and specificity. They are systematically assigning a mention of "technology transfer" only to a specific "Technology transfer" code, not to the general "Knowledge sharing" parent code, thus avoiding redundant or overlapping coding.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity here is architectural. The prompt fails to model the expert's hierarchical and mutually exclusive codebook structure, causing it to systematically miscategorize specific child concepts into the general parent category where they don't belong.)

4. Detailed Rationale

The root cause of this disagreement is that the expert is operating within a structured, multi-level coding framework, while the LLM was given a flat, context-free instruction. The expert's logic is clear and is standard practice in robust qualitative analysis: a specific instance should be coded with the most specific applicable code.

The African Group submission is a perfect illustration. The text explicitly mentions "technology transfer." The LLM, following its overly broad prompt, correctly identifies this as a form of knowledge sharing. The expert, however, correctly identifies "technology transfer" as a specific subcategory and (presumably) assigns it to a separate "Technology transfer" code, leaving this general parent code blank. The prompt is the culprit because it is not "aware" of the other, more specific codes in the system and therefore cannot respect the necessary boundaries between them. It has taught the LLM a flawed and overly simplistic model of the expert's sophisticated task.

5. Recommendation for Improvement

The prompt for this high-level code must be fundamentally re-engineered to teach the LLM the expert's crucial rule of mutual exclusivity. It must be taught to ignore specific instances that are better captured by other, more granular codes.

Recommendation:
The prompt should be rewritten to be highly specific, focusing only on general mentions of knowledge sharing and actively excluding the specific subcategories that have their own codes.

Example of a Revised Prompt:

"Your task is to identify general proposals for knowledge sharing that are not better described by a more specific mechanism.

Code as 'Mentioned' ONLY IF the text proposes a broad, undefined exchange of information or expertise.

You MUST NOT code for specific mechanisms that have their own, more precise codes. Explicitly exclude standalone mentions of:

'Technology transfer.'

'Capacity building.'

The creation of a 'data registry' or information hub.

'Joint research projects.'

The creation of formal 'expert groups' or advisory panels."

This revised, highly constrained prompt provides the LLM with the necessary conceptual boundaries to navigate the expert's complex codebook, respect the hierarchy, and dramatically increase its alignment with the golden standard.

#### [ ] CA : Capacity building
I SEE THAT I MADE A MINOR ERROR IN THE AGGREGATION OF SOME OF THE SUB-CATEGORIES. THIS CATEGORY IS PART OF THE KNOWLEDGE SHARING

#### [ ] CB : Data registry
I SEE THAT I MADE A MINOR ERROR IN THE AGGREGATION OF SOME OF THE SUB-CATEGORIES. THIS CATEGORY IS PART OF THE KNOWLEDGE SHARING

#### [ ] CC : Joint research projects
I SEE THAT I MADE A MINOR ERROR IN THE AGGREGATION OF SOME OF THE SUB-CATEGORIES. THIS CATEGORY IS PART OF THE KNOWLEDGE SHARING

#### [ ] CD : Technology transfer
I SEE THAT I MADE A MINOR ERROR IN THE AGGREGATION OF SOME OF THE SUB-CATEGORIES. THIS CATEGORY IS PART OF THE KNOWLEDGE SHARING

#### [ ] CE : Promotion of research & innovation
##### Analysis for Code: C9 - Promotion of research & innovation

1. Prompt/Instruction Analysis

This is a textbook case of a prompt failing because it cannot operate within a complex, hierarchical system.

The ORIGINAL_CODE_PROMPT attempts to create a distinction from another code ("R&D funding") by including the negative constraint "without specific funding commitments."

The GOLDEN_DEFINITION mirrors this, specifying "without specific mention of financial investment."

On paper, the instructions are clear. However, the consistent disagreements prove that this simple negative constraint is insufficient. The prompt is a flawed hypothesis because it fails to account for the expert's broader, unstated rule of applying the most specific code possible. This code is not just separate from "R&D funding"; it must also be distinct from "Knowledge sharing" (e.g., technology transfer, joint research) and "Expert group."

2. Disagreement Pattern Analysis

The disagreements provided show a strong and systematic pattern of false positives from the LLM. This error is not random; it is a predictable consequence of the prompt's failure to respect the expert's structured, mutually exclusive codebook. The errors fall into two clear categories:

Failure of the Negative Constraint: In a significant number of cases (African Group, Ecuador, GRULAC, Ghana), the LLM completely failed to adhere to its own negative constraint. It correctly found the keyword "research" or "innovation" but ignored the fact that it was directly and explicitly linked to "invest," "financial resources," or "funds." This is a basic failure of the prompt's logic.

Failure to Respect Mutual Exclusivity: In many other cases, the LLM correctly identified a relevant concept but failed to place it in the most specific category. For example:

It coded "technology development and transfer" (African Group) which belongs in "Knowledge sharing."

It coded the creation of "scientific and technical assessment bodies" (Kenya) which belongs in "Expert group."

It coded "cooperation in research" (Iceland) which likely belongs under a "joint research" subcategory of "Knowledge sharing."

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is architectural. The prompt fails to model the expert's hierarchical and mutually exclusive codebook, leading it to systematically miscategorize specific child concepts into this more general parent category where they do not belong.)

4. Detailed Rationale

The core of this disagreement is that the expert is correctly treating their codebook as a structured system with a principle of specificity, while the LLM's prompt treats this code as an isolated, standalone task. The expert's logic is clear: if a mention of research is explicitly tied to funding, it is coded as "R&D funding." If it's about creating a committee, it's an "Expert group." This "Promotion of research" code is correctly being used by the expert as a residual category—it applies only when a call for research is pure and does not fit into any other, more specific bucket.

The Ecuador submission is the most definitive evidence. The text calls for "financial resources to support... R&D&I projects." This is a textbook example for the "R&D funding" code. The LLM's failure to respect its own negative constraint and the expert's correct exclusion of this instance perfectly highlight the prompt's inadequacy. It has failed to teach the LLM the most crucial part of the expert's process: checking for a better, more specific fit first.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's hierarchical logic. It needs to be given a sequence of checks and a strong set of negative constraints to enforce the rule of mutual exclusivity.

Recommendation:
The prompt should be rewritten as a multi-step, conditional instruction that forces the LLM to check for more specific codes before applying this general one.

Example of a Revised Prompt:

"Your task is to identify general proposals for the promotion of research and innovation that are not better described by a more specific funding or collaborative mechanism. This is a residual category.

First, check if the text mentions any of the following. If it does, DO NOT apply this code:

Any mention of 'funding,' 'investment,' 'financial resources,' 'grants,' or a financial mechanism tied to research.

Any mention of 'technology transfer,' 'technical assistance,' or 'joint research' between parties.

Any proposal to create a formal 'expert group,' 'committee,' 'panel,' or 'advisory body.'

If, and only if, none of the above are present, you may code as 'Mentioned' for pure, standalone calls to 'encourage research,' 'promote innovation,' or 'support studies' on a topic."

This revised, hierarchical prompt structure is essential for moving the LLM beyond simple keyword matching and toward the kind of structured, relational reasoning that you, as a data scientist, know is critical for accurate classification in a complex system.

#### [ ] CF : Voluntary certification
##### Analysis for Code: C9 - Voluntary certification

1. Prompt/Instruction Analysis

This is a classic case of a prompt failing because it does not operate within the context of a larger, structured coding system.

The ORIGINAL_CODE_PROMPT is conceptually over-broad. It instructs the LLM to find "optional or non-mandatory certification programs, eco-labels, or verification schemes." It explicitly tells the LLM to treat these related-but-distinct concepts as interchangeable.

The GOLDEN_DEFINITION, while simple in its text ("adopt measures relating to the certification"), is clearly being applied by the expert with a powerful, unstated rule of mutual exclusivity.

The LLM's prompt is a flawed hypothesis because it fails to respect the boundaries of the expert's more granular codebook, where concepts like "labelling" and "standards" have their own dedicated codes.

2. Disagreement Pattern Analysis

The disagreements provided show a strong and systematic pattern of false positives from the LLM, with one false negative. The primary errors stem from the prompt's failure to respect the expert's structured codebook:

Systematic Conflation with Other Codes: In the majority of cases, the LLM correctly identified a concept that belongs to a different, more specific code. The expert correctly excluded these, but the LLM's prompt forced the error. For example:

It flagged "eco-labeling" (Cambodia, Colombia, USA), which the expert correctly assigns to a "Labelling" code.

It flagged "standards" (Australia, Japan), which the expert correctly assigns to a "Performance standard" code.

It flagged "plastic credit scheme" (Cambodia), which the expert correctly assigns to a "Trading system" code.

Lack of a "Substantive Proposal" Filter: In some cases (EU, Canada), the LLM flagged a general mention of "voluntary commitments" or a word in a long list of options. The expert's disagreement shows they are looking for a concrete, forward-looking proposal for a new voluntary certification scheme, not just a passing mention.

One False Negative: The LLM missed the instance in the Bosnia and Herzegovina submission, indicating that while its prompt is too broad, it may also be missing a specific keyword that the expert's more holistic understanding captures.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is architectural. The prompt fails to model the expert's structured, mutually exclusive codebook, leading the LLM to systematically miscategorize data by placing specific measures (like eco-labels) into a general category where they don't belong.)

4. Detailed Rationale

The root of this disagreement is that the expert is operating with a clean, structured dataset where each concept has its own home, while the LLM was given a messy, overlapping instruction. The expert's logic is clear and correct from a data integrity perspective: if a measure is an "eco-label," it goes in the "Labelling" bucket to avoid double-counting.

The LLM's prompt for "Voluntary certification" directly contradicts this structural logic by explicitly telling it to include "eco-labels." The Colombia submission, with its mention of "Ecodesign and ecolabeling standards," is a perfect example. The LLM, correctly following its flawed prompt, codes it here. The expert, correctly following their structured methodology, assigns it to a more specific code and leaves this one blank. The prompt is the culprit because it is not "aware" of the other codes in the system and therefore cannot respect the necessary boundaries between them.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's crucial rule of mutual exclusivity. It needs to be taught not just what to look for, but also what to ignore because it belongs in a different, more specific category.

Recommendation:
The prompt should be rewritten to be much more specific, focusing on the formal process of certification and actively excluding the related concepts that have their own codes.

Example of a Revised Prompt:

"Your task is to identify proposals for a formal, voluntary certification scheme or system that is not better described by a more specific measure.

Code as 'Mentioned' ONLY IF the text proposes a specific, optional program where an entity can choose to have its products or processes verified against a set of criteria.

You MUST NOT code for related but distinct concepts that are covered by other codes. Explicitly exclude standalone mentions of:

'Eco-labels' or any form of 'labelling.'

The creation of 'standards' or 'criteria.'

'Plastic credit schemes.'

General 'voluntary commitments' or 'voluntary initiatives' that are not specific certification programs."

This revised, highly constrained prompt provides the LLM with the necessary conceptual boundaries to navigate the expert's complex codebook and dramatically increase its alignment with the golden standard.

#### [ ] CG : Voluntary labelling
##### Analysis for Code: C9 - Voluntary labelling

1. Prompt/Instruction Analysis

This case reveals a critical conceptual flaw in the ORIGINAL_CODE_PROMPT's design. The prompt given to the LLM is conceptually over-broad and conflationary. It instructs the LLM to look for "optional product labeling schemes or non-mandatory information disclosure," which encourages it to group several distinct soft instruments under one umbrella.

The GOLDEN_DEFINITION ("adopt measures on what information should be included on the labels") is more focused, but the disagreements prove that its application by the expert is governed by a powerful, unstated rule of mutual exclusivity. The LLM's prompt is a flawed hypothesis because it fails to respect the boundaries of the expert's more granular and structured codebook, where concepts like "certification" and "labelling" are treated as separate, distinct codes.

2. Disagreement Pattern Analysis

The disagreements provided show a strong pattern of false positives from the LLM, coupled with one critical false negative. The primary errors stem from the prompt's failure to respect the expert's structured codebook:

Systematic Conflation with "Voluntary Certification": In the majority of cases (African Group, China, Egypt, Korea, Morocco, Sierra Leone), the LLM correctly identified explicit mentions of "voluntary certification schemes" or "eco-label certification." The expert's "Not mentioned" code for all of these proves they are correctly and systematically assigning this concept only to the "Voluntary certification" code. The LLM's prompt for this code lacks the necessary negative constraint to respect that boundary.

Lack of a "Substantive Proposal" Filter: In other cases (Canada, Cook Islands), the LLM flagged a general mention of "labelling measures" in a long list of options or a high-level discussion of "voluntary provisions." The expert's disagreement shows they are looking for a concrete, forward-looking proposal for a voluntary labelling scheme, not just a passing mention of the concept.

One False Negative: The LLM missed the instance in the AOSIS submission. This is a crucial piece of data. It suggests that while the LLM's prompt is far too broad, it is also incomplete, as it failed to capture the specific signal that the expert correctly identified in that document.

3. Primary Culprit Determination

Primary Culprit: Prompt Ambiguity

(Note: The ambiguity is architectural. The prompt fails to model the expert's structured, mutually exclusive codebook, leading the LLM to systematically miscategorize data by placing specific measures (like certification) into a general category where they don't belong.)

4. Detailed Rationale

The root of this disagreement is that the expert is operating with a clean, structured dataset where each concept has its own home, while the LLM was given a messy, overlapping instruction. The expert's logic is clear and correct from a data integrity perspective: if a measure is a "voluntary certification scheme," it goes in the "Voluntary certification" bucket to avoid double-counting.

The LLM's prompt for "Voluntary labelling" directly contradicts this structural logic. The China submission, with its explicit mention of "Certify green plastic products" under "Voluntary approaches," is a perfect example. The LLM, correctly following its flawed prompt, codes it here. The expert, correctly following their structured methodology, assigns it to the "Voluntary certification" code and leaves this one blank. The prompt is the culprit because it is not "aware" of the other codes in the system and therefore cannot respect the necessary boundaries between them.

5. Recommendation for Improvement

The prompt must be fundamentally re-engineered to teach the LLM the expert's crucial rule of mutual exclusivity. It needs to be taught not just what to look for, but also what to ignore because it belongs in a different, more specific category.

Recommendation:
The prompt should be rewritten to be highly specific, focusing on the formal act of labelling and actively excluding the related concept of certification.

Example of a Revised Prompt:

"Your task is to identify proposals for a formal, voluntary product labelling or eco-labelling scheme that is not better described as a certification process.

Code as 'Mentioned' ONLY IF the text proposes a specific, optional program for applying a physical label or eco-label to a product to disclose information to consumers.

You MUST NOT code for the related but distinct concept of certification. Explicitly exclude standalone mentions of:

'Certification schemes' or the act of 'certifying' a product.

General 'voluntary provisions' that do not specifically mention labelling.

General 'information sharing' that is not a product label."

This revised, highly constrained prompt provides the LLM with the necessary conceptual boundaries to navigate the expert's complex codebook and dramatically increase its alignment with the golden standard.

#### [ ] CH : Target
##### Analysis for Code: C9 - Target

1. Prompt/Instruction Analysis

This is a fascinating case where the ORIGINAL_CODE_PROMPT is simultaneously too narrow and misaligned with the expert's application, despite appearing textually similar to the GOLDEN_DEFINITION.

The LLM's prompt is extremely strict and quantitative: "Look for specific, measurable targets with concrete numbers, percentages, or deadlines." It is an instruction to find a number.

The Golden Definition's example ("Reduction targets and timelines to phase out...") provides the crucial, unstated context. It suggests that the expert is coding not just for existing concrete numbers, but for the proposal of a target-setting framework itself.

The LLM's prompt is a flawed hypothesis because it interprets "measurable target" in its most literal, quantitative sense, while the expert is applying a more abstract, conceptual definition that includes the intent to set a target.

2. Disagreement Pattern Analysis

The disagreements for this code are complex and, crucially, occur in both directions. This is a powerful signal that the issue is not a simple one-way error.

Systematic LLM False Negatives (The Dominant Pattern): In the majority of cases (AOSIS, Colombia, New Zealand, Norway, etc.), the LLM correctly followed its strict instructions and concluded that no concrete number was present. Its reasoning is flawless based on its prompt: it found many instances of countries proposing to create targets (e.g., "Parties should set a target...") or using placeholders (e.g., "by the year [XXX]"), but correctly identified that no specific, measurable target was actually stated. The expert, however, coded these as "Mentioned," proving their definition is broader and includes the proposal of a target-setting mechanism.

Systematic LLM False Positives (The Contradictory Pattern): In numerous other cases (Japan, Morocco, Switzerland, USA), the LLM found perfect, textbook examples of quantitative, time-bound targets, such as "eliminate... by 2040." The expert's "Not mentioned" code for all of these is a significant contradiction, suggesting either a deep, unstated rule or an inconsistency in the application of the golden standard.

3. Primary Culprit Determination

Primary Culprit: Inherent Subjectivity / Grey Area

(Note: This is chosen because there are two distinct, opposing systemic failures. The primary failure is the prompt being too narrow (Prompt Ambiguity), but this is compounded by significant inconsistencies in the golden standard's application, creating a complex, multi-faceted "grey area.")

4. Detailed Rationale

This disagreement is multi-layered. The first and most frequent problem is that the LLM's prompt is too literal. The expert is clearly operating on a higher level of abstraction, where a formal proposal to "set a target" is, for the purposes of this code, equivalent to stating a target. The Colombia submission, with its use of placeholders like "XX%" and "[XXX]," is a perfect example. The LLM correctly sees no number; the expert correctly sees the formal structure of a target. The prompt is failing to capture this conceptual leap.

However, this is complicated by the second pattern. The expert's exclusion of clear, quantitative targets like "eliminate plastic pollution by 2040" (Morocco, Switzerland, USA) is difficult to explain with a single, consistent rule. It points to a deep subjectivity or potential inconsistency in the golden standard itself. If the codebook's own example is "eliminate by x year," then excluding "eliminate by 2040" is a direct contradiction. This makes it impossible to derive a single, coherent rule from the provided data. The boundary of what constitutes a "target" is fluid and not being applied consistently.

5. Recommendation for Improvement

To resolve this complex disagreement, both the prompt's logic and the golden standard's application need to be clarified and aligned. A two-pronged approach is essential.

Recommendation:

Broaden the Prompt's Core Logic: The prompt must be re-engineered to operate at the same conceptual level as the expert. It should be taught to recognize both concrete targets and formal proposals for target-setting.

Revised Positive Instruction: "Code as 'Mentioned' if the text either (a) states a specific, measurable target with a number, percentage, or deadline, OR (b) makes a formal proposal to establish a target-setting mechanism, even if it uses placeholders like '[XXX]' or calls for Parties to 'set a target'."

Audit the Golden Standard for Consistency: This is the more critical step. The instances where the expert ignored perfect, quantitative targets (Japan, Morocco, USA, etc.) must be reviewed. This audit will achieve one of two things:

It will correct what appear to be clear errors in the benchmark data, improving its integrity.

It will reveal a hidden, highly specific rule (e.g., "Only code for reduction targets, not elimination targets," or "Only code if the target is legally binding, not aspirational"). This unstated rule must then be explicitly engineered into the LLM's prompt as a negative constraint.

Only by tackling both the prompt's narrowness and the golden standard's apparent inconsistencies can a reliable and replicable coding system be achieved.

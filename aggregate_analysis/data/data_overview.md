Note: 
After uploading, I noticed that the dataset rows are in a bit of a wild order compared to the original codebook.
I will be re-uploading the datasets where they are ordered properly. For now there is a section below on how to sort the data (which sub-codes with which parent codes)

# Analysis outputs (per run folder)

Each run folder (e.g., `Iteration_1/`, `Iteration_2/`, …, `Iteration_6_large/`) contains **evaluation outputs** comparing the LLM-coded results against the NVivo “gold” dataset, on a **per-code** basis.

The files currently uploaded in each run are:

- `confusion_by_code.csv`
- `macro_summary.csv`
- `micro_summary.csv`
- `coding_result_enriched`
  (contains raw results + quotes and reasoning traces)
- `codebook.json`/`prompts/`
    (file (folder for iteration 6) that contains the code definitions used. In iteration 6, we opted to split the larger JSON structure into individual ones for better adjustment of prompts for code boundaries) 

Below is what each file contains and how to interpret it.

---

## 1) `confusion_by_code.csv`

This is the **main per-code evaluation table**.  
Each row corresponds to **one code column** (e.g., `A : C1 Objectives - end plastic pollution`, `AL : 1. Upstream`, `C9_Regulatory_Ban`, etc.).

### Key columns

**Identity**
- `code`: the code name

**Confusion matrix counts (per code across all countries)**
- `TP`: True Positives  
  (NVivo = 1 and LLM = 1)
- `FP`: False Positives  
  (NVivo = 0 and LLM = 1)
- `FN`: False Negatives  
  (NVivo = 1 and LLM = 0)
- `TN`: True Negatives  
  (NVivo = 0 and LLM = 0)

**Derived metrics**
- `precision` = TP / (TP + FP)  
  “When the model predicts True, how often is it correct?”
- `recall` = TP / (TP + FN)  
  “Of the true cases, how many did the model detect?”
- `specificity` = TN / (TN + FP)  
  “Of the false cases, how many did the model correctly leave false?”
- `f1` = harmonic mean of precision and recall  
  Useful when positives are rare.
- `accuracy` = (TP + TN) / total
- `balanced_accuracy` = (recall + specificity) / 2  

**Support (base rates)**
- `support_true`: number of NVivo positives for this code (TP + FN)
- `support_pred`: number of LLM positives for this code (TP + FP)

### Why code-level “0 scores” can still look “good”
Some codes are very rare. If NVivo has **zero positives** for a code, then:
- recall is undefined in spirit (we compute it as 0 using eps),
- F1 becomes 0,
- but TN may be huge, producing high specificity and high accuracy.

That’s why adding `specificity` is often necessary to interpret “mostly-negative” codes.

---

## 2) `macro_summary.csv`

This file contains **macro-averaged metrics**, i.e. the mean of each metric across codes:

- `precision`, `recall`, `specificity`, `f1`, `accuracy`, `balanced_accuracy`

Macro averages treat each code equally (rare codes count as much as common codes).

Format:
- `metric`: metric name  
- `macro_mean`: the macro average value across all scored codes

---

## 3) `micro_summary.csv`

This file contains **micro-averaged metrics**, computed by:
1) summing TP/FP/FN/TN across all codes first, then  
2) computing metrics once from those global totals

Micro averages are dominated by:
- codes with more cases (and especially by the majority negative class, since TN can be huge).

---

# Sorting `confusion_by_code.csv` in a consistent “schema order”

# Sorting the code column (full parent + child hierarchy)

Some collaborators will want to inspect **all granular NVivo/LLM columns**, not just the “parent-only” view.  
In this schema, many codes are arranged as **parent + mutually-exclusive child options** (or parent + subdimensions). The cleanest way to sort is to use the **letter-prefix ordering** (A, B, C, …, AA, AB, …) and then keep any “C9_*” blocks grouped by family.

Below is the recommended hierarchy and ordering.

---

## 1) C1 Objectives — end plastic pollution (A–D)

**Parent**
- `A : C1 Objectives - end plastic pollution`

**Children (detail of how it was mentioned)**
- `B : Mentioned with time frame`
- `C : Mentioned, no time frame`
- `D : Not mentioned`

Example of interpretation: A is the overall “mentioned” umbrella. B/C/D describe *how* it appears (if it does).  

---

## 2) C2 Objectives — reduce production of plastics (E–H)

**Parent**
- `E : C2 Objectives - reduce production of plastics`

**Children**
- `F : Mentioned with specification`
- `G : Mentioned, no specification`
- `H : Not mentioned`

---

## 3) C3 Objectives — benefits of plastics (I–K)

**Parent**
- `I : C3 Objectives - benefits of plastics`

**Children**
- `J : Mentioned`
- `K : Not mentioned`

---

## 4) C4 Objectives — protect human health (L–N)

**Parent**
- `L : C4 Objectives - protect human health`

**Children**
- `M : Mentioned`
- `N : Not mentioned`

---

## 5) C5 Objectives — protect biodiversity and (marine) environment (O–Q)

**Parent**
- `O : C5 Objectives - protect biodiversity and (marine) environment`

**Children**
- `P : Mentioned`
- `Q : Not mentioned`

---

## 8) C6 Objectives — addressing the full life cycle of plastics (Z–AC)

**Parent**
- `Z : C6 Objectives - addressing the full life cycle of plastics`

**Children**
- `AA : Mentioned`
- `AB : Not mentioned`
- `AC : Partial mention`

---

## 9) C7 Objectives — other objectives (AD–AJ)

**Parent**
- `AD : C7 Objectives - other objectives`

**Subcodes (topic tags / categories)**
- `AE : Circular economy`
- `AF : Climate change`
- `AG : ESM`
- `AH : Mentioned`
- `AI : Not mentioned`
- `AJ : Sustainable production`
---

## 10) C8 Value chain (AK–AO)

**Parent**
- `AK : C8 Value chain`

**Children (granular value-chain coverage)**
- `AL : 1. Upstream`
- `AM : 2. Midstream`
- `AN : 3. Downstream`
- `AO : 4. Cross value chain`

---

## 11) C9 Type of measure (C9_*)

**Economic**
- `C9_Economic_Deposit_systems`
- `C9_Economic_Penalty`
- `C9_Economic_Public_procurement`
- `C9_Economic_RandD_funding`
- `C9_Economic_Subsidy`
- `C9_Economic_Tax_incentive`
- `C9_Economic_Trading_system`

**Regulatory**
- `C9_Regulatory_Ban`
- `C9_Regulatory_EPR`
- `C9_Regulatory_Judicial_measure`
- `C9_Regulatory_Legal_recognition`
- `C9_Regulatory_Mandatory_action_plan`
- `C9_Regulatory_Mandatory_certification`
- `C9_Regulatory_Mandatory_infrastructure`
- `C9_Regulatory_Mandatory_labelling`
- `C9_Regulatory_Mandatory_reports`
- `C9_Regulatory_Moratorium`
- `C9_Regulatory_Performance_standard`
- `C9_Regulatory_Requirements_and_surveillance_in_trade_systems`

**Soft**
- `C9_Soft_Assessment,_monitoring_and_evaluation`
- `C9_Soft_Education_programs`
- `C9_Soft_Expert_group`
- `C9_Soft_Harmonization`
- `C9_Soft_Information_and_Guidance`
- `C9_Soft_Knowledge_sharing`
- `C9_Soft_Promotion_of_RandI`
- `C9_Soft_Voluntary_certification`
- `C9_Soft_Voluntary_labelling`

---

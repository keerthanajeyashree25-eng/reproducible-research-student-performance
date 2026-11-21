# Preregistration: Study Time and Academic Performance

## 1. Research Title
Association Between Study Time and Student Academic Performance

## 2. Research Question
Among students represented in the selected dataset, is studying at least 2 hours per day associated with higher examination scores compared with studying less than 2 hours per day?

## 3. Dataset
- Dataset: Student Performance Factors
- Source: https://www.kaggle.com/datasets/lainguyn123/student-performance-factors
- Author: lainguyn123
- Version: Initial local copy available 2026-11-21
- Download date: 2026-11-21

## 4. Study Design
Observational quantitative research using secondary data.

## 5. Population
Students represented in the selected dataset for whom study hours and examination scores are recorded.

## 6. Exposure
Study time of at least 2 hours per day.

## 7. Comparator
Study time of less than 2 hours per day.

## 8. Primary Outcome
Examination score on the dataset's 0-100 scale.

## 9. Observation Window
The dataset's recorded study-time measure and examination score. The observation window is unspecified by the dataset documentation available in this project.

## 10. Hypotheses
Null hypothesis (H0): The average exam score in the high study-time group is equal to or lower than the average score in the low study-time group.

Alternative hypothesis (H1): The average exam score in the high study-time group is higher than the average score in the low study-time group.

## 11. Exclusion Criteria
- Records missing study hours.
- Records missing examination scores.
- Examination scores outside the 0-100 range.
- Duplicate records, if duplicates can be identified using a documented rule.

## 12. Data Transformations
- Preserve the original raw dataset.
- Rename Hours_Studied to study_hours and Exam_Score to exam_score in the analysis copy.
- Create a binary exposure group using the fixed threshold of 2 hours.
- Validate score range and record missingness.
- Do not change the exposure threshold based on observed results.

## 13. Primary Statistical Test
Welch independent-samples t-test with a one-sided alternative and significance level of 0.05.

## 14. Effect Size
Report means, mean difference, 95% confidence interval, Cohen's d, and sample size in each group.

## 15. Robustness Checks
- Mann-Whitney U test.
- Continuous study-hours linear regression.
- Sensitivity to missing-data handling.
- Documented evaluation of influential or extreme observations.

## 16. Reproducibility
Pin dependencies, preserve raw data, separate interim and processed datasets, use fixed seeds where applicable, and store scripts and tests in version control.

## 17. Ethics
Use the dataset in accordance with its licence and terms. Do not attempt to identify individuals.

## 18. Limitations
Observational data cannot establish causality. Confounding and representativeness may limit inference.

## 19. Preregistration Lock
The hypotheses, outcome, threshold, exclusion rules, and primary test are committed before the outcome analysis in this project.

## 20. Status
Preregistration prepared before local outcome analysis.
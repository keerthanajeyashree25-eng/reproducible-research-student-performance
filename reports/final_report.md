# Research Report

## Title
Association Between Study Time and Student Academic Performance

## 1. Introduction
This research investigates whether studying at least 2 hours per day is associated with higher examination scores than studying less than 2 hours per day.

## 2. Research Question
Among students represented in the dataset, is studying at least 2 hours per day associated with higher examination scores?

## 3. Dataset
- Dataset name: Student Performance Factors
- Source: https://www.kaggle.com/datasets/lainguyn123/student-performance-factors
- Author: lainguyn123
- Download date: 2026-11-21
- Raw observations: 6607
- Included observations: 6606
- Variables: Hours_Studied and Exam_Score

## 4. Data Preparation
The analysis copy selected only study hours and exam score, renamed both variables, removed missing values and duplicates, excluded the one examination score outside 0-100, and excluded negative study hours. The preregistered binary threshold was 2 hours.

## 5. Statistical Methods
- Descriptive statistics
- Welch independent-samples t-test
- Mean difference and 95% confidence interval
- Cohen's d
- Mann-Whitney U robustness check
- Continuous study-hours linear regression

## 6. Results
- High group sample size: 531
- Low group sample size: 3
- High group mean: 69.0753
- Low group mean: 71.0000
- Mean difference: -1.9247
- 95% confidence interval: [-47.0492, 43.1998]
- Cohen's d: -0.2376
- Welch one-sided test p-value: 0.5642
- Mann-Whitney U one-sided p-value: 0.2579

The prespecified one-sided evidence does not support the alternative hypothesis. The low-study group is too small for a stable estimate.

## 7. Robustness Checks
The continuous regression was directionally positive: each additional study hour was associated with a 0.2754-point higher exam score (95% CI [0.2073, 0.3434]; p = 1.1061e-14; R-squared = 0.1062). This differs from the binary comparison result, so the binary finding should be interpreted cautiously.

The Mann-Whitney U one-sided p-value was 0.2579 and does not support the alternative hypothesis.

## 8. Discussion
The binary result is likely driven by an extreme imbalance: 531 observations met the threshold and only 3 did not. The continuous regression is much more informative and is consistent with a positive association across the full study-hours range. Neither result establishes causality.

## 9. Limitations
The study is observational and may contain confounding. The 2-hour binary comparison has sparse low-study data. Dataset provenance and collection procedures should be verified before broader generalization.

## 10. Conclusion
The binary preregistered test did not provide statistically significant evidence that at least 2 study hours were associated with higher examination scores. The continuous analysis showed a positive association.

## 11. Reproducibility
The repository includes pinned dependencies, a requirements lockfile, synthetic pytest checks, reusable analysis code, the processed analysis copy, and commands for rerunning the pipeline.

## 12. Deviations
No deviation from the preregistered hypothesis, threshold, outcome, or primary test occurred. Missing values and duplicates were checked; one exam score outside 0-100 was excluded as prespecified.

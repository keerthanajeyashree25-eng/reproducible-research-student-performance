import numpy as np
from scipy.stats import mannwhitneyu, ttest_ind
from statsmodels.stats.weightstats import CompareMeans, DescrStatsW


def run_analysis(df):
    high = df.loc[df["study_group"] == "High", "exam_score"]
    low = df.loc[df["study_group"] == "Low", "exam_score"]

    t_result = ttest_ind(high, low, equal_var=False, alternative="greater")
    difference = high.mean() - low.mean()
    cm = CompareMeans(DescrStatsW(high), DescrStatsW(low))
    ci = cm.tconfint_diff(usevar="unequal", alpha=0.05)

    pooled_sd = np.sqrt(
        (
            (len(high) - 1) * high.var(ddof=1)
            + (len(low) - 1) * low.var(ddof=1)
        )
        / (len(high) + len(low) - 2)
    )

    cohen_d = difference / pooled_sd
    mw_result = mannwhitneyu(high, low, alternative="greater")

    return {
        "high_n": len(high),
        "low_n": len(low),
        "high_mean": high.mean(),
        "low_mean": low.mean(),
        "mean_difference": difference,
        "ci_lower": ci[0],
        "ci_upper": ci[1],
        "cohen_d": cohen_d,
        "welch_p": t_result.pvalue,
        "mann_whitney_p": mw_result.pvalue,
    }

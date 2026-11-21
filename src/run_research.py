from analysis import run_analysis
from preprocessing import prepare_data


df = prepare_data("data/raw/StudentPerformanceFactors.csv")
df.to_csv("data/processed/analysis_data.csv", index=False)

results = run_analysis(df)
for key, value in results.items():
    print(f"{key}: {value}")

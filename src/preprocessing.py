from data_validation import validate_data
import pandas as pd


def prepare_data(file_path):
    df = pd.read_csv(file_path)

    if not {"Hours_Studied", "Exam_Score"}.issubset(df.columns):
        raise ValueError(
            "The raw file is not the Kaggle CSV; required columns are missing."
        )

    df = df[["Hours_Studied", "Exam_Score"]].copy()
    df = df.rename(columns={
        "Hours_Studied": "study_hours",
        "Exam_Score": "exam_score",
    })
    df = df.dropna(subset=["study_hours", "exam_score"])
    df = df.drop_duplicates()
    df = df.loc[df["exam_score"].between(0, 100)]
    df = df.loc[df["study_hours"].ge(0)]
    return validate_data(df)

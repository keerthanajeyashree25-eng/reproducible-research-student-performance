import pandas as pd


def validate_data(df):
    required_columns = ["study_hours", "exam_score"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    if df[required_columns].isnull().any().any():
        raise ValueError("Missing values detected")

    if not df["study_hours"].ge(0).all():
        raise ValueError("Study hours cannot be negative")

    if not df["exam_score"].between(0, 100).all():
        raise ValueError("Exam score must be between 0 and 100")

    df = df.copy()
    df["study_group"] = df["study_hours"].ge(2).map({
        True: "High",
        False: "Low",
    })
    return df

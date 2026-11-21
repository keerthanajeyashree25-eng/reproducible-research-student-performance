import pandas as pd
import pytest

from src.data_validation import validate_data


def test_valid_synthetic_data():
    fixture = pd.DataFrame({
        "study_hours": [1, 3, 0.5, 4],
        "exam_score": [50, 80, 40, 90],
    })
    result = validate_data(fixture)
    assert len(result) == 4
    assert result["study_group"].tolist() == ["Low", "High", "Low", "High"]


def test_invalid_score():
    fixture = pd.DataFrame({
        "study_hours": [1, 3],
        "exam_score": [50, 110],
    })
    with pytest.raises(ValueError):
        validate_data(fixture)


def test_missing_column():
    fixture = pd.DataFrame({"study_hours": [1, 3]})
    with pytest.raises(ValueError):
        validate_data(fixture)


def test_negative_study_hours():
    fixture = pd.DataFrame({
        "study_hours": [-1, 3],
        "exam_score": [50, 80],
    })
    with pytest.raises(ValueError):
        validate_data(fixture)


def test_missing_values():
    fixture = pd.DataFrame({
        "study_hours": [1, None],
        "exam_score": [50, 80],
    })
    with pytest.raises(ValueError):
        validate_data(fixture)

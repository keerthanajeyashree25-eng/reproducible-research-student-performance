# Reproducible Research: Study Time and Academic Performance

## Overview
This project investigates the association between study time and student examination scores using a preregistered observational research design.

## Research Question
Among students represented in the dataset, is studying at least 2 hours per day associated with higher examination scores compared with studying less than 2 hours per day?

## Preregistration
The hypotheses, exposure threshold, comparator, exclusion criteria, statistical methods, and robustness checks are documented in `preregistration.md`.

## Project Structure
- `data/`: raw, interim, processed, and synthetic data.
- `src/`: reusable Python code.
- `notebooks/`: data-validation and analysis notebooks.
- `tests/`: synthetic pipeline tests.
- `reports/`: research report and figures.
- `docs/`: documentation.

## Reproducibility
- Pinned dependencies and an environment lockfile.
- Synthetic pipeline validation.
- Version-controlled code and preregistration.
- A documented real-data analysis pipeline.

## Setup
```text
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements-lock.txt
```

## Pipeline Tests
```text
python -m pytest -v
```

## Research Analysis
```text
python src/run_research.py
```

## Ethical Considerations
Use the dataset in accordance with its licence and terms. Do not attempt to identify individuals.

## Limitations
Observational analysis cannot establish causality. Results are limited by dataset quality, representativeness, and measurement procedures.

## Licence
Specify the project licence before public redistribution.
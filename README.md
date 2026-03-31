# QA Analyst Assessment

SDET Technical Assessment - Two-Part Assignment for SS&C Technologies.

**Language:** Python 3.7+

## Repository Structure

```
qa-analyst-assessment/
├── part1-functional/
│   ├── remove_duplicates.py    # Pure function to remove duplicates
│   └── README.md
├── part2-api-testing/
│   ├── test_jsonplaceholder_api.py  # API test suite (pytest)
│   ├── requirements.txt
│   └── README.md
├── .gitignore
└── README.md
```

## Part 1: Functional Programming - Remove Duplicates
A pure function that removes duplicates from a list while preserving the original order of first occurrences. Uses `functools.reduce` for a functional programming approach with no side effects.

```bash
cd part1-functional
python remove_duplicates.py
```

## Part 2: API Testing - JSONPlaceholder API
Automated tests for the JSONPlaceholder REST API using pytest and requests, covering GET, POST, and error handling scenarios.

```bash
cd part2-api-testing
pip install -r requirements.txt
pytest test_jsonplaceholder_api.py -v
```

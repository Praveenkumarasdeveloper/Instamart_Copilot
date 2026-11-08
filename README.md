Project directory: c:\Users\PRAVEEN_KUMAR\jupyter_notebook\Jupyter notebook\Masai_Code
README exists: True
# Instamart Copilot Project

This repository contains the completed Instamart assignment (Parts A-D), its original Jupyter notebooks, datasets, SQLite database, mock LLM, SQL queries, and generated outputs.

## Project Overview

This project covers data cleaning, customer analytics, machine learning, support-ticket triage, and a policy-based refund assistant.

## Project structure

```text
Instamart_GitHub_Ready/
├── data/                 # Original and cleaned datasets, policies, SQLite database
├── notebooks/            # Data_generate_code.ipnby ,mock_llm.ipynb & .py (preserved)
├── src/
│   ├── part_a.py          # Part A notebook runner
│   ├── part_b.py          # Part B notebook runner
│   ├── part_c.py          # Part C notebook runner
│   ├── part_d.py          # Part D notebook runner
│   ├── notebook_runner.py # Shared notebook execution helper
│   └── main.py            # Runs Parts A-D in order
├── sql/queries.sql        # Seven SQL queries from Part A
├── outputs/               # Existing project outputs and ledgers
├── state/                  # Agent checkpoints
├── mock_llm.py             # Original offline mock model
├── requirements.txt        # Project dependencies
└── README.md
```

## Parts covered

- **Part A:** CSV data cleaning, validation, SQLite database creation and SQL analysis.
- **Part B:** RFM customer segmentation, K-means clustering, lapse prediction and retention outputs.
                Best Cross-Validation F1-score: 0.650552962900789
                Logistic Regression Accuracy: 0.728448275862069
                Logistic Regression F1-score: 0.6480446927374302
- **Part C:** Support-ticket PII redaction, zero-shot/few-shot classification, validation, retry and token-budget guardrails, customer-aware routing.
- **Part D:** Policy document chunking, TF-IDF retrieval, grounded policy answers, refund tools, ReAct agent, token/time/iteration safeguards, checkpointing and resume.

## Project Notebooks

### Part A — Data Cleaning and SQL Database
- [Data Cleaning Notebook](Part_A_Data_Cleaning.ipynb)
- [SQL Database Notebook](Part_A_SQL_Database.ipynb)

### Part B — Customer Segmentation and Lapse Prediction
- [Customer Segmentation and Lapse Prediction Notebook](Part_B_Customer%20Segments%20and%20Lapse%20Prediction.ipynb)

### Part C — Support Ticket Triage
- [Support Ticket Triage Notebook](Part_C_Support%20Ticket%20Triage%20with%20Guardrails%20.ipynb)

### Part D — Policy RAG Assistant and Refund Agent
- [Policy RAG Assistant and Refund Agent Notebook](Part_D_Policy%20RAG%20Assistant%20and%20Refund%20Agent.ipynb)

## SQL Queries
- [View SQL Queries](sql/queries.sql)

## Setup

Use Python 3.10 or newer. From the project root, install dependencies:

```bash
python -m pip install -r requirements.txt
```

The runner uses Jupyter's Python kernel to execute the original notebooks. Make sure the selected environment has an available `python3` Jupyter kernel. A few exploratory/debug cells in the supplied notebooks contain recorded errors; the runner continues so later assignment cells can execute. Review executed notebook outputs for cell-level errors.

## Run the complete project

Run from the project root:

```bash
python -m src.main
```

To run one part only:

```bash
python -m src.part_a
python -m src.part_b
python -m src.part_c
python -m src.part_d
```

The Python files in `src/` are lightweight entry points that execute the preserved original notebooks. The notebooks remain the source of truth for the assignment calculations and model settings; they have not been rewritten or replaced. Executed notebook copies are saved under `outputs/`.

## SQL

## SQL Queries — Part A

The project includes seven SQL queries covering:

1. Customers with qualifying completed spend
2. Revenue by city and product category
3. Products priced above average
4. Customers without completed orders
5. Customers spending above the customer average
6. Customer spending rankings within each city using window functions
7. Daily revenue and cumulative running totals

**SQL source file:** [View all seven SQL queries](sql/queries.sql)

The seven original Part A analytical SQL queries are available in `sql/queries.sql`. They use the `customers`, `products`, and `orders` SQLite tables.

## Libraries

Third-party dependencies are listed in `requirements.txt`. Standard-library modules such as `sqlite3`, `json`, `pathlib`, `re`, and `time` are included with Python and do not need separate installation.

## Offline model

Part C and Part D use the supplied deterministic `mock_llm.py` implementation. This project does not require a hosted LLM API key or make external model API calls.

## Notes

- Original notebooks, source datasets, policy documents, SQLite database and existing outputs are retained.
- Run commands from the repository root so relative data paths resolve correctly.
- Some outputs and ledgers are generated by executing the notebooks; rerunning may append new agent/refund log entries as designed.

## Technologies Used

- Python

- Jupyter Notebook

- Pandas and NumPy

- SQLite and SQL

- Machine Learning

- Retrieval-Augmented Generation (RAG)

- Git and GitHub
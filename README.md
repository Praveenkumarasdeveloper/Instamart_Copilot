# Instamart Data Science Capstone Project

## Project Overview
This project analyses Instamart customer, product, order, and support-ticket data using Python, SQL, Machine Learning, and Generative AI. It covers data cleaning, customer segmentation, lapse prediction, ticket classification, and a policy-based refund assistant.

## Project Parts
- **Part A – Data Cleaning & SQL:** Data preprocessing, validation, and SQL analysis.
- **Part B – Customer Segmentation & Lapse Prediction:** RFM analysis, K-Means clustering, and classification models.
- **Part C – Support Ticket Classification:** Text processing, PII redaction, ticket classification, and prioritisation.
- **Part D – Policy RAG & Refund Agent:** Policy retrieval, refund calculation, structured responses, and agent workflow.

## Project Folder Structure

```text
Masai_Code/
│
├── data/
│   ├── raw/
│   ├── clean/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   └── orders.csv
│   ├── policies/
│   └── instamart.db
│
├── notebooks/
│   ├── Part_A_Data_Cleaning.ipynb
│   ├── Part_A_SQL_Database.ipynb
│   ├── Part_B_Customer_Segments_and_Lapse_Prediction.ipynb
│   ├── Part_C_Support_Ticket_Classification.ipynb
│   └── Part_D_Policy_RAG_and_Refund_Agent.ipynb
│
├── outputs/
│   ├── customer_segments.csv
│   ├── retention_list.csv
│   ├── lapse_model.joblib
│   ├── triage_results.csv
│   └── refund_ledger.jsonl
│
├── sql/
│   └── queries.sql
│
├── src/
│   ├── part_a.py
│   ├── part_b.py
│   ├── part_c.py
│   ├── part_d.py
│   ├── validate.py
│   └── main.py
│
├── state/
├── README.md
└── requirements.txt
```

## Project Setup and Reproduction

1. Clone the repository:
   ```bash
   git clone <your-github-repository-url>
   cd Masai_Code
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the notebooks in order: Part A Data Cleaning, Part A SQL, Part B, Part C, and Part D.

## Limitations and Next Steps
Results depend on the available dataset and selected features. LLM-generated outputs may require human validation. Future improvements include larger datasets, model tuning, and more robust evaluation.
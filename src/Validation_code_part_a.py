from pathlib import Path
import pandas as pd
import sqlite3
import math

# Find the main project folder
#BASE_DIR = Path(__file__).resolve().parents[1]


BASE_DIR = Path.cwd()

# Load cleaned CSV files
customers = pd.read_csv(BASE_DIR / "data/clean/Customer_data_Cleaned.csv")
products = pd.read_csv(BASE_DIR / "data/clean/Product_Cleaned.csv")
orders = pd.read_csv(BASE_DIR / "data/clean/Order_details_cleaned.csv")

# -------------------------------
# 1. CUSTOMER VALIDATION
# -------------------------------

assert len(customers) == 1200
assert customers["customer_id"].is_unique
assert customers["city"].nunique() == 6
assert customers["age"].notna().all()
assert customers["age"].between(10, 100).all()
assert set(customers["gender"].unique()) == {"Male", "Female", "Nan"}

# -------------------------------
# 2. PRODUCT VALIDATION
# -------------------------------

assert len(products) == 40
assert products["product_id"].is_unique
assert products["price_inr"].gt(0).all()

# -------------------------------
# 3. ORDER VALIDATION
# -------------------------------

assert len(orders) == 12305 
assert orders["order_id"].is_unique
assert (orders["status"] == "completed").sum() == 11106
assert (orders["status"] == "cancelled").sum() == 1199
assert (orders["status"] == "pending").sum() == 0
assert orders["order_amount"].notna().all()

completed = orders[orders["status"] == "completed"]
cancelled = orders[orders["status"] == "cancelled"]

assert completed["delivery_minutes"].notna().all()
assert cancelled["delivery_minutes"].isna().sum() == 1199

total_revenue = completed["order_amount"].sum()
assert math.isclose(total_revenue, 2995662.2, abs_tol=0.01)

# -------------------------------
# 4. SQLITE DATABASE VALIDATION
# -------------------------------

db_path = BASE_DIR / "data/instamart.db"
conn = sqlite3.connect(db_path)

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

table_names = set(tables["name"])

assert {"customers", "products", "orders"}.issubset(table_names)

assert pd.read_sql_query(
    "SELECT COUNT(*) AS n FROM customers", conn
).iloc[0]["n"] == 1200

assert pd.read_sql_query(
    "SELECT COUNT(*) AS n FROM products", conn
).iloc[0]["n"] == 40

assert pd.read_sql_query(
    "SELECT COUNT(*) AS n FROM orders", conn
).iloc[0]["n"] == 12959

conn.close()

# -------------------------------
# FINAL RESULT
# -------------------------------

print("Customer checks: PASSED")
print("Product checks: PASSED")
print("Order checks: PASSED")
print("SQLite database checks: PASSED")
print("ALL CHECKPOINTS PASSED")

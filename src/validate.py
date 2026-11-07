
from pathlib import Path
import pandas as pd

# 1. Set project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "clean"

# 2. Load cleaned CSV files
customers = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
orders = pd.read_csv(DATA_DIR / "orders.csv")

# 3. Validate row counts
assert len(customers) == 1200, "Customer row count is incorrect"
assert len(products) == 40, "Product row count is incorrect"
assert len(orders) == 12309, "Order row count is incorrect"

# 4. Validate unique order IDs
assert orders["order_id"].nunique() == 12309, "Duplicate order IDs found"
assert orders["order_id"].duplicated().sum() == 0, "Duplicate order IDs found"

# 5. Validate order status counts
status_counts = orders["status"].value_counts().to_dict()

assert status_counts == {
    "completed": 11110,
    "cancelled": 1199
}, "Order status counts are incorrect"

# 6. Validate order amounts
assert orders["order_amount"].isna().sum() == 0, "Missing order amounts found"

# 7. Validate delivery times
completed = orders["status"] == "completed"
cancelled = orders["status"] == "cancelled"

assert orders.loc[completed, "delivery_minutes"].isna().sum() == 0, \
    "Completed orders have missing delivery times"

assert orders.loc[cancelled, "delivery_minutes"].isna().sum() == 1199, \
    "Cancelled order delivery-time count is incorrect"

assert (orders["delivery_minutes"].dropna() < 0).sum() == 0, \
    "Negative delivery times found"

# 8. Validate completed order revenue
total_revenue = orders.loc[completed, "order_amount"].sum()

assert abs(total_revenue - 2998668.80) < 0.01, \
    "Completed order revenue is incorrect"

# 9. Print validation results
print("Customer rows:", len(customers))
print("Product rows:", len(products))
print("Order rows:", len(orders))
print("Completed orders:", completed.sum())
print("Cancelled orders:", cancelled.sum())
print("Duplicate order IDs:", orders["order_id"].duplicated().sum())
print("Missing order amounts:", orders["order_amount"].isna().sum())
print("Missing completed delivery times:",
      orders.loc[completed, "delivery_minutes"].isna().sum())
print("Negative delivery times:",
      (orders["delivery_minutes"].dropna() < 0).sum())
print("Completed order revenue:", round(total_revenue, 2))

print("\nALL CHECKPOINTS PASSED")

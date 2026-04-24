import os
from client import get_aggregates

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.abspath(os.path.join(
    BASE_DIR,
    "..",
    "company_Model",
    "salary_mpc_fe_dataset_250k.csv"
))

# Example 1: Aggregation of the full dataset
total_sum, total_count = get_aggregates(DATASET)
print(f"Total count: {total_count}, Total sum: {total_sum:.2f}")

# Example 2: Aggregation by company
for company in ["C009", "C078", "C066"]:
    s, c = get_aggregates(DATASET, company_id=company)
    print(f"{company} count: {c}, sum: {s:.2f}")

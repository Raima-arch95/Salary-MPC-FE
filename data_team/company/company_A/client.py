import csv

def get_aggregates(salary_mpc_fe_dataset_250k, company_id=None, salary_col="base_salary_usd"):

    local_sum = 0
    local_count = 0

    with open(salary_mpc_fe_dataset_250k, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if company_id and row["company_id"] != company_id:
                continue

            local_sum += float(row[salary_col])
            local_count += 1

    return local_sum, local_count
import csv

def get_aggregates(salary_mpc_fe_dataset_250k, company_id=None, salary_col="total_comp_usd"):

    if not (isinstance(salary_mpc_fe_dataset_250k,str)):
        raise ValueError("Wrong type submitted to the function gat_aggregates --  need string")

    local_sum = 0
    local_count = 0
    try:
        with open(salary_mpc_fe_dataset_250k, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                if company_id and row["company_id"] != company_id:
                    continue

                local_sum += float(row[salary_col])
                local_count += 1
    except:
        raise ValueError("Error while fetching the file")

    return local_sum, local_count

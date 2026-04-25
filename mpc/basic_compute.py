def compute_average(company_data):
    total_sum = 0
    total_count = 0

    for (local_sum, local_count) in company_data:
        total_sum += local_sum
        total_count += local_count

    if total_count == 0:
        raise ValueError("Total employee count cannot be zero")

    return total_sum / total_count

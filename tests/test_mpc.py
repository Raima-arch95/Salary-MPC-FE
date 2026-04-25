from mpc.basic_compute import compute_average

# Simulated company data
company_data = [
    (150000, 3),
    (200000, 4),
    (180000, 3)
]

avg = compute_average(company_data)

print("Test Average:", avg)

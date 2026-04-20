from companies.company_A.client import get_aggregates as A
from companies.company_B.client import get_aggregates as B
from companies.company_C.client import get_aggregates as C

from mpc.basic_compute import compute_average


def main():
    # Step 1: Collect data from companies
    company_data = [
        A(),
        B(),
        C()
    ]

    print("Collected Data:", company_data)

    # Step 2: Compute global average
    avg = compute_average(company_data)

    # Step 3: Display result
    print("Global Average Salary:", avg)


if __name__ == "__main__":
    main()

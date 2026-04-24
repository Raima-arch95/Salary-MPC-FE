from mock_companies.company_A import get_aggregates as A
from mock_companies.company_B import get_aggregates as B
from mock_companies.company_C import get_aggregates as C

from mpc.group_compute import compute_group_average
import asyncio


def main():
    company_data = [
        A(),
        B(),
        C()
    ]

    print("Collected Structured Data:", company_data)

    global_avg, role_avgs = asyncio.run(compute_group_average(company_data))

    print("Global Average Salary:", global_avg)
    print("Average Salary by Role:", role_avgs)


if __name__ == "__main__":
    main()

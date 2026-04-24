from mock_companies.company_A import get_aggregates as A
from mock_companies.company_B import get_aggregates as B
from mock_companies.company_C import get_aggregates as C

from mpc.group_compute import compute_group_average
from encryption.fe import encrypt, decrypt

import asyncio


def main():
    company_data = [
        A(),
        B(),
        C()
    ]

    print("Collected Structured Data:", company_data)

    global_avg, role_avgs = asyncio.run(compute_group_average(company_data))

    print("\n--- ENCRYPTED OUTPUT ---")

    encrypted_global = encrypt(global_avg)
    encrypted_roles = {role: encrypt(val) for role, val in role_avgs.items()}

    print("Encrypted Global Average:", encrypted_global)
    print("Encrypted Role Averages:", encrypted_roles)

    print("\n--- DECRYPTED OUTPUT ---")

    print("Global Average Salary:", decrypt(encrypted_global))
    print("Average Salary by Role:",
          {role: decrypt(val) for role, val in encrypted_roles.items()})


if __name__ == "__main__":
    main()

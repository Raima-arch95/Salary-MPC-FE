from mock_companies.company_A import get_aggregates as A
from mock_companies.company_B import get_aggregates as B
from mock_companies.company_C import get_aggregates as C

from mpc.group_compute import compute_group_average
from encryption.fe import encrypt, decrypt, decrypt_role

import asyncio


def validate_company_output(data):
    if "total" not in data or "by_role" not in data:
        raise ValueError("Invalid format: missing keys")

    if not isinstance(data["total"], tuple):
        raise ValueError("Invalid total format")

    for role, val in data["by_role"].items():
        if not isinstance(val, tuple):
            raise ValueError(f"Invalid format for role {role}")


def main():
    # STEP 1 — Collect data
    company_data = [
        A(),
        B(),
        C()
    ]

    print("Collected Structured Data:", company_data)

    # STEP 2 — Validate structure
    for c in company_data:
        validate_company_output(c)

    # STEP 3 — Secure computation (MPC)
    global_avg, role_avgs = asyncio.run(compute_group_average(company_data))

    # STEP 4 — Encrypt results
    print("\n--- ENCRYPTED OUTPUT ---")

    encrypted_global = encrypt(global_avg)
    encrypted_roles = {
        role: encrypt(val) for role, val in role_avgs.items()
    }

    print("Encrypted Global Average:", encrypted_global)
    print("Encrypted Role Averages:", encrypted_roles)

    # STEP 5 — Authorized decryption
    print("\n--- DECRYPTED OUTPUT (AUTHORIZED) ---")

    KEY = "fe-key-123"

    print("Global Average Salary:", decrypt(encrypted_global, KEY))

    decrypted_roles = {}
    for role, val in encrypted_roles.items():
        try:
            decrypted_roles[role] = decrypt_role(role, val, KEY)
        except Exception as e:
            decrypted_roles[role] = str(e)

    print("Average Salary by Role:", decrypted_roles)

    # STEP 6 — Unauthorized access test
    print("\n--- UNAUTHORIZED ACCESS TEST ---")

    WRONG_KEY = "wrong-key"

    try:
        print("Trying to decrypt global avg with wrong key:")
        print(decrypt(encrypted_global, WRONG_KEY))
    except Exception as e:
        print("Access Denied:", e)


if __name__ == "__main__":
    main()

from mpyc.runtime import mpc

async def compute_average_secure(company_data):
    await mpc.start()

    secint = mpc.SecInt()

    total_sum = secint(0)
    total_count = secint(0)

    for (local_sum, local_count) in company_data:
        total_sum += secint(local_sum)
        total_count += secint(local_count)

    # Check for division by zero
    if await mpc.output(total_count) == 0:
        await mpc.shutdown()
        raise ValueError("Total employee count cannot be zero")

    secure_avg = total_sum / total_count

    avg = await mpc.output(secure_avg)

    await mpc.shutdown()

    return avg

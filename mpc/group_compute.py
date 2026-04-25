from mpyc.runtime import mpc

async def compute_group_average(company_data):
    await mpc.start()

    secfxp = mpc.SecFxp()

    total_sum = secfxp(0)
    total_count = secfxp(0)

    role_sums = {}
    role_counts = {}

    for company in company_data:
        local_sum, local_count = company["total"]

        total_sum += secfxp(local_sum)
        total_count += secfxp(local_count)

        for role, (r_sum, r_count) in company["by_role"].items():
            if role not in role_sums:
                role_sums[role] = secfxp(0)
                role_counts[role] = secfxp(0)

            role_sums[role] += secfxp(r_sum)
            role_counts[role] += secfxp(r_count)

    global_avg = await mpc.output(total_sum / total_count)

    role_avgs = {}
    for role in role_sums:
        role_avgs[role] = await mpc.output(role_sums[role] / role_counts[role])

    await mpc.shutdown()

    return global_avg, role_avgs

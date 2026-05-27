def compute_autocall_payoff(
    path,
    nominal,
    coupon_rate,
    autocall_barrier,
    protection_barrier,
    initial_price,
    obs_per_year
):

    coupon_per_obs = coupon_rate / obs_per_year
    n_observations = len(path) - 1

    # AUTOCALL
    for t in range(1, n_observations + 1):

        performance = path[t] / initial_price

        if performance >= autocall_barrier:
            coupons = nominal * coupon_per_obs * t
            return nominal + coupons

    # MATURITY
    final_perf = path[-1] / initial_price

    if final_perf >= protection_barrier:
        return nominal
    else:
        return nominal * final_perf
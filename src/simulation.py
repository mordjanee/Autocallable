import numpy as np

def simulate_gbm_paths(
    initial_price,
    risk_free_rate,
    volatility,
    maturity_years,
    obs_per_year,
    n_simulations,
    seed=42
):
    np.random.seed(seed)

    n_steps = maturity_years * obs_per_year
    dt = 1 / obs_per_year

    paths = np.zeros((n_simulations, n_steps + 1))
    paths[:, 0] = initial_price

    for t in range(1, n_steps + 1):
        z = np.random.normal(0, 1, n_simulations)

        paths[:, t] = paths[:, t - 1] * np.exp(
            (risk_free_rate - 0.5 * volatility**2) * dt
            + volatility * np.sqrt(dt) * z
        )

    return paths
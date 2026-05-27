import numpy as np
import pandas as pd

def compute_payoffs(paths, payoff_fn, **kwargs):

    return np.array([
        payoff_fn(path, **kwargs)
        for path in paths
    ])


def monte_carlo_price(payoffs, risk_free_rate, maturity_years):

    discount_factor = np.exp(-risk_free_rate * maturity_years)
    return discount_factor * payoffs.mean()


def summary(payoffs):

    return pd.DataFrame({
        "Metric": [
            "Mean",
            "Median",
            "Min",
            "Max"
        ],
        "Value": [
            payoffs.mean(),
            np.median(payoffs),
            payoffs.min(),
            payoffs.max()
        ]
    })
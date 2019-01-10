import numpy as np
from numpy import random
from pandas import DataFrame


def simulate_target_column(df, weights, intercept=0.0):
    """
    Return a column of target values simulated from the logistic regression model.

    `weights` - dict mapping feature names to weights
    `df`      - data frame containing feature columns
    """
    assert set(weights) <= set(df.columns), "Weight names don't match columns"
    features, weights = zip(*weights.items())
    X = np.array([df[col] for col in features]).T
    weights = np.array(weights)
    return random.binomial(1, logistic(X @ weights + intercept)).astype(np.bool)


def logistic(x):
    neg = x < 0
    out = np.empty_like(x, dtype=np.float)
    out[neg] = np.exp(x[neg]) / (1 + np.exp(x[neg]))
    out[~neg] = 1 / (1 + np.exp(-x[~neg]))
    return out


if __name__ == '__main__':
    df = DataFrame({
        'feature_1': [-10, 10, 0],
        'feature_2': [100, -100, 0],
        'mytarget': [False, True, False],
    })
    print(np.array([simulate_target_column(df, {'feature_1': 1.2, 'feature_2': 1.0})
                    for _ in range(10)]))

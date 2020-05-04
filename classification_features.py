#!/usr/bin/env python
import numpy as np
from sklearn import feature_selection


def explode_list_values(df, column_name):
    values = set(chain.from_iterable(df[column_name]))
    new_column_names = [f"{column_name}_{i}" for i in range(values)]
    n_rows, _ = df.shape
    for name in new_column_names:
        df[name] = pd.Series([False] * n_rows)
    for i, row in enumerate(df[column_name]):
        for flag in row:
            df[i, flag] = True


def test_1():
    X = np.array([0, 0, 1, 1]).reshape(4, 1)
    y = np.array([0, 0, 1, 1])
    chi2 = feature_selection.chi2(X, y)
    print(f"test_1: chi2 score = {chi2}")


if __name__ == "__main__":
    test_1()


from io import StringIO

df = pd.read_csv(StringIO(fp.read().replace("\t", "")))

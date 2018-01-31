import numpy as np
import pandas as pd


def approximate(a_n, x, k):
    return sum(a_n(x, i) for i in range(k+1))


def get_terms(f, a_n, xs, k=10):
    return [
        (f(x), approximate(a_n, x, k=k))
        for x in xs
    ]

# 11.10.16
# 1/x
def f(x):
    return 1. / x

def a_n(x, n):
    return -(((x + 3) ** n) /
             (3 ** (n + 1)))

xs = np.linspace(-4, -2, 10, False)

# In [269]: pd.DataFrame.from_records(get_terms(f, a_n, xs, k=3))
# Out[269]:
#           0         1
# 0 -0.250000 -0.246914
# 1 -0.263158 -0.261827
# 2 -0.277778 -0.277333
# 3 -0.294118 -0.294025
# 4 -0.312500 -0.312494
# 5 -0.333333 -0.333333
# 6 -0.357143 -0.357136
# 7 -0.384615 -0.384494
# 8 -0.416667 -0.416000
# 9 -0.454545 -0.452247


# In [271]: pd.DataFrame.from_records(get_terms(f, a_n, xs, k=10))
# Out[271]:
#           0         1
# 0 -0.250000 -0.250001
# 1 -0.263158 -0.263158
# 2 -0.277778 -0.277778
# 3 -0.294118 -0.294118
# 4 -0.312500 -0.312500
# 5 -0.333333 -0.333333
# 6 -0.357143 -0.357143
# 7 -0.384615 -0.384615
# 8 -0.416667 -0.416667
# 9 -0.454545 -0.454545

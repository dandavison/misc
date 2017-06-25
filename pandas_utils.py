from collections import namedtuple

import pandas as pd


def iternamedtuples(df):
    Row = namedtuple('Row', df.columns)
    for row in df.itertuples():
        yield Row(*row[1:])


def df_to_array(df):
    assert isinstance(df.index, pd.MultiIndex)
    shape = tuple(map(len, df.index.levels)) + (len(df.columns),)
    return df.values.reshape(shape)

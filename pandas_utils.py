from collections import namedtuple

from pandas import *


def iternamedtuples1(df):
    Row = namedtuple('Row', df.columns)
    for row in df.itertuples():
        yield Row(*row[1:])


def iternamedtuples2(df=DataFrame()):
    Row = namedtuple('Row', df.columns)
    for row in df.itertuples():
        yield Row(*row[1:])


if __name__ == '__main__':
    print list(iternamedtuples1(DataFrame()))
    print list(iternamedtuples2())

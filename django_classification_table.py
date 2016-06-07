import operator
from collections import namedtuple
from datetime import datetime
from datetime import timedelta

import pandas as pd
from django.db.models import Q


class Predicate(namedtuple('Predicate', ['query', 'name', 'value'])):

    def negate(self):
        return Predicate(~self.query, self.name, not self.value)


def tabulate(queryset, predicates):
    [columns] = {tuple(p.name for p in preds) for preds in zip(*predicates)}
    columns += ('Count',)

    rows = []
    for preds in product(*predicates):
        query = reduce(operator.and_, (pred.query for pred in preds))
        row = tuple(pred.value for pred in preds)
        row += (queryset.filter(query).count(),)
        rows.append(row)

    return pd.DataFrame.from_records(rows, columns=columns)

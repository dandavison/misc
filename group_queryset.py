def group_queryset(qs, key, n=None):
    from itertools import groupby
    qs = qs.order_by(*key)
    if n is not None:
        qs = qs[:n]
    gps = groupby(qs, lambda obj: [getattr(obj, k) for k in key])
    gps = [(k, list(vals)) for k, vals in gps]
    return gps

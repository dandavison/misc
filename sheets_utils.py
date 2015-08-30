def dump(fp, objects, cls):
    """
    serialize as csv
    """

    fields = [col.name for col in cls.Dialect.columns]

    rows = []
    for obj in objects:
        _obj = {}
        for k, v in obj.__dict__.items():
            if k not in fields:
                continue
            if isinstance(v, basestring):
                v = clean_string(v)
            if isinstance(v, unicode):
                _obj[k] = v.encode('utf-8')
            else:
                _obj[k] = v
        rows.append(cls(**_obj))

    writer = cls.writer(fp)
    if fp.mode == 'a':
        writer.needs_header_row = False
    writer.writerows(rows)


def clean_string(s):
    bad = ['\n', '\r', '\t', '\v', '\f']
    for c in bad:
        s = s.replace(c, ' ')
    return s


def make_sheets_class(obj):
    """
    Create a class that models this object
    """
    # TODO: silly hack
    # This should really return a class that fits the
    # object, rather than writing the code to define such a class.

    obj = obj.__dict__

    ok_keys = []
    for k in sorted(obj.keys()):
        cls = obj[k].__class__
        if cls not in [bool, str, unicode, float, int, type(None)]:
            print 'excluding %s (class %s)' % (k, cls)
        else:
            ok_keys.append(k)

    print 'class Row(sheets.Row):'
    print '    Dialect = sheets.Dialect(use_header_row=True, delimiter="\\t")'
    for k in ok_keys:
        print '    %s = sheets.%s()' % (k, get_column_class(obj[k].__class__))


def get_column_class(cls):
    return {
        bool: 'BooleanColumn',
        str: 'StringColumn',
        unicode: 'StringColumn',
        float: 'FloatColumn',
        int: 'IntegerColumn',
        type(None): 'StringColumn',
    }[cls]


################

DJANGO_FIELD2SHEETS_COLUMN = {
    models.FloatField:  FloatColumn,
    models.IntegerField: IntegerColumn,
    models.CharField: StringColumn,
    models.BooleanField: BooleanField,
    models.NullBooleanField: BooleanField,
    models.ForeignKey: IntegerColumn,
}


def from_django_model(model, **dialect_kwargs):
    attrs = {
        'django_model': model,
        'Dialect': options.Dialect(**dialect_kwargs),
        '__module__': __module__,
    }
    name = model.__class__.__name__ + 'Sheet'
    return FromDjangoRowMeta(name, (Row,), attrs)

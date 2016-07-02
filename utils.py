def format_sql(sql):
    import sqlparse
    return sqlparse.format(unicode(sql), reindent=True)


def format_queryset_sql(qs):
    return format_sql(qs.values_list('pk').query)


def format_markdown_table_from_counts(counts):
    table = '| %s | count |\n' % (
        ' | '.join('val_%d' % i for i, key in enumerate(counts.keys()[0])))
    table += '|%s|---|\n' % '|'.join('---' for _ in counts.keys()[0])
    for val, cnt in counts.most_common():
        table += '| %s | %d |\n' % (' | '.join(val), cnt)
    return table


def format_markdown_table(rows, columns=None):

    def format_row(row):
        return '|%s|' % '|'.join(map(str, row))

    def format_hline(row):
        return '|%s---|' % '---|'.join('' for _ in row)

    table = []
    if columns is not None:
        table.append(format_row(columns))
        table.append(format_hline(columns))
    for row in rows:
        table.append(format_row(row))

    return '\n'.join(table)


def git_dir():
    """
    Base dir of current git repo
    """
    import os
    import subprocess

    stdout, stderr = (subprocess
                      .Popen('git rev-parse --git-dir'.split(' '),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
                      .communicate())

    if stderr:
        raise subprocess.CalledProcessError(stderr)

    return os.path.dirname(stdout)


def classification_metrics(n_true_neg=None,
                           n_true_pos=None,
                           ppv=None,
                           npv=None):

    TP = int(ppv * n_true_pos)
    FN = n_true_pos - TP
    TN = int(npv * n_true_neg)
    FP = n_true_neg - TN

    n_class_pos = TP + FP
    n_class_neg = TN + FN

    return {
        'n_true_neg': n_true_neg,
        'n_true_pos': n_true_pos,
        'n_class_neg': n_class_neg,
        'n_class_pos': n_class_pos,
        'sens': TP / float(n_true_pos),
        'spec': TN / float(n_true_neg),
        'ppv': ppv,
        'npv': npv,
    }


def make_df(rows):
    """
    rows: list-of-list-of-key-value-pairs
    """
    from itertools import starmap
    import pandas

    column_labels, rows = zip(*list(starmap(zip, rows)))
    [column_labels] = set(column_labels)
    return pandas.DataFrame.from_records(
        list(rows),
        columns=column_labels,
        index=column_labels[0])


def paste(max_display_lines=5):
    import subprocess
    from textwrap import dedent

    code = dedent(subprocess
                  .check_output(["reattach-to-user-namespace", "pbpaste"]))
    formatted_code = code.splitlines()
    if len(formatted_code) > max_display_lines:
        formatted_code = formatted_code[:max_display_lines] + ['...']
    print '\n'.join(formatted_code)
    exec(code, globals())


def counter_by(pairs):
    """
    `pairs` is [(a, b)]

    Return counts of `b` values, grouped by `a`
    """
    from collections import Counter
    from itertools import groupby

    return {
        key: Counter(pair[1] for pair in pairs)
        for key, pairs in groupby(sorted(pairs), lambda pair: pair[0])
    }


def group_by(pairs):
    """
    `pairs` is [(a, b)]

    Return sorted lists of `b` values, grouped by `a`
    """
    from itertools import groupby

    return {
        key: sorted(pair[1] for pair in pairs)
        for key, pairs in groupby(sorted(pairs), lambda pair: pair[0])
    }


def print_dict(d):
    for item in sorted(d.items()):
        print '%-30s %s' % (item)


def format_sql(sql):
    import sqlparse
    return sqlparse.format(unicode(sql), reindent=True)


def format_markdown_table_from_counts(counts):
    table = '| %s | count |\n' % (' | '.join('val_%d' % i
                                             for i, key in enumerate(counts.keys()[0])))
    table += '|%s|---|\n' % '|'.join('---' for _ in counts.keys()[0])
    for val, cnt in counts.most_common():
        table += '| %s | %d |\n' % (' | '.join(val), cnt)
    return table


def format_markdown_table(rows, columns=None):
    def format_row(row):
        return '|%s|' % '|'.join(map(str, row))
    def format_hline(row):
        return '|%s---|' % '---|'.join('' for _ in row)

    table = []
    if columns is not None:
        table.append(format_row(columns))
        table.append(format_hline(columns))
    for row in rows:
        table.append(format_row(row))

    return '\n'.join(table)



def time(expr):
    from datetime import datetime
    then = datetime.now()
    res = eval(expr)
    print res.status_code, datetime.now() - then


def refresh(obj):
    return obj._default_manager.get(pk=obj.pk)


class DumpResponse(object):
    'Middleware class to dump response to disk'
    def process_response(self, request, response):
        url = '__'.join((request.META['PATH_INFO'],
                         request.META['QUERY_STRING']))
        url = url.replace('/', '__').replace(',', '__').replace('=', '__')
        with open(url, 'w') as fp:
            fp.write(response.content)

        return response


def git_dir():
    """
    Base dir of current git repo
    """
    stdout, stderr = (subprocess
                      .Popen('git rev-parse --git-dir'.split(' '),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
                      .communicate())

    if stderr:
        raise subprocess.CalledProcessError(stderr)

    return os.path.dirname(stdout)


def classification_metrics(n_true_neg=None, n_true_pos=None, ppv=None, npv=None):
    TP = int(ppv * n_true_pos)
    FN = n_true_pos - TP
    TN = int(npv * n_true_neg)
    FP = n_true_neg - TN

    n_class_pos = TP + FP
    n_class_neg = TN + FN

    return {
        'n_true_neg': n_true_neg,
        'n_true_pos': n_true_pos,
        'n_class_neg': n_class_neg,
        'n_class_pos': n_class_pos,
        'sens': TP / float(n_true_pos),
        'spec': TN / float(n_true_neg),
        'ppv': ppv,
        'npv': npv,
    }


import os
import tempfile
def open_as_html(string):
    path = '/tmp/buffer.html'
    with open(path, 'w') as fp:
        fp.write(string)
        os.system("open -a /Applications/Google\ Chrome.app %s" % path)


def get_enum_map(enum):
    return {i: v.name for i, v in enumerate(enum)}


# Recursive defaultdict
from collections import defaultdict

if False:
    class recursive_defaultdict(defaultdict):
        '''
        http://mail.python.org/pipermail/python-list/2007-August/1120960.html
        '''
        def __init__(self):
            self.default_factory = type(self)

recursive_defaultdict = lambda: defaultdict(recursive_defaultdict)

def recursive_todict(d):
    if isinstance(d, dict):
        return {
            k: recursive_todict(v)
            for k, v in d.iteritems()
        }
    else:
        return d


from itertools import starmap

import pandas

def make_df(rows):
    """
    rows: list-of-list-of-key-value-pairs
    """
    column_labels, rows = zip(*list(starmap(zip, rows)))
    [column_labels] = set(column_labels)
    return pandas.DataFrame.from_records(
        list(rows),
        columns=column_labels,
        index=column_labels[0])


import subprocess
from textwrap import dedent

def paste(max_display_lines=5):
    code = dedent(subprocess.check_output(["reattach-to-user-namespace", "pbpaste"]))
    formatted_code = code.splitlines()
    if len(formatted_code) > max_display_lines:
        formatted_code = formatted_code[:max_display_lines] + ['...']
    print '\n'.join(formatted_code)
    exec(code, globals())

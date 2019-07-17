def format_sql(queryset):
    import sqlparse
    from django.core.exceptions import EmptyResultSet
    try:
        sql = str(queryset.values_list('pk').query)
    except EmptyResultSet:
        return 'EmptyResultSet'
    else:
        return sqlparse.format(sql, reindent=True)


def execute_sql(sql):
    if not sql.rstrip().endswith(';'):
        sql = sql + ';'
    with connection.cursor() as c:
        c.execute(sql)
        return c.fetchall()


if False:
    from django.utils.termcolors import colorize

    for col in ['red', 'blue']:
        exec(f"""
    def {col}(s):
        print(colorize(s, fg='{col}', opts=['bold']))
    """)


def exec_url(url):
    import requests
    resp = requests.get(url)
    resp.raise_for_status()
    print(resp.content)
    answer = raw_input('OK to execute? (y/n): ')
    if answer == 'y':
        exec(resp.content)
    else:
        print('Got %s, not executing' % answer)


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
    print('\n'.join(formatted_code))
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


def pretty_print(obj):
    if isinstance(obj, dict):
        pretty_print_dict(obj)
    elif hasattr(obj, '__iter__'):
        for item in sorted(obj):
            pretty_print(obj)
    else:
        print(obj)


def pretty_print_dict(d):
    for item in sorted(d.items()):
        print('%-60s %s' % (item))


def format_tree(root):
    # Hack: create tree of directories and use `tree` utility to draw tree.
    import os
    import subprocess
    from tempfile import mkdtemp

    def _make_directory_tree(node, root_dir):
        if not isinstance(node, dict):
            os.mkdir('%s/%s' % (root_dir, node))
        else:
            for key in node:
                child_dir = '%s/%s' % (root_dir, key)
                os.mkdir(child_dir)
                _make_directory_tree(node[key], child_dir)

    tempdir = mkdtemp()
    root_dir = '%s/%s' % (tempdir, 'root')
    os.mkdir(root_dir)
    _make_directory_tree(root, root_dir)
    with chdir(root_dir):
       tree = subprocess.check_output(['tree', '--noreport'])
    subprocess.check_call(['rm', '-r', tempdir])
    return tree


def print_tree(root):
    print(format_tree(root))


from contextlib import contextmanager
@contextmanager
def chdir(to_dir):
    import os
    from_dir = os.getcwd()
    os.chdir(to_dir)
    yield
    os.chdir(from_dir)


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
    print(res.status_code, datetime.now() - then)


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
        os.system(r"open -a /Applications/Google\ Chrome.app %s" % path)


def get_enum_map(enum):
    return {i: v.name for i, v in enumerate(enum)}


def venn(*sets):
    from itertools import combinations
    import numpy as np
    import pandas as pd

    n = len(sets)
    venn =  (pd.DataFrame(np.zeros((n, n)),
                          index=range(1, n+1),
                          columns=range(1, n+1))
             .astype(object))

    for ((i, s_i), (j, s_j)) in combinations(enumerate(sets, 1), 2):
        venn.ix[i, i] = len(s_i)
        venn.ix[j, j] = len(s_j)
        venn.ix[i, j] = len(s_i & s_j)
        venn.ix[j, i] = (len(s_i - s_j), len(s_j - s_i))

    return venn


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
    print('\n'.join(formatted_code))
    exec(code, globals())

def bits(x):
    bits = bin(x)[2:]
    return ' '.join(''.join(nib) for nib in chunked(bits, 4))


def parse_mips_instruction_16(instr):
    opcode, rd, rs, rt, funct = instr[:4], instr[5:8], instr[8:11], instr[11]


def histogram_datetimes(dtimes, **kwargs):
    import datetime
    import numpy as np
    to_timestamp = np.vectorize(lambda x: (x - datetime.datetime(1970, 1, 1)).total_seconds())
    from_timestamp = np.vectorize(lambda x: datetime.datetime.utcfromtimestamp(x))

    hist, bin_edges = np.histogram(to_timestamp(list(dtimes)), **kwargs)

    for count, dt in zip(hist, from_timestamp(bin_edges)):
        print('%-20s %d' % (dt.strftime('%Y-%m-%d'), count))


def histogram(x, **kwargs):
    import numpy as np
    hist, bin_edges = np.histogram(x, **kwargs)
    for count, val in zip(hist, bin_edges):
        print('%-20s %d' % (val, count))


def report_rate_of_change(source, interval):
    import time

    y0 = source()
    t0 = time.time()

    while True:
        time.sleep(interval)
        y1 = source()
        t1 = time.time()
        print('%.1f items/sec' % ((y1 - y0) / (t1 - t0)))


def print_diff(obj1, obj2):
    import datadiff
    from clint.textui import colored

    red = lambda s: colored.red(s, bold=True)
    green = lambda s: colored.green(s, bold=True)

    print_git_diff(str(datadiff.diff(obj1, obj2)))


def print_git_diff(diff):
    from clint.textui import colored; green = lambda s: colored.green(s, bold=True)
    from clint.textui import colored; red = lambda s: colored.red(s, bold=True)

    for line in diff.splitlines():
        if line.startswith('-'):
            print(red(line))
        elif line.startswith('+'):
            print(green(line))
        else:
            print(line)


from contextlib import contextmanager
from django.db import connection
from django.db import transaction


def max_queries(n, trace=True):
    from functools import wraps
    from django.db import connection
    from clint.textui.colored import red as col

    def _max_queries(func):

        def __max_queries(*args, **kwargs):
            q0 = len(connection.queries)
            ret = func(*args, **kwargs)
            q1 = len(connection.queries)
            if trace:
                print(col("%s: %d queries" % (func.__name__, q1 - q0)))
            if q1 - q0 > n:
                raise AssertionError("%d queries in %s" % (
                    q1 - q0,
                    func.__name__,
                ))
            return ret

        return wraps(func)(__max_queries)

    return _max_queries


def print_queries(func):
    from functools import wraps
    from django.db import connection
    from clint.textui.colored import green as col

    def _print_queries(*args, **kwargs):
        q0 = len(connection.queries)
        ret = func(*args, **kwargs)
        q1 = len(connection.queries)
        print(col("%s: %d queries" % (func.__name__, q1 - q0)))
        return ret

    return wraps(func)(_print_queries)


@contextmanager
def rollback():
    """
    Run statements in a transaction and do not commit.
    """
    if transaction.is_managed():
        raise RuntimeError("May not be run in a transaction")
    class Rollback(Exception):
        pass
    try:
        with transaction.commit_on_success():
            yield
            raise Rollback()
    except Rollback:
        pass


def log(func):
    from functools import wraps
    from django.db import connection

    def _log(*args, **kwargs):
        from clint.textui import colored; blue = lambda s: colored.blue(s, bold=True)
        print(blue(func.__name__))
        return func(*args, **kwargs)

    return wraps(func)(_log)


def trace(func):
    from functools import wraps
    from django.db import connection

    def _print_queries(*args, **kwargs):
        q0 = len(connection.queries)
        ret = func(*args, **kwargs)
        q1 = len(connection.queries)
        print("%s(%s, %s): %d queries" % (
            func.__name__,
            args,
            kwargs,
            q1 - q0,
        ))
        return ret

    return wraps(func)(_print_queries)

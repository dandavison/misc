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


from itertools import starmap

def make_df(rows):
    """
    rows: list-of-list-of-key-value-pairs
    """
    import pandas
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
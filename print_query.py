import sqlparse


def print_query(query):
    print sqlparse.format(unicode(query), reindent=True)

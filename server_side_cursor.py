"""
Utilities for working with server-side cursors.

http://thebuild.com/blog/2010/12/13/very-large-result-sets-in-django-using-postgresql/
http://thebuild.com/blog/2010/12/14/using-server-side-postgresql-cursors-in-django/
"""
import psycopg2

from django.db import connection
from django.db.transaction import atomic


def queryset_iterator(query, chunk_size=100):
    """
    Return an iterator over rows of the result set.
    """
    cursor = get_server_side_cursor(query)
    while True:
        chunk = cursor.fetchmany(chunk_size)
        if not chunk:
            return
        for row in chunk:
            yield row


def get_server_side_cursor(query, name='cursor', **kwargs):
    """
    Return a server-side cursor for the result set of the query.

    `query` must be an object whose string representation is a SQL
    query. In particular, it may be either a string of SQL code, or
    the object returned by the .query property on a django queryset.

    kwargs are passed to the psycopg2 server-side cursor
    constructor. E.g. use to iterate over namedtuples/dicts, use

    cursor_factory=psycopg2.extras.NamedTupleCursor
    cursor_factory=psycopg2.extras.DictCursor
    """
    if connection.connection is None:
        connection.cursor()
    cursor = connection.connection.cursor(name=name, **kwargs)
    cursor.execute(quote(str(query)))
    return cursor


def quote(query):
    """
    Fix certain quoting issues.

    E.g

    query = (LaneSampleCall.objects
             .filter(allele1__position__chrom='chr1'))
    with atomic():
        cursor = get_server_side_cursor(query.query)
        print next(cursor)
    ProgrammingError: column "chr1" does not exist
    LINE 1: ...ition"."id" ) WHERE "sequencing_seqposition"."chrom" = chr1

    Whereas this works as expected:

    query = (LaneSampleCall.objects
             .filter(allele1__position__chrom="'chr1'"))
    """
    # TODO
    return query


if __name__ == '__main__':
    query = (LaneSampleCall.objects
             .values_list('id', 'allele1__position__start'))

    with atomic():
        cursor = get_server_side_cursor(
            query.query,
            cursor_factory=psycopg2.extras.NamedTupleCursor)
        print cursor.fetchmany(1)

    it = queryset_iterator(query.query)
    with atomic():
        print next(it)

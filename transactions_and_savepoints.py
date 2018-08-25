from contextlib import contextmanager

from django.db import connection
from django.db import transaction


@contextmanager
def rollback():
    with transaction.atomic():
        yield
        transaction.set_rollback(True)


def demo(model_cls):

    def print_state():
        print(model_cls.objects.values_list('email', flat=True))

    def create(key):
        model_cls.objects.create(email=key)

    model_cls.objects.all().delete()

    print('start')
    print(model_cls.objects.all())

    print('create a')
    create('a')
    print_state()  # [a]

    # We're not in a transaction and, despite not raising an Exception, this doesn't create a real savepoint.
    sid_0 = connection.savepoint()
    print('savepoint 0 (sid=%r)' % sid_0)

    print('create b')
    create('b')
    print_state()  # [a, b]


    print('rollback outside transaction')
    # This doesn't do anything (You might think there'd be an exception).
    transaction.savepoint_rollback(sid_0)
    print_state()  # [a, b]


    print('start transaction')
    with rollback():
        print('create c')
        create('c')
        print_state()  # [a, b, c]

        # This is a real savepoint
        with rollback():
            print('savepoint 1')

            print('create d')
            create('d')
            print_state()

            with rollback():
                print('savepoint 2')

                print('delete a')
                model_cls.objects.filter(email='a').delete()
                print_state()  # [b, c, d]

                print('rollback to savepoint 2')
                # And here we really do rollback the latest object creation
            print_state()  # [a, b, c]

            print('"rollback" to savepoint 1')
        print_state()

    print('after transaction')
    print_state()  # [a, b]

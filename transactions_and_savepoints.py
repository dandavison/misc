from django.db import connection
from django.db import transaction


def demo(model_cls):

    def print_state():
        print(model_cls.objects.values_list('email', flat=True))

    model_cls.objects.all().delete()

    print('start')
    print(model_cls.objects.all())

    print('create a')
    model_cls.objects.create(email='a')
    print_state()  # [a]

    # We're not in a transaction and, despite not raising an Exception, this doesn't create a real savepoint.
    sid_0 = connection.savepoint()
    print('savepoint 0 (sid=%r)' % sid_0)

    print('create b')
    model_cls.objects.create(email='b')
    print_state()  # [a, b]


    print('rollback outside transaction')
    # This doesn't do anything (You might think there'd be an exception).
    transaction.savepoint_rollback(sid_0)
    print_state()  # [a, b]


    print('start transaction')
    try:
        with transaction.atomic():

            print('create c')
            model_cls.objects.create(email='c')
            print_state()  # [a, b, c]

            # This is a real savepoint
            sid_1 = connection.savepoint()
            print('savepoint 1 (sid=%r)' % sid_1)

            print('create d')
            model_cls.objects.create(email='d')
            print_state()

            sid_2 = connection.savepoint()
            print('savepoint 2 (sid=%r)' % sid_2)

            print('delete a')
            model_cls.objects.filter(email='a').delete()
            print_state()  # [b, c, d]

            print('rollback to savepoint 1')
            # And here we really do rollback the latest object creation
            transaction.savepoint_rollback(sid_1)
            print_state()  # [a, b, c]

            print('"rollback" to savepoint 2')
            transaction.savepoint_rollback(sid_2)
            print_state()

            # The exception aborts the entire transaction
            0/0
    except ZeroDivisionError:
        pass

    print('after transaction')
    print_state()  # [a, b]

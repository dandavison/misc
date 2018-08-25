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
    sid = transaction.savepoint()
    print('savepoint')

    print('create b')
    model_cls.objects.create(email='b')
    print_state()  # [a, b]


    print('rollback outside transaction')
    # This doesn't do anything (You might think there'd be an exception).
    transaction.savepoint_rollback(sid)
    print_state()  # [a, b]


    print('start transaction')
    try:
        with transaction.atomic():

            print('create c')
            model_cls.objects.create(email='c')
            print_state()  # [a, b, c]

            # This is a real savepoint
            sid = transaction.savepoint()
            print('savepoint 1')

            print('create d')
            model_cls.objects.create(email='d')

            print('delete a')
            model_cls.objects.filter(email='a').delete()
            print_state()  # [b, c, d]

            print('rollback to savepoint')
            # And here we really do rollback the latest object creation
            transaction.savepoint_rollback(sid)
            print_state()  # [a, b, c]

            # The exception aborts the entire transaction
            0/0
    except:
        pass

    print('after transaction')
    print_state()  # [a, b]

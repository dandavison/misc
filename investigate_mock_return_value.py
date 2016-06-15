from unittest import mock


class MyClass:
    def mymethod(self):
        raise AssertionError("Should not be called")


with mock.patch.object(MyClass, 'mymethod', return_value='my_return_value') as my_patch:
    print(my_patch.called)
    instance = MyClass()
    print(instance.mymethod())
    print(my_patch.called)

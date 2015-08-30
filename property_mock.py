import mock

class BaseForm(object):
    form_id = (
        mock.PropertyMock(side_effect=NotImplementedError(
            "subclasses must define a class attribute named form_id")))

class ConcreteForm(BaseForm):
    form_id = 'foo'



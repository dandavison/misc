from mock import Mock
from mock import patch


class X(object):
    def m(self):
        obj = Mock()
        obj.prop = 'real m'
        return obj


print X().m().prop


with patch.object(X, 'm', return_value='patched m'):
    print X().m()


mock_obj = Mock()
mock_obj().prop = 'patched m 2'

with patch.object(X, 'm', mock_obj):
    print X().m().prop

# http://codeinthehole.com/writing/how-to-reload-djangos-url-config/
import sys
from django.conf import settings

def reload_urlconf(urlconf=None):
    if urlconf is None:
        urlconf = settings.ROOT_URLCONF
    if urlconf in sys.modules:
        reload(sys.modules[urlconf])

# From Matt Rasmussen
import django
from django.conf import settings
from django.db import models
from django.db import connections
from django.db.utils import ConnectionHandler

# Minimal settings config setup.
settings.configure(DATABASES={'default': {}})
django.setup()

try:
    # Can only configure once.
    settings.configure(DATABASES={'default': {}})
except RuntimeError:
    pass

# Can run django setup as many times as you want.
django.setup()


# Define a model.
class Gene(models.Model):
    class Meta(object):
        db_table = 'gene'  # Manually map to a table.
        app_label = 'test_app'  # Must supply a dummy app_label.

    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)


# Conf for connecting to a db.
db_conf = {
    'HOST': 'localhost',
    'PORT': 6432,
    'NAME': 'postgres',
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'USER': 'postgres',
    'PASSWORD': '123',
}
db_alias = 'my_db'

# Must install config to global connections list, but we can use whatever
# alias we want.
connections.databases[db_alias] = db_conf

# Just use the same alias with the query set.
print Gene.objects.using(db_alias).values()

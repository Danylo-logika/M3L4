import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "M3L4.settings")
django.setup()


from M3L4A.models import User


user = User(name='getpack', email='getup@gmail.com')


user.save()
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.test import TestCase
from .models import User

# Create your tests here.
print(User.objects.all())
User.objects.create(101, "재준","이",27,"울산","000-0000-0000",12)
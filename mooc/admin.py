from django.contrib import admin

from .models import Homework
from .models import Lecture
# Register your models here.
admin.site.register(Homework)
admin.site.register(Lecture)

from django.contrib import admin

from modelapp.models import Student
from modelapp.models import Bike
# Register your models here.
admin.site.register(Student)
admin.site.register(Bike)
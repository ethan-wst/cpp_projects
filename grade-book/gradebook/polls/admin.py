from django.contrib import admin

from .models import Course
from .models import Assignment_Weight
from .models import Assignment_Grade

admin.site.register(Course)
admin.site.register(Assignment_Weight)
admin.site.register(Assignment_Grade)
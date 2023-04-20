from django.contrib import admin
from .models import (
    StudentStatus,
    Student,
    TeacherType,
    Teacher,
    Course,
    Group,
)


admin.site.register((
    StudentStatus,
    Student,
    TeacherType,
    Teacher,
    Course,
    Group,
))
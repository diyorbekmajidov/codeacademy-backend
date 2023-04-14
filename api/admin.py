from django.contrib import admin
from .models import (
    City,
    District,
    Address,
    Student,
    StudentContact,
    Course,
    Group,
    Assignment,
    Task,
    Lesson,
    Submission,
)


admin.site.register((
    City,
    District,
    Address,
    Student,
    StudentContact,
    Course,
    Group,
    Assignment,
    Task,
    Lesson,
    Submission,
))
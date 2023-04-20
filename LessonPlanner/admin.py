from django.contrib import admin
from .models import (
    AssignmentType,
    Assignment,
    TaskLevel,
    Task,
    Lesson,
    Muster,
    Submission,
)


admin.site.register((
    AssignmentType,
    Assignment,
    TaskLevel,
    Task,
    Lesson,
    Muster,
    Submission,
))
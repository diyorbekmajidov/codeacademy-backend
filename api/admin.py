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


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'address', 'created_at', 'updated_at')
    list_display_links = ('full_name',)
    list_filter = ('address__city', 'address__district')
    search_fields = ('first_name', 'last_name', 'address__city__name', 'address__district__name')


admin.site.register(Student, StudentAdmin)

admin.site.register(City)
admin.site.register(District)
admin.site.register(Address)
admin.site.register(StudentContact)
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Assignment)
admin.site.register(Task)
admin.site.register(Lesson)
admin.site.register(Submission)

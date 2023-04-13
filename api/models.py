from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name       = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class District(models.Model):
    name       = models.CharField(max_length=100)
    city       = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    city       = models.ForeignKey(City, on_delete=models.CASCADE)
    district   = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city} - {self.district}'


class Student(models.Model):
    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    email        = models.EmailField()
    main_phone   = models.CharField(max_length=14)
    second_phone = models.CharField(max_length=14, blank=True, null=True)
    github       = models.CharField(max_length=100, unique=True, blank=True, null=True)
    address      = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name
    

class Course(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    start_date  = models.DateField(blank=True, null=True)
    end_date    = models.DateField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Group(models.Model):
    name        = models.CharField(max_length=100)
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class StudentGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group   = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student} - {self.group}'


class Teacher(models.Model):
    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    email        = models.EmailField()
    main_phone   = models.CharField(max_length=14)
    second_phone = models.CharField(max_length=14, blank=True, null=True)
    github       = models.CharField(max_length=100, unique=True, blank=True, null=True)
    address      = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name
    

class TeacherGroup(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group   = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.teacher} - {self.group}'
    

class Lesson(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    start_date  = models.DateTimeField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    group       = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher     = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.group}'


class Homework(models.Model):
    name        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    name        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    homework    = models.ForeignKey(Homework, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class LessonHomework(models.Model):
    lesson      = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    homework    = models.ForeignKey(Homework, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.lesson} - {self.homework}'
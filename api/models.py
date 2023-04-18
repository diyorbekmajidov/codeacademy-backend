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
    address      = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name


class StudentContact(models.Model):
    main_phone   = models.CharField(max_length=14)
    second_phone = models.CharField(max_length=14, blank=True, null=True)
    email        = models.EmailField(blank=True, null=True)
    github       = models.CharField(max_length=100, unique=True, blank=True, null=True)
    student      = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.main_phone


class Course(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    start_date  = models.DateField(blank=True, null=True)
    end_date    = models.DateField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    headmaster  = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Group(models.Model):
    name        = models.CharField(max_length=100)
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    teacher     = models.ForeignKey(User, on_delete=models.CASCADE)
    students    = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    name        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    homework    = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Lesson(models.Model):
    name        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    group       = models.ForeignKey(Group, on_delete=models.CASCADE)
    assignments = models.ManyToManyField(Assignment)

    def __str__(self):
        return self.name
    

class Submission(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    student     = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    task        = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')

    def __str__(self):
        return f'{self.student.full_name} - {self.task.name}'
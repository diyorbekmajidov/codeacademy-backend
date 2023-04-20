from django.db import models


class StudentStatus(models.Model):
    name         = models.CharField(max_length=50, unique=True)    # 'active', 'inactive' 'graduated', 'suspended', 'dropped'
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50, blank=True)
    github       = models.CharField(max_length=64, unique=True)
    codewars     = models.CharField(max_length=64, blank=True, unique=True, null=True)
    status       = models.ForeignKey(StudentStatus, on_delete=models.DO_NOTHING)
    phone        = models.CharField(max_length=20, blank=True)
    email        = models.CharField(max_length=127, blank=True, unique=True, null=True)
    tg_username  = models.CharField(max_length=64, blank=True, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.first_name
    
    def __str__(self):
        return self.full_name


class TeacherType(models.Model):
    name         = models.CharField(max_length=50, unique=True)    # 'main' or 'assistant'
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50, blank=True)
    type         = models.ForeignKey(TeacherType, on_delete=models.DO_NOTHING)
    github       = models.CharField(max_length=64, unique=True)
    codewars     = models.CharField(max_length=64, blank=True, unique=True, null=True)
    phone        = models.CharField(max_length=20, blank=True)
    email        = models.CharField(max_length=127, blank=True, unique=True, null=True)
    tg_username  = models.CharField(max_length=64, blank=True, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.first_name
    
    def __str__(self):
        return self.full_name


class Course(models.Model):
    name         = models.CharField(max_length=50, unique=True)
    description  = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name         = models.CharField(max_length=50, unique=True)
    description  = models.TextField(blank=True)
    course       = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    students     = models.ManyToManyField(Student, blank=True)
    teachers     = models.ManyToManyField(Teacher, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

   
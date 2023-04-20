from django.db import models
from ClassRoom.models import Student, Group, Course


class AssignmentType(models.Model):
    name = models.CharField(max_length=50, unique=True, default='homework') # 'homework', 'project', 'practice', 'test'
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    link = models.URLField(blank=True)
    type = models.ForeignKey(AssignmentType, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TaskLevel(models.Model):
    name = models.CharField(max_length=50, unique=True, default='easy') # 'easy', 'medium', 'hard'
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    level = models.ForeignKey(TaskLevel, on_delete=models.DO_NOTHING)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    assignments = models.ManyToManyField(Assignment)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Muster(models.Model):
    student = models.ManyToManyField(Student)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.lesson}"


class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, blank=True, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.DO_NOTHING)
    is_correct = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.assignment}"
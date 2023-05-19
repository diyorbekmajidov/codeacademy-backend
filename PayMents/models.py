from django.db import models
from ClassRoom.models import Student
# Create your models here.

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return  self.student.first_name

from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    studentNumber = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
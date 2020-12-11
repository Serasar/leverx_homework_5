from django.db import models

# Create your models here.

class Lecture(models.Model):

    name = models.CharField(max_length=20)
    description = models.TextField()
    slide = models.FileField()

class Homework(models.Model):

    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()

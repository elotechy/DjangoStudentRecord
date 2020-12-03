from django.db import models

# Create your models here.

class Level(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class StudentUser(models.Model):
    fullname = models.CharField(max_length=100)
    studentID = models.CharField(max_length=5)
    number = models.CharField(max_length=15)
    level = models.ForeignKey(Level, on_delete = models.CASCADE)

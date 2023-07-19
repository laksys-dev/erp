from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    address=models.CharField(max_length=100)
    #fname =models.CharField(max_length=50)
    def __str__(self):
        return '[' + self.name +',' + self.address + ']'

from textwrap import dedent
from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Mandal(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length= 256)
    father_name = models.CharField(max_length=256)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=25)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)

    def __str__(self):
        return self.ename

from django.db import models
from department.models import Department

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.FloatField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
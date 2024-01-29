from django.db import models

# Create your models here.

class task(models.Model):
    task_name = models.CharField(max_length=100)
    priority=models.TextField()
    date=models.DateField()
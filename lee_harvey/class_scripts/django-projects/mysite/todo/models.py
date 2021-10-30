from django.db import models
from django.db.models.expressions import Value

# Create your models here.
class Todo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
from django.db import models
from django.db.models.fields import Field

# Create your models here.
class Todo(models.Model):
  task_id = models.AutoField(primary_key=True)
  task = models.CharField(max_length=255)
  completed = models.BooleanField(default=False)

class Note(models.Model):
  note_id = models.AutoField(primary_key=True)
  note_text = models.CharField(max_length=500)
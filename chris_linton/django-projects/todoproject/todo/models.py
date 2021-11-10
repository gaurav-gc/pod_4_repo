from django.db import models

# Create your models here.

# for modeling each item in todo list
class Todo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
    # create a field that records if task has been completed as a boolean value initially set to false
    completed = models.BooleanField(default=False)

# for modeling each note created
class Note(models.Model):
    # create a field that will contain a unique identifier for each note
    note_id = models.AutoField(primary_key=True)
    # create a field that will contain the text of the note
    note_text = models.TextField()
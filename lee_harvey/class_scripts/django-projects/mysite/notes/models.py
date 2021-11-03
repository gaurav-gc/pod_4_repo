from django.db import models
from django.db.models.expressions import Value

# Create your models here.

class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    notes = models.CharField(max_length=255)
from django.db import models

# Create your models here.

class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    note = models.CharField(max_length=255)
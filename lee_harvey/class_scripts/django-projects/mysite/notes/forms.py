from typing import Sized
from django import forms
from .models import Notes

class NotesForm(forms.Form):
    notes = forms.CharField(label = 'Add note', max_length = 255)
from typing import Sized
from django import forms
from .models import Notes

class NotesForm(forms.Form):
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":60}), label = 'Note', max_length = 255)
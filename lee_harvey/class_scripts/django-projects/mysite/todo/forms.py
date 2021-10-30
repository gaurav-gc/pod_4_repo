from django import forms

from .models import Todo

class TodoForm(forms.Form):
    task = forms.CharField(label = 'Add task', max_length = 255)

from django import forms

from .models import Todo

class TodoForm(forms.Form):
    task = forms.CharField(label = 'Task', max_length = 255)

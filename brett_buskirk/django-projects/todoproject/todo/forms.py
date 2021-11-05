from django import forms

class TodoForm(forms.Form):
  task = forms.CharField(label = 'Add task', max_length = 255)

class NoteForm(forms.Form):
  note_text = forms.CharField(label = 'Add note', max_length=500)
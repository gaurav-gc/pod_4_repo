from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(label = 'Add task:', max_length = 255)
# create class for making a Note form
class NoteForm(forms.Form):
    # create character field for entering note
    note = forms.CharField(label = 'Add note:', max_length=None)
from django import forms

class NoteForm(forms.Form):
    note = forms.CharField(label = 'Add note', max_length = 255)
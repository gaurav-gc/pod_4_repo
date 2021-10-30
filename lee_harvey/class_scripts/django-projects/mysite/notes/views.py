from django.shortcuts import render
from .models import Notes
from .forms import NotesForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def notes(request):
    if request.method == 'GET':
        notes = Notes.objects.all().order_by('note_id')
        form = NotesForm()
        return render(request=request,
                    template_name = 'notes.html',
                    context = {'notes':notes, 'form':form})
    
    # when user submits form
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data['notes']
            Notes.objects.create(notes = note)
        # "redirect" to the Notes homepage   
        return HttpResponseRedirect(reverse('notes'))

def note(request, note_id):
    if request.method == 'GET':
        notes = Notes.objects.get(pk = note_id)
        form = NotesForm(initial = {'notes':notes.notes})
        return render(request = request,
                    template_name = 'note.html',
                    context = {
                        'form':form,
                        'note_id': note_id
                    })
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = NotesForm(request.POST)
            if form.is_valid():
                note = form.cleaned_data['notes']
                Notes.objects.filter(pk = note_id).update(notes = note)
        elif 'delete' in request.POST:
            Notes.objects.filter(pk=note_id).delete()
        return HttpResponseRedirect(reverse('notes'))
from django.shortcuts import render
from .models import Notes
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# note list homepage
def notes(request):
    if request.method == 'GET':
        notes = Notes.objects.all().order_by('note_id')
        form = NoteForm()
        return render(request=request,
                    template_name = 'notelist.html',
                    context = {'note':notes, 'form':form})
    
    # when user submits form
    if request.method == 'POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data['note']
            Notes.objects.create(note=note)
        # "redirect" to the note homepage   
        return HttpResponseRedirect(reverse('notes'))


def note(request, note_id):
    if request.method == 'GET':
        note = Notes.objects.get(pk=note_id)
        form = NoteForm(initial = {'note':note.note})
        return render(request = request,
                    template_name = 'notedetail.html',
                    context = {
                        'form':form,
                        'note_id': note_id
                    })
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = NoteForm(request.POST)
            if form.is_valid():
                note=form.cleaned_data['note']
                Notes.objects.filter(pk=note_id).update(note=note)
        elif 'delete' in request.POST:
            Notes.objects.filter(pk=note_id).delete()
        return HttpResponseRedirect(reverse('notes'))
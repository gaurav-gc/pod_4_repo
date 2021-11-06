from django.shortcuts import render
from .models import Todo, Note
from .forms import TodoForm, NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# todo list homepage
def todo(request):
    # when user requests to access todo/ page
    if request.method == 'GET':
        # QuerySet of Todo objects that are completed
        completed_tasks = Todo.objects.filter(completed='True')
        # QuerySet of Todo objects that are not completed
        incomplete_tasks = Todo.objects.filter(completed='False')
        # create an instance of the TodoForm class
        form = TodoForm()
        # return and render form and QuerySet info to html template
        return render(request=request,
                      template_name = 'list.html',
                      context = {'completed_tasks':completed_tasks, 'incomplete_tasks':incomplete_tasks, 'form':form})
    
    # when user submits form
    if request.method == 'POST':
        # add user input data into new instance of TodoForm
        form = TodoForm(request.POST)
        # check if data input in form is valid (of the correct type)
        if form.is_valid():
            # data passed into task attribute field of new Todo object
            task = form.cleaned_data['task']
            # create a new Todo object in the QuerySet
            Todo.objects.create(task=task)
        # redirect to the todo homepage, reversing post back to get request  
        return HttpResponseRedirect(reverse('todo'))

# task page denoted by task_id number in url
def task(request, task_id):
    # when user requests to access todo/<int:task_id> page
    if request.method == 'GET':
        # looking up specific instance of Todo object by primary key
        todo = Todo.objects.get(pk=task_id)
        # create an instance of the TodoForm class &
        # pre-populate character field with name of task
        form = TodoForm(initial = {'task':todo.task})
        # return and render form and QuerySet info to html template
        return render(request = request,
                      template_name = 'detail.html',
                      context = {
                          'form':form,
                          'task_id': task_id
                      })
    # when user submits form
    if request.method == 'POST':
        # if save button was clicked by user / save is in post request 
        if 'save' in request.POST:
            # save user update input to instance of TodoForm
            form = TodoForm(request.POST)
            # check if data input in form is valid (of the correct type)
            if form.is_valid():
                # data passed into task attribute field of Todo object
                task=form.cleaned_data['task']
                # update Todo object in the QuerySet
                Todo.objects.filter(pk=task_id).update(task=task)
        # if delete button was clicked by user / delete is in post request 
        elif 'delete' in request.POST:
            # delete Todo object from the QuerySet
            Todo.objects.filter(pk=task_id).delete()
        # if mark complete button was clicked by user / complete is in post request 
        elif 'complete' in request.POST:
            # update Todo object in the QuerySet as completed
            Todo.objects.filter(pk=task_id).update(completed=True)
        # redirect to the todo homepage, reversing post back to get request
        return HttpResponseRedirect(reverse('todo'))

def note(request):
    # when user requests to access todo/note/ page
    if request.method == 'GET':
        # QuerySet of all Note objects
        notes = Note.objects.all()
        # create an instance of the NoteForm class
        form = NoteForm()
        # return and render form and QuerySet info to html template
        return render(request = request,
                      template_name = 'notes.html',
                      context = {
                          'notes': notes,
                          'form': form,
                      })
    # when user submits form
    if request.method == 'POST':
        # add user input data into new instance of NoteForm
        form = NoteForm(request.POST)
        # check if data input in form is valid (of the correct type)
        if form.is_valid():
            # data passed into note_text attribute field of new Note object
            note_text = form.cleaned_data['note']
            # create a new Note object in the QuerySet
            Note.objects.create(note_text=note_text)
        # redirect to the note homepage, reversing post back to get request
        return HttpResponseRedirect(reverse('note'))
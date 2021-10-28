from django.shortcuts import render

# Create your views here.


def hello(request, name='World'):
    if request.method == 'GET':
        return render(request,  'hello.html', context = { 'name' : name })


def goodbye(request, name='Django'):
    if request.method == 'GET':
        return render(request,  'goodbye.html', context = { 'name' : name })


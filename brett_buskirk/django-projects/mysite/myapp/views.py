from django.shortcuts import render

# Create your views here.
def hello(request):
  if request.method == 'GET':
    return render(request, template_name='hello.html')

def hello(request, name='world'):
  if request.method == 'GET':
    return render(request, template_name='hello.html', context= { 'name': name })

def goodbye(request, name):
  if request.method == 'GET':
    return render(request, template_name='goodbye.html', context={ 'name': name })
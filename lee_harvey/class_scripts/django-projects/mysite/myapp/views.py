from django.shortcuts import render

# Create your views here.
# def both(request,title, name='World'):
#     print(request)
#     if 'hello' in request:
#         name='World'
#     elif 'goodbye' in request:
#         name='Django'
#     else:
#         render(request, "error.html", name)
#         return
#     if request.method == 'GET':
#         return render(request,  f'{title}.html', context = { 'name' : name }) 

def hello(request, name='Django'):
    if request.method == 'GET':
        return render(request,  'hello.html', context = { 'name' : name })


def goodbye(request, name='Django'):
    if request.method == 'GET':
        return render(request,  'goodbye.html', context = { 'name' : name })


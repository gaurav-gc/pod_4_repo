from django.shortcuts import render

#courtesy of Corey Schafer https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
posts = [
    {
        'author': 'Brendan Ngwa Nforbi',
        'title': 'Dayroom Post 1',
        'content': 'First post content',
        'date_posted': 'October 26, 2018'
    },
    {
        'author': 'Andre Ngwa Nforbi',
        'title': 'Dayroom Post 2',
        'content': 'Second post content',
        'date_posted': 'October 27, 2018'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'dayroom/home.html', context)

def about(request):
    return render(request, 'dayroom/about.html', {'title': 'About'})



from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Spenzy',
        'title': 'Blog Post 1',
        'content': 'Randomly written content',
        'date_posted': 'January 1, 2019'
    },
    {
        'author': 'Potato',
        'title': 'Blog Post 2',
        'content': 'Randomly written content but newer',
        'date_posted': 'January 4, 2019'
    }
]


# Views Section
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

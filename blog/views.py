from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



'''
posts = [
    {
        'author': 'Michael',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September, 23, 2022'
    },
    {
        'author': 'Fernanda',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September, 24, 2022'
    }
]
'''



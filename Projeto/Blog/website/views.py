from django.shortcuts import render
from .models import Post

def hello_blog(request):
    list_posts = Post.objects.filter(approved=True)
    
    data = {
        'posts': list_posts
    }
    
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})
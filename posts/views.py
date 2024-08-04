from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)  # Correctly use 'Post' model and retrieve 'post'
    return render(request, 'post.html', {'post': post})

def home_page(request):
    return render(request, 'home.html')

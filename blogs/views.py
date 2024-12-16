from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    posts = BlogPost.objects.order_by('-date_added')
    return render(request, 'blogs/index.html', {'posts': posts})


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')
    return render(request, 'blogs/register.html', {'form': form})


def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    return render(request, 'blogs/new_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})

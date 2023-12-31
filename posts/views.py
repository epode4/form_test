from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {

        'posts' : posts
    }

    return render(request, 'index.html', context)


def detail(request, id):

    post = Post.objects.get(id=id)

    context = {
        'post':post
    }

    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', id=post.id)

    else:
        form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def delete(request, id):
    post = Post.objects.get(id=id)

    post.delete()

    return redirect('posts:index')


def update(request, id):

    post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:detail', id=id)


    else:

        form = PostForm(instance=post)

    context = {
        'form' : form
    }

    return render(request, 'update.html', context)

        



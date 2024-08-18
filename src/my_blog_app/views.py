from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import PostForm, UserRegistrationForm
from .models import Post

def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('blog_login')
    else:
        form = UserRegistrationForm()

    return render(request, 'my_blog_app/register.html', {'form' : form})

def add_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.save()
            messages.success(request, 'Post added!')
            return redirect('blog_index')
    else:
        form = PostForm()

    return render(request, 'my_blog_app/add_post.html', {'form' : form})

def index(request):

    context = {
        'posts' : Post.objects.all()
    }
    
    return render(request, 'my_blog_app/index.html', context)

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_index')
    
    return render(request, 'my_blog_app/login.html')


def user_logout(request):
    logout(request)
    return redirect('blog_index')

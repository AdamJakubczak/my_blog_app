from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import PostForm, UserRegistrationForm
from .models import Post

def delete_post(request, post_id):

    post = get_object_or_404(Post, post_id=post_id)

    if post.post_author != request.user:
        messages.error(request, 'Not Your post! Can\'t touch this')
        return redirect('blog_index')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post removed :(')
        return redirect('blog_index')
    
    return render(request, 'my_blog_app/delete_post.html', {'post' : post})
        

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

    posts = Post.objects.all()
    page_num = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)

    page_obj = paginator.page(page_num)
    
    return render(request, 'my_blog_app/index.html', {'page_obj' : page_obj})

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Henlow!')
            return redirect('blog_index')
    
    return render(request, 'my_blog_app/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out :(')
    return redirect('blog_index')

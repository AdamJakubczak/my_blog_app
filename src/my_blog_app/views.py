from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout


def index(request):
    
    return render(request, 'my_blog_app/index.html')

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

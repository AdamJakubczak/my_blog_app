from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout

posts = [
    {
        'post_title' : 'title 1',
        'post_content' : 'post content for the first item',
        'post_author' : 'Adam Jakubczak',
        'post_date' : '23.10.2024'
    },
    {
        'post_title' : 'title 2',
        'post_content' : 'post content for the second item',
        'post_author' : 'Oliwia Listwenik',
        'post_date' : '29.10.2024'
    },

]


def index(request):

    context = {
        'posts' : posts
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

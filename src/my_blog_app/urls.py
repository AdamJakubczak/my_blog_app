from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index' ),
    path('login/', views.user_login, name='blog_login'),
    path('logout/', views.user_logout, name='blog_logout'),
    path('add_post/', views.add_post, name='add_post'),
]

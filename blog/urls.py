from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000 ---> local, from coming, it takes you to the 'post_list' within 'views'
    # mydjangosite.com --> online
    path('', views.post_list, name='post_list'),
    # 127.0.0.1:8000/post/2 ---> local ,for example the 2 will be the pk and passes to views.py
    # mydjangosite.com/post/2 ---> online
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.1:8000/post/new --> local
    # mydjangosite.com/post/new --> online
    path('post/new/', views.post_new, name='post_new'),

]
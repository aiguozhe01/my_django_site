from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000, from coming, it takes you to the 'post_list' within 'views'
    path('', views.post_list, name='post_list'),
]
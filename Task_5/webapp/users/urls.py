from django.urls import path

from . import views

urlpatterns = [
    # ex: /users/
    path('', views.index, name='index'),
    # ex: /users/register/
    path('register', views.register, name='register')
]

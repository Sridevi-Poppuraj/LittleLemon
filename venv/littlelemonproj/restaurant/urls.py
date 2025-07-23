from django.contrib import admin
from django.urls import path
from .views import sayHello
from. import views

urlpatterns = [
    path('', sayHello, name='sayHello'),
    path('1', views.index, name='index')
]
from django.contrib import admin
from django.urls import path, include
from .views import sayHello
from. import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', sayHello, name='sayHello'),
    path('1', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('book/', views.BookingListView.as_view()),
    path('book/<int:pk>', views.BookingDetailView.as_view()),
]
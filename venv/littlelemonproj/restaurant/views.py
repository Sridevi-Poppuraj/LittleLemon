from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from .serializers import MenuItemSerializer, BookingSerializer

def sayHello(request):
  return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()               # all menu items in DB
    serializer_class = MenuItemSerializer  

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingListView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
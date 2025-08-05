from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

def sayHello(request):
  return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()               # all menu items in DB
    serializer_class = MenuItemSerializer  

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingListView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class BookingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
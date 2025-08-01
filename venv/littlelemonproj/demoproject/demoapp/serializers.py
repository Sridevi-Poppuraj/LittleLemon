from django.contrib.auth.models import User
from rest_framework import serializer
from .models import MenuItem

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
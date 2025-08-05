from django.test import TestCase
from django.urls import reverse
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Pasta", price=12.50, inventory=5)
        self.item2 = Menu.objects.create(title="Burger", price=9.99, inventory=8)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
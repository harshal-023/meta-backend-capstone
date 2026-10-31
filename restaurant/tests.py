from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu
from .serializers import menuSerializer

# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
        self.assertEqual(str(item), "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        queryset = Menu.objects.all()
        serializer = menuSerializer(queryset, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
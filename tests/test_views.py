from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()  # REST framework test client
         # Create a test user
        self.user = User.objects.create_user(username="palak.khatri", password="Test@123")

        # Generate token for the test user
        self.token = Token.objects.create(user=self.user)

        # Authenticate the test client with the token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        """Create test instances of the Menu model"""
        self.menu1 = Menu.objects.create(title="Pizza", price=100,inventory=1)
        self.menu2 = Menu.objects.create(title="Burger", price=50,inventory=1)
        self.menu3 = Menu.objects.create(title="Pasta", price=70,inventory=1)

    def test_get_all(self):
        """Retrieve all Menu objects and compare with serialized data"""
        response = self.client.get(reverse('menu-items'))  # URL name in urls.py
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
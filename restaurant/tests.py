from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Menu, Booking


class MenuModelTest(APITestCase):
    def test_menu_str(self):
        item = Menu.objects.create(title='Pasta', price=12.50, inventory=10)
        self.assertEqual(str(item), 'Pasta : 12.50')


class BookingModelTest(APITestCase):
    def test_booking_str(self):
        booking = Booking.objects.create(
            name='Alice', no_of_guests=4, booking_date='2026-09-01T19:00:00Z'
        )
        self.assertEqual(str(booking), 'Alice - 4 guests')


class RegistrationTest(APITestCase):
    def test_registration_creates_user_and_token(self):
        url = reverse('registration')
        response = self.client.post(url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'strongpassword123',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertTrue(User.objects.filter(username='testuser').exists())


class MenuAPITest(APITestCase):
    def setUp(self):
        Menu.objects.create(title='Greek Salad', price=8.00, inventory=20)

    def test_anyone_can_list_menu(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_unauthenticated_cannot_create_menu_item(self):
        response = self.client.post('/api/menu/', {
            'title': 'Bruschetta', 'price': 5.00, 'inventory': 15
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='pass12345')

    def test_unauthenticated_cannot_access_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_booking(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/bookings/', {
            'name': 'Bob',
            'no_of_guests': 2,
            'booking_date': '2026-09-05T18:30:00Z',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

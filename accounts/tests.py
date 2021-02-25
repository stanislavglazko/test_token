from rest_framework.test import APITestCase
from rest_framework import status


class RegistrationTest(APITestCase):
    def test_registration(self):
        data = {'username': 'John',
                'password': 'SnowSnowSnow',
                'email': 'johnnysnow@gmail.com'}
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

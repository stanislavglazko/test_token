from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class RegistrationTest(APITestCase):
    def test_registration(self):
        data = {'username': 'John',
                'password': 'SnowSnowSnow',
                'email': 'johnnysnow@gmail.com'}
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserProfileTest(APITestCase):
    profile_list_url = reverse('all-profiles')

    def setUp(self):
        self.user = self.client.post('/auth/users/',
                                     data={'username': 'eddardstark',
                                           'password': 'i-keep-dying'})
        response = self.client.post('/auth/jwt/create/',
                                    data={'username': 'eddardstark',
                                          'password': 'i-keep-dying'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_userprofile_list(self):
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_detail(self):
        response = self.client.get(reverse('profile', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_update(self):
        profile_data = {'city': 'Winterfell', 'is_administrator': True}
        response = self.client.put(reverse('profile', kwargs={'pk': 1}),
                                   data=profile_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

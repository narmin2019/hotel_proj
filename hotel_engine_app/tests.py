from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
# Create your tests here.

class Register(TestCase):
    def setUp(self):
        pass

    def test_get_regiser_page(self):
        response = self.client.get('/register')
        self.assertEquals(response.status_code, 200)

    def test_registration(self):
        post_data = {'name': 'Ali',
                    'surname': 'Valiyev',
                    'email':'rasim@valiyev.com',
                    'username':'rasim@valiyev.com',
                    'password': '123456'}

        response = self.client.post('/register', post_data)

        # when registration finished successfully, site redirects the new user to the homepage
        self.assertEqual(response.status_code, 302)  # 302 is status code for redirected responses in http protocol

        # check if registered user exists in database
        # We don't use objects.get method to avoid NotFoundException.
        # Instead we use filter().first to get 'None' if searching user isn't exists in database
        user = User.objects.filter(username='rasim@valiyev.com').first()
        self.assertIsNotNone(user)

        # check if user info is correctly applied
        self.assertEquals(user.get_full_name(), 'Ali Valiyev')
        self.assertEquals(user.email, 'rasim@valiyev.com')

        # Test authorization after registration
        # Authorized user's name and surname must shown at tof of the home page. So,
        response = self.client.get('/')
        self.assertContains(response, user.get_full_name())

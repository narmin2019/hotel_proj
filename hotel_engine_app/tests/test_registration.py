from django.test import TestCase
from django.contrib.auth.models import User


class RegistrationTest(TestCase):

    def test_register(self):
        user_info = {'name': 'Ali',
                    'surname': 'Valiyev',
                    'email':'ali@valiyev.com',
                    'username':'ali@valiyev.com',
                    'password': '123456'}

        response = self.client.post('/register', user_info)

        # when registration finished successfully, site redirects the new user to the homepage
        self.assertEqual(response.status_code, 302)  # 302 is status code for redirected responses in http protocol

        # check if registered user exists in database
        # We don't use objects.get method to avoid NotFoundException.
        # Instead, we use filter(...).first to return None (null) if searching user isn't exists in database
        user = User.objects.filter(username='ali@valiyev.com').first()
        self.assertIsNotNone(user)

        # check if user info is correctly applied
        self.assertEquals(user.get_full_name(), 'Ali Valiyev')
        self.assertEquals(user.email, 'ali@valiyev.com')

        # Test authorization after registration
        # Authorized user's name and surname must be shown at top of the home page. So,
        response = self.client.get('/')
        self.assertContains(response, user.get_full_name())

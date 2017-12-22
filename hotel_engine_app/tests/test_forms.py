from django.test import TestCase
from hotel_engine_app.forms import LoginForm, SearchForm, RegisterForm


class FormsTest(TestCase):

    def test_login_form(self):

        login_data = {'email': 'ali@valiyev.com', 'password': '123456'}
        login_form = LoginForm(login_data)

        # test valid state
        self.assertTrue(login_form.is_valid())

        # test invalid state
        login_data['email'] = ''
        login_data['password'] = ''

        login_form = LoginForm(login_data)

        self.assertFalse(login_form.is_valid())

    def test_register_form(self):
        register_data = {'name': 'Ali',
                    'surname': 'Valiyev',
                    'email':'ali@valiyev.com',
                    'username':'ali@valiyev.com',
                    'password': '123456'}

        register_form = RegisterForm(register_data)

        #  check valid state
        self.assertTrue(register_form.is_valid())

        #  check invalid state

        register_data['email'] = ''
        register_form = RegisterForm(register_data)
        self.assertFalse(register_form.is_valid())
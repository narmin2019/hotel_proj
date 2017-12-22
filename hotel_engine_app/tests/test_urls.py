from django.test import TestCase

class UrlsTest(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_get_register_page(self):
        response = self.client.get('/register')
        self.assertEquals(response.status_code, 200)

    def test_get_login_page(self):
        response = self.client.get('/login')
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout')
        #  should redirect to login page
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/login')

    def test_404_not_found(self):
        response = self.client.get('/urls-that-doesnt-exists')
        self.assertEquals(response.status_code, 404)
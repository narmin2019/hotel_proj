from django.test import TestCase


class TestSearch(TestCase):

    def test_default_is_top_hotels(self):
        response = self.client.get('/')
        self.assertContains(response, 'Top Hotels!')

    def test_search(self):
        query = 'sample search query'
        response = self.client.post('/', {'region': query})
        self.assertContains(response, 'Search Result')
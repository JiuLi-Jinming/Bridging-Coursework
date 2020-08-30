from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import cv_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/cv')
        self.assertEqual(found.func, cv_page)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>CV</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))


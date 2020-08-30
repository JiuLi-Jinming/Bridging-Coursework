from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from django.test import TestCase
from blog.views import blog_home


class HomePageTest(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, blog_home)

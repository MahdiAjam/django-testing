from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import HomeView, AboutView

class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home:home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_about(self):
        url = reverse('home:about')
        self.assertEquals(resolve(url).func.view_class, AboutView)

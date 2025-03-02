from django.test import TestCase
from home.forms import UserRegistrationForm
from django.contrib.auth.models import User

class TestRegistrationForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='mahdi', email='mahdi@gmail.com', password='mahdi')

    def test_valid_data(self):
        form = UserRegistrationForm(data={'username': 'bob', 'email': 'bob@gmail.com', 'password': 'bob',
                                          'password2': 'bob'})
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_exist_email(self):
        form = UserRegistrationForm(data={'username': 'kevin', 'email': 'mahdi@gmail.com', 'password': 'kevin',
                                          'password2': 'kevin'})
        self.assertEquals(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))

    def test_unmatched_passwords(self):
        form = UserRegistrationForm(data={'username': 'mark', 'email': 'mark@gmail.com', 'password': 'mark',
                                          'password2': 'markkkkkkk'})
        self.assertEquals(len(form.errors), 1)
        self.assertTrue(form.has_error)

from django.test import TestCase
from .forms import LoginForm, RegisterForm, UpdateUserForm, UpdateProfileForm, AirQualityForm_User

class FormsTestCase(TestCase):
    def test_login_form_valid(self):
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_valid(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword'
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):
        form_data = {
            'username': '',
            'email': 'invalid-email',
            'password1': 'password1',
            'password2': 'password2'
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_valid(self):
        form_data = {'email': 'newemail@example.com'}
        form = UpdateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_user_form_invalid(self):
        form_data = {'email': 'invalid-email'}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_air_quality_form_user_invalid(self):
        form_data = {
            'location': '',
            'latitude': 'invalid-lat',
            'longitude': 'invalid-long',
            'so2': 'invalid-so2',
            'o3': 'invalid-o3',
            'pm2_5': 'invalid-pm2_5',
            'pm10': 'invalid-pm10'
        }
        form = AirQualityForm_User(data=form_data)
        self.assertFalse(form.is_valid())

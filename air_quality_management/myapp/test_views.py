from django.test import TestCase
from django.urls import reverse
from .models import AirQualityData, Pollutant, Sensor
from .forms import LoginForm, RegisterForm, UpdateUserForm, UpdateProfileForm, AirQualityForm_User
from django.contrib.auth.models import User


class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_homepage_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

        # Test POST request
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects to homepage upon successful login

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirects to index upon logout

    def test_register_view(self):
        response = self.client.get(reverse('register'))  # Use 'register_view' here
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

        # Test POST request
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects to login page upon successful registration

    def test_user_view(self):
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_profile.html')

    def test_city_details_view(self):
        # Create some test data
        pollutant = Pollutant.objects.create(SO2=0.1, O3=0.2, PM2_5=0.3, PM10=0.4)
        air_quality_data = AirQualityData.objects.create(
            city='Test City',
            latitude=1.23,
            longitude=4.56,
            pollutant_id=pollutant,
            main_pollutant='SO2',
            air_quality_index=75.0,
            pol_level='Fair',
            provider='testuser'
        )

        response = self.client.get(reverse('city_details', args=[air_quality_data.pollutant_id.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'city_details.html')

    def test_air_quality_data_list_view(self):
        response = self.client.get(reverse('air_quality_data_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data/air_quality_data_list.html')


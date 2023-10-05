from django.test import TestCase
from myapp.models import AirQualityData, Pollutant, Sensor, Profile
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

class AirQualityDataModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test Pollutant instance
        cls.pollutant = Pollutant.objects.create(
            SO2=0.5,
            O3=0.3,
            PM2_5=10.0,
            PM10=20.0
        )

    def test_air_quality_data_creation(self):
        # Create a test User instance
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test Image file
        image = Image.new('RGB', (100, 100))
        image_io = BytesIO()
        image.save(image_io, 'JPEG')
        image_file = SimpleUploadedFile("test.jpg", image_io.getvalue())

        # Create a test Profile instance
        profile = Profile.objects.create(
            user=user,
            avatar=image_file,
            bio='Test bio'
        )

        # Create a test AirQualityData instance
        air_quality_data = AirQualityData.objects.create(
            city='Test City',
            latitude=0.0,
            longitude=0.0,
            pollutant_id=self.pollutant,
            main_pollutant='PM2.5',
            air_quality_index=25.5,
            pol_level='Low',
            provider='Test Provider'
        )

        # Check if the AirQualityData instance was created successfully
        self.assertEqual(air_quality_data.city, 'Test City')
        self.assertEqual(air_quality_data.pollutant_id, self.pollutant)
        self.assertEqual(air_quality_data.main_pollutant, 'PM2.5')
        self.assertEqual(air_quality_data.air_quality_index, 25.5)
        self.assertEqual(air_quality_data.pol_level, 'Low')
        self.assertEqual(air_quality_data.provider, 'Test Provider')
        self.assertEqual(air_quality_data.user_profile, profile)

class PollutantModelTest(TestCase):
    def test_pollutant_creation(self):
        pollutant = Pollutant.objects.create(
            SO2=0.5,
            O3=0.3,
            PM2_5=10.0,
            PM10=20.0
        )

        self.assertEqual(pollutant.SO2, 0.5)
        self.assertEqual(pollutant.O3, 0.3)
        self.assertEqual(pollutant.PM2_5, 10.0)
        self.assertEqual(pollutant.PM10, 20.0)

class SensorModelTest(TestCase):
    def test_sensor_creation(self):
        sensor = Sensor.objects.create(
            code='Test Code',
            name='Test Sensor'
        )

        self.assertEqual(sensor.code, 'Test Code')
        self.assertEqual(sensor.name, 'Test Sensor')

class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        image = Image.new('RGB', (100, 100))
        image_io = BytesIO()
        image.save(image_io, 'JPEG')
        image_file = SimpleUploadedFile("test.jpg", image_io.getvalue())

        profile = Profile.objects.create(
            user=user,
            avatar=image_file,
            bio='Test bio'
        )

        self.assertEqual(profile.user, user)
        self.assertEqual(profile.avatar, 'profile_images/test.jpg')
        self.assertEqual(profile.bio, 'Test bio')

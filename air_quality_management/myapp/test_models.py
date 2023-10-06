from django.test import TestCase
from django.contrib.auth.models import User
from .models import AirQualityData, Pollutant, Sensor, Profile


class AirQualityDataModelTest(TestCase):
    def test_str_representation(self):
        self.maxDiff = None
        air_quality_data = AirQualityData(
            city="Test City",
            latitude=42.12345,
            longitude=72.98765,
            pollutant_id=Pollutant.objects.create(SO2=1.23, O3=2.34, PM2_5=3.45, PM10=4.56),
            main_pollutant="PM2.5",
            air_quality_index=123.456,
            pol_level="Moderate",
            provider="Test Provider"
        )
        actual_str = str(air_quality_data)
        expected_str = (
            f"Data ID: {air_quality_data.data_id}, City: {air_quality_data.city}, "
            f"Latitude: {air_quality_data.latitude}, Longitude: {air_quality_data.longitude}, "
            f"Pollutant ID: {air_quality_data.pollutant_id}, AQI: {air_quality_data.air_quality_index}, "
            f"Timestamp: {air_quality_data.timestamp}, Pollution Level: {air_quality_data.pol_level}, "
            f"Provider: {air_quality_data.provider}"
        )
        self.assertEqual(actual_str.strip(), expected_str)


class PollutantModelTest(TestCase):
    def test_str_representation(self):
        pollutant = Pollutant(SO2=1.23, O3=2.34, PM2_5=3.45, PM10=4.56)
        expected_str = "Pollutant: SO2=1.23, O3=2.34, PM10=4.56"
        self.assertEqual(str(pollutant), expected_str)


class SensorModelTest(TestCase):
    def test_str_representation(self):
        sensor = Sensor(code="TestCode", name="TestSensor")
        expected_str = "TestSensor"
        self.assertEqual(str(sensor), expected_str)


class ProfileModelTest(TestCase):
    def test_str_representation(self):
        user = User(username="testuser")
        profile = Profile(user=user, bio="Test Bio")
        expected_str = "testuser"
        self.assertEqual(str(profile), expected_str)

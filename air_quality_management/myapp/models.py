from django.db import models
import uuid  # Required for unique book instances.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns.
from django.utils.translation import gettext as _

# Create your models here.
class AirQualityData(models.Model):
    data_id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        help_text=_('Unique Id for this data'))
    location_id = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    pollutant_id = models.ForeignKey('Pollutant', on_delete=models.SET_NULL, null=True)
    air_quality_index = models.DecimalField(max_digits=4, decimal_places=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    pol_level = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Data ID: {self.data_id}, Location: {self.location_id}, Pollutant: {self.pollutant_id}, AQI: {self.air_quality_index}"

class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longtitude = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Pollutant(models.Model):
    SO2 = models.DecimalField(max_digits=18, decimal_places=0)
    O3 = models.DecimalField(max_digits=18, decimal_places=0)
    PM2_5 = models.DecimalField(max_digits=18, decimal_places=0)
    PM10 = models.DecimalField(max_digits=18, decimal_places=0)

    def __str__(self):
        return f"Pollutant: SO2={self.SO2}, O3={self.O3}, PM10={self.PM10}"

class Sensor(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

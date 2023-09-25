from django.db import models
import uuid  # Required for unique book instances.
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class AirQualityData(models.Model):
    data_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Unique Id for this data'
    )
    city = models.CharField(max_length=200)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    pollutant_id = models.ForeignKey('Pollutant', on_delete=models.SET_NULL, null=True)
    main_pollutant = models.CharField(max_length=10)
    air_quality_index = models.DecimalField(max_digits=10, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)
    pol_level = models.CharField(max_length=200, blank=True)
    provider = models.CharField(max_length=200)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Data ID: {self.data_id}, City: {self.city}, Latitude: {self.latitude}, Longitude: {self.longitude}, " \
               f"Pollutant ID: {self.pollutant_id}, AQI: {self.air_quality_index}, Timestamp: {self.timestamp}, " \
               f"Pollution Level: {self.pol_level}, Provider: {self.provider} "


class Pollutant(models.Model):
    SO2 = models.DecimalField(max_digits=18, decimal_places=4)
    O3 = models.DecimalField(max_digits=18, decimal_places=4)
    PM2_5 = models.DecimalField(max_digits=18, decimal_places=4)
    PM10 = models.DecimalField(max_digits=18, decimal_places=4)

    def __str__(self):
        return f"Pollutant: SO2={self.SO2}, O3={self.O3}, PM10={self.PM10}"


class Sensor(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

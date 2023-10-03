from django.contrib import admin
from .models import Profile,AirQualityData, Pollutant, Sensor

admin.site.register(Profile)
admin.site.register(Sensor)

class AirQualityDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'timestamp', 'main_pollutant', 'air_quality_index', 'pol_level', 'provider')
    list_filter = ('city', 'provider')
    fields = ['city', ('longitude', 'latitude'), ('main_pollutant', 'pol_level'), ('pollutant_id', 'air_quality_index'), 'provider']

admin.site.register(AirQualityData, AirQualityDataAdmin)

class PollutantAdmin(admin.ModelAdmin):
    list_display = ('SO2', 'O3', 'PM2_5', 'PM10')
    
admin.site.register(Pollutant, PollutantAdmin)

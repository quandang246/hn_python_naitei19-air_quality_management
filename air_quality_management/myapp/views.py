from django.shortcuts import render, get_object_or_404
from .models import AirQualityData, Location, Pollutant, Sensor
from django.shortcuts import render
from django.views import View

def homepage(request):
    """
    View for the homepage.
    """
    # You can add logic here to fetch data from your models if needed
    # For now, we'll render the homepage template with some dummy data
    dummy_data = []

    context = {
        'data': dummy_data,
    }
    return render(request, 'homepage.html', context)

def login_view(request):
    """
    View for the login.
    """
    # You can add logic here to fetch data from your models if needed
    # For now, we'll render the homepage template with some dummy data
    dummy_data = []

    context = {
        'data': dummy_data,
    }
    return render(request, 'login.html', context)

def register_view(request):
    """
    View for the login.
    """
    # You can add logic here to fetch data from your models if needed
    # For now, we'll render the homepage template with some dummy data
    dummy_data = []

    context = {
        'data': dummy_data,
    }
    return render(request, 'register.html', context)

class city_details(View):
    template_name = 'city_details.html'

    def get(self, request, *args, **kwargs):
        # You can fetch data for the city here if needed
        city_data = {}

        context = {
            'city_data': city_data,
        }

        return render(request, self.template_name, context)

def air_quality_data_list(request):
    """
    View to display a list of air quality data.
    """
    air_quality_data = AirQualityData.objects.all()
    context = {
        'air_quality_data': air_quality_data,
    }
    return render(request, 'data/air_quality_data_list.html', context)

def air_quality_data_detail(request, data_id):
    """
    View to display details of a specific air quality data point.
    """
    air_quality_data = get_object_or_404(AirQualityData, data_id=data_id)
    context = {
        'air_quality_data': air_quality_data,
    }
    return render(request, 'my_app/air_quality_data_detail.html', context)

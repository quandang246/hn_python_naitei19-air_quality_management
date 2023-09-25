from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.views import View
from django.db import transaction
from .models import AirQualityData, Pollutant, Sensor
from .forms import LoginForm, RegisterForm
from .forms import UpdateUserForm, UpdateProfileForm
from .forms import AirQualityForm_User


def index(request):
    """
    View for the homepage.
    """
    # You can add logic here to fetch data from your models if needed
    # For now, we'll render the homepage template with some dummy data
    dummy_data = []

    context = {
        'data': dummy_data,
    }
    return render(request, 'index.html', context)


def homepage(request):
    """
    View for the homepage.
    """
    data = AirQualityData.objects.all()
    return render(request, 'homepage.html', {'data': data})


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome back!')
                return redirect('homepage')

        messages.error(request, _('Invalid username or password'))
        return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, _("You've been logged out."))
    return redirect('index')


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, _('You have signed up successfully'))
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})


def user_view(request):
    """
    View to display a list of air quality data.
    """
    dummy_data = []

    context = {
        'data': dummy_data,
    }
    return render(request, 'user/user_profile.html', context)


class city_details(View):
    template_name = 'city_details.html'

    def get(self, request, pollutant_id, *args, **kwargs):
        # Retrieve the AirQualityData object based on the location_id
        air_quality_data = get_object_or_404(AirQualityData, pollutant_id_id=pollutant_id)

        # Retrieve the pollutant data related to the AirQualityData object
        pollutants = get_object_or_404(Pollutant, id=pollutant_id)

        context = {
            'air_quality_data': air_quality_data,
            'pollutants': pollutants,
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


@login_required
def profile(request):
    air_quality_data = AirQualityData.objects.filter(provider=request.user.username)[:2]

    context = {
        'air_quality_data': air_quality_data,
    }
    return render(request, 'user/user_profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    success_message = _('Successfully Changed Your Password')
    success_url = reverse_lazy('users-profile')


@login_required
def reports_history(request):
    air_quality_data = AirQualityData.objects.filter(provider=request.user.username)

    context = {
        'air_quality_data': air_quality_data,
    }
    return render(request, 'reports_history.html', context)


def _pollution_level(air_quality_index):
    if air_quality_index <= 33:
        return _("Very Good")
    elif 34 <= air_quality_index <= 66:
        return _("Good")
    elif 67 <= air_quality_index <= 99:
        return _("Fair")
    elif 100 <= air_quality_index <= 149:
        return _("Bad")
    elif 150 <= air_quality_index <= 200:
        return _("Very Bad")
    elif air_quality_index > 200:
        return _("Hazardous")


@login_required
def report_air_quality(request):
    if request.method == 'POST':
        form = AirQualityForm_User(request.POST)
        if form.is_valid():
            city = form.cleaned_data['location']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            so2 = form.cleaned_data['so2']
            o3 = form.cleaned_data['o3']
            pm2_5 = form.cleaned_data['pm2_5']
            pm10 = form.cleaned_data['pm10']

            with transaction.atomic():
                # Save pollutant to database
                pollutant_obj = Pollutant(SO2=so2, O3=o3, PM2_5=pm2_5, PM10=pm10)
                pollutant_obj.save()

                # Get primary key
                pol_id = pollutant_obj

                # Pollution level calculation
                SO2STANDARD = 0.25
                O3STANDARD = 0.065
                PM2_5STANDARD = 25
                PM10STANDARD = 50

                so2_aqi = so2 * 100 / SO2STANDARD  # Input for 8h period - Standard 0.25pmm
                o3_aqi = o3 * 100 / O3STANDARD  # Input for 8h period - Standard 0.065pmm
                pm2_5_aqi = pm2_5 * 100 / PM2_5STANDARD  # Input for 24h period - Standard 25ug/m3
                pm10_aqi = pm10 * 100 / PM10STANDARD  # Input for 24h period - Standard 50ug/m3
                main_pol = {so2_aqi: "SO2", o3_aqi: "O3", pm2_5_aqi: "PM2.5", pm10_aqi: "PM10"}
                air_quality_index = max(so2_aqi, o3_aqi, pm2_5_aqi, pm10_aqi)

                # Get username
                aqi_data = AirQualityData(city=city, latitude=latitude, longitude=longitude,
                                          pollutant_id=pol_id, main_pollutant=main_pol.get(max(main_pol)),
                                          air_quality_index=air_quality_index,
                                          timestamp=datetime.now(), pol_level=_pollution_level(air_quality_index),
                                          provider=request.user.username)
                aqi_data.save()
                return redirect('homepage')
    else:
        form = AirQualityForm_User()

    return render(request, 'user/user_aqi_form_create.html', {'form': form})

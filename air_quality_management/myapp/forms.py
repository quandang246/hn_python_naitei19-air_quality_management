from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from .models import Profile, AirQualityData
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=65,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': _('Enter your username')}))
    email = forms.EmailField(max_length=200,
                             required=True,
                             widget=forms.EmailInput(attrs={'placeholder': _('Enter your email')}))
    password1 = forms.CharField(max_length=65,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': _('Create password')}))
    password2 = forms.CharField(max_length=65,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': _('Confirm password')}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class AirQualityForm_User(forms.Form):
    location = forms.CharField(label='Location', widget=forms.HiddenInput(), required=False)
    latitude = forms.FloatField(label='Latitude', widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(label='Longitude', widget=forms.HiddenInput(), required=False)
    so2 = forms.FloatField(label='SO2')
    o3 = forms.FloatField(label='O3')
    pm2_5 = forms.FloatField(label='PM2.5')
    pm10 = forms.FloatField(label='PM10')

class UpdateReportForm(forms.Form):
    location = forms.CharField(label='Location', widget=forms.HiddenInput(), required=False)
    latitude = forms.FloatField(label='Latitude', widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(label='Longitude', widget=forms.HiddenInput(), required=False)
    so2 = forms.FloatField(label='SO2')
    o3 = forms.FloatField(label='O3')
    pm2_5 = forms.FloatField(label='PM2.5')
    pm10 = forms.FloatField(label='PM10')

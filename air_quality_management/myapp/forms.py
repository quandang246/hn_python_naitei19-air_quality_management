from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
# from .models import Profile
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
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

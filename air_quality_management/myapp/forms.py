from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=30)
    email = forms.EmailField(label=_('Email'))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('Re-enter password'), widget=forms.PasswordInput())

    # Kiem tra du lieu nhap lai mat khau
    # Truoc tien kiem tra password1 nhap chua, neu roi thi lay thong tin password1 va password2
    # thong qua thuoc tinh cleaned_data de kiem tra.
    # Neu 2 gia tri bang nhau va khong co dau cach thi xem nhu hop le va return password2
    # Neu khong thi raise loi "Mat khau khong hop le"
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError(_("Invalid password"))

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError(_("Username has invalid characters"))
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError(_("Account has already existed"))

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],
                                 email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password1'])

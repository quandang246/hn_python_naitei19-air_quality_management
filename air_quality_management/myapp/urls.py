from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile, edit_profile
from myapp.views import ChangePasswordView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('city_details/', views.city_details.as_view(), name='city_details'),  # Replace 'city_details_view' with your actual view function.
    path('air-quality-data/', views.air_quality_data_list, name='air_quality_data_list'),
    path('air-quality-data/<uuid:data_id>/', views.air_quality_data_detail, name='air_quality_data_detail'),
    path('login/', views.login_view, name='login'),  # Replace 'login_view' with your actual view function.
    path('register/', views.register_view, name='register'),  # Replace 'register_view' with your actual view function.
    path('profile/', profile, name='users-profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]

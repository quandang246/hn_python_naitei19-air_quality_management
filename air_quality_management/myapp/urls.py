from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile, edit_profile
from .views import ChangePasswordView

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('city_details/<int:location_id>/', views.city_details.as_view(), name='city_details'),
    path('air-quality-data/', views.air_quality_data_list, name='air_quality_data_list'),
    path('air-quality-data/<uuid:data_id>/', views.air_quality_data_detail, name='air_quality_data_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('user/', views.user_view, name='user_profile'),
    path('profile/', profile, name='users-profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]

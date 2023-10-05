from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile, edit_profile, report_view, edit_reports, delete_reports
from .views import ChangePasswordView, ResetPasswordView

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('city_details/<int:pollutant_id>/', views.city_details.as_view(), name='city_details'),
    path('air-quality-data/', views.air_quality_data_list, name='air_quality_data_list'),
    path('air-quality-data/<uuid:data_id>/', views.air_quality_data_detail, name='air_quality_data_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('register/', views.register_view, name='register'),
    path('user/', views.user_view, name='user_profile'),
    path('profile/', profile, name='users-profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('reports-history/', views.reports_history, name='reports_history'),
    path('report_air_quality', views.report_air_quality, name='report_air_quality'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmation.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_completed.html'), name='password_reset_complete'),
    path('reports-view/<uuid:data_id>/', report_view, name='report_view'),
    path('reports-edit/<uuid:data_id>/', edit_reports, name='edit_reports'),
    path('reports-delete/<uuid:data_id>/', delete_reports, name='delete_reports'),
]

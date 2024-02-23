from django.urls import path

from .views import register, log_in, get_profile, get_main_page

app_name = 'drivers'

urlpatterns = [
    path('', get_main_page, name='get_main_page'),
    path('register/', register, name='register'),
    path('log_in/', log_in, name='log_in'),
    path('profile/<int:pk>/', get_profile, name='get_profile')
]

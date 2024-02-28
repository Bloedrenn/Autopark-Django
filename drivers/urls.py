from django.urls import path

from .views import get_main_page, register, log_in, log_out, get_profile, show_available_cars, confirm_car_choice

app_name = 'drivers'

urlpatterns = [
    path('', get_main_page, name='get_main_page'),
    
    path('register/', register, name='register'),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('profile/<int:pk>/', get_profile, name='get_profile'),
    
    path('cars/', show_available_cars, name='show_available_cars'),
    path('car_choice_confirmation/<int:pk>/', confirm_car_choice, name='confirm_car_choice')
]

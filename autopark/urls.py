from django.urls import path

from .views import register_driver, get_driver_profile

app_name = 'autopark'

urlpatterns = [
    path('drivers/register/', register_driver, name='register_driver'),
    path('drivers/profile/<int:pk>/', get_driver_profile, name='get_driver_profile')
]

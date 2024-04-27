from django.urls import path

from .views import get_main_page, register, UserLoginView, UserLogoutView, UserProfileView

app_name = 'clients'

urlpatterns = [
    path('', get_main_page, name='get_main_page'),

    path('register/', register, name='register'),
    path('log_in/', UserLoginView.as_view(), name='log_in'),
    path('log_out/', UserLogoutView.as_view(), name='log_out'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='get_profile')
]

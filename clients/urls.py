from django.urls import path

from .views import register, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', register, name='register'),
    path('log_in/', UserLoginView.as_view(), name='log_in'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='get_profile')
]

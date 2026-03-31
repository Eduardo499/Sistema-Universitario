from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register, name='register'),
]
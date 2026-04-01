from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('register/success/', register_success, name='register_success'),
    path('profile/', profile, name='profile'),
    path('admin_home/', admin_home, name='admin_home'),


]
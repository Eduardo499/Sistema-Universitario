from django.urls import path
from .views import *

app_name = 'configs'

urlpatterns = [
    path('configs/', configs_home, name='configs_home'),
]
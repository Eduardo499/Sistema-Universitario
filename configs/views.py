from django.shortcuts import render

# Create your views here.
def configs_home(request):
    return render(request, 'configs/configs_home.html')
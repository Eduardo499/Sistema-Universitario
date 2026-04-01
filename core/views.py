from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    return render(request, 'core/public_home.html')
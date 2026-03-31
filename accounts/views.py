from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    print("REGISTER VIEW OK")
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/register_success.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
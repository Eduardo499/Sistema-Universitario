from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'accounts/register.html', {'form': form, 'role': request.POST.get('role') or form.initial.get('role')})

def register_success(request):
    return render(request, 'accounts/register_success.html')

@login_required
def profile(request):
    user = request.user

    if user.role == 'aluno':
        return render(request, 'accounts/aluno_home.html', {'user': user})
    elif user.role == 'professor':
        return render(request, 'accounts/professor_home.html', {'user': user})
    elif user.role == 'admin':
        return render(request, 'accounts/admin_home.html', {'user': user})
    else:
        return redirect('accounts:login')
    
def admin_home(request):
    return render(request, 'accounts/admin_home.html')
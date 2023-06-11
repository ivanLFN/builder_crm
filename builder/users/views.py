from django.shortcuts import render, redirect
from users.forms import CustomUserRegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            return redirect('home_page')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

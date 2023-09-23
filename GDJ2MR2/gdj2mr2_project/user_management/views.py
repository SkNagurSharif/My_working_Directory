
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



#login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to a desired page
    else:
        form = UserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'user_management/login.html', {'form': form})


def home(request):
    return render(request, 'user_management/home.html')

"""

from .forms import ExtendedUserCreationForm

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                role=form.cleaned_data.get('role'),
                profile_picture=form.cleaned_data.get('profile_picture'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                college_name=form.cleaned_data.get('college_name'),
                address=form.cleaned_data.get('address'),
            )
            # ... (handle email verification, etc.)
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})


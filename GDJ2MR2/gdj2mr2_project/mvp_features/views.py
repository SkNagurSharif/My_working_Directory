# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login

from gdj2mr2_project.mvp_features.models import Equipment
from .forms import EquipmentForm, RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or desired URL
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def add_equipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'add_equipment.html', {'form': form})

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipments': equipments})


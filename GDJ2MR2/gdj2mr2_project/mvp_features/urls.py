from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('equipment_list/', views.equipment_list, name='equipment_list'),
]

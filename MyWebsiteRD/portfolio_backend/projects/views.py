from django.shortcuts import render

# Create your views here.
# projects/views.py

from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

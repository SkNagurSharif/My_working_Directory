from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_ROLES = [
        ('STUDENT', 'Student'),
        ('AUDITOR', 'Auditor'),
        ('MANAGER', 'Manager'),
        ('SUPERVISOR', 'Supervisor'),
        ('ADMIN', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='STUDENT')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    college_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)

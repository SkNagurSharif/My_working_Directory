from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from captcha.fields import ReCaptchaField  # assuming you're using django-recaptcha for CAPTCHA

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=UserProfile.USER_ROLES)
    profile_picture = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    college_name = forms.CharField(max_length=100, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role', 
                  'profile_picture', 'first_name', 'last_name', 'college_name', 'address')

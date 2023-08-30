from django import forms
from .models import Course
from .models import User

class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'image']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'profile_picture']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
from django import forms
from django.forms import ModelForm
from .models import Report

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from django.contrib.auth import login, authenticate

# Submit Report
class CreateReport(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['full_name', 'email', 'phone_number', 'location', 'department', 'issue_type', 'priority_level', 'description']

        widgets  = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email address...',
                'readonly': 'readonly'  # Will be auto-filled
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number...'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder':'Select location...'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder':'Eg. Nursing, Administration...'
            }),
            'issue_type': forms.Select(attrs={
                'class': 'form-control', 'placeholder':'Select type...'
            }),
            'priority_level': forms.Select(attrs={
                'class': 'form-control', 'placeholder':'Select priority level...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder':'Enter description...'
            }),
        }




# Register User
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    # Login
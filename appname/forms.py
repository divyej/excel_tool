# appname/forms.py
from django import forms
from .models import ExcelFile
from .models import CustomUser  # Add this import statement
from django.contrib.auth.forms import AuthenticationForm

class ExcelFileForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ('file',)
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
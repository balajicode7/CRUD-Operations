from django import forms
from .models import EmployeeModel
from django.core import validators


class Employee(forms.ModelForm):
    class Meta:
        model= EmployeeModel
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contact': forms.NumberInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }


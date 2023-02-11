from django import forms 
from .models import *

class SignUp(forms.ModelForm):
    
    class Meta():
        model = User
        fields = '__all__'
        
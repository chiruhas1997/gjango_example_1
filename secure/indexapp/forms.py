from django import forms
from django.contrib.auth.models import User
from indexapp.models import UserProfilInfo

class UserForm(forms.ModelForm):
    password:forms.CharField( widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
    
class UserProfilForm(forms.ModelForm):
    class Meta:
        model=UserProfilInfo
        fields=('portfolip_site','profile_pic')
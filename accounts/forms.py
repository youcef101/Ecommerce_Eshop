from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

class createNewUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']
SEXE=(('Homme','Homme'),('Femme','Femme'))
class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone','sexe','address', 'city','country','image']
        widgets = {
            'phone': TextInput(attrs={'class': 'input','placeholder':'phone'}),
            'sexe': Select(attrs={'class': 'input','placeholder':'sexe'},choices=SEXE),
            'address': TextInput(attrs={'class': 'input','placeholder':'address'}),
            'city': TextInput(attrs={'class': 'input','placeholder':'city'}),
            'country': TextInput(attrs={'class': 'input','placeholder':'country' }),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        widgets = {
            'username': TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email': EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }
       
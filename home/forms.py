from django import forms 
from django.forms import ModelForm
from .models import *
class searchForm(forms.Form):
    query=forms.CharField(max_length=100)
    catid=forms.IntegerField()

class contactMessage(ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','subject','message'] 



from django import forms
from django.db import models
from django.forms import fields
from .models import Flashsell

class Flashform(forms.ModelForm):
    class Meta:
        model=Flashsell
        fields= '__all__'
        

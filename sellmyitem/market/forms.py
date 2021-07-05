from django import forms
from django.forms import fields, models
from .models import Postitem


class Marketform(forms.ModelForm):
    class Meta:
        model = Postitem
        fields=['about_product','price','product_img','product_tag','contact']


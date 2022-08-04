from django.db import models  
from django.forms import fields  
from django.forms import ModelForm
from .models import Movie  
from django import forms  
  
  
class UserImageForm(ModelForm):  

    class meta:  
        model = Movie  
        fields = '__all__'  
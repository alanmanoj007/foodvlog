from django.db import models
from . models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class register(UserCreationForm):
    Firstname=forms.CharField(max_length=250,blank=True)
    Lastname=forms.CharField(max_length=250)
    Username=forms.CharField(max_length=250,unique=True,blank=True)
    Password=forms.CharField()

    class Meta:
        model = User
        fields = ('username' , 'Firstname', 'Lastname','Password')



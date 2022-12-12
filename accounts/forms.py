from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from .widgets import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class RequestForm(ModelForm):

	class Meta:
		model = Request
		fields = '__all__'
		widgets = {
            'trainingDate' : DatePickerInput(),
            'trainingTime' : TimePickerInput(),
            'b2bDate' : DatePickerInput(),
            'b2cDate' : DatePickerInput(),
            }


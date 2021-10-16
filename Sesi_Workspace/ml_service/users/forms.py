from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField() # By default required = True

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'email']

class PredictionForm(forms.Form):
	petal_length = forms.FloatField()

	class Meta:
		fields = ['petal_length']

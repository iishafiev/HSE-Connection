from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.html import strip_tags


class LoginForm(AuthenticationForm):
	username = forms.EmailField(
		widget=forms.EmailInput(attrs={
			'class': 'form-control',
			'placeholder': 'Email'
	}))

	password = forms.CharField(
		widget=forms.PasswordInput(attrs={ 
			'class':'form-control',
			'placeholder':'Пароль'
	}))
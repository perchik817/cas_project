from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from . import models

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required = True)
	
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	
	def save(self, commit = True):
		user = super(NewUserForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class Order_form(forms.ModelForm):
	class Meta:
		model = models.Order
		fields = '__all__'
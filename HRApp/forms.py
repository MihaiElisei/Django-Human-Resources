from django import forms
from .models import Role, Department, Nationality, Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# EMPLOYEE
class EmployeeCreateForm(forms.ModelForm):	
	class Meta:
		model = Employee
		exclude = ['is_blocked', 'is_deleted', 'created', 'updated']
		

# ADD NEW USER
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		

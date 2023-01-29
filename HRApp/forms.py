from django import forms
from .models import *
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
		

# CREATE EMERGENCY FORM
class EmergencyForm(forms.ModelForm):
	class Meta:
		model = Emergency
		fields = ['employee', 'fullname', 'tel', 'location', 'relationship']


# CREATE FAMILY FORM
class FamilyForm(forms.ModelForm):
	class Meta:
		model = Relationship
		fields = ['employee', 'status', 'spouse', 'occupation', 'tel', 'children', 'nextofkin', 'contact', 'relationship', 'father', 'foccupation', 'mother', 'moccupation']


# CREATE BANK FORM
class BankAccountForm(forms.ModelForm):
	class Meta:
		model = Bank
		fields = ['employee', 'name', 'branch', 'account', 'salary']


# CREATE LEAVE FORM
class CreateLeave(forms.ModelForm):
	reason = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
	
	class Meta:
		model = Leave
		exclude = ['user', 'defaultdays', 'hrcomments', 'status', 'is_approved', 'updated', 'created']

from django import forms
from .models import Role, Department, Nationality, Employee
from django.contrib.auth.models import User


# EMPLoYEE
class EmployeeCreateForm(forms.ModelForm):	
	class Meta:
		model = Employee
		exclude = ['is_blocked', 'is_deleted', 'created', 'updated']
		widgets = {
				'bio': forms.Textarea(attrs={'cols': 5, 'rows': 5})
		}



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *


# Render Index Page
def index(request):
    return render(request, "index.html")


# RENDER DASHBOARD PAGE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="accounts/login")
def dashboard(request):
    return render(request, "dashboard/dashboard_home.html")


# RENDER ALL EMPLOYEES
def all_employees(request):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')

	dataset = dict()
	departments = Department.objects.all()
	employees = Employee.objects.all()

	#pagination
	query = request.GET.get('search')
	if query:
		employees = employees.filter(
			Q(firstname__icontains=query) |
			Q(lastname__icontains=query)
		)
	paginator = Paginator(employees, 10) #show 10 employee lists per page
	page = request.GET.get('page')
	employees_paginated = paginator.get_page(page)

	dataset['employee_list'] = employees_paginated
	dataset['departments'] = departments
	dataset['all_employees'] = Employee.objects.all()
	dataset['title'] = 'Employees list view'
	return render(request, 'dashboard/all_employees.html', dataset)
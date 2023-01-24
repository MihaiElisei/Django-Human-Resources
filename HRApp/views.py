from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import EmployeeCreateForm
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

    # PAGINATION
    query = request.GET.get('search')
    if query:
        employees = employees.filter(
			Q(firstname__icontains=query) |
			Q(lastname__icontains=query)
		)

    paginator = Paginator(employees, 10)  # show 10 employee lists per page
    page = request.GET.get('page')
    employees_paginated = paginator.get_page(page)

    dataset['employee_list'] = employees_paginated
    dataset['departments'] = departments
    dataset['all_employees'] = Employee.objects.all()
    dataset['title'] = 'Employees list view'
    return render(request, 'dashboard/all_employees.html', dataset)


# CREATE NEW EMPLOYEE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def create_employee(request):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')

	if request.method == 'POST':
		form = EmployeeCreateForm(request.POST, request.FILES)
		
		if form.is_valid():
			instance = form.save(commit=False)
			user = request.POST.get('user')
			assigned_user = User.objects.get(id=user)

			instance.user = assigned_user

			instance.title = request.POST.get('title')
			instance.image = request.FILES.get('image')
			instance.firstname = request.POST.get('firstname')
			instance.lastname = request.POST.get('lastname')
			instance.othername = request.POST.get('othername')
			instance.sex = request.POST.get('sex')
			instance.bio = request.POST.get('bio')
			instance.birthday = request.POST.get('birthday')

			nationality_id = request.POST.get('nationality')
			nationality = Nationality.objects.get(id=nationality_id)
			instance.nationality = nationality

			department_id = request.POST.get('department')
			department = Department.objects.get(id=department_id)
			instance.department = department

			instance.address = request.POST.get('address')
			instance.education = request.POST.get('education')
			instance.lastwork = request.POST.get('lastwork')
			instance.position = request.POST.get('position')
		
			role = request.POST.get('role')
			role_instance = Role.objects.get(id=role)
			instance.role = role_instance

			instance.startdate = request.POST.get('startdate')
			instance.employeetype = request.POST.get('employeetype')
			instance.employeeid = request.POST.get('employeeid')
			instance.dateissued = request.POST.get('dateissued')

			instance.save()
			return redirect('/employees/')
		else:
			messages.error(request, 'Trying to create dublicate employees with a single user account ', extra_tags='alert alert-warning alert-dismissible show')
			return redirect('create_employee')

	dataset = dict()
	form = EmployeeCreateForm()
	dataset['form'] = form
	dataset['title'] = 'register employee'
	return render(request, 'dashboard/add_employee.html', dataset)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import EmployeeCreateForm, CreateUserForm
from .models import *


# RENDER INDEX PAGE
def index(request):
    return render(request, "index.html")


# RENDER DASHBOARD PAGE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="accounts/login")
def dashboard(request):
    return render(request, "dashboard/dashboard_home.html")


# ------------------------EMPLOYEES

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
			instance.firstname = request.POST.get('firstname')
			instance.lastname = request.POST.get('lastname')
			instance.othername = request.POST.get('othername')
			instance.sex = request.POST.get('sex')
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
			instance.employeeid = request.POST.get('id')
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


# EDIT EMPLOYEE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def employee_edit_data(request, id):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	employee = get_object_or_404(Employee, id=id)
	if request.method == 'POST':
		form = EmployeeCreateForm(request.POST or None, request.FILES or None, instance=employee)
		if form.is_valid():
			instance = form.save(commit=False)

			user = request.POST.get('user')
			assigned_user = User.objects.get(id=user)

			instance.user = assigned_user

			instance.title = request.POST.get('title')
			instance.firstname = request.POST.get('firstname')
			instance.lastname = request.POST.get('lastname')
			instance.othername = request.POST.get('othername')
			instance.sex = request.POST.get('sex')
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
			# messages.success(request, 'Account Updated Successfully !!!', extra_tags='alert alert-success alert-dismissible show')
			return redirect('employees')

		else:

			messages.error(request, 'Error Updating account', extra_tags='alert alert-warning alert-dismissible show')
			return HttpResponse("Form data not valid")

	dataset = dict()
	form = EmployeeCreateForm(request.POST or None,request.FILES or None,instance = employee)
	dataset['form'] = form
	dataset['title'] = 'edit - {0}'.format(employee.get_full_name)
	return render(request,'dashboard/add_employee.html',dataset)


# DELETE EMPLOYEE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, "Employee Deleted Successfully!")
    return redirect('/employees/')


# -----------------------------USERS
# CREATE NEW USER
def create_user(request):
	if request.method == 'POST':
		form = CreateUserForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			username = form.cleaned_data.get("username")

			messages.success(request,'Account created for {0} !!!'.format(username),extra_tags = 'alert alert-success alert-dismissible show' )
			return redirect('dashboard')
		else:
			messages.error(request,'Username or password is invalid',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('create_user')


	form = CreateUserForm()
	dataset = dict()
	dataset['form'] = form
	dataset['title'] = 'register users'
	return render(request,'account/create_user.html',dataset)
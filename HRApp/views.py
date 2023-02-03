from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import *
from .models import *
from .manager import *


# RENDER INDEX PAGE
def index(request):
	if request.user.is_authenticated:
		return render(request, "dashboard/dashboard_home.html")
	else:
		return render(request, "index.html")


# RENDER DASHBOARD PAGE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def dashboard(request):
    return render(request, "dashboard/dashboard_home.html")


# ------------------------EMPLOYEES

# RENDER ALL EMPLOYEES
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
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
    paginator = Paginator(employees, 5)  # show 10 employees per page
    page = request.GET.get('page')
    employees_paginated = paginator.get_page(page)

    dataset['employee_list'] = employees_paginated
    dataset['departments'] = departments
    dataset['all_employees'] = Employee.objects.all()
    dataset['title'] = 'All Employees'
    return render(request, 'dashboard/all_employees.html', dataset)


# CREATE NEW EMPLOYEE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
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
			messages.success(request, 'The Employee was added successfully')
			return redirect('employees')
		else:
			messages.error(request, 'Oppppsss... Something went wrong! Please review your inputs!')
			return redirect('create_employee')
	dataset = dict()
	form = EmployeeCreateForm()
	dataset['form'] = form
	dataset['title'] = 'register employee'
	return render(request, 'dashboard/add_employee.html', dataset)


# EDIT EMPLOYEE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
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
			messages.success(request, 'The Employee was updated successfully')
			
		else:
			messages.error(request, 'Oppppsss... Something went wrong! Please review your inputs!')
			

	dataset = dict()
	form = EmployeeCreateForm(request.POST or None, request.FILES or None, instance = employee)
	dataset['form'] = form
	dataset['title'] = 'edit - {0}'.format(employee.get_full_name)
	return render(request,'dashboard/add_employee.html',dataset)


# DELETE EMPLOYEE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, "Employee Deleted Successfully!")
    return redirect('/employees/')


# -----------------------------USERS
# CREATE NEW USER
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def create_user(request):
	if request.method == 'POST':
		form = CreateUserForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			username = form.cleaned_data.get("username")

			messages.success(request,'Account created for {0} !!!'.format(username))
			return redirect('all_users')
		else:
			messages.error(request,'Username or password is invalid. Please Try again!')
			return redirect('create_user')


	form = CreateUserForm()
	dataset = dict()
	dataset['form'] = form
	dataset['title'] = 'register users'
	return render(request,'account/create_user.html',dataset)

# VIEW ALL USERS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def all_users(request):
	employees = Employee.objects.all()
	
	paginator = Paginator(employees,5)  
	page = request.GET.get('page')
	employees_paginated = paginator.get_page(page)

	return render(request,'account/all_users.html',{'employees':employees_paginated, 'title':'Users List'})


# USER PROFILE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def user_profile(request):
	user = request.user
	if user.is_authenticated:
		employee = Employee.objects.filter(user = user).first()
		emergency = Emergency.objects.filter(employee = employee).first()
		relationship = Relationship.objects.filter(employee = employee).first()
		bank = Bank.objects.filter(employee = employee).first()

		dataset = dict()
		dataset['employee'] = employee
		dataset['emergency'] = emergency
		dataset['family'] = relationship
		dataset['bank'] = bank

		return render(request,'dashboard/user_profile.html',dataset)
	return HttpResponse("Sorry, you are not authorized to access this!")

	
# USERS DETAILS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def user_detail(request,id):
	if not request.user.is_authenticated:
		return redirect('/')
	
	employee = get_object_or_404(Employee, id = id)
	employee_emergency_instance = Emergency.objects.filter(employee = employee).first()
	employee_family_instance = Relationship.objects.filter(employee = employee).first()
	bank_instance = Bank.objects.filter(employee = employee).first()
	
	dataset = dict()
	dataset['employee'] = employee
	dataset['emergency'] = employee_emergency_instance
	dataset['family'] = employee_family_instance
	dataset['bank'] = bank_instance
	dataset['title'] = 'profile - {0}'.format(employee.get_full_name)
	return render(request,'dashboard/user_profile.html',dataset)


# BLOCK USERS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def block_users(request,id):
	user = get_object_or_404(User,id = id)
	emp = Employee.objects.filter(user = user).first()
	emp.is_blocked = True
	emp.save()
	user.is_active = False
	user.save()
	return redirect('all_users')


# UNBLOCK USERS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def unblock_users(request,id):
	user = get_object_or_404(User,id = id)
	emp = Employee.objects.filter(user = user).first()
	emp.is_blocked = False
	emp.save()
	user.is_active = True
	user.save()
	return redirect('all_users')


# CREATE EMERGENCY DETAILS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def emergency_form(request):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	if request.method == 'POST':
		form = EmergencyForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			id = request.POST.get('employee')

			employee_object = Employee.objects.get(id = id)
			name = employee_object.get_full_name
			
			instance.employee = employee_object
			instance.fullname = request.POST.get('fullname')
			instance.tel = request.POST.get('tel')
			instance.location = request.POST.get('location')
			instance.relationship = request.POST.get('relationship')

			instance.save()
			messages.success(request,'Emergency Details Successfully Created')
			return redirect('employees')
		else:
			messages.error(request,'Error Creating Emergency Details')
			return redirect('emergency_form')

	dataset = dict()
	form = EmergencyForm()
	dataset['form'] = form
	dataset['title'] = 'Create Emergency'
	return render(request,'dashboard/emergency.html',dataset)


# EDIT EMERGENCY DETAILS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def emergency_edit(request,id):
	if not (request.user.is_authenticated and request.user.is_superuser):
		return redirect('/')

	emergency = get_object_or_404(Emergency, id = id)
	employee = emergency.employee
	if request.method == 'POST':
		form = EmergencyForm( data = request.POST, instance = emergency)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.employee = employee
			instance.fullname = request.POST.get('fullname')
			instance.tel = request.POST.get('tel')
			instance.location = request.POST.get('location')
			instance.relationship = request.POST.get('relationship')

			instance.save()
			messages.success(request,'Emergency Details Successfully Updated')
			return redirect('employeeinfo',id = employee.id)
		else:
			messages.error(request,'Error Updating Emergency Details')
			return redirect('employeeinfo',id = employee.id)
	dataset = dict()
	form = EmergencyForm(request.POST or None,instance = emergency)
	dataset['form'] = form
	dataset['title'] = 'Updating Emergency Details for {0}'.format(employee.get_full_name)
	return render(request,'dashboard/emergency.html',dataset)


# CREATE FAMILY DETAILS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def family_form(request):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')
		
	if request.method == 'POST':
		form = FamilyForm(data = request.POST)
		
		if form.is_valid():
			instance = form.save(commit = False)
			id = request.POST.get('employee')
			employee_object = Employee.objects.get(id = id)
			name = employee_object.get_full_name
			
			instance.employee = employee_object
			instance.status = request.POST.get('status')
			instance.spouse = request.POST.get('spouse')
			instance.occupation = request.POST.get('occupation')
			instance.tel = request.POST.get('tel')
			instance.children = request.POST.get('children')
			instance.father = request.POST.get('father')
			instance.mother = request.POST.get('mother')

			instance.save()
			messages.success(request,'Family Details Successfully Created')
			return redirect('employees')
		else:
			messages.error(request,'Error Creating Family Details')
			return redirect('family_form')
	dataset = dict()

	form = FamilyForm()

	dataset['form'] = form
	dataset['title'] = 'Family Form'
	return render(request,'dashboard/family.html',dataset)


# EDIT FAMILY DETAILS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def family_edit(request,id):
	if not (request.user.is_authenticated and request.user.is_authenticated):
		return redirect('/')
	relation = get_object_or_404(Relationship, id = id)
	employee = relation.employee

	if request.method == 'POST':
		form = FamilyForm(data = request.POST, instance = relation)
		if form.is_valid():
			instance = form.save(commit = False)
			id = request.POST.get('employee')
			
			instance.employee = employee
			instance.status = request.POST.get('status')
			instance.spouse = request.POST.get('spouse')
			instance.occupation = request.POST.get('occupation')
			instance.tel = request.POST.get('tel')
			instance.children = request.POST.get('children')
			instance.nextofkin = request.POST.get('nextofkin')
			instance.contact = request.POST.get('contact')
			instance.relationship = request.POST.get('relationship')
			instance.father = request.POST.get('father')
			instance.mother = request.POST.get('mother')

			instance.save()
			messages.success(request,'Family Details Successfully Updated')
			return redirect('employeeinfo',id = employee.id)
		else:
			messages.error(request,'Error Updating Family Details')
			return redirect('employeeinfo',id = employee.id)
			
	dataset = dict()
	form = FamilyForm(request.POST or None, instance = relation)

	dataset['form'] = form
	dataset['title'] = 'Update Family Details'
	return render(request, 'dashboard/family.html', dataset)


# CREATE BANK DETAILS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def bank_form(request):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	if request.method == 'POST':
		form = BankAccountForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			employee_id = request.POST.get('employee')
			employee_object = get_object_or_404(Employee,id = employee_id)

			instance.employee = employee_object
			instance.name = request.POST.get('name')
			instance.branch = request.POST.get('branch')
			instance.account = request.POST.get('account')
			instance.salary = request.POST.get('salary')

			instance.save()

			messages.success(request,'Bank Details Successfully Created')
			return redirect('employees')
		else:
			messages.error(request,'Error Creating Bank Details')
			return redirect('bank_form')
	dataset = dict()
	form = BankAccountForm()
	dataset['form'] = form
	dataset['title'] = 'Bank Details Form'
	return render(request, 'dashboard/bank.html', dataset)


# EDIT BANK DETAILS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def bank_edit(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	bank_instance_obj = get_object_or_404(Bank, id = id)
	employee = bank_instance_obj.employee

	if request.method == 'POST':
		form = BankAccountForm(request.POST, instance = bank_instance_obj)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.employee = employee

			instance.name = request.POST.get('name')
			instance.branch = request.POST.get('branch')
			instance.account = request.POST.get('account')
			instance.salary = request.POST.get('salary')

			instance.save()

			messages.success(request,'Bank Details Successfully Updated')
			return redirect('employeeinfo',id = employee.id)
		else:
			messages.error(request,'Error Updating Bank Details')
			return redirect('employeeinfo',id = employee.id)
	dataset = dict()

	form = BankAccountForm(request.POST or None,instance = bank_instance_obj)
	
	dataset['form'] = form
	dataset['title'] = 'Update Bank Account'
	return render(request,'dashboard/bank.html',dataset)


# BIRTHDAYS
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def birthdays(request):	
	if not request.user.is_authenticated:
		return redirect('/')

	employees = Employee.objects.birthdays_current_month()
	month = datetime.date.today().strftime('%B')

	paginator = Paginator(employees, 5)
	page = request.GET.get('page')
	employee_list = paginator.get_page(page)

	context = {
	'birthdays':employee_list,
	'month':month,
	'count_birthdays':employees.count(),
	'title':'Birthdays',
	'employee_list':employee_list,
	}
	return render(request,'dashboard/birthdays.html',context)


# -----------------------------LEAVE

# CREATE LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def create_leave(request):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = CreateLeave(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			instance.save()

			messages.success(request,'Leave Request Sent')
			return redirect('leaves_list')
		else:
			messages.error(request,'Please check your dates')
			return redirect('create_leave')

	dataset = dict()
	form = CreateLeave()
	dataset['form'] = form
	dataset['title'] = 'Apply for Leave'
	return render(request,'dashboard/create_leave.html',dataset)


# ALL LEAVES LIST
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def all_leaves(request):
	leaves = Leave.objects.all_leaves()
	if request.user.is_superuser:
		paginator = Paginator(leaves, 3)
	else:
		paginator = Paginator(leaves, 8)
	page = request.GET.get('page')
	all_leaves = paginator.get_page(page)
	return render(request,'dashboard/all_leaves.html',{'leave_list': all_leaves})

# LEAVE ACTION
def leaves_action(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')

	leave = get_object_or_404(Leave, id = id)
	employee = Employee.objects.filter(user = leave.user)[0]
	return render(request,'dashboard/leave_action.html',{'leave':leave,'employee':employee,'title':'{0}-{1} leave'.format(leave.user.username,leave.status)})


# APROVE LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def approve_leave(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	user = leave.user
	employee = Employee.objects.filter(user = user)
	leave.approve_leave

	messages.success(request,'Leave successfully approved!')
	return redirect('leaves_list')


# UNAPPROVE LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def unapprove_leave(request,id):
	if not (request.user.is_authenticated and request.user.is_superuser):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.unapprove_leave
	messages.success(request,'Leave successfully unapproved!')
	return redirect('leaves_action', id=id) 

# ALL APPROVED LEAVES
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def approved_leaves(request):
	if not (request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	leaves = Leave.objects.all_approved_leaves() 

	paginator = Paginator(leaves, 5)
	page = request.GET.get('page')
	leave_list = paginator.get_page(page)

	return render(request,'dashboard/approved_leaves.html',{'leave_list':leave_list})

# REJECT LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def reject_leave(request,id):
	dataset = dict()
	leave = get_object_or_404(Leave, id = id)
	leave.reject_leave
	messages.success(request,'Leave is successfully rejected!')
	return redirect('leaves_list')

# ALL REJECTED LEAVES
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def rejected_leaves(request):
	if not (request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	leaves = Leave.objects.all_rejected_leaves() 
	paginator = Paginator(leaves, 5)
	page = request.GET.get('page')
	leave_list = paginator.get_page(page)

	return render(request,'dashboard/rejected_leaves.html',{'leave_list':leave_list,'title':'rejected leave list'})
from django.contrib import admin
from django.urls import path, include
from HRApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to access the frontend page
    path('', views.index, name='index'),
    # Path to accounts
    path('accounts/', include('allauth.urls')),
    # Path to access the dashboard page
    path('dashboard/', views.dashboard, name='dashboard'),
    # Path to access all employees page
    path('employees/', views.all_employees, name='employees'),
    # Create new employee
    path('employees/create/', views.create_employee, name='create_employee'),
    # Edit Employee
    path('employee/profile/edit/<int:id>/', views.employee_edit_data, name='edit'),
    # Path to delete the employees 
    path('delete_employee/<int:id>', views.delete_employee, name="delete_employee"),

    # --------USERS----------
    # Path to create User
    path('create-user/', views.create_user, name='create_user'),
]

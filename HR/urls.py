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
    # Path to all users
    path('users/all/', views.all_users, name='all_users'),
    # Path to block an user
    path('users/<int:id>/block', views.block_users, name='block_users'),
    # Path to unblock users
    path('users/<int:id>/unblock', views.unblock_users, name='unblock_users'),
    # Path to user profile
    path('user-profile/', views.user_profile, name='userprofile'),
    # Path to Employee info
    path('employee/profile/<int:id>/', views.user_detail, name='employeeinfo'),
    # Path to emergency form
    path('emergency/create/', views.emergency_form, name='emergency_form'),
    # Path to emergency form edit
    path('emergency/edit/<int:id>', views.emergency_edit, name='emergency_edit'),
    # Path to family form
    path('family/create/', views.family_form, name='family_form'),
    # Path to edit family details
    path('family/edit/<int:id>', views.family_edit, name='family_edit'),
    # Path to bank details form
    path('bank/create/', views.bank_form, name='bank_form'),
    # Path to edti bank details
    path('bank/edit/<int:id>/', views.bank_edit, name='bank_edit'),
    # Path to birthdays page
    path('birthdays/', views.birthdays, name='birthdays'),

    # --------LEAVES----------
    # Path to apply for leave form
    path('leave/apply/', views.create_leave, name='create_leave'),
    # Path to see all pending leaves
    path('leaves/all/', views.all_leaves, name='leaves_list'),
    # Path to leaves action page
    path('leaves/all/action/<int:id>/', views.leaves_action, name='leaves_action'),
    # Path to approve leave
    path('leave/approve/<int:id>/', views.approve_leave, name='aprove_leave'),
    # Path to unaporove leave
    path('leave/unapprove/<int:id>/', views.unapprove_leave, name='unapprove_leave'),
    # Path to approved leave page
    path('leaves/approved/all/', views.approved_leaves, name='approved_leaves'),
    # Path to reject leave
    path('leave/reject/<int:id>/', views.reject_leave, name='reject'),
    # Path to rejected leaves
    path('leaves/rejected/all/', views.rejected_leaves, name='rejected_leaves'),
]

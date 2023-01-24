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
]

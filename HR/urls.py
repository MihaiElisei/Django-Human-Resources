from django.contrib import admin
from django.urls import path, include
from HRApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to access the frontend page
    path('', views.index, name='index'),
    # Path to accounts
    path('accounts/', include('allauth.urls')),
]

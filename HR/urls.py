from django.contrib import admin
from django.urls import path
from HRApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to access the frontend page
    path('', views.index, name='index'),
]

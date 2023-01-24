from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.


# Render Index Page
def index(request):
    return render(request, "index.html")


# Render Dashboard Page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="accounts/login")
def dashboard(request):
    return render(request, "dashboard/dashboard_home.html")

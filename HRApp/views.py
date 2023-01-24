from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


# Render Index Page
def index(request):
    return render(request, "index.html")


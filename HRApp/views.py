from django.shortcuts import render

# Create your views here.


# Render Index Page
def index(request):
    return render(request, "index.html")
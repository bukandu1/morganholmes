from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home page
def home(request):
    return render(request, 'mh/home.html')

def about(request):
    return render(request, 'mh/about.html')
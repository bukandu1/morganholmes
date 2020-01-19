from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Test data for main page
investors = [
    {
        'name': 'ChrisDC',
        'payments': '$200',
        'date_posted': 'January 18, 2020'
    },
    {
        'name': 'BevNU',
        'payments': '$1200',
        'date_posted': 'January 20, 2020'
    },
]

# Home page
def home(request):
    return render(request, 'mh/home.html', {'title': "Morgan & Holmes"})

def about(request):
    return render(request, 'mh/about.html')

def overview(request):
    context = {
        'investors': investors
    }
    return render(request, 'mh/overview.html', context)
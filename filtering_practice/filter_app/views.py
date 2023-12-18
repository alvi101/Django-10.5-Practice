from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    context = {
        'name': 'Alvi',
        'address': 'Dhaka',
        'language': 'python',
        'lst': ['django', 'is', 'fun'],
        'details': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'date': datetime.datetime.now(),
        'str': 'this is random string',
    }
    return render(request, 'index.html', context)

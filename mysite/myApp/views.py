from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request, 'home.html')
#return HttpResponse("Hello, world. You're at the My APP.")

def login(request):


        return render(request, 'login.html')

def sign_up(request):
    print('test')
    return render(request, 'sign_up.html')

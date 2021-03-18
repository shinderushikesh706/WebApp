from django.shortcuts import render
#from models import User

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def index(request):
    return render(request, 'home.html')


# return HttpResponse("Hello, world. You're at the My APP.")

def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        print(request)
        #User.username.objects.all()
        return render(request, 'home.html')


ensure_csrf_cookie(login)


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign_up.html')
    if request.method == 'POST':
        print(request)
        print('test')
        return render(request, 'login.html')

def contact_us(request):
    print('we are at contact')
    return render(request, 'contact_us.html')
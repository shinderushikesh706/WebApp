from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages

from myApp.models import User, Contact


def index(request):

    return render(request, 'home.html')


# return HttpResponse("Hello, world. You're at the My APP.")

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':

        # User.username.objects.all()
        return render(request, 'home.html')


ensure_csrf_cookie(login)


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign_up.html')
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')



        messages.success(request, 'Welcome'+username+', You have successfully created account')

        return render(request, 'login.html')


ensure_csrf_cookie(sign_up)


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Hey '+name+' Thanks for Feedback')

    return render(request, 'contact_us.html')


def about(request):
    return render(request, 'about.html')

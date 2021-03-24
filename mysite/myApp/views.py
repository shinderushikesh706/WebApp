from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
# from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages
from myApp.models import Contact
from django.contrib.auth.models import auth, User


def index(request):
    return render(request, 'home.html')


# return HttpResponse("Hello, world. You're at the My APP.")

def Userlogin(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.success(request, 'Hey ' + username + ' check your credentials')
                return redirect('login')

        else:
            return render(request, 'login.html')


ensure_csrf_cookie(Userlogin)

def Userlogout(request):

    auth.logout(request)

    return redirect('/login')


def sign_up(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':

#           firstname = request.POST['firstname']
#           lastname = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.success(request, 'this username ' + username + ' already taken')
                    return redirect('sign_up')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()

                    messages.success(request, 'Welcome' + username + ', You have successfully created account')
                    return render(request, 'login.html')
            else:
                messages.success(request, 'Hey' + username + ', both password not matching')
                return redirect('sign_up')

        else:
            return render(request, 'sign_up.html')


ensure_csrf_cookie(sign_up)


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Hey ' + name + ' Thanks for Feedback')

    return render(request, 'contact_us.html')


def about(request):
    return render(request, 'about.html')

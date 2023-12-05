from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        x = request.POST['fname']
        y = request.POST['lname']
        z = request.POST['user']
        p = request.POST['email']

        a = request.POST['pass']
        b = request.POST['cpass']
        if a == b:
            if User.objects.filter(email=p).exists():
                messages.error(request, 'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=x, last_name=y, username=z, email=p, password=a)
                user.save()
                messages.success(request,'Registration successful')
                return redirect('register')
        else:
            messages.error(request,'password not match')
            return redirect('/accounts/register')

    else:
        return render(request, 'accounts/register.html')
def login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Invalid login')
            return render(request, 'accounts/signin.html')
    return render(request, 'accounts/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
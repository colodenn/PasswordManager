from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Passwords

# Create your views here.

def index(request):
    return render(request, 'manager/home.html')

@login_required
def dashboard(request):
    username = request.user.id
    passwordobject = Passwords.objects.all().filter(user=username).values()
    print(passwordobject)
    return render(request,'manager/dashboard.html', {'passwordobject':passwordobject})


@login_required
def changepassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwid = request.POST.get('id')
        url = request.POST.get('url')
        password = request.POST.get('password')

        entry = Passwords.objects.filter(user=request.user.id).get(id=pwid)
        entry.url = url
        entry.password = password
        entry.username = username
        entry.save()

    return redirect('/dashboard')

@login_required
def deletepassword(request):
    if request.method == 'POST':
        pwid = request.POST.get('id')
        print(pwid)

        entry = Passwords.objects.filter(user=request.user.id).get(id=pwid)
        print(entry)
        entry.delete()
       
    return redirect('/dashboard')

@login_required
def addpassword(request):
    if request.method == 'POST':
       
        username = request.POST.get('username')
        url = request.POST.get('url')
        password = request.POST.get('password')
        user = User.objects.get(id=request.user.id)
      

        Passwords(user=user,url=url,password=password,username=username).save()
    return redirect('/dashboard') 

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, reverse, redirect
# Create your views here.
from App.models import User


def home(req):
    return render(req, 'home.html')


def register(req):
    if req.method == 'POST':
        u = User.objects.create_user(req.POST.get('username'), req.POST.get('email'), req.POST.get('userpass'))
        u.save()
        return redirect(reverse('App:login'))
    if req.method == 'GET':
        return render(req, 'register.html')


def Login(req):
    if req.method == 'POST':
        u = authenticate(username=req.POST.get('username'), password=req.POST.get('userpass'))

        if u.is_active:
            login(req, u)
            return redirect(reverse('App:home'))
    if req.method == 'GET':
        return render(req, 'login.html')


def Logout(req):
    logout(req)
    return redirect(reverse('App:home'))
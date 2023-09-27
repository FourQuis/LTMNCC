from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

import authentication

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")
def signup(request):
    if request.method == "POST":
        usernames = request.POST['name']  
        emails = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        check = request.POST['agree-term']
        myuser = User.objects.create_user(usernames,emails,pass1)
        myuser.save()

        messages.success(request,"Successfully created")
        
        return redirect('signin')
    return render(request, "authentication/signup.html")
def signin(request):
    if request.method == 'POST':
        username = request.POST['name']
        pass1 = request.POST['pass']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            return render(request, 'authentication/index.html',)
        else:
            messages.error(request,"Bad Credentials")
            return  redirect(home)
    return render(request, "authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request, "Sign out successfully")
    return redirect(home)
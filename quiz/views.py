from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    
    return render(request,'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request , username = email , password = password)
        if user is None :
            messages.error(request,'Invalid Username or Password! please try again.')
            return redirect('login')
        login(request,user)
        return redirect('index')
        
    return render(request,'login.html')

def register_view(request):
    if request.user.is_authenticated :
        return redirect('index')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm-password']
        if password != confirmPassword :
            messages.error(request,"Passwords didn't match.")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already registered.")
            return redirect('register')
        try:
            user = User.objects.create_user(
                username = email,
                first_name = name,
                email = email,
                password = password
            )
            user.save()
            messages.success(request,"Account Registered Successfully")
            return redirect('login')
        except Exception as e:
            messages.error(request,"An error occurred : {e}")
            return redirect('register')
        
    return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required(login_url ='/login/')
def quizzes(request):
    context = {
        'categories' : Category.objects.all(),
        
    }
    return render(request, 'quizzes.html',context)
def category_view(request,name):
    context ={
        'name' : name ,
        'categories' : Category.objects.all(),
        'questions' : Question.objects.all(),
        'answers' : Answer.objects.all(),
        'i' : 0,
    }
    return render(request,'category.html',context)
    



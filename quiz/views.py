from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import random

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
    answers = Answer.objects.all()
    questions = Question.objects.all()
    categories = Category.objects.all()
    context ={
        'name' : name ,
        'categories' : categories,
        'questions' : questions,
        'answers' : answers,
        }
    if request.method == 'POST':
        correct = -1
        check = 0
        any_answer_selected = False
        correct_ans =  []
        questions = questions.filter(category__category_name=name)
        for question in questions: 
            check+=1
            answer = Answer.objects.filter(question = question,answer = request.POST.get(question.question)).first()
            if answer:
                any_answer_selected = True
            if answer.is_correct:
                correct+=1
                correct_ans.append({f"{answer.question}":f"{answer.answer}"})
        
        if not any_answer_selected:
            correct = None
                    
        
        if check > 0:
            correct+=1  
            print(check , correct)      
            context['correct'] = correct*100/check
            context['correct_answers']=correct_ans
            print(correct_ans)
        # print(request.POST)
            
        
        
    return render(request,'category.html',context)
  
def get_quiz(request):
    try:
        questions = list(Question.objects.all())
        data = []
        random.shuffle(questions)
        for q in questions:
            data.append({
                'category' : q.category.category_name,
                'question' : q.question,
                'marks' : q.marks,
                'answer' : q.get_answer()
            })
            
        
        payload = {'status': True , 'Data' : data}
        
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
        return HttpResponse("Something Went Wrong")
    

def contact_view(request):
    return render(request,'contact.html')


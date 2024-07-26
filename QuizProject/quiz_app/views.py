from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Quiz, Question
from .forms import QuizForm, QuestionForm
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponse

def home (request):
    return render (request, 'quiz_app/home.html',)

# def home(request):
#     if request.user.is_authenticated:
#         return redirect('user_quizzes')
#     return render(request, 'quiz_app/home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken.')
                return redirect (reverse('register'))
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken.')
                return redirect (reverse('register'))
            
            else:
                user = User.objects.create_user(username=username, password=password,
                                                email=email, first_name=first_name, last_name=last_name)
                
                user.save()
                messages.success(request, 'Account created successfully.')
                return redirect (reverse('login'))
            
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect (reverse('register')) 
        
    
    else:
        return render(request,'quiz_app/register.html')
                

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect (reverse('create'))
        
        else:
            messages.info(request, 'Invalid Username or Password')
            return render (request, 'quiz_app/login.html')
    
    else: 
        return render (request, 'quiz_app/login.html')
    

def user_logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.creator = request.user
            quiz.save()
            return redirect('add_question', quiz_id=quiz.id)
    else:
        form = QuizForm()
    return render(request, 'quiz_app/create_quiz.html', {'form': form})

@login_required
def add_question(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            if 'add_another' in request.POST:
                return redirect('add_question', quiz_id=quiz.id)
            else:
                return redirect('quiz_detail', quiz_id=quiz.id)
    else:
        form = QuestionForm()
    return render(request, 'quiz_app/add_question.html', {'form': form, 'quiz': quiz})

@login_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def all_quizzes(request):
    quizzes = Quiz.objects.all().order_by('-created_at')
    return render(request, 'quiz_app/all_quizzes.html', {'quizzes': quizzes})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    
    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            submitted_answer = request.POST.get(f'question_{question.id}')
            if submitted_answer == question.answer:
                score += 1
        return render(request, 'quiz_app/quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total': total
        })
    
    return render(request, 'quiz_app/take_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def user_quizzes(request):
    quizzes = Quiz.objects.filter(creator=request.user).order_by('-created_at')
    return render(request, 'quiz_app/user_quizzes.html', {'quizzes': quizzes})

def copy_link(request, quiz_id):
    if request.method == 'POST':
        quiz_link = request.build_absolute_uri(reverse('take_quiz', args=[quiz_id]))
        messages.success(request, f'Quiz link copied: {quiz_link}')
    return redirect('quiz_detail', quiz_id=quiz_id)





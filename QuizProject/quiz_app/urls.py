from django.urls import path
from quiz_app import views

urlpatterns = [
    path('copy_link/<int:quiz_id>/', views.copy_link, name='copy_link'),
    path('my-quizzes/', views.user_quizzes, name='user_quizzes'),
    path('take_quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('all_quizzes/', views.all_quizzes, name='all_quizzes'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/add_question/', views.add_question, name='add_question'),
    path('create_quiz/', views.create_quiz, name='create'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home')
]

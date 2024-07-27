from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

def get_default_user():
    return get_user_model().objects.first().id

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)
    created_at = models.DateTimeField(auto_now_add=True)
    takers = models.ManyToManyField(User, related_name='taken_quizzes', blank=True)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    op1 = models.CharField("Option 1", max_length=500)
    op2 = models.CharField("Option 2", max_length=500)
    op3 = models.CharField("Option 3", max_length=500)
    ANSWER_CHOICES = [
        ('op1', 'Option 1'),
        ('op2', 'Option 2'),
        ('op3', 'Option 3'),
    ]
    answer = models.CharField(max_length=3, choices=ANSWER_CHOICES)

    def __str__(self):
        return self.text
    
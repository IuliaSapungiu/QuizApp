from django import forms
from quiz_app import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['text', 'op1', 'op2', 'op3', 'answer']

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

# class addQuestionform(forms.ModelForm):
#     class Meta:
#         model=models.Quiz
#         fields="__all__"



# class QuizForm(forms.ModelForm):
#     def __init__(self, quiz, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for question in quiz.questions.all():
#             choices = [(answer.id, answer.text) for answer in question.answers.all()]
#             self.fields[f'question_{question.id}'] = forms.MultipleChoiceField(
#                 choices=choices,
#                 widget=forms.CheckboxSelectMultiple,
#                 label=question.text
#             )


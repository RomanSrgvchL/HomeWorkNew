from django import forms

from core import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['poll', 'question', 'count_answer']



class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['question', 'answer']

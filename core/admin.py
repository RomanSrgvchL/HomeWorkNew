from django.contrib import admin

from core.models import Creator, Poll, Question, Answer


@admin.register(Creator)
class Creator(admin.ModelAdmin):
    list_display = ['nickname']


@admin.register(Poll)
class Poll(admin.ModelAdmin):
    list_display = ['theme']


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ['question']


@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display = ['answer']

from django.core.validators import MinValueValidator
from django.db import models


class Creator(models.Model):
    nickname = models.CharField('Никнейм', max_length=100)
    dr = models.DateTimeField('дата регистриции', auto_now_add=True)

    def __str__(self):
        return self.nickname


class Poll(models.Model):
    creator = models.ForeignKey(Creator, verbose_name='Создатель', on_delete=models.CASCADE, related_name='polls')
    theme = models.CharField('Тема', max_length=100)
    dc = models.DateTimeField('дата создания', auto_now_add=True)
    number = models.IntegerField('число участниов', default=0)
    count_question = models.IntegerField('Число вопросов', default=0, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.theme


class Question(models.Model):
    poll = models.ForeignKey(Poll, verbose_name='Опрос', on_delete=models.CASCADE, related_name='questions')
    question = models.CharField('Вопрос', max_length=100)
    dc = models.DateTimeField('дата создания', auto_now_add=True)
    count_answer = models.IntegerField('Число ответов', default=0, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField('Ответ', max_length=100)
    count = models.IntegerField('счётчик', default=0)

    def __str__(self):
        return self.answer

from django.db import models


class Creator(models.Model):
    nickname = models.CharField('никнейм', max_length=100)
    dr = models.DateTimeField('дата регистриции', auto_now_add=True)

    def __str__(self):
        return self.nickname


class Poll(models.Model):
    creator = models.ForeignKey(Creator, verbose_name='creator', on_delete=models.CASCADE, related_name='polls')
    theme = models.CharField('тема', max_length=100)
    dc = models.DateTimeField('дата создания', auto_now_add=True)
    number = models.IntegerField('число участниов', default=0)
    count_question = models.IntegerField('число вопросов', default=0)

    def __str__(self):
        return self.theme


class Question(models.Model):
    poll = models.ForeignKey(Poll, verbose_name='poll', on_delete=models.CASCADE, related_name='questions')
    question = models.CharField('вопрос', max_length=100)
    count_answer = models.IntegerField('число ответов', default=0)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name='question', on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField('ответ', max_length=100)
    count = models.IntegerField('счётчик', default=0)

    def __str__(self):
        return self.answer

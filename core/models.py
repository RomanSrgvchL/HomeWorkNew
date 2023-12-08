from django.db import models


class Creator(models.Model):
    nick = models.CharField('имя', max_length=100)
    dr = models.DateTimeField('дата регистриции', auto_now_add=True)

    def __str__(self):
        return self.nick


class Poll(models.Model):
    creator = models.ForeignKey(Creator, verbose_name='creator', on_delete=models.CASCADE, related_name='опросы')
    theme = models.CharField('название', max_length=100)
    answer1 = models.CharField('ответ1', max_length=100)
    answer2 = models.CharField('ответ2', max_length=100)
    answer3 = models.CharField('ответ3', max_length=100)
    res1 = models.IntegerField('результат1', default=0)
    res2 = models.IntegerField('результат2', default=0)
    res3 = models.IntegerField('результат3', default=0)
    dc = models.DateTimeField('дата создания', auto_now_add=True)

    def __str__(self):
        return f'Опрос "{self.theme}"'

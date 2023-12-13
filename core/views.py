from django.contrib import messages
from django.shortcuts import render
from django.views import View

from core import models
from django.views.generic import ListView, DetailView, TemplateView, CreateView


class Mainpage(TemplateView):
    template_name = 'core/mainpage.html'
    extra_context = {'title': 'Главная страница'}


class Info(TemplateView):
    template_name = 'core/info.html'
    extra_context = {'title': 'Информация о проекте'}


class Creators(ListView):
    template_name = 'core/creators.html'
    extra_context = {'title': 'Создатели опросов'}
    context_object_name = 'creators'
    model = models.Creator


class Creator(DetailView):
    template_name = 'core/creator.html'
    model = models.Creator
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        creator = self.object
        return super().get_context_data(title=creator)


class Polls(ListView):
    template_name = 'core/polls.html'
    extra_context = {'title': 'Опросы'}
    context_object_name = 'polls'
    model = models.Poll


class Poll(DetailView):
    template_name = 'core/poll.html'
    model = models.Poll
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        poll = self.object
        return super().get_context_data(title=poll)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.number += 1
        self.object.save()
        messages.success(request, 'Форма успешно отправлена!')
        # доработать - после обновления страницы сообщение должно пропадать
        return super().get(request, *args, **kwargs)

    # доработать - после отправки формы увеличивать answer.count на 1

class Result(DetailView):
    template_name = 'core/result.html'
    extra_context = {'title': 'Результаты'}
    model = models.Poll
    pk_url_kwarg = 'id'


class Create(CreateView):
    template_name = 'core/create.html'
    extra_context = {'title': 'Создать опрос'}
    model = models.Poll
    fields = ['theme']

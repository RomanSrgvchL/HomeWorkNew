from django.shortcuts import render
from django.views import View

from core import models
from django.views.generic import ListView, DetailView, TemplateView


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
        return super().get(request, *args, **kwargs)
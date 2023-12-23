from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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

        for question in self.object.questions.all():
            answer_id = request.POST.get(str(question))
            answer = question.answers.all()[int(answer_id) - 1]
            answer.count += 1
            answer.save()

        return redirect(request.path)


class Result(DetailView):
    template_name = 'core/result.html'
    extra_context = {'title': 'Результаты'}
    model = models.Poll
    pk_url_kwarg = 'id'


class Create(CreateView):
    template_name = 'core/create.html'
    extra_context = {'title': 'Создать опрос'}
    model = models.Creator
    fields = ['nickname']

    def form_valid(self, form):
        creator = form.save(commit=True)
        theme = self.request.POST.get('theme')
        count_question = self.request.POST.get('count_question')
        models.Poll.objects.create(creator=creator, theme=theme, count_question=count_question)
        return redirect("nextcreate")

    # поставить проверки на введённые значения

class NextCreate(CreateView):
    template_name = 'core/nextcreate.html'
    extra_context = {'title': 'Создать опрос'}
    model = models.Question
    fields = ['poll', 'question', 'count_answer']
    success_url = reverse_lazy('nextcreate')

    def form_valid(self, form):
        poll = models.Poll.objects.last()
        question = self.request.POST.get('question')
        count_answer = self.request.POST.get('count_answer')
        models.Question.objects.create(poll=poll, question=question, count_answer=count_answer)
        return redirect("nextcreate")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_question'] = models.Poll.objects.last().count_question
        context['question_list'] = list(range(1, context['count_question'] + 1))
        return context
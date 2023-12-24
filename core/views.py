from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.forms import formset_factory, modelformset_factory
from .forms import QuestionForm, AnswerForm

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


class CreateCreator(CreateView):
    template_name = 'core/createcreator.html'
    extra_context = {'title': 'Создать опрос'}
    model = models.Creator
    fields = ['nickname']
    success_url = reverse_lazy('createpoll')


class CreatePoll(CreateView):
    template_name = 'core/createpoll.html'
    extra_context = {'title': 'Создать опрос'}
    model = models.Poll
    fields = ['creator', 'theme', 'count_question']
    success_url = reverse_lazy('createquestions')


class CreateQuestions(View):

    def get(self, request, *args, **kwargs):
        poll = models.Poll.objects.last()
        QuestionFormSet = formset_factory(QuestionForm, extra=poll.count_question)
        formset = QuestionFormSet()
        return render(request, 'core/createquestions.html', {'formset': formset, 'title': 'Создать опрос'})

    def post(self, request, *args, **kwargs):
        poll = models.Poll.objects.last()
        QuestionFormSet = formset_factory(QuestionForm, extra=poll.count_question)
        formset = QuestionFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                question = form.save()
            return HttpResponseRedirect('/createanswers')
        return render(request, 'core/createquestions.html', {'formset': formset, 'title': 'Создать опрос'})


class CreateAnswers(View):

    def get(self, request, *args, **kwargs):
        poll = models.Poll.objects.last()
        count_question = poll.count_question
        sum = 0
        if count_question > 1:
            for i in range(count_question - 1, -1, -1):
                question = models.Question.objects.all().order_by('-dc')[i]
                sum += question.count_answer
        else:
            sum = models.Question.objects.last().count_answer
        AnswerFormSet = formset_factory(AnswerForm, extra=sum)
        formset = AnswerFormSet()
        return render(request, 'core/createanswers.html', {'formset': formset, 'title': 'Создать опрос'})

    def post(self, request, *args, **kwargs):
        AnswerFormSet = formset_factory(AnswerForm, extra=2)
        formset = AnswerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                answer = form.save()
            return HttpResponseRedirect('/')
        return render(request, 'core/createanswers.html', {'formset': formset, 'title': 'Создать опрос'})




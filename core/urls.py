from django.urls import path

from core.views import Mainpage, Info, Creators, Creator, Polls, Poll,  Result, CreateCreator,\
    CreatePoll, CreateQuestions, CreateAnswers

urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path('info/', Info.as_view(), name='info'),
    path('creators/', Creators.as_view(), name='creators'),
    path('creator/<id>', Creator.as_view(), name='creator'),
    path('polls/', Polls.as_view(), name='polls'),
    path('poll/<id>', Poll.as_view(), name='poll'),
    path('result/<id>', Result.as_view(), name='result'),
    path('createcreator/', CreateCreator.as_view(), name='createcreator'),
    path('createpoll/', CreatePoll.as_view(), name='createpoll'),
    path('createquestions/', CreateQuestions.as_view(), name='createquestions'),
    path('createanswers/', CreateAnswers.as_view(), name='createanswers'),
]
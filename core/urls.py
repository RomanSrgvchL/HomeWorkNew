from django.urls import path

from core.views import Mainpage, Info, Creators, Creator, Polls, Poll


urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path('info/', Info.as_view(), name='info'),
    path('creators/', Creators.as_view(), name='creators'),
    path('creator/<id>', Creator.as_view(), name='creator'),
    path('polls/', Polls.as_view(), name='polls'),
    path('poll/<id>', Poll.as_view(), name='poll'),
]
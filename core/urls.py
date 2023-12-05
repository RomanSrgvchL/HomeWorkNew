from django.urls import path

from core.views import Homepage
from core.views import Info


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('info', Info.as_view(), name='info')
]
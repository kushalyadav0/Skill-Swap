from django.urls import path
from .views import home
from .views import chat_api

urlpatterns = [
    path('',home, name='home'),
    path('chat/', chat_api, name='chat_api')
]

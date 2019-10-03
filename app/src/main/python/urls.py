from django.urls import path

from app.src.main.python.views import main

urlpatterns = [
    path('', main.index, name='index'),
]

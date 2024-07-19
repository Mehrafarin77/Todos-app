from django.urls import path
from .views import *

urlpatterns = [
    path('', show_todos, name='todos')
]

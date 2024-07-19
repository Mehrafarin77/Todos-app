from django.shortcuts import render
from .models import *

# Create your views here.
def show_todos(request):
    items = TodoItems.objects.all()
    return render(request, template_name='todos.html', context={'todos': items})
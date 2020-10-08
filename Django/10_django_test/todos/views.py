from django.http import request
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Todo

# Create your views here.
@login_required
def index(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }
    return render(request,'todos/index.html',context)

def create(request):
    pass
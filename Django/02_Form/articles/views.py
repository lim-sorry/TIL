from django.http import request
from django.shortcuts import render
from .forms import ArticleForm

# Create your views here.
def index(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/index.html', context)
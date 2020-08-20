# 200820 workshop

1. base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <title>
        {% block title %}
        {% endblock title %}
    </title>
</head>
<body>
    <div class="container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>
```



2. index.html

![image-20200820174747599](C:%5CUsers%5CJS%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200820174747599.png)

```html
{% extends 'base.html' %}


{% block title %}
  index
{% endblock title %}


{% block content %}
  <h2>INDEX</h2>
  <a href="{% url 'articles:new' %}">NEW</a><br>
  <hr>
  {% for article in articles %}
    <h3>제목: {{ article.title }}</h3>
    <h4>내용: {{ article.content }}</h4>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
  {% endfor %}  
{% endblock content %}
```



3. new.html

![image-20200820174351309](C:%5CUsers%5CJS%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200820174351309.png)

```html
{% extends 'base.html' %}


{% block title %}
  new
{% endblock title %}


{% block content %}
  <h2>NEW</h2>
  <form action="{% url 'articles:create' %}" method="post">
    {% csrf_token %}
    <label for="title">TITLE: </label>
    <input type="text" id='title' name='title'><br>
    <label for="content">CONTENT: </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
    <input type="submit" value='작성'>
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```



4. detail.html

![image-20200820174714076](C:%5CUsers%5CJS%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200820174714076.png)

```html
{% extends 'base.html' %}


{% block title %}
  detail
{% endblock title %}


{% block content %}
  <h2>DETAIL</h2>
  <hr>
  <h3>{{ article.title }}</h3>
  <p>{{ article.content }}</p>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  <a href="{% url 'articles:edit' article.pk %}">EDIT</a>
  <a href="{% url 'articles:delete' article.pk %}">DELETE</a><br>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```



5. edit.html

![image-20200820174615573](C:%5CUsers%5CJS%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200820174615573.png)

```html
{% extends 'base.html' %}


{% block title %}
  edit
{% endblock title %}


{% block content %}
  <h2>EDIT</h2>
  <form action="{% url 'articles:update' article.pk %}" method="post">
    {% csrf_token %}
    <label for="title">TITLE: </label>
    <input type="text" id='title' name='title' value='{{ article.title }}'><br>
    <label for="content">CONTENT: </label>
    <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
    <input type="submit" value='수정'>
  </form>
  <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock content %}
```



6. urls.py

```python
from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```



7. views.py

```python
from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:new')


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)    


def update(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:detail', pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```


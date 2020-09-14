# Django 복습

- 가상환경

  ```bash
  # 가상환경 설치
  $ python -m venv venv
  # 가상환경 실행
  $ source venv/Scripts/activate
  ```

- 라이브러리

  ```bash
  # 라이브러리 설치
  $ pip install django
  ```

- .gitignore
  - https://gitignore.io

- 프로젝트 및 앱

  ```bash
  # 프로젝트 생성
  $ django-admin startproject {project_name} {project_dir}
  # 서버 구동 확인
  $ python manage.py runserver
  # 앱 생성
  $ python manage.py startapp {app_name}
  ```

- 앱

  ```bash
  # project/setting.py
  INSTALLED_APPS = [
      'articles',
  ]
  ...
  ```

- urls

  ```python
  # project/urls.py
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls'))
  ]
  ...
  ```

  ```python
  # app/urls.py
  from django.urls import path
  
  app_name = 'articles'
  urlpatterns = [
      
  ]
  ...
  ```

- models

  ```python
  # app/models.py
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=50)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ...
  ```

- 마이그레이션

  ```bash
  # 설계도 파일 생성
  $ python manage.py makemigrations
  # 설계도 데이터베이스 반영 상태 확인
  $ python manage.py showmigrations
  # 설계도 데이터베이스 반영
  $ python manage.py migrate
  ```

  
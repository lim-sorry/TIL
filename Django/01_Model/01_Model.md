# 01_Model

### 사전절차

- Project
  - 프로젝트 생성 후 디렉토리로 이동한다.
  - 앱 생성 후 setting.py의 `INSTALLED_APPS`에 추가한다.

```bash
$ django-admin startproject {project_name}
$ python manage.py startapp {app_name}
```



### Model

- Model
  - `models.Model`을 상속한다.
  - 클래스 변수에 필드를 생성한다.

```python
class Article(models.Model): # 상속
    title = models.CharField(max_length=10) # max_length 필요
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # datetime instance
```



### Migration

- Make Migration
  - models.py으로 새로운 마이그레이션을 생성한다.
  - 모델이 업데이트 될때마다 마이그레이션을 생성 해주어야 한다.

- Migrate
  - 마이그레이션으로 새로운 테이블을 생성한다.
  - 모델의 변경사항과 DB의 스키마를 동기화하는 작업이다.
- Sqlmigrate
  - 마이그레이션에 대한 SQL 구문을 확인할 수 있다.
- Showmigrations
  - 마이그레이션이 반영되었는지 확인할 수 있다.

```bash
$ python manage.py makemigrations
$ python manage.py sqlmigrate articles 0001
$ python manage.py migrate
$ python manage.py showmigrations
```



### Create

- Extensions
  - `ipython`, `django-extensions`을 설치한다.
  - `INSTALLED_APPS`에 django_extensions을 추가한다.
  - `shell_plus`에 진입한다.

```bash
$ pip install ipython django-extensions
$ python manage.py shell_plus
```

- 데이터 작성법
  - 모델 클래스를 통해 인스턴스를 생성한다. 이때 인스턴스 변수는
    1. 생성 후 인스턴스 변수에 직접 값을 할당하거나
    2. 생성할 때 키워드 인자를 활용해 생성하거나
    3. `create` 메소드로 생성할 수 있다.
  - 1번과 2번의 경우  `save()`로 데이터를 저장해줘야한다.

```python
# 1번
article = Article()
article.title = 'title'
article.content = 'content'
article.save()
# 2번
article = Article(title='title', content='content')
article.save()
# 3번
Article.objects.create(title='title', content='content')
```



### Read

- `all()`
  - QuerySet을 반환한다.
  - 리스트는 아니지만 리스트처럼 동작한다.
- `get()`
  - 객체가 없으면 `DoesNotExist` 에러가 발생한다.
  - 객체가 여러개일 경우 `MultipleObjectReturned` 에러가 발생한다.
  - unique 혹은 Not Null 특징을 가진 경우(primary key) 사용할 수 있다.

- `filter()`
  - 지정된 조회 매개 변수와 일치하는 객체를 포함하는 QuerySet을 반환한다.



### Update & Delete

- `delete()`
  - 객체를 삭제한다.
- `save()`
  - 객체의 속성을 변경한 후 다시 저장한다.



### GET & POST

- `GET`
  - 사용자의 요청에 응답한다.
  - `url` 주소로 새로운 웹을 요청할 때
  - `a` 태그로 다른 웹을 요청할 때
- `POST`
  - 데이터베이스에 접근한다.
  - `form` 태그로 데이터베이스 접근을 요청할 때
  - `{% csrf_token %}`을 발급하여 검증을 받아야 접근할 수 있다.


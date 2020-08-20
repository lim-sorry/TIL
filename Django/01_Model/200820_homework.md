# 200820 homework

1. 

```bash
$ python manage.py makemigrations
$ python manage.py migration
```



2. 

```python
# 3
post = Post('제목', '내용')
post.save()
```



3. 

```python
# 4
post4 = Post.objects.all().get(id=1)
```



4. 

```python
my_post.title = "안녕하세요"
my_post.content = "반갑습니다"
my_post.save()
```



5. 

```python
posts = Post.objects.all()
```


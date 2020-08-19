# 200819 homework

1. Model 반영하기

>Migration

```bash
$ python manage.py makemigrations
$ python manage.py sqlmigrate {{ app_name }} {{ mig_number }}
$ python manage.py migrate
$ python manage.py showmigrations
```



2. Model 변경사항 저장하기

> migrations/0001_initial.py

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
```

> makemigrations

```bash
$ python manage.py makemigrations
```



3. Python Shell

>shell_plus

```bash
$ python manage.py shell_plus
```



4. Django Model Field

> CharField, TextField, DateTimeField, BooleanField, BinaryField
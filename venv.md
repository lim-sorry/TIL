- Virtual Environment
  - 프로젝트마다 다른 요구사항에 맞춰줄 수 있다.
  - 각 라이브러리 간 충돌을 줄일 수 있다.

```bash
$ python -m venv {name:venv} 	# 가상환경 생성
$ source venv/Scripts/activate 	# 활성화
$ deactivate 					# 비활성화
```



- VENV preferences
  - `venv` 환경을 설정하고 터미널을 연다.

    새로운 환경이므로 `pip`로 필요한 라이브러리를 설치한다.

  - https://gitignore.io 에서 `.gitignore`을 만들어 `git`을 관리한다.

    Windows, Python, VisualStudioCode, Django, venv 등등

  - Requirements로 필요한 패키지 요구사항을 명시한다.

    `$ pip freeze > requirements.txt`

    업데이트마다 새롭게 요구사항도 업데이트 해준다.



- pip install -r requirements.txt

- 
- 

- python manage.py dumpdata {app_name}.{Model_name} [--options]
- python manage.py loaddata {fixtures_path}
- app/fixtures/
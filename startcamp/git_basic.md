# Git

> Git은 분산 버전 관리 시스템(DVCS)이다.
>
> 소스코드의 버전 및 이력을 관리할 수 있다.



## 준비사항

윈도우에서 `git`을 활용하기 위해서는 `git bash`가 필요하다.

`git`을 활용할 때 GUI 기반 툴들도 존재한다. (ex-`sourcetree`)

설치를 완료한 뒤엔 `author`정보를 입력한다.

```bash
$ git config --global user.name "User Name"
$ git config --global user.email "User Email"

$ git config --global --list
```



## 로컬 저장소(Local Repository) 활용하기

### 1. 저장소 초기화

```bash
$ git init
```

- 저장소를 초기화하면, `.git`이라는 폴더가 생성된다. 여기에 `git`과 관련된 모든 정보가 들어간다.
- `git bash`에 `(master)`라고 표시되는데, 이는 현재 `master` 브랜치에 있다는 것을 의미한다.



### 2. add

작업 공간(`working directory`)에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`라는 공간으로 이동시켜야 한다.

```bash
$ git add .  # 현재 디렉토리의 모든 파일
$ git add a.txt  # 특정 파일
$ git add assets/  # 특정 폴더
```



`add`하기 전 상태

```bash
$ git status

```


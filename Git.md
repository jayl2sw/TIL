# GIT

### 초기설정

* 최초 한번만 설정합니다.

1. Commit (버전 상태 만듬) 누가 커밋을 남겼는지 확인 할 수 있도록 이름과 이메일을 설정합니다.

```bash
# - 하나는 축약문 -- 전체단어 
# ex) -o --option , but 축약문은 겹칠 수 있다.

$ git config --global user.name jayl2cu
$ git config --global user.email jayl2cu@gmail.com
```

2. 설정된 내용 확인

```bash
$ git config --global --list
# or
$ git config --global -l
```


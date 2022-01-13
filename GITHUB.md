# Github

## 회원가입

### 설정 변경

* main 브랜치를 master 브랜치로 기본값 수정 (편의성 위해)



## 원격 저장소(Github)와 로컬 저장소(.git) 연결

### Repository 생성

* `git remote` : `git remote add <단축 이름> <url>`

* `git push` : `git push <리모트 저장소 이름> <브랜치 이름>`

  `-u` : master라는 현재 브랜치를 자동으로 origin 이라는 원격 저장소의 master 브랜치로 연결

 ```bash
 # git으로 원격 저장소 설정을 할 때, origin이라는 별명을 가진 해당하는 주소(경로)로 업로드 할 수 있도록 설정
 # 처음 한번만 설정 
 git remote add origin http://github.com/jayl2sw/TIL.git 
 
 # master 브랜치에 있는 것을 origin 경로로 올린다.
 git push -u origin master 
 ```

 

Git ignore
# branch  

* add -> commit -> push -> 팀원에게 알리기 -> 팀원 pull

* 커뮤니케이션이 중요 !

  하지만 이렇게 항상 알릴 수 는 없기 때문에 branch를 사용한다.

![image-20220113151623429](C:\Users\Jay Lee\Desktop\TIL\GITHUB.assets\image-20220113151623429.png)

* 일반적으로 사용 하는 branch 명 :  

  * `master` : 성역 (함부로 건들지 않는다.)

  * `dev` : develop (여러가지 기능)

  * `chat` : Chat 기능

  * `release` : master에 합치기 전에 최종 테스트

  * `hot fix` : 급하게 버그 또는 문제가 발생했을 때 사용 



---

### branch 명령어 

* 브랜치 `생성, 삭제, 조회` 명령어

```bash
#브랜치 조회
$ git branch

#원격 저장소의 브랜치 목록 확인
$ git branch -r

# 브랜치 생성
$ git branch {branch_name}
```



* `merge`를 통해 나중에 병합
* 저기에 있는 개발 내역을 나한테 가지고 온다.
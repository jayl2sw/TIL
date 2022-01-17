# Python

## python 의 주요기능

`저장  `: dust = 60  dust에 60을 저장한다.

같다 : dust == 60

무엇을 저장하는가? 숫자, 글자, 참/거짓

58 == int  vs  '58' == string

`variable` :  박스 하나

`list` : 박스 여러개의 묶음

`dictionary` : `list`에 이름을 붙인 것

조건

`if` : 만약 뒤의 식이 True 이면 아래 문장 실행

`elif` : if가 아닐 때, 다른 if

`else` : if 과 elif가 모두 아닐 때, 실행



반복

* `while` : True인 동안 계속해서 반복해서 실행 
  * 반드시 종료조건이 필요

```python
n = 0
while n < 3: # n이 3
    print(dust[n])
    n = n + 1
```



* `for` : 정해진 범위 안에서 반복해서 실행
  * 종료조건이 필요없음

```python
for var in range:
    
```



### Python 함수

1) Built in Funcion (내장함수 )

2. non-built in Function 



### Module

#### random

`random.choice()`

`random.sample(range, how many)`



### API

##### Json(JavaScript Object Notation)

* 데이터만을 주고 받기 위한 표기법

* 파이썬의 Dicrionary 와 list구조로 쉽게 변환하여 사용 할 수 있다.



### pip

* python module 설치 명령

  

### request (Third-Party Library)

* python을 통해서 요청 보내는 방법

* `get()` : url에 조회 요청을 보냄



# 2022-01-17

**Program :** 일련의 명령어의 모음

언어 : 자신의 **생각을 나타내고 전달**하기 위해 사용하는 체계

#### 컴퓨터 프로그래밍언어

선언전 지식 : 사실에 대한 내용

명령적 지식 : How-to

'' = '' : 할당  

'' == '' : 같다.

객체: 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것.



`type()` : 변수에 할당된 값의 타입

`id()` : 문자의 id

숫자 + 숫자 (덧셈)

문자 + 문자 (문자를 연결)

문자 * 숫자 (문자를 여러번 작성)

**변수할당** : 같은 값을 동시에 할당할 수 있음

다른값을 동시에 할당 할 수 있음

에러의 특정 

#### 식별자(Identifiers)	

* 변수의 이름을 어떻게 지을 수 있을 까?
* 영문 알파벳, 언더스코어, 숫자
* 길이제한 x 대소문자 구별 예약어 x

```python
RedApple
red_apple <- snake case
```

내장 함수나 모듈 등의 이름으로도 만들면 안됨. 기존의 이름에 다른 값을 할당하게 되므로 더 



#### 사용자 입력

`input([prompt])` 

주석 코드에 대한 설명(컴퓨터는 실행 x)



### 파이썬 자료형

* `Boolean Type` : True/False  리스트, set 등이 비어있으면 False
  * `bool()` : T인지 F인지 반환 bool([])=> false bool([0]) =>t

* `None` : 값이 없음을 표현하기 위함

* `int` : 모든 정수타입

  * 진수 표현 
    * 2진수 0b, 8진수 0o, 16진수 0x

  * Floating point rounding error
    * 부동 소수점에서 실수 연산 과정에서 발생 가능 

* `String Type` : 모든 문자는 str type

  * 작은 따옴표나 큰 따옴표를 활용하여 표기

  * Immutable : 어떠한 값이 불변하다. 할당이 불가능 하다.
  * Iterable : 반복 가능하다.

* Escape Sequence

  * \n \t \\r \0 \\\ \\' \\"

* String Interpolation

  * %-String - 거의 대부분의 

  * .format()

  * f-String

### Container

컨테이너: 여러개의 값을 담을 수 있는 것(객체), 서로 다른 자료형을 저장 할 수 있음

순서가 있는 데이터 (Ordered) vs 순서가 없는 데이터 (Unordered)

시퀀스형: 리스트, 튜플, 레인지

비시퀀스형: 세트, 딕셔너리

#### List

* 숫서를 가지는 0개 이상의 객체를 참조하는 자료형 
  * 생성된 이후 내용 변경이 가능

* list = []
* list = list()



tuple: 수정 불가능

tuple 생성 주의사항

단일 항목의 경우

하나의 항목으로 구성된 튜플은 생성시 값뒤에 쉼표를 붙여야함

() 혹은 tuple()을 통해 생성 

튜플은 일반적으로 파이썬 내부에서 활용

추후 함수에서 복수의 값을 반환 할 때, 사용 

range(): 숫자의 시퀀스를 나타내기 위해 사용

range(n,m,s)



패킹, 언패킹 연산자 

패킹: 대입문의 좌변 변수에 위치

우변의 객체 수가 좌변의 변수 수보다 많을 경우 객체를 순서대로 대입

언패킹:

set: 수학에서 집합과 같은 구조를 가짐

중복없이 순서가 없는 자료 구조 => 인덱스 접근 불가능

set() = 빈셋 생성

{} = 빈 딕셔너리 생성

아래의 리스트레서 고유한 지역을 등장한 순서대로 출력하시오.

=> set을 사용하면 순서가 사라짐

딕셔너리: 순서 없이 키-값쌍으로 이뤄진 객체를 참조하는 자료형

= {} or dict()

key에는 list 불가능하다 

key를 통해서 Value로 접근 따라서 key는 중복 및 변경이 불가능하다.

value는 모든 값으로 설정 가능 

### 형변환

암시적 : 사용자 의도x, 파이썬이 내부적으로 자료형을 변환하는 경우 

ex) bool, Numeric Type

명시적 : str, float => int



### 컨테이너 형 변환

딕셔너리, 레인지로는 변환 불가능 하다.

dictionary를 변환하는 경우 key만 나온다



## 연산자

#### 기타 : 인덱싱(Indexing)

* 시퀀스의 특정 인덱스 값에 접근
  *  해당 인덱스가 없는 경우 IndexError

#### 기타 : 슬라이싱

* 시퀀스를 특정 단위로 슬라이싱

```python
[1, 2, 3, 5][1:4] # 뒤에는 미포함
array[a:b:c] => a 부터 b 전까지 c씩 띄워서
```



프로그램 구성 단위

* 표현식
  * 새로운 데이터 값을 생성하거나 계산하는 코드 조각

* 문장
* 함수 
  * 특정 명령을 수행하는 묶음
* 모듈
  * 다른 프로그램에서 불러와 사용하기 위한 것
* 패키지
  * 프로그램과 모듈 묶음
* 라이브러리
  * 패키지 모음



### 정리

숫자 / boolean / None

String = 문자열의 나열

[list] = 요소들의 시퀀스

(tuple) = 변경 불가능

{set} = 중복 불가능

{dictionary} = key를 통해서 value에 접근 key:중복 불가능, 변경 불가능 value 

## 조건문

### if, elif, else

### 조건 표현식 (list.comprehension)

```python
value = num if num >= 0 else -num
# if num >=0 : expression
# value = num : 참일 경우
# -num : 거짓일 경우
```



## 반복문

### for (통 만들기!)

* for반복 가능한 애들을 꺼내준다 

### while (조건 생각!)

* 조건이 참인 동안 실행 '종료조건(거짓)'



### dictionary 순회

```python
grades = {'kim': 80, 'lee':100}

for key in grades:
    print(key, grades[key])
for key in grades.keys():
    print(key, grades[key])
for value in grades.values():
    print(value)
for key, value in grades.items():
    print(key, value)
```



### enumerate 순회

```python
members = ['민수', '영희', '철수']

print(list(enumerate(members)))

for idx, value in enumerate(members):
    print(idx, value)
```



List Conprehension 실습

```python
cubic_list = []
for number in range(1,4):
    cubic_list.append(number ** 3)

cubic_list                    
                    
```



### 반복문 제어 

`break` : 반복문을 즉시 종료시킨다.

```python
n = 0 
while True:
    if n ==1:
   		break
    print(n)
    n += 1

for i in range(10):
    if i > 1:
        print('0과 1만 필요해!')
       	break
       
```

`continue` : 이후의 코드블록은 수행하지 않고, 다음 반복을 수행

`pass` : 아무것도 하지 않음.

* 그냥 자리 패우는 용도로 사용

`else` : 끝까지 반복문을 실행한 이후에 else문 실행ㄴ

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break 		# b가 없기 때문에 break를 만나지 못한다 --> else로 간다.
else:
    print('b가 없습니다.')
    
for char in 'banana':
    if char == 'b':
	    print('b!')
        break		# break를 통해 반복문이 중단 되었기 때문에 else가 실행 되지 않는다.
else:
    print('b가 없습니다.')
```



### [] vs list()

* 둘 중에 성능은 항상 대괄호 방식이 더 좋음
* 특히 list() 방식은 C 언어 방식
* 최우선은 가독성!! 성능보다 가독성!

```python
list_a = []
for i in range(3):
    list_a.append(i)
```

"Simple is better than complex"

"Keep it simple, stipid"

### 성능 (loop & map & list comp)

* for -> 버전이 올라가면서 성능이 향상되었다.


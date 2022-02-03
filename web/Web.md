# Web

현재의 웹 표준

W3C (WWW컨소시엄)		WHATWG (Apple, Google, Microsoft, Mozilla 기업들간의 표준)

HTML5								HTML Living Standard => 기술 표준화 

익스플로러는 브라우저가 아니다. 크롬만이 브라우저이다!



단순히 웹 사이트 보는 것이 아닌 디버깅등 개발자 도구를 위해 브라우저를 사용

## HTML (Hyper Text Markup Language)

Hyper Text: 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트 

Markup Language: 태크 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

웹페이지 작성을 하기 위한 언어! 

Example

\<h1>HTML\</h1>

<h2\> HyperTest <h2\>

1. 검색기능에 노출되기 위한 수단!
2. 접근성 (찾아가기 쉽다.)

#### HTML 기본구조

* `html`: 문서의 최상위(root) 요소

* `head` : 문서 메타데이터 요소
  * 문서 제목, 인코딩, 스타일, 외부파일 로딩 등
  * 일반적으로 브라우저에 나타나지 않는 내용
  * `<title>` : 브라우저 상단 title
  * `<meta>`
  * 예시 Open Graph Protocol
    * 메타데이터를 표현하는 새로운 규약
    * HTML문서의 메타 데이터를 통해 문서의 정보를 전달
    * 메타정보에 해당하는 제
  * `<link>` : 외부 리소스 연결 요소(CSS, favicon)등
  * `<script>` : 스크립트 요소(javaScript파일/ 코드)
  * `<style>`: CSS 직접 작성
* `body` : 문서 본문 요소
  * 실제 화면 구성과 관련된 내용

#### DOM(Document Object Model)트리

* 텍스트 파일인 HTML문서를 브라우저에서 렌더링 하기 위한 구조
  * HTML 문서에 대한 모델을 구성함



#### 요소(element)

HTML의 요소는 태그와 내용으로 구성되어있다.

* `<h1>contents</h1>`:  <여는 태그> 내용 </닫는 태그> 
  * 어떻게 마크업 할 것인가?

* 태그 : 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
* 내용이 없는 태그들
  * `<br/>, hr, img, input, link, meta` : 기능을 하는 친구들 
* 요소는 중첩 될 수 있음
  * 요소의 중첩을 통해 하나의 문서를 구조화
  * 여는 태그와 닫는 태그의 쌍 확인!
  * 오류 발생 X, 레이아웃이 깨진 상태로 출력되기 때문에 디버깅이 힘들어 질 수 있음.

#### 속성(attribute)

* 태그별로 사용할 수 있는 속성은 다르다
* `<a href="http://google.com>구글</a>`
  * 속성 지정시 공백 사용하지 않는다.
* 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
* 요소의 시작태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재

#### HTML Global Attribute



#### 시맨틱 태그

* HTML5에서 의미론적 요소를 담은 태그의 등장

* 기존 영역을 의미하는 div 태그를 대체하여 사용

  * `<header>, <nav>, <aside>, <section>, <article>, <footer> `
  * 단순히 영역을 나누기 위한 측면

* Non semantic 요소

  * `<div>, <span>`

* 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용

* 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 

  

### HTML 문서 구조화

#### 텍스트 요소

* `<a></a>`: href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
* `<b></b>`, `<strong>` : 굵은 글씨 요소, 중요한 강조하고자하는 요소
  * 눈으로 볼 때는 차이 없음
* `<i></i>`, `<em></em>` : 이탤릭체 요소, 중요한 강조하고자 하는 요소
* `<br>` : 텍스트 내에 줄바꿈 생성
* `<img>` : src 속성을 활용하여 이미지 표현
* `<span></span>` : 의미없는 인라인 컨테이너

​	![image-20220203103117661](Web.assets/image-20220203103117661.png)



#### 그룹컨텐츠

* `<p></p>` : 하나의 문단
* `<hr>` : 수평선
* `<ol></ol>`: 순서가 있는 리스트
* `<ul></ul>` : 순서가 없는 리스트
* `<pre></pre>` : HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자 유지
* `<blockquote></blockquote>`: 텍스트가 긴 인용문 주로 들여쓰기를 한 것으로 표현됨
* `<div></div>`: 의미 없는 블록 레벨 컨테이너

![image-20220203103145197](Web.assets/image-20220203103145197.png)



#### Table

01_table.html 참고



#### form

`<form>`은 정보(데이터)를 서버에 제출하기 위한 영역

* `<form>` 기본 속성
  * action  : form을 처리할 서버의 URL
  * method : form을 제출할 때 사용한 HTTP 메서드 (Get or Post) (요청을 보내는 방법)
    * GET : 오로지 조회만을 위한 요청 (기본값)
    * POST : 어떠한 행위를 한다 (CRUD)
  * enctype : method가 post인 경우 데이터의 유형
    * multipart/form-data : 파일 전송시



#### input

다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

* `<input>` 대표적인 속성
  * name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
  * value : form control에 적용되는 값 (이름/값 페어로 전송됨)
  * `required, readonly, autofocus, autocomplete, disable, placeholder`i

##### input label

* label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  * 사용자는 선택할 수 있는 영역이 늘어나 편리해짐
* `<input>`에 id속성을, `<label>`의 for 속성을 활용하여 상호 연관시킴



##### input유형 - 일반 (type)

* 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML 기본 검증 혹은 추가 속성 활용 가능
  * text
  * password
  * email
  * number : min, max, step 속성들을 활용하여 범위 지정가능
  * file: accept 속성 활용하여 파일 타입가능
* 항목중 선택
  * 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야함.
  * checkbox : 다중 선택
  * radio : 단일 선택
* 기타
  * 다양한 종류의 input을 위한 picker 제공
    * color, date etc
  * hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    * hidden: 사용자에게 보이지 않는 input

+ mdn



## CSS (Cascading Style Sheets)


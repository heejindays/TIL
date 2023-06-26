## 0) 새로운 프로젝트 만들기

- django 새로 프로젝트 만드는 방법 (예시 : dbtest)

- 새롭게 프로젝트 만들기 : django-admin startproject dbtest   

-  세팅하는 방법
  - dbtest >dbtest > settings
  - INSTALLED_APPS = [이 대괄호 안에 새로운 앱인 "dbtest" 추가]



- 파이썬 터미널 창에 입력

  - python manage.py makemigrations dbtest

  - (dsde02) C:\workspaces\workspace_django\dbtest>python manage.py migrate

  - python manage.py migrate (모델의 변경사항을 데이터베이스에 전달)

    - 가상 환경이 맞는지, 이후 OK 메시지가 계속 뜨는지 확인

    

  - python manage.py shell

  - from dbtest.models import MyBoard
  
- from django.utils import timezone
  
- test = MyBoard(myname='testuser', mytitle='testtile', mydate=timezone.now())
    test.save()

  - MyBoard.objects.all()
  
  - exit()
  
    

----------------------------------------------------------------------




## 1) templates

 

- dbtest 프로젝트 > dbtest 앱 > templates 폴더 안에 
- 각 html 파일들을 하나씩 만들어야 함
- 새로 템플릿 폴더를 만들면 세팅 안에 "DIRS": [BASE_DIR/"templates"] 추가



### 1-1) index.html

- 게시판 메인 화면

- 화면에 넣고 싶은 것들이 어떤 모양으로 나올지 고려

    ```<h1>Hello, Django</h1>
    <table border="1">
        <col width="50">
        <col width="100">
        <col width="500">
        <col width="100">
        <tr>
            <th>번호</th>
            <th>작성자</th>
            <th>제목</th>
            <th>작성일</th>
        </tr>
    ```

- <h>태그로 타이틀을 적고 테이블을 만듦

- 이제 각 테이블 안에 값이 들어갈 수 있도록 해야 함

```{% if not list %}
	{% if not list %}
		<tr><th colspan="4">----작성한 글이 존재하지 않습니다---</th></tr>
	{% else %}
		{% for dto in list %}
			<tr>
            	<td>{{ dto.id }}</td>
            	<td>{{ dto.writer }}</td>
            	<td><a href="detail/{{ dto.id }}">{{ dto.title }}</a></td>
            	<td>{{ dto.todate }}</td>
        	</tr>
        {% endfor %}
    {% endif %}
```

- 만약 리스트가 없다면 작성한 글이 없다는 메시지가 나옴

- 각 칸 안에 들어갈 값<tr>태그와 <td> 태그로 적어둠
- 이 값들은 나중에 연결될 예정
- 주의할 점은 {% if %} 으로 시작했으면 {% endif %} 로 닫아야 함
- dto.id는 장고가 자동으로 만든 id 값이 1씩 늘어나면서 들어감

```<tr>
 <tr>
 	<td colspan="4" align="right">
    	<input type="button" value="글작성" onclick="location.href='insertform/'">
    </td>
 </tr>
```

- 글작성 버튼을 눌렀을 때 이동시키고 싶으면

- 글 작성 눌렀을 때 입력하는 페이지(insertform/)로 넘어가게 해야 함

- insertform/은 글 작성하는 페이지고

- insertres/는 작성한 내용의 값을 새로 만드는 페이지

  
  

## 1-2) insert.html 

    <h1>Insert</h1>
    <form action="/insertres/" method="post"> {% csrf_token %}

- form action="" : 웹 페이지에서 사용자가 입력한 정보를 서버로 보내는 것
   (예: 텍스트, 선택 항목, 체크박스 등)
- form 태그가 테이블 전체를 다 감싸고 있어야 함  (서버로 보낼 것 전부 감싸기)
- 주의해야 할 점 :
  - insert.html 페이지에서 form 태그 action 경로를 설정할 때
  - 앞에 / 가 붙어야 root / insertres 가 됨
  - 보내고 싶은 곳은 http://127.0.0.1:8000/insertres/ 이기 때문



- 폼 태그의 액션 속성에는 서브밋 이벤트가 필요함 (서브밋이 있어야 폼태그가 작동함)

- name속성을 적어줘야 form 태그를 통해 전달이 됨 (views.py에서 name 값으로 활용)
- input, textarea 속성도 가운데 들어가는 내용이 값이 됨

- post 방식으로 할 경우 form 태그 안에 위치 상관 없이 {% csrf_token %} 붙여야 공격으로부터 안전

```
<table border="1">
	<tr>
		<th>이름</th>
		<td><input type="text" name="writer"></td>
	</tr>
	<tr>
		<th>제목</th>
		<td><input type="text" name="title"></td>
	</tr>
	<tr>
		<th>내용</th>
		<td><textarea rows="10" cols="60" name="content"></textarea></td>
	</tr>
    <tr>
        <td colspan="2" align="right">
            <input type="button" value="취소" onclick=location.href='/'>
            <input type="submit" value="작성" onclick=location.href='/'>
		</td>
	</tr>
</table>
```



- name이 지정되어있는 <input>, <textaread> 입력 필드는 해당 태그 사이에 있는 값이 value
- 사용자가 입력한 이 값을 views.py에서 해당 이름으로 접근 가능



## 1-3) update.html

- 마찬가지로 {% csrf_token %}을 form 태그 안에 적어서 보호해야 함
- 글번호가 id인데 안 보이게 해둠 (hidden)

```
<h1>Update</h1>
<form action="/updateres/" method="post"> {% csrf_token %}
    <input type="hidden" name="id" value="{{ dto.id }}">
    
    <table>
      <tr>
        <th>작성자</th>
        <td><input type="text" value="{{ dto.writer }}" readonly></td>
      </tr>
      <tr>
        <th>제목</th>
        <td><input type="text" value="{{ dto.title }}" name="mytitle"></td>
      </tr>
      <tr>
      <th>내용</th>
        <td>
          <textarea rows="10" cols="60" name="content">{{ dto.content }}</textarea>
        </td>
      </tr>
      <tr>
        <td colspan="2" align="right">
          <input type="button" value="수정취소" onclick="location.href='{% url 'detail' dto.id %}'">
          <input type="submit" value="수정완료">
        </td>
      </tr>
	</table>
</form>
```



- 수정할 수 있는 페이지를 보여주는 페이지
- 전체적인 틀은 글 작성 페이지와 동일함
- submit 버튼을 누르면 form 태그의 action속성을 통해 "/updateres/" 으로 데이터를 전송
-  <input type="hidden"> 사용자에게 보이지 않고, 숨겨진 상태로 폼 데이터를 전송
- 사용자가 직접 입력하지 않고, 서버에서 값이 할당
- 특정 항목이나 개체를 식별하는 값(예: 데이터베이스 ID)을 폼과 함께 서버로 전송할 때 사용



## 1-4) detail.html

- index에서 제목을 눌렀을 때 나오는 html 페이지

```
<table border="1">
	<tr>
		<th>작성자</th>
        <td><input type="text" value="{{ dto.myname }}" readonly></td>
    </tr>
    <tr>
        <th>제목</th>
        <td><input type="test" value="{{ dto.mytitle }}" readonly></td>
    </tr>
    <tr>
        <th>내용</th>
        <td>
            <textarea rows="10" cols="60" readonly>{{ dto.mycontent }}</textarea>
        </td>
    </tr>
    <tr>
        <td colspan="2" align="right">
            <input type="button" value="목록" onclick="location.href='/'">
            <input type="button" value="수정" onclick="location.href='/updateform/{{ dto.id }}'">
            <input type="button" value="삭제" onclick="location.href='/delete/{{ dto.id }}'">
        </td>
    </tr>
</table>
```

- 테이블을 만들고 작성자, 제목, 내용을 각각 자세히 살펴볼 수 있도록
- 목록 버튼을 누르면 처음(index)으로 이동
- 수정 버튼을 누르면 /updateform/{{ dto.id }} 으로 이동 
  - (dto.id는 고유한 id번호가 / 뒤에 1씩 늘어나서 붙는다)
- 삭제 버튼을 누르면 '/delete/{{ dto.id }}'으로 이동



<hr>



### 2) models

- views가 import해서 가져다 쓸 수 있도록 모델을 만들어야함

- from django.db import models
- Django에서 제공하는 `models` 모듈을 현재 파일에서 import한다



class MultiBoard(models.Model):
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=1000)
    todate = models.DateField()



- models에 파이썬 클래스를 만들었음
- 속성 4개를 만들고 CharField를 사용해서 문자열 필드를 만듦
- 최대 글자수는 각각 100(이름), 500(제목), 2000(본문)이 되게 할 것이다
- MyBoard 클래스가 모델 객체가 됨



<hr>



## 3) settings

dbtest앱 안에 있는 setting.py 파일에 세팅을 해야햠



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

- 이렇게 db.sqlite3을 추가로 설정을 해야 함

- 그리고 INSTALLED_APPS = [] 안에도 새로 만든 "detest"가 들어있는지 확인



<hr>



## 4) views.py 
- urls에서 views로 넘어오면 함수로 각각 연결을 해야 함

- 그 전에 맨 위에 모듈 import를 해줘야 함

  

**from django.shortcuts import render, redirect**
HTML을 랜더링 하겠다 / 다른 URL로 리디렉션 하겠다 
(주어진 URL로 클라이언트 이동 시키겠다)



**from . models import MultiBoard**
현재 디렉토리에서 `models.py` 파일에 정의된 
`MyBoard` 모델을 가져오겠다



**from django.utils import timezone**
시간대와 관련된 기능을 제공하는 모듈



- 이렇게 총 3개의 모듈을 import함

- 사용하고 싶은 모듈을 다 넣었다면
- 이 밑으로는 함수를 넣어서 연결될 수 있도록 설정



### 4-1) index 

데이터 값을 모두 다 가져오고 싶다면?

def index(request):
    return render(request, "index.html", {"list": MultiBoard.objects.all()})



- MultiBoard.objects.all() == select * from dbtest_multiBoard; 이 쿼리랑 같은 의미
- 그 테이블의 모든 데이터를 가지고 와서 "list"에 넣겠다
- 그 다음 "index.html"으로 보내겠다



### 4-2) detail

def detail(request, id):
    multiboard = MultiBoard.objects.get(id=id)
    return render(request, "detail.html", {"dto": multiboard})



- dto라는 이름으로 multiboard의 값을 템플릿에 전달한다는 의미

- detail을 찾을 수 있는 유일한 한가지 방법은 id이기 때문에 id 값을 가져와서 사용
- get() 함수는 조건을 만족하는 것을 하나 가져옴



### 4-3) insert

def insert_form(request):
    return render(request, "insert.html")



- inert_form의 경우는 새로 작성할 페이지로 보내기만 하면 끝

  

def insert_res(request):
    writer = request.POST['writer']
    title = request.POST['title']
    content = request.POST['content']
    result = MultiBoard.objects.create(writer=writer, title=title, content=content, todate=timezone.now())



​    if result:
​        return redirect("index")
​    else:
​        return redirect("/insertform/")



- request.POST로 사용자가 POST로 전송한 데이터를 가져옴
- `'writer'`, `'title'`, `'content'`는 HTML 폼에서 각각의 입력 필드의 `name` 속성으로 지정된 값

- create() : 데이터베이스에 새로운 객체를 생성

  

- 수정하고 나서 저장할 때 리다이렉트 하는 이유
- return render(request, "index.html", {"list":MyBoard.object.all()})
- 위 같은 방법으로 작성하면 새로 고침할 때마다 값이 저장됨
- (기본) 클라이언트가 서버에 요청 + 서버는 처리 후 클라이언트에게 응답
- (리다이렉트) 서버가 클라이언트한테 응답하다가 다시 요청한다
- 리다이렉트를 하면 서버에서 클라이언트로 일단 응답을 해서 response 객체가 만들어지는데
- 이후 클라이언트한테 닿기 전에 다시 요청함 (그 과정에서 새로운 객체가 만들어짐)



### 4-3) update

def update_form(request, id):
    return render(request, "update.html", {"dto": MultiBoard.objects.get(id=id)})



- update도 수정하는 링크와 수정된 내용을 전달하는 링크 2개로 나뉨
- update_form : MultiBoard에서 id가 id인 것을 가져와서 update.html에 응답한다



def update_res(request):
    id = request.POST['id']
    title = request.POST["title"]
    content = request.POST["content"]

​    multiboard = MultiBoard.objects.filter(id=id)

​    result_title = multiboard.update(title=title)
​    result_content = multiboard.update(content=content)

​    if result_title + result_content == 2:
​        return redirect("/detail/"+id)
​    else:
​        return redirect("/updateform/"+id)



- update() : 데이터베이스에 있는 객체의 필드 값을 업데이트

- filter() : 데이터베이스에서 특정 조건을 만족하는 객체들을 검색

- MultiBoard 모델에서 id가 주어진 id와 일치하는 객체를 필터링

  

- if result_title + result_content == 2: 에서 숫자 2는 update() 함수의 반환값

- result_title과 result_content는 업데이트된 객체의 개수를 나타내는 값
-  각각의 update() 함수가 성공적으로 실행되어 업데이트된 객체의 개수가 1인 경우, 
- result_title과 result_content 값은 각각 1임

- result_title + result_content의 값이 2가 되는 것은 
- title과 content 두 개의 필드가 모두 성공적으로 업데이트되었을 때를 의미



1. `filter()`:

   - `filter()` 함수는 지정한 조건을 만족하는 모든 객체를 반환

   - 만약 조건을 만족하는 객체가 없을 경우, 빈 `QuerySet`을 반환

   - `filter()` 함수는 항상 `QuerySet`을 반환하며, 해당하는 객체들의 컬렉션

   - 여러 개의 객체를 반환할 수 있으므로, `QuerySet`을 순회하거나 필요에 따라 필터링된 객체를 선택하여 사용 가능

     

2. `get()`:

   - `get()` 함수는 지정한 조건을 만족하는 단일 객체를 반환
   - 만약 조건을 만족하는 객체가 없거나, 조건을 만족하는 객체가 둘 이상인 경우, 
   - `DoesNotExist` 또는 `MultipleObjectsReturned` 예외가 발생
   - `get()` 함수는 해당하는 단일 객체를 반환하므로, 단일 객체에 바로 접근 가능
   - 주로 고유한 식별자인 `id`나 유일한 필드를 기준으로 객체를 검색할 때 사용



### 4-4) update



def delete(request, id):
    result = MultiBoard.objects.filter(id=id).delete()

​    if result[0]:
​        return redirect("index")
​    else:
​        return redirect(f"/detail/{id}")



- delete() : 데이터베이스에서 객체를 삭제
- delete()는 반환되는 값은 튜플 형태로 (삭제된 객체 수, {dictionary})로 구성
- result[0]는 이 튜플의 첫 번째 요소인 삭제된 객체 수

- id가 같은 데이터들을 찾아서 지울것

-  삭제 작업이 실패했거나 해당 객체가 이미 삭제되었으면 (delete가 실패하면) 디테일페이지로 이동함



<hr>

## 5) urls.py 

- 여기에서도 사용할 모듈들을 추가해야 함

from django.contrib import admin
from django.urls import path
from . import views



urtpatterns = [ ] 안에 새로 생긴 것을 하나씩 추가 (쉼표로 연결)
name으로 값을 지정할 수도 있음



```
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("detail/<int:id>", views.detail, name="detail"),

	path("insertform/", views.insert_form, name="insertform"),
	path("insertres/", views.insert_res),

	path("updateform/<int:id>", views.update_form, name="updateform"),
	path("updateres/", views.update_res),
	path("delete/<int:id>", views.delete, name="delete"),

]
```


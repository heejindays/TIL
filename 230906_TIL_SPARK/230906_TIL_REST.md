## REST

- **REST** 
  - REST (REpresentational State Transfer)
  - 웹 서비스 및 웹 애플리케이션의 설계 원칙을 정의하는 아키텍처 스타일
  - 자원(resource) 중심으로 요청 / 응답
  - **자원 (Resources)**: 모든 것은 자원으로 표현되며, 각 자원은 고유한 식별자(URI)를 가짐 (예를 들어, 웹 페이지, 이미지, 데이터베이스 엔트리 등)
  - **표현 (Representation)**: 자원은 여러 표현 형식(HTML, JSON, XML, 이미지 등)으로 나타낼 수 있음 클라이언트는 요청에 대한 응답을 받음.

<br>

- **배우는 이유는?**
  - DE : 가공될 데이터를 제공할 때 REST 서버를 구축
  - DA/DS : 서버에 요청해서 응답을 받아올 수 있음

<br>

- HTTP 요청 메서드 "http request method"

<br>

- **HTTP 메서드의 주요 역할**
  - GET : resource 요청 (read)
  - POST : recource 저장 (create)
  - PUT : resource 수정 (update) > 덮어 쓰기
  - PATCH : resource 수정 (update) > 일부 수정
  - DELETE : resource 삭제 (delete)

<br>

- get 방식으로 요청해서 응답 받기
- Get the main page from a web-server:
- curl https://www.example.com/

<br>

- restfull 연습을 하기 좋은 페이지 (jsonplaceholder)
  - https://jsonplaceholder.typicode.com/

<br>

- get 방식으로 crul해서 posts 요청 후 응답받기
  - curl https://jsonplaceholder.typicode.com/posts

<br>

- posts 중에서 id가 1인 resource만 가져오기 (뒤에 /1)
  - curl https://jsonplaceholder.typicode.com/posts/1

<br>

- -X : method 명시
  - curl -X GET https://jsonplaceholder.typicode.com/posts/1

<br>

- 1부터 100까지 있을 때 101번째가 궁금하면?

  - curl https://jsonplaceholder.typicode.com/posts/101

  - {} 비어있는 중괄호로 응답됨
  - 서버가 그렇게 만들어져 있음 (잘못된 요청이 오면 비어있는 json 나오도록)
  - 그렇지 않으면 500번대 에러 메시지가 나옴

<br>

- -i : response header와 body를 같이 출력
  - curl -i GET https://jsonplaceholder.typicode.com/posts

<br>

- post
- -d : data
  - curl -d "title=test&body=insert" https://jsonplaceholder.typicode.com/posts
  - {
      "title": "test",
      "body": "insert",
      "id": 101
    }

<br>

- -H : header 변경
  - curl -H "Content-Type: application/json" -d "{\"title\":\"test\", \"body\":\"insert\"}" https://jsonplaceholder.typicode.com/posts

<br>

- put (덮어쓰기 수정)
  - curl -X PUT -d "title=test" https://jsonplaceholder.typicode.com/posts/1

<br>

- patch (일부 수정)
  - curl -X PATCH -d "title=test" https://jsonplaceholder.typicode.com/posts/1

<br>

- delete
  - curl -X DELETE https://jsonplaceholder.typicode.com/posts/1

    

<hr>

- **AXIOS**
  - 브라우저와 node.js를 위한 간단한 HTTP 클라이언트
  - https://axios-http.com/kr/



- REST(ful) 요청하기 위해서 사용 : axios



<hr>

- **django restframework**
  - https://www.django-rest-framework.org/
  - ORM은 "Object-Relational Mapping"

<br>

- 장고 레스트 프레임워크로 만들어보기

- http://127.0.0.1:8000/myboard/

<br>

- POST 직접 보내서 테스트 (2번 테스트)
- curl -d "myname=heejin&mytitle=test&mycontent=dummytest" http://127.0.0.1:8000/myboard/
- curl -d "myname=bom&mytitle=test&mycontent=dummytest2" http://127.0.0.1:8000/myboard/

<br>

- GET (id:2 넣어서 보내기)
  - curl http://127.0.0.1:8000/myboard/2

<br>

- PUT

  - curl -X PUT -d "mytitle=2" http://127.0.0.1:8000/myboard/2

  - column에 null 허용이 안되어있어서 에러 발생!
  - models.py에서 field에 null=True로 설정하면 가능해짐

<br>

- PATCH
  - curl -X PATCH -d "mytitle=2" http://127.0.0.1:8000/myboard/2

<br>

- **PUT은 안 되고 PATCH는 되는 이유는?**
- put : 덮어쓰기 
  - {id : "", myname:"", mycontent:"", mydate} 여야 하는데
  - {mytitle:""}만 만들어지니까 불가
- patch : 부분 수정 
  - {id : "", myname:"", mycontent:"", mydate} 형태가 그대로 유지됨

<br>

- DELETE

- curl -X DELETE http://127.0.0.1:8000/myboard/2
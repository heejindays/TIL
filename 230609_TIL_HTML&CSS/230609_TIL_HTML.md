# HTML (6/9)

**중요 개념 다시 체크!**

- `클라이언트`가 `서버`에 요청

- `서버`는 `클라이언트`에게 응답

<br>

## **form** 
- 안에 있는 데이터를 서버에 전달
데이터를 많이 전달하고 싶을 때 사용 (자주 사용됨)

- action="주소"란?
해당 form에 있는 내용을 이 경로로 요청 한다

- 클라이언트가 서버에 데이터를 요청할 때

- ? 이후 값 전달하는 것 : 쿼리 스트링

- k=v&k=v 형태로 요청함

<br>

## **method**
1) get : 요청할 때 사용함

- header 부분에 요청이 들어가서 보임

- ? 이후 쿼리 스트링이 주소줄에 보임

2) post : 데이터가 겉으로 보이지 않도록

- body 부분에 요청이 들어가서 안보임

- form 태그 아니면 보낼 수 없음

```
** 확인하는 방법

개발자 도구 > Network > 화면에서 액션을 하고 > Name에서 확인하고 싶은 내용 클릭 후 > Payload
```

form 태그 안에서
name 속성이 붙은 것들의 value 

값을 보낼 것

<br>

## **Input**

- input 태그는 타입이 굉장히 많음

- input type="text" : 텍스트로 작성한 것이 값이 됨

- input type="passward" : 작성한 것이 *표시 됨

- input type="radio" : 선택을 하는 동그라미(1개만 선택) 단, 같은 이름으로 만들어야 선택 가능

- input type="checkbox" : TRUE로 체크 되면 선택 (여러개 중복 선택 가능)

- textarea는 줄글 작성 가능

- input type="submit" :  submit event가 발생
action으로 넘어가서 링크 이동 됨 (버튼)

- input type="reset" :  아에 없어짐

<br>

## **Select**

option : 선택할 수 있는 박스 생성함

optgroup : 선택 박스에서 그 안에 그룹을 만들 수 있음


___
<br>

`onclick`은 무엇인가?

- html10-form-res.html로 넘어가서
`onclick` = `click 이벤트가 발생했을 때`라는 의미

- 나중에 자바 공부할 때 다시 배울 예정
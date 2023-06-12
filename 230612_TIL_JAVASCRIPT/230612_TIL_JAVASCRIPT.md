# javacript (6/12)

## 1) index

- script 의 위치 상관 없음

- 예전에는 head에 넣으면 위에서부터 읽어 내려 가다가  화면이 늦게 뜨는 경우가 있어서 화면이 다 구현된 다음에 액션이 실행되도록 했었음

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        function embeddedTest(){
            var doc = document.getElementsByTagName("li")[1];
            doc.style.color = "red";
            doc.innerHTML = "<strong>javascript가 html 문서를 변화시켰습니다!</strong>"
        }
    </script>

    <script src="resources/js/basic.js"></script>

</head>
<body>
    
    <h1>자바스크립트 기본 문법</h1>

    <ol>
    	 // 그 줄 안에서 해결되는 방식
        <li onclick="alert('inline');">inline 방식</li>

		// 같은 파일 안에서 작성되는 방식 (바로 위에 함수 있음)
        <li onclick="embeddedTest();">내부 작성 방식</li>

		// 다른 파일에 작성해서 불러오는 방식
        <li onclick="fileTest();">외부 js 파일</li>
    
	</ol>

</body>
</html>
```



## 2) val

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        // 전역 변수 (10을 variable 변수에 넣겠다)
        var variable = 10;


		// Document.getElementById() 매서드는?
		// 주어진 문자열과 일치하는 id 속성을 가진 요소를 찾고, 
		// 이를 나타내는 Element 객체를 반환

        function val01(){
            // 밖에 있는 변수를 계속 가져다 쓸 수 있음
            variable = variable + 5;
            document.getElementById("value01").innerHTML = 
            "<b style='color:red; background: yellow;'>" + variable + "</b>"
        }

        function val02(){
            // 지역 변수 : 변수가 함수 내부에서 사용하고 끝남
            var innerVal = variable + 5;
            document.getElementById("value02").innerHTML = 
            "<b style='color:red; background: yellow;'>" + innerVal + "</b>"
        }

        function jsType(){
            // 변수가 선언되면서 각각의 값이 들어감
            var inferVal = "문자";
            alert(inferVal + "-> type : " + typeof(inferVal))

            inferVal = 33;
            alert(inferVal + "-> type : " + typeof(inferVal))

            inferVal = true;
            alert(inferVal + "-> type : " + typeof(inferVal))

            inferVal = null;
            alert(inferVal + "-> type : " + typeof(inferVal))

            inferVal = new val01();
            alert(inferVal + "-> type : " + typeof(inferVal))

            // 파이썬 람다와 비슷한 익명 함수
            // 자바스크립트에서도 함수가 값처럼 쓰일 수 있음
            inferVal = function(){alert("타입 추론");}
            alert(inferVal + "-> type : " + typeof(inferVal))
        }

    </script>


</head>
<body>
    
    <h1>var 변수 = 값</h1>

    <dl>변수 선언 규칙</dl>
    <dd>대소문자 구분</dd>
    <dd>영문, $, _로 시작</dd>
    <dd>영문, $, _, 숫자로 시작</dd>
    <dd>키워드(예약어) 사용 불가</dd>
    <br/>

    <dt>변수의 범위</dt>
    <dd>전역변수 : window 객체에 포함됨
        <button onclick="val01();">확인</button>
        <p id="value01"></p>
    </dd>
    <dd>지역변수 : 함수나 객체 내부에 선언
        <button onclick="val02();">확인</button>
        <p id="value02"></p>
    </dd>
    <br/>

    <dt>타입의 종류
        <button onclick="jsType();">확인</button>
        <dd>string</dd>
        <dd>number</dd>
        <dd>boolean</dd>
        <dd>null</dd>
        <dd>object</dd>
        <dd>function</dd>
    </dt>
</body>
</html>
```



## 3) alert

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // alert : 단순 대화창으로 확인 버튼만 있음
        function alertTest(){
            alert("단순 대화창!");
        }

        // confirm은 true(확인)와 false(취소)를 호출함
        function confirmTest(){
            if(confirm("배경을 파란색으로 변환할까요?")){
                alert("파란색으로 변환합니다")
                document.body.style.backgroundColor="skyblue";
            } else {
                alert("배경색을 없앱니다");
                document.body.style.backgroundColor="";
            }
        }

        function confirmTest02(){
            if(confirm("배경을 노란색으로 변환할까요?")){
                alert("노란색으로 변환합니다")
                document.body.style.backgroundColor="yellow";
            } else {
                alert("배경색을 분홍색으로 변환합니다");
                document.body.style.backgroundColor="pink";
            }
        }

        // alert으로 입력값 별로 여러 메시지를 쓸 수 있음 (대화창)
        // 입력 받는 값을 가지고 조건을 걸 수 있음 > txt 변수에 값을 넣음
        function promptTest(){
            var txt = prompt("좋아하는 과목을 선택해주세요(1 : python, 2 : html, 3 : javascript)");

            if (txt == 1){
                alert("python 재밌죠!"); 
            } else if (txt == 2){
                alert("html 쉽죠!")
            } else if (txt ==3){
                alert("javascript는 작동시키는 맛이 있어요!")
            } else if (txt == null){
                alert("취소하지 말아주세요!");
            } else {
                alert("1, 2, 3 중에 하나만 입력해주세요")
            }
        }


    </script>

</head>
<body>
    
    <h1>window 객체의 대화형 매서드</h1>

    <p>alert(내용) : 경고, 코드 디버깅 용
        <button onclick="alertTest();">확인</button>
    </p>

    <p>confirm(내용) : 확인/취소 버튼 (true / false 리턴)
        <button onclick="confirmTest();">확인</button>
    </p>

    <p>
        confirm(내용) : confirm 연습용
        <button onclick="confirmTest02()">노란색 변경 버튼</button>
    </p>

    <p>prompt(내용) : 텍스트박스, 확인/취소 버튼 (텍스트 / null 리턴)
        <button onclick="promptTest();">확인</button>
    </p>

</body>
</html>
```


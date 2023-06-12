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



## 4) function

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // 함수 이름이 있으니까 바로 호출 가능
        function func01(){
            alert("함수의 이름이 있습니다!");
        }


        // 함수 이름이 없어도 실행 가능
        // 함수를 값으로 사용
        var func02 = function(){
            alert("함수의 이름이 없어요!");
        }


        // inner()의 '내부 함수!'가 출력되지 않는 이유는 호출되지 않았기 때문
        // "내부 함수!"가 아니고 "즉시 실행!"이 나옴

        // (function(){ alert("즉시 실행!"); })();
        // 익명함수를 정의하고 즉시 실행하는 패턴
        // 값을 감싸고 뒤에 즉시 실행 연산자인 () 괄호를 붙여서 실행
        // function(){alert("즉시 실행!")} 이거 자체가 값
        function func03() {
            function inner() {
                alert("내부 함수!");
            }
            // inner();
            (function(){
                alert("즉시 실행!");
            })();
        }


        // 익명 함수 자체 통으로 값으로 올 수 있음
        function literalPrn(literal){
            literal("안녕하세요 아규먼트 입니다")
        }

        function func04(){
            literalPrn(function(msg){alert(msg);});
        }

        // closureTest01는 closureTest("홍길동")이라는 함수를 값으로 받음
        // clusureTest(val)을 실행하려고 보니까 val 자리에 "홍길동" 이라는 값을 주면됨
        // closureTest 함수 안에 있는 함수에 val 자리에 "홍길동"이라는 값을 주고
        // suffix 자리에는 "님, 안녕하세요!" 라는 값을 주고 둘을 더함

        function closureTest(val){
            var suffix = "님, 안녕하세요!";

            function innerFunc(){
                alert(val + suffix);
            }

            return innerFunc;
        }

        var closureTest01 = closureTest("홍길동");

        // closureTest02는 val 자리에 '김선달' 이라는 값을 받음
        // 외부 함수에 접근 가능하니까
        // clusureTest()라는 함수가 위에 있어서 갖다 씀
        // 위 과정이랑 똑같은데 대신 val 자리에 '김선달'이 들어감
        // 함수 자체에 ()괄호가 있어서 아래 붙이지 않아도 됨

        function closureTest02(val){
            closureTest(val)();
        }

    </script>
</head>
<body>
    
    <h1>function : 기능</h1>

    <h2>함수의 종류</h2>
    <p onclick="func01();">명시적 함수</p>
    <p onclick="func02();">익명 함수</p>
    <p onclick="func03();">즉시 실행 함수</p>
    <p onclick="func04();">함수 리터럴</p>
    <p onclick="closureTest01()">클로저 : 외부함수에 접근 가능</p>
    <p onclick="closureTest02('김선달')">클로저 : 외부함수에 접근 가능</p>

</body>
</html>
```



## 5) control

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        button{
            width: 50px;
        }
    </style>

    <script>
        function ifTest(){
            var i = prompt("1이나 2를 입력해주세요", "1")
            // prompt 안에 ,"1" 이렇게 기본값 설정 가능

            if (i == 1) {
                alert("1 입니다");
            } else if (i == 2){
                alert("2 입니다")
            } else {
                alert("1이나 2만 입력해주세요!")
            }
        }

          
        // switch / case : 자바스크립트는 해당하는 값 이후 다 호출하기 때문에
        // 멈추고 싶을 때는 break를 중간중간 사용해야 함
        // default : 모든 케이스에 맞지 않을 때 사용
        function switchTest(){
            var season = prompt("좋아하는 계절을 입력해주세요 (봄, 여름, 가을, 겨울)");

            switch(season){
                case "봄":
                    alert("봄에는 벚꽃엔딩")
                    break;
                case "여름":
                    alert("여름에는 바다")
                    break;
                case "가을":
                    alert("가을에는 단풍")
                    break;
                case "겨울":
                    alert("겨울에는 스키장")
                    break;
                default:
                    alert("봄, 여름, 가을, 겨울 중 하나만 입력해주세요!")    
            }
        }


        function forTest(){

            // 자바스크립트에서 증감 연산자 (++, --)
            // 변수의 앞, 뒤에 증감 연산자를 붙이게 되면 변수가 가진 값을 1씩 증가 /감소
            
            // var x = 5;
            // var y = 10;

            // console.log(x++);  // 출력: 5, x는 이후에 1이 증가된다
            // console.log(++x);  // 출력: 7, x는 먼저 1이 증가된다
            // console.log(y--);  // 출력: 10, y는 이후에 1이 감소된다
            // console.log(--y);  // 출력: 8, y는 먼저 1이 감소된다

            // 전위 연산자 : 연산자를 변수 앞에 붙여서 연산 먼저, 값을 나중에 리턴
            // 후위 연산자 : 연산자를 변수 뒤에 붙여서 리턴 먼저, 연산을 나중에

            var i = 5;
            console.log(++i);
            console.log(i++);
            console.log(i);

            var a = 10;
            var b = 3;
            var result = a++ + --b + b++ + ++a;
            //           10(11) + 2() + 2(3) + 12(12)
            console.log(result);

            // for 변수 in 컬렉션(파이썬)
            // for (변수 ; 조건 ; 증감식) (자바스크립트)

            // 조건이 거짓이 될 때까지 반복해서 수행
            for (var i = 0; i < 10 ; i++) {
                console.log(i);
            }

            // 구구단 출력해 보자

            // 2*1 = 2
            // 2*2 = 4
            // 2*3 = 6

            for (var i = 2; i < 10 ; i++) {
                console.log(i+"단");
                for (var j = 1; j < 10; j++){
                    console.log(i + "*" + j + "=" + (i*j));
                }
            }
        }


        function whileTest(){
            var i = 0;
            while (i < 10) {
                console.log(i);
                i++ // i를 1씩 늘려라
            }
            console.log("------------")


            // 원래는 조건을 확인하고 명령을 실행함
            // 자바스크립트에는 do while 이라는 개념이 있음
            // do : 안에 있는 명령을 먼저 무조건 한번 실행 하고 
            // while 조건을 판별함

            var j = 10;
            do {
                console.log(j);
                j--; //j에서 1씩 빼라
            } while(j > 0);
        }

    </script>

</head>
<body>
    
    <button onclick="ifTest();">if</button>
    <br/>
    <button onclick="switchTest();">switch</button>
    <br/>
    <button onclick="forTest();">for</button>
    <br/>
    <button onclick="whileTest();">while</button>
    <br/>

</body>
</html>
```



## 6) DOM

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // ID : 유일한 그 하나
        // 하나 선택된 그 객체를 Node라고 함
        // document.getElenentByID 값이 반환하는 값은 node이다
        // innerHTML : <태그>내용<태그>에서 '내용' 부분

        function searchID(){
            var doc = document.getElementById("test");
            console.log(doc);
            doc.innerHTML = "id로 탐색!";
            doc.style.color = "red";
        }

        // 노드들이 여러개 잡히면 노드 리스트 NODE LIST
        // Elements 여러개니까 list가 됨
        // NodeList [input, input, input]
        // 없는 걸 찾으라고 하면 NodeList [] 비어있는 리스트가 나옴
        // 몇 개 인지 모르기 때문에 일단 노드 리스트로 나옴

        function searchName(){
            var doc = document.getElementsByName("test02");
            doc[1].value = "name으로 탐색!";
            console.log(doc)
        }

        // p로 검색하니까 무조건 노드 리스트
        function serchTagName(){
            // var doc = document.getElementsByTagName("p");
            var doc = document.getElementsByClassName("p");
            doc[3].innerHTML = "tag name 으로 탐색!";
            doc[3].style.color = "blue";
            console.log(doc)
        }

        // querySelector : 선택자 날려서 그거에 맞는거 하나 가져올 것
        // querySelector = 노드 1개 반환
        // querySelectorAll = 노드 리스트로 반환
        // #test : id=test인 것 이니까 선택자로 하나만 찾아오라는 의미 
        function searchQS(){
            // var doc = document.querySelector("#test");
            // doc.innerHTML = "querySelector(css표현식)"

            var doc = document.querySelectorAll("#test");
            doc[0].innerHTML = "querySelectorAll(css 표현식)";
        }
    </script>

</head>
<body>
    
    <p onclick="searchQS()">DOM 탐색</p>

    <p id="test" onclick="searchID()">1. 엘리먼트의 id로 탐색</p>

    <p onclick="searchName()">2. 엘리먼트의 name으로 탐색
        <br/>
        <input type="text" name="test02" /><br/>
        <input type="text" name="test02" /><br/>
        <input type="text" name="test02" /><br/>
    </p>

    <p onclick="serchTagName()">3. 엘리먼트의 tag name으로 탐색 </p>

</body>
</html>
```



## 7) object

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // object01()을 객체로 만들고 싶음
        // this : 객체를 만들었을 때 객체의 속성
        // this : 다양한 의미로 쓰이기 때문에 여기에서 어떻게 쓰였는지를 확인해야함
        // var : 해당 객체에서 사용할 수가 없음
        // name02 : 내부 변수니까 밖에서 쓸 수 없음
        
        function object01(){
            // name 속성을 "홍길동"으로
            this.name = "홍길동";
            // name02 변수를 "hong-gd"로 (지역 변수)
            var name02 = "hong-gd";
            // 외부에서 name02 변수의 값을 반환
            this.getName02 = function(){
                return name02;
            }
        }

        // 객체 리터럴 (객체 값 자체) : {} 중괄호로 만듦
        // 키 : 밸류 형태면 이게 객체 자체라는 걸 알아야 함
        // **중괄호 열고 만들어진 것은 이거 자체가 객체라는 사실만 알면됨

        var object02 = {
            name : "kim-sd",
            prn : function(){
                alert(object02.name + " : 010-1111-1111");
            }
        }
        

        // undefined : 변수가 정의되지 않았다
        function objTest(){
            var obj01 = new object01();
            // alert(obj01.name);
            // alert(obj01.name02);
            // alert(obj01.getName02());

            // alert(object02.name);
            // object02.prn();

            obj01.prn()
        }

        // 프로토타입의 객체를 확장하고 싶다
        // this.name은 오브젝트01이 가지고 있는걸 가져옴
        // 원래 만들어져 있는 걸 수정하고 싶다면 .prototype을 사용
        // 함수에 기능을 추가하고 싶을 때 함수를 수정하는게 아님
        object01.prototype.prn=function(){
            alert(this.name + "010-2222-2222")
        }


    </script>
</head>
<body>
    
    <h1>객체</h1>

    <pre>
        객체의 구성
        - property : 속성
        - function(method) : 기능
        - this : 객체 내부의 매서드나 속성을 정의
        - prototype : 객체 확장
    </pre>

    <button onclick="objTest()">확인</button>

</body>
</html>
```



## 8) string

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // 문자열은 그냥 합쳐짐
        function strTest01(){
            var str01 = "string";
            var str02 = "Test";
            var str03 = str01 + " " + str02;
            alert(str03);

            // 문자열 합치기 concat 함수
            var str04 = str01.concat(" ", str02);
            alert(str04);

            // join도 가능
            // 5-10-15-20 으로 나옴
            var joinTest = ["5", "10", "15", "20"].join("-") //사이에 '-'을 넣겠다
            alert(joinTest);
        }

            // 문자열에 다른 걸 더하면 문자열이 됨
            // 문자열 하나가 추가됨

        function strTest02(){
            var numVal = 12.5;
            var bool = true;
            var result = "str" + numVal + 1 + bool;
            alert(result);
        }


        function strTest03(){


            var str = prompt("이름을 입력하세요 : ");
            var span = document.getElementById("res");


            if (str == "멀캠") {
                span.textContent = str + "님, 환영합니다."
            } else if (str.toLowerCase() == "multicampus") {
                span.textContent = "welsome, " + str;
            } else {
                span.textContent = "이름을 확인해주세요"
            }
            

            // == 2개는 숫자랑 문자를 비교했는데 같다고 나옴
            var numVal = 10;
            if (numVal == "10"){
                alert("== 연산자 사용! (10 == '10')");
            } else {
                alert("== 연산자 사용! (10 != '10')");
            }

            // // === 3개는 엄격하게 비교
            if (numVal === '10'){
                alert("=== 연산자 사용! (10 === '10')");
            } else {
                alert("=== 연산자 사용! (10 !== '10')");
            }


            var strObj = new String("멀캠");
            var strVal = "멀캠";

            // ==은 너그럽게 같다고 나옴
            if (strObj == strVal) {
                alert("같다");
            } else {
                alert("다르다");
            }

            // 1번은 객체고 2번은 값이니까
            if (strObj === strVal) {
                alert("같다");
            } else {
                alert("다르다");
            }
        }

            // indexOf : 왼쪽에서 오른쪽으로 검색 (0부터)
            // lastIndexOf : 오른쪽에서 왼쪽으로 검색
            // 홍길동이 2개니까 값이 2번 다르게 나옴
            // 없는 값을 검색하면 -1이 나옴
        function strTest04(){
            var str = "홍길동 이순신 유재석 강호동 홍길동";
            var prop = prompt("검색할 이름을 작성해 주세요");
            alert("indexOf : " + str.indexOf(prop));
            alert("lastIndexOf : " + str.lastIndexOf(prop));
        }

            // 어디에서부터 어디까지 잘라올 것인지
            // (sIdx+1, eIdx-1)까지 잘라옴 두 번째는 하나 전까지 잘라옴
        function strTest05(){
            var strVal = "문자열 추출하기. 관련 매서드 : indexof, substring.";
            var sIdx = strVal.indexOf(":");
            var eIdx = strVal.lastIndexOf(".");
            var sub = strVal.substring(sIdx+1, eIdx);
            alert(sub);

            // 배열 Array로 가져와짐 > ['indexof', 'substring']
            // split(",")을 기준으로 잘라오라는 뜻
            var splitVal = sub.split(",");
            console.log(splitVal);
            alert(splitVal[0]);
            alert(splitVal[1]);
        }

            // hint : split, prop.length
            // 전체 문장에서 사과, 바나나, 키위, 수박을 잘라야 겠다
            // 그리고 ,를 기준으로 각각 나눈다
            // 그리고 앞에 배열에 들어있는 번호대로 나눠서 키 : 밸류 모양으로 바꾼다
        
            function strTest06(){
            var prop = prompt("쉼표로 구분하여 키워드를 입력하세요", "사과, 바나나, 키위, 수박");
        
            // 1번) , 기준으로 자르자
            prop = prop.split(",");
            // alert(typeof(prop));
            // console.log(prop);
            // alert(prop.length);

            // 2번) prop의 0번지부터 마지막 번지까지 반복하자
            // 3번) 문자열을 결과로 만들자 
            var result = "";
            for (var i = 0; i <prop.length; i++) {
                // alert(prop[i]);
                result += i + " : " + prop[i] + "<br/>";
            }

            document.getElementById("key").innerHTML = result;
        }
    </script>

</head>
<body>
    
    <p>문자열 합치기
        <button onclick="strTest01();">클릭</button>
    </p>

    
    <p>다른 자료형 합치기
        <button onclick="strTest02();">클릭</button>
    </p>

    
    <p>문자열 비교하기
        <button onclick="strTest03();">클릭</button>
        <br/>
        <span id="res"></span>
    </p>

    
    <p>문자열 검색하기
        <button onclick="strTest04();">클릭</button>
    </p>

    
    <p>문자열 추출하기
        <button onclick="strTest05();">클릭</button>
    </p>

    
    <p>키워드 나누기
        <button onclick="strTest06();">클릭</button>
    </p>
    <div id="key"></div>

</body>
</html>
```



## 9) number

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // Number("2") + 1 : 숫자 객체
        // parselnt("2") + 1 : 숫자 값

        // typeof(Number("2") + 1) : 넘버 타입
        // typeof(parselnt("2") + 1) : 넘버 타입


        // new Number() 숫자 생성하기
        function numberObj(){
            var num01 = 3;
            // alert(num01 + " : " + typeof(num01));
            var num02 = new Number(3);
            // alert(num02 + " : " + typeof(num02));
            
            // parseInt() 문자열을 숫자로 바꿔주는 것
            // alert(parseInt("1") + 1);

            // Not a Number 문자 형태를 숫자로 바꿀 순 없음
            // alert(parseInt("a"));

            // isNaN : 숫자 아닌게 맞니? 숫자가 아닌 것이 들어가야 true가 됨
            var num = prompt("숫자만 입력해주세요");
            if (isNaN(num)) {
                alert("숫자가 아닙니다");
            } else {
                alert("숫자입니다");
            }
        }

        function randomNum(){

            // Math 자바 스크립트에 있는 숫자 연산 내장 모듈
            // Math.random() 랜덤으로 숫자 나오게 함 : 0.0 <= x < 1.0
            // math.floor : 소수점 이하를 버림한다
            // math.round : 소수점 이하를 반올림한다
            // math.ceil : 소수점 이하를 올림한다

            // 최소값 : 10 그리고 최대값 : 100
            // 10부터 100까지 랜덤한 숫자가 나옴
            // 공식 : Math.random() * (max - min) + min 
            var min = 10;
            var max = 100;
            var ran = Math.round(Math.random() * (max - min) + min);
            console.log(ran);

        }

        function randomBG(){
            var rnum = function(){
                return Math.round(Math.random()*256);
            }

            // style 색상 표현식 : rgb(256, 256, 256)
            document.body.style.backgroundColor="rgb("+rnum()+", "+rnum()+", "+rnum()+")";
        }

    </script>

</head>
<body>
    
    <h1>숫자</h1>

    <button onclick="numberObj()">숫자</button>
    <br/>
    <button onclick="randomNum()">랜덤 숫자</button>
    <br/>
    <button onclick="randomBG()">랜덤 배경색</button>

    <hr/>


    <!-- 이 아래 부분 숙제 -->
    <button onclick="randomCircle();">랜덤 원</button>
    <br>
    <button onclick="circleArea();">원의 넓이 / 둘레</button>
    <br>

    원의 넓이 : <span id="area"></span>
    <br/>
    원의 둘레 : <span id="len"></span>
    <br>
    <br>
    <div id="circle"></div>

    <style>
        #circle{
            border: 1px solid red;
            display: none;
        }
    </style>

        <!-- 
            
        randomCircle()이라는 함수를 만들건데
        변수 rnum에 어떤 값을 넣을 것이냐면
        Math.floor는 내림을 하는 함수를 값으로 넣을 것이다

        Math.floor 함수 안에는 Math.random 함수가 있는데 
        이는 0 이상 1 미만의 구간에서 함수를 만든다
        이 값에 * 200을 했으니까 0이상 200미만으로 랜덤 숫자가 나온다

        circle이라는 변수에는 
        "circle"을 찾아서 객체로 바꾼 다음에 값으로 넣을 것이다

        circle의 넓이는 랜덤 숫자 px이고
        circle의 높이는 랜덤 숫자 px이다

        borderRadius 테두리를 둥글게 만드는 것은 
        rnum 값을 2로 나눈 것의 내림 값 px 만큼
        
        -->

    <script>
        
        function randomCircle(){
            var rnum = Math.floor(Math.random()*200);
            var circle = document.getElementById("circle");

            circle.style.width = rnum + "px";
            circle.style.height = rnum + "px";

            circle.style.borderRadius = Math.floor(rnum/2) + "px";

            circle.style.display = "block";
            // circle.style.display = "inline";

        }

        // 여기는 아래 내용 채우기
        // 원의 넓이 구하는 공식 : 반지름 * 반지름 * 3.14
        // 원의 둘레 구하는 공식 : 반지름 * 2 * 3.14
        
        function circleArea(){

            var area = document.getElementById("area");

            var len = document.getElementById("len");

            // 넓이랑 둘레 구해서
            // id="area"에는 넓이 / id='len'에는 둘레 넣어서 html에 표시 하자
        }
    </script>

</body>
</html>
```


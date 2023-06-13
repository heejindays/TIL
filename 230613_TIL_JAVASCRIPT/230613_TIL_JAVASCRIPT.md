# javascript (6/13)

## 1) number

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
        Math.floor는 소수점 이하를 버리는 함수를 값으로 넣을 것이다

        Math.floor 함수 안에는 Math.random 함수가 있는데 
        이는 0 이상 1 미만의 구간에서 함수를 만든다
        이 값에 * 200을 했으니까 0이상 200미만으로 랜덤 숫자가 나온다

        circle이라는 변수에는 
        "circle"을 찾아서 객체로 바꾼 다음에 값으로 넣을 것이다

        circle의 넓이는 랜덤 숫자 px이고
        circle의 높이는 랜덤 숫자 px이다

        borderRadius 테두리를 둥글게 만드는 것은 
        rnum 값을 2로 나눈 것의 내림 값 만큼 (px)

        display 스타일 속성을 block으로 설정 원을 화면에 표현함
        (다른 거 아래에 블록으로)
        
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

        // 아래 내용 채우기
        // 원의 넓이 구하는 공식 : 반지름 * 반지름 * 3.14
        // 원의 둘레 구하는 공식 : 반지름 * 2 * 3.14
        
        function circleArea(){

            var circlewidth = document.getElementById("circle").style.width;
            
            // 지름
            var r2 = parseInt(circlewidth);
            // console.log(circlewidth);
            // console.log(r2);
            var r = Math.floor(r2/2)

            // 넓이
            // var area = Math.PI * r * r
            var area = Math.PI * (Math.pow(r,2));

            // 둘레
            var len = Math.PI * r2;

            document.getElementById("area").innerHTML = Math.floor(area);
            document.getElementById("len").innerHTML = Math.floor(len);


            // // 반지름
            // var radius =
            // var area = radius * radius * 3.14
            // document.getElementById("area");

            // // 넓이
            // var radius =
            // var len = radius * 2 * 3.14
            // document.getElementById("len");


            // 넓이랑 둘레 구해서
            // id="area"에는 넓이 / id='len'에는 둘레 넣어서 html에 표시 하자
        }
    </script>

</body>
</html>
```



## 2) date

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // onload = onload=function()
        // 윈도우(브라우저)가 로딩될 때 function 실행
        // 이벤트를 연결시켜주는 것

        onload=function(){
            document.getElementsByTagName("button")[0].onclick = testDate01;
            document.getElementsByTagName("button")[1].onclick = testDate02;
            document.getElementsByTagName("button")[2].onclick = testDate03;
            document.getElementsByTagName("button")[3].onclick = testDate04;
            document.getElementsByTagName("button")[4].onclick = testDate05;

        }

        // 문서에서 버튼이라는 엘리멘트를 다 가져옴
        // 노드 리스트를 다 가져올텐데 0번지를 가져올거고
        // 온클릭으로 클릭 이벤트 발생했을 때 testDate01을 호출
        // 이걸 콜백이라고 함!

        // 콜백(call back) : 지금 당장 실행되는게 아니고 특정하게 필요할 때 호출함
        // 특정 이벤트가 발생했을 때 실행되는 것이 콜백

        function testDate01(){
            //Date 객체 생성
            var date = new Date();

            var inputDate = document.getElementById("today");

            inputDate.innerHTML = date.toDateString() + "<br/>";
            inputDate.innerHTML += date.toLocaleDateString() + "<br/>";
            inputDate.innerHTML += date.toLocaleString() + "<br/>";
            inputDate.innerHTML += date.toLocaleTimeString() + "<br/>";

        }

        function testDate02(){
            var dayOfWeek = ["일", "월", "화", "수", "목", "금", "토"]

            // 2023/06/13으로 출력
            // 오늘 날짜 데이트 객체에서 연, 월, 일을 따로 가져와야 함
            // 2023/06/13 (화)으로 출력

            var today = new Date();

            var year = today.getFullYear();
            // getMonth() : Get month as a number (0-11) 0부터 시작한다
            var month = today.getMonth() + 1;
            var day = today.getDate();
            // the first day of the week (day 0) is Sunday.
            var weekDay = dayOfWeek[today.getDay()];

            // document.getElementById("today").innerHTML = year + "/" + month + "/" + day;
            document.getElementById("today").innerHTML = year + "/" + month + "/" + day + "(" + weekDay+")";
        }


        function testDate03(){

            // 자바스크립드의 월은 0부터 시작함
            var year = 2023;
            var month = 10;
            var day = 31;
            var date = new Date(year, month -1, day);

            document.getElementById("specific").innerHTML = date;
        }

        function testDate04(){
            // .value를 붙이면 데이스트링 값만 가져오겠다는 뜻 (년-월-일)
            var dates = document.getElementById("dates").value;
            // console.log(dates);
            // input 태그에서 가져오면 string
            var inputDate = document.getElementById("inputDate").value;
            // console.log(inputDate);
            // console.log(typeof(inputDate));
            var date = new Date(dates);
            // getDate() : 가져 오는 것
            // setDate() : 값을 넣는 것 (그 안에 add days가 있음)
            date.setDate(date.getDate() + parseInt(inputDate));

            document.getElementById("result").value = date.toLocaleDateString();

        }


        function testDate05(){

            // getTime() 이용하여 D-Day 구하자!
            // 6월 13일, 10월 31일 입력하면 남은 일수 나오도록

            var inputList = document.getElementsByClassName("dday");
            console.log(inputList);
            // 클래스에서 날짜 값을 가져옴
            var start = inputList[0].value;
            var end = inputList[1].value;
            // console.log(start);
            // console.log(end);

            // 각자 날짜 값으로 객체를 만듦
            var startDate = new Date(start);
            console.log(startDate);
            var endDate = new Date(end);
            console.log(endDate);

            // 두 날짜의 차이를 밀리초에서 일 단위로 변환
            var result = (endDate.getTime() - startDate.getTime()) / (1000*60*60*24);

            inputList[2].value = result;


        }



        // textContent랑 innerHTML의 차이는?

    </script>
</head>
<body>
    
    <h1>오늘 날짜 출력하기</h1>
    <span id="today"></span>
    <br/>
    <button>오늘 날짜</button>
    <button>오늘 날짜(표현)</button>


    <h1>특정 날짜 출력하기</h1>
    <span id = "specific"></span>
    <br/>
    <button>특정 날짜</button>


    <h1>경과 날짜 구하기</h1>
    <label>지정 날짜</label>
    <input type = "date" id="dates">
    <br/>
    <label>경과일</label>
    <input type = "number" id="inputDate">
    <br/>
    <label>경과 후 날짜</label>
    <input type = "text" id="result" readonly>
    <br/>
    <button>경과 날짜</button>


    <h1>D-day</h1>
    <label>시작 날짜</label>
    <input type = "date" class="dday">
    <br/>
    <label>종료 날짜</label>
    <input type = "date" class="dday">
    <br/>    
    <label>남은 일수</label>
    <input type = "text" readonly class="dday">
    <br/>
    <button>남은 일수 구하기</button>

</body>
</html>
```



## 3) array

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        function arrayTest(){

            var arrayObj = new Array()
            var arrayLiteral = ["v1", "v2", 3, 4] // 파이썬의 리스트처럼
            // alert(arrayLiteral);

            var arrayObj02 = new Array(5); // 5칸짜리 비어있는 배열이 만들어짐
            // alert(arrayObj02); //,,,,
            // alert(arrayObj02[0]); //undefined
            // alert(arrayObj02.length); // 길이는 5개

            var arrayObj03 = new Array(1, 2, 3, 4, 5);
            alert(arrayObj03); // 1, 2, 3, 4, 5
        }

        function multiArr(){
            // 3칸으로 나누고 그 안에 각각 3칸씩
            var arrLen = 3;
            var arr = new Array(arrLen);
            for (var i = 0; i < arr.length; i++) {
                arr[i] = new Array(arrLen);
            }
            arr[0][0] = "수박";
            arr[0][1] = "오렌지";
            arr[0][2] = "귤";

            arr[1][0] = 1;
            arr[1][1] = 2;
            arr[1][2] = 3;

            arr[2][0] = ["python", "html"];
            arr[2][1] = ["css", "javascript", "jquery"];
            arr[2][2] = ["django", ["machine learning", "deep learning"]];

            // alert(arr); // 배열을 호출하면 쭉 나옴
            // alert(arr.toString());
            // alert(arr[0]) // 수박, 오렌지, 귤
            // alert(arr[2][1][1]) // javascript
            alert(arr[2][2][1][0]) // machine learning
        }

        function joinTest(){
            var arr = ["1", "2", "3", "4", "5"].join("+");
            alert(arr);
            alert(eval(arr)); //문자열로 표현된 코드를 실행함 (보안 취약)
        } 

        function sortTest01(){
            var arr = ["a", "c", "d", "b"];
            arr.sort(); // 정렬
            alert(arr);
        }

        function sortTest02(){
            var arr = [1, 3, 2, 9, 5, 11, 24];
            arr.sort(compareNum); // 아스키코드 순으로 정렬이 됨
            alert(arr);
        }

        // compareFunction 정렬 순서를 정의하는 함수
        // 왜 a - b 일까?
        // https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
        function compareNum(a, b){ 
            return a - b;
        }

        // 내림차순으로 정렬하기(복습)
        function reverseTest(){
            var arr = [19, 2, 22, 41, 33, 17];
            arr.reverse();
            alert(arr);
        }

        function pushAndShift(){
            var queue = new Array();

            //push : 배열 뒤에 값을 추가할 수 있음
            queue.push("first");
            queue.push("second");
            console.log(queue);
            queue.push("third");
            console.log(queue);
            console.log("-----");

            // shift : 오른쪽 첫 번째 요소를 잘라내기 해서 꺼내옴
            var a = queue.shift();
            console.log("a : " +a)
            console.log(queue)
            console.log("-----");

            // pop : 왼쪽 맨 뒤에 요소를 잘라내기 해서 가져옴
            var b = queue.pop()
            console.log("b : " +b)
            console.log(queue)
        }
        
        function sliceTest(){
            var arrayTest01 = new Array(1, 2, 3, 4, 5, 6, 7);
            var array01 = arrayTest01.slice(1, 3); // 인덱스 1부터 3전까지
            alert(array01);

            // arrayTest02 : 4칸 만들어져 있고 그 안에 각각 2칸씩 나뉘어짐
            var arrayTest02 = new Array(4);

            arrayTest02[0] = new Array(1, 2);
            arrayTest02[1] = new Array(3, 4);
            arrayTest02[2] = new Array(5, 6);
            arrayTest02[3] = new Array(7, 8);

            var array02 = arrayTest02.slice(1, 3); 
            alert(array02);

            // 얕은 값 복사가 발생
            // 값이 연동되어 바뀌지 않도록 하려면 새롭게 배열을 만들어야 함
            array02[0][0] = 300;
            alert(arrayTest02);
        }

    </script>

</head>
<body>
    
    <h1 onclick="arrayTest();">배열 객체</h1>

    <ul>
        <li onclick="multiArr();">다중 배열</li>
        <li onclick="joinTest();">join 함수</li>
        <li>배열 정렬
            <ul>
                <li onclick="sortTest01();">sort() : 문자 정렬</li>
                <li onclick="sortTest02();">sort() : 숫자 정렬</li>
                <li onclick="reverseTest();">reverse() : 거꾸로 출력</li>
            </ul>
        </li>
        <li>
            배열 저장 방식
            <ul>
                <li onclick="pushAndShift();">push()</li>
                <li>shift()</li>
                <li>pop()</li>
            </ul>
        </li>
        <li onclick="sliceTest();">slice() : 배열의 부분을 가지고 새 배열 생성</li>
    </ul>
</body>
</html>
```



## 4) popup

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <button onclick="popUp();">팝업창</button>

    <script>
        function popUp(){

            // open(url, target, windowFeatures)
            open("js12-popup-res.html", "", "width=300px, height=300px");
        }
    </script>

</body>
</html>
```

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    화이팅!

</body>
</html>
```



## 5) window (내용 파악 실습)

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <script type="text/javascript">
        // 이미 있는 ID들의 배열
        var ids=["multi","java","script"];
        
        // 중복확인 버튼을 누르면 confirmChk() 함수가 실행
        function confirmChk(){

            // 사용자가 입력한 id값 배열의 0번지 값(노드 하나일테니까)을 id로 가져온다
            var id=document.getElementsByName("id")[0].value;

            // div 배열의 0번지의 요소를 가져온다
            var div=document.getElementsByTagName("div")[0];

            // indexOf() : 배열에서 특정 요소의 인덱스를 검색하고, 
            // 있으면 그 값을 반환하고
            // 해당 요소가 배열에 존재하지 않을 경우 -1을 반환

            // 만약 사용자가 입력한 id 값이 
            // 위에 있는 ids=["multi","java","script"]에 있는 값이면
            if(ids.indexOf(id)!=-1){
                div.innerHTML="<b>아이디가 존재합니다.</b>"; //ID가 이미 존재한다고 나옴
            }else{
                
                // 만약 ids의 인덱스에 배열이 없으면 (indexOf(id) == -1이면) 바로 사용 가능
                // 사용할 수 있는 아이디입니다 라는 문구가 나오고 확인 버튼이 나옴
                // 
                var userId="사용할 수 있는 아이디입니다."
                        +"<input type='button' value='확인'"
                        +"onclick='insertId(\""+id+"\")'>"; //   
                        // \"특수문자를 문자로 취급하게 해주는 것
                        // (\""+id+"\") : 들어가는 값이 문자열이어야 하니까

                // 위에서 받은 userID를 아래 비어있는 div 태그 내용 부분에 넣는다
                div.innerHTML=userId;       
            }
        }
        
        function insertId(id){
            // 부모 창에 있는 id의 [0]번지를 찾아서 id 값을 value에 넣는다
            // 회원가입 창에 값을 전달
            opener.document.getElementsByName("id")[0].value=id;

            // 부모 창에 있는 pwd [0]번지를 찾아서 포커스를 둔다
            // 아이디 입력이 끝나면 바로 패스워드 쪽으로 넘어가게 됨
            opener.document.getElementsByName("pwd")[0].focus();
            close();
        }
    </script>

</head>
<body>
    
    <!-- 테이블을 만들 것이다 -->
	<table>
		<tr>
            <!-- input 태그로 사용자로부터 아이디를 입력할 수 있도록 한다 -->
            <!-- type = text 로 입력 필드를 만들어서 id 값을 받는다 -->
			<td>아이디</td> 
			<td><input type="text" name="id"/></td>
		</tr>
		<tr>
            <!-- 테이블의 2 열을 하나로 합친다 -->
			<td colspan="2">
                <!-- 첫번째에는 중복확인이라는 버튼을 만들어서 클릭하면 confirmChk() 실행 -->
				<input type="button" value="중복확인" onclick="confirmChk()"/>
                <!-- 두번째에는 취소이라는 버튼을 만들어서 클릭하면 self.close() 실행 -->
                <!-- self.close()는 지금 창을 닫아버림 -->
				<input type="button" value="취소" onclick="self.close()"/>
			</td>
		</tr>
	</table>
	<div></div>

</body>
</html>
```

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script type="text/javascript">

        // 전달 버튼을 누르면 아래 test() 함수가 실행된다
        function test(){

            // 아래 전달 버튼을 눌러서 들어온 값 배열의 0번지를 val 변수에 넣는다
            var val=document.getElementsByName("test")[0].value;

            // opener : 부모 창의 문서에 접근하는 것
            // getElementsByTagName("h1") 문서에서 모든 <h1>요소를 가져오는데
            // ("hi")[1] 이 부분이 13-window의 '팝업창 만들기' 부분
            // 그 중에서 [1]번지 자리에 있는 값을 선택한다
            // 부모창 <h1>요소의 내용을 'val' 변수의 값으로 변경한다
            opener.document.getElementsByTagName("h1")[1].innerHTML=val;

            //나 윈도우 종료
            self.close();
        }
    </script>
    
</head>
<body>

    <!-- text를 입력할 수 있는 구역을 만든다 -->
	<input type="text" name="test"/>

    <!-- 버튼을 만드는데 클릭하면 test() 함수가 실행되고 버튼명은 전달이다 -->
	<input type="button" onclick="test()" value="전달"/>

    <!-- 버튼을 만드는데 클릭하면 self.close() 함수가 실행되고 버튼명은 창닫기이다 -->
    <!-- self.close()는 지금 창을 닫아버림 -->
    <input type="button" onclick="self.close()" value="창닫기">

</body>
</html>
```

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <script type="text/javascript">
        // 이미 있는 ID들의 배열
        var ids=["multi","java","script"];
        
        // 중복확인 버튼을 누르면 confirmChk() 함수가 실행
        function confirmChk(){

            // 사용자가 입력한 id값 배열의 0번지 값(노드 하나일테니까)을 id로 가져온다
            var id=document.getElementsByName("id")[0].value;

            // div 배열의 0번지의 요소를 가져온다
            var div=document.getElementsByTagName("div")[0];

            // indexOf() : 배열에서 특정 요소의 인덱스를 검색하고, 
            // 있으면 그 값을 반환하고
            // 해당 요소가 배열에 존재하지 않을 경우 -1을 반환

            // 만약 사용자가 입력한 id 값이 
            // 위에 있는 ids=["multi","java","script"]에 있는 값이면
            if(ids.indexOf(id)!=-1){
                div.innerHTML="<b>아이디가 존재합니다.</b>"; //ID가 이미 존재한다고 나옴
            }else{
                
                // 만약 ids의 인덱스에 배열이 없으면 (indexOf(id) == -1이면) 바로 사용 가능
                // 사용할 수 있는 아이디입니다 라는 문구가 나오고 확인 버튼이 나옴
                // 
                var userId="사용할 수 있는 아이디입니다."
                        +"<input type='button' value='확인'"
                        +"onclick='insertId(\""+id+"\")'>"; //   
                        // \"특수문자를 문자로 취급하게 해주는 것
                        // (\""+id+"\") : 들어가는 값이 문자열이어야 하니까

                // 위에서 받은 userID를 아래 비어있는 div 태그 내용 부분에 넣는다
                div.innerHTML=userId;       
            }
        }
        
        function insertId(id){
            // 부모 창에 있는 id의 [0]번지를 찾아서 id 값을 value에 넣는다
            // 회원가입 창에 값을 전달
            opener.document.getElementsByName("id")[0].value=id;

            // 부모 창에 있는 pwd [0]번지를 찾아서 포커스를 둔다
            // 아이디 입력이 끝나면 바로 패스워드 쪽으로 넘어가게 됨
            opener.document.getElementsByName("pwd")[0].focus();
            close();
        }
    </script>

</head>
<body>
    
    <!-- 테이블을 만들 것이다 -->
	<table>
		<tr>
            <!-- input 태그로 사용자로부터 아이디를 입력할 수 있도록 한다 -->
            <!-- type = text 로 입력 필드를 만들어서 id 값을 받는다 -->
			<td>아이디</td> 
			<td><input type="text" name="id"/></td>
		</tr>
		<tr>
            <!-- 테이블의 2 열을 하나로 합친다 -->
			<td colspan="2">
                <!-- 첫번째에는 중복확인이라는 버튼을 만들어서 클릭하면 confirmChk() 실행 -->
				<input type="button" value="중복확인" onclick="confirmChk()"/>
                <!-- 두번째에는 취소이라는 버튼을 만들어서 클릭하면 self.close() 실행 -->
                <!-- self.close()는 지금 창을 닫아버림 -->
				<input type="button" value="취소" onclick="self.close()"/>
			</td>
		</tr>
	</table>
	<div></div>

</body>
</html>
```


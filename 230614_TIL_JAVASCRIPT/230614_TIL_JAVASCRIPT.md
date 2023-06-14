# javascript (6/14)

## 1) check

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        #colorbox{
            width: 320px;
            height: 320px;
            position: relative;

            /* position: relative : 요소 내의 자식 요소에 
            top, right, bottom, left 값을 지정하면 위치 조정 */
        }

        /* 4개 한꺼번에 만들고 */
        #red, #yellow, #blue, #black{
            width: 150px;
            height: 150px;
            border: 1px solid black;
            position: absolute; 
        }

        /* 왼쪽으로부터 160px 떨어지게 이동 */
        #yellow {
            left: 160px;
        }

        /* 위쪽으로부터 160px 떨어지게 이동 */
        #blue{
            top: 160px;
        }

        /* 왼쪽에서 160px, 위에서 160px 떨어지게 이동 */
        #black{
            left: 160px;
            top: 160px;
        }
    </style>

    <script>

        // 전체 선택 체크
        function allSelect(check){
            var chks = document.getElementsByName("chk"); // chks : 노드리스트(array)
            for(var i = 0 ; i < chks.length ; i++){
                chks[i].checked = check;
            }
        }

        // 색 채우기
        function selectColor(){
            var chks = document.getElementsByName("chk");
            for (var i = 0; i < chks.length; i++) {
                if (chks[i].checked) {
                    document.getElementById(chks[i].value).style.backgroundColor = chks[i].value // 값 자체가 색
                } else {
                    document.getElementById(chks[i].value).style.backgroundColor = "";
                }
            }
        }


        function clearAll(){

            // 1. 체크박스 모두 해제
            var checkbox = document.querySelectorAll("input[name]") 
            // 페이지에 있는 모든 name 속성을 가진 input 요소를 선택
            for (var i = 0; i<checkbox.length; i++) {
                checkbox[i].checked = false; // 다 false로 만듦
            }

            // 2. 색상 모두 없애기
            var colorbox = document.querySelectorAll("#colorbox > div");
            for(var i = 0; i <colorbox.length; i++) {
                colorbox[i].style.backgroundColor = ""; // 다 색 없앰
            }
        }

    </script>

</head>
<body>
    
    <div id = "colorbox">
        <div id="red"><b>red</b></div>
        <div id="yellow">yellow</div>
        <div id="blue">blue</div>
        <div id="black">black</div>
    </div>

    <div id="base">
        <!-- this : checkbox -->
        <!-- .checked : 체크 되어있으면 True 아니면 False -->
        <input type="checkbox" name="all" onclick="allSelect(this.checked);"/>전체선택<br/>

        <input type="checkbox" name="chk" value="red">빨강<br/>
        <input type="checkbox" name="chk" value="yellow">노랑<br/>
        <input type="checkbox" name="chk" value="blue">파랑<br/>
        <input type="checkbox" name="chk" value="black">검정<br/>

        <input type="button" value="선택" onclick="selectColor();"><br/>
        <input type="button" value="초기화" onclick="clearAll()"><br/>

    </div>

</body>
</html>
```



## 2) DOM - 1

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        /* <a> 태그의 자식 태그인 <img> 태그 사이즈(화살표) */
        a > img {
            width: 50px;
            height: 50px;
        }
        #gallery {
            width: 200px;
            height: 200px;
        }
        p {
            width: 350px;
            height: 250px;
        }
        /* 이미지 수직으로 가운데 정렬 */
        img {
            vertical-align: middle;
        }
        /* 텍스트 밑줄 없앰 (장식 없음) */
        a {
            text-decoration: none;
        }
    </style>


    <!-- DOM : 문서를 찾아서 객체화 해서 쓸 수 있음 -->
    <script>
        var num = 1;

        function prevGallery(){
            
            // 1. num 숫자 감소시키자
            num--;

            // 2. 만일 num 값이 1보다 작아지면 6으로 바꾸자
            if (num < 1) {
                num = 6;
            }
            
            // 3. gallery 에서 찾아서 src 값 바꾸자
            document.getElementById("gallery").src = "resources/imgs/img0"+num+".png";

            return false;
        }

        function nextGallery(){
            num++;
            if (num > 6) {
                num = 1;
            }
            document.getElementById("gallery").src = "resources/imgs/img0"+num+".png";

            return false; // 버튼을 클릭했을 때 페이지가 새로고침되지 않도록
        }
    </script>

</head>
<body>
    
    <div id="gallerywrap">
        <p>
            <!-- 왼쪽 화살표 클릭 시 이전 이미지 -->
            <a href="#" onclick="return prevGallery()">
                <img src="resources/imgs/arrowleft.png" alt="">
            </a>

            <img src="resources/imgs/img01.png" alt="" id="gallery">

            <!-- 오른쪽 화살표 클릭 시 다음 이미지 -->
            <a href="#" onclick="return nextGallery();">
                <img src="resources/imgs/arrowright.png" alt="">
            </a>
            <a href=""></a>
        </p>

    </div>

</body>
</html>
```



## 3) DOM - 2

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        function searchParent(){
            // child02는 1번지 하나 가져옴 : 노드
            var child02 = document.getElementsByTagName("p")[1];
            var parent = child02.parentNode; // 부모 노드<div>를 찾아서 활용 가능
            console.log(parent);
            console.log(typeof(parent)); //object 
            alert(parent.nodeName) // nodeName:"DIV"

        }

        function searchChildren(){
            var div = document.getElementsByTagName("div")[0];

            var children = div.childNodes; 
            // childNodes; 태그만 가지고 오는게 아니고 text 노드까지 같이 가져옴
            // child03의 배경색을 blue로 바꾸자

            console.log(children);
            // 엔터로 줄바꿈한 부분이 공백 문자 노드로 'text'로 잡힘
            // 주석도 comment로 잡힘
            // 그래서 [5]번지로 잡아야 원하는 child03이 잡힌다
            
            children[5].style.backgroundColor="blue";
        }
    </script>
</head>
<body>
    
    <h1>부모 탐색, 자식 탐색</h1>

    <!-- 부모가 <div>, 자식이 <p> -->
    <div>
        <p>child01</p>
        <p>child02</p>
        <p>child03</p>
    </div>

    <button onclick="searchParent();">부모탐색</button>
    <button onclick="searchChildren();">자식탐색</button>

</body>
</html>
```



## 4) DOM - 3

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        function eleCreate(){
            
            // createElement() 엘리먼트를 만든다
            // div = <div></div>
            var div = document.createElement("div");

            // 속성 지정하는 법

            // 1.
            /*
            var attr = document.createAttribute("style"); // 속성 만들기
            attr.nodeValue = "border: 2px solid blue"; // 속성에 값 넣기
            div.setAttributeNode(attr); // 노드에 속성으로 넣음
            */

            // 2.
            div.setAttribute("style", "border:2px solid red")

            // text 생성
            // div = <div style="border:2px solid blue">엘리먼트 생성 매서드</div>
            var txt = document.createTextNode("엘리먼트 생성 매서드");
            div.appendChild(txt); // 자식 요소로 추가

            document.body.appendChild(div); // body에 추가가 되어야 함
        }
    </script>

</head>
<body>
    
    <button onclick="eleCreate();">엘리먼트 생성하기</button>

</body>
</html>
```



## 5) DOM - 4

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        img, #imgview{
            width: 300px;
            height: 300px;
        }
    </style>

    <script>
        function createImg(){

            // 1. 이름이 rdo인 요소들을 모두 가져오자
            var radios = document.getElementsByName("rdo");
            
            // 2. 가지고 온 요소들을 반복해서 체크되어있는지 학인하고
            var imgPath = "";

            for (var i = 0; i < radios.length; i++) {
                // 2-1. 만일 체크 되었다면 자신의 value 속성을 참고하여 이미지 경로를 만들자
                if (radios[i].checked) {
                    imgPath = "resources/imgs/" + radios[i].value;
                }
            }
            
            // 3. img 태그를 생성하고
            var img = document.createElement("img");

            // 3-1. (2-1)에서 완성한 imgPath 값을 src 속성에 대입하자
            img.setAttribute("src", imgPath);

            var div = document.getElementById("imgview");
            var chd = document.querySelector("#imgview > img");
            div.replaceChild(img, chd);

            // replaceChild(새로운애, 원래 있던 애)

        }

        function deleteImg(){
            document.getElementById("imgview").innerHTML = "<img src=''>";
        }
    </script>

</head>
<body>
    
    <input type="radio" name="rdo" value="img01.png"/>img01<br/>
    <input type="radio" name="rdo" value="img02.png"/>img02<br/>
    <input type="radio" name="rdo" value="img03.png"/>img03<br/>
    <br/>
    <button onclick="createImg()">이미지 생성</button>
    <button onclick="deleteImg()">이미지 삭제</button>

    <div id="imgview">
        <img src="" alt="">
    </div>

</body>
</html>
```



## 6) DOM - 5

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        img{
            /* 이미지를 수직 가운데 정렬 */
            vertical-align: middle;
            width: 300px;
            height: 300px;
        }
        a{
            font-size: 30px;
            text-decoration: none;
        }
    </style>

    <script>
        onload=function(){
             var anchs = document.querySelectorAll("a");
             var img = document.querySelector("img");

             var count = 1;

            //  클릭하면 함수가 실행됨
             anchs[0].onclick=function(){
                var imgAlt = img.getAttribute("alt");
                
                if (imgAlt == "img01") {
                    count = 6;
                    // setAttribute("설정할속성이름", "속성의값")
                    img.setAttribute("alt", "img06");
                    img.setAttribute("src", "resources/imgs/img06.png");
                } else {
                    img.setAttribute("alt", "img0" +(--count));
                    img.setAttribute("src", "resources/imgs/img0"+count+".png");
                }
             }
             anchs[1].onclick=function(){

             }
        }

    </script>

</head>
<body>
    
    <div>

        <!-- # : 내부에서 찾음 / # 뒤에 없으니까 내부에서 동작 -->
        <a href="#" id="lt">◀</a>
        <img src="resources/imgs/img01.png" alt="img01">
        <a href="" id="rt">▶</a>

    </div>

</body>
</html>
```



## 7) DOM - 6

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        p{
            border: 1px dotted red;
        }
    </style>

    <script>

        function addAppend(){
            var fieldset = document.getElementById("addele")
            var p = document.createElement("p");

            // textContent : 태그 포함해서 그냥 문자열이 됨
            p.textContent = "자식 태그들 중 마지막에 붙인다";
            fieldset.appendChild(p); // 자식 요소로 들어감
            // appendChil 부모를 찾은 다음에 마지막으로 들어감
            // (p) 이렇게 하나만 써도 됨
        }

        var count = 1;
        function addBefore(){
            var p = document.createElement("p"); // <p> 만들고
            var fieldset = document.getElementById("addele");

            p.textContent = "엘리먼트의 앞에 붙인다" + (count++); // 텍스트도 넣고

            var div = document.querySelector("#addele > div");
            fieldset.insertBefore(p, div); // 자식 요소로 넣음
            // insertBefore(새로운 것, 원래 있던 것)
            // 자식 노드 중에서 '원래 있던 것(기준점)' 앞에 바로 붙임
            // (부모, 추가할 것, 기준점 알려줘야 함)
        }

        function moveElement(){
            var child = document.querySelector("fieldset").children[0];
            var target = document.body; // body에 넣으려고 보니까 이미 fieldset에 있음

            target.appendChild(child);
            // <legend>부모태그</legend>는 [0]라서 안나옴
            // 이미 문서에 포함되어있는 경우에는 body로 이동
        }

    </script>
</head>
<body>
    
    <h1>태그 추가하기</h1>

    <button onclick="addAppend()">appendChild()</button>
    <button onclick="addBefore()">insertBefore()</button>
    <button onclick="moveElement()">element 이동()</button>

    <fieldset id="addele">
        <legend>부모태그</legend>
        <div>div태그</div>
    </fieldset>

</body>
</html>
```



## 8) DOM-7

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>

        // 추가 버튼을 누르면 tableVal() 함수 실행
        function tableVal(){
            var doc = document.forms[0]; // 지금 문서에서 [0]번째 form 요소 값

            // array 형식으로 각각의 값을 vals에 넣음
            // 값을 가져오고 싶으면 name 사용
            var vals = [doc.id.value, doc.pw.value, doc.addr.value, doc.phone.value];

            // 유효성 검사 (유효한 값 확인)
            for (var i = 0 ; i < vals.length; i++) {
                // i번째 vals의 값이 null 이거나(값 자체가 없음)
                // '' 비어있는 문자열 값이거나 정의되지 않으면 : (true)
                // alert 메시지
                if (vals[i] == null || vals[i] == "" || vals[i] == undefined) {
                    alert("입력을 다시 한번 확인해 주세요!");
                    return;
                }
            }

            // document.getElementById("addtr") : ID 'addtr'을 찾아서
            // .appendChild : 그 맨 아래에 자식 요소를 붙일건데
            // createRow(vals) : 이 함수를 실행한 다음 붙일 것이다
            document.getElementById("addtr").appendChild(createRow(vals));
        }



        function createRow(vals){

            // <tr>이라는 요소를 새로 만들고 이걸 tr 변수에 넣는다
            // <tr>은 테이블 행을 만드는 것
            var tr = document.createElement("tr");

            // 위에서 받은 vals의 길이(개수)만큼 반복할건데 (for)
            // 반복할 때 마다 <td>라는 요소를 새로 만들고 td 변수에 넣는다
            // <td> 테이블 셀 만드는 것
            for (var i =0; i < vals.length; i++) {
                var td = document.createElement("td");

                //새로 만든 td에 vals의 i 번째 값을 반복해서 추가한다
                td.textContent = vals[i];

                //그렇게 만들어진 td를 tr 안에 마지막에서부터 붙인다
                // td는 tr의 자식
                tr.appendChild(td);
            }

            // 아이디, 비밀번호, 주소, 전화번호를 값을 받았지만 [삭제]는 따로 만들어줘야 함
            // <td>이라는 요소를 새로 만들고 이걸 dTd 변수에 넣는다 (칸 만들기)
            var dTd = document.createElement("td");

            // dTd <td> 태그 안에 버튼을 만든다
            // 버튼명은 삭제고
            // 클릭하면 delRow() 함수가 실행된다
            dTd.innerHTML = "<input type='button' value='삭제' onclick='delRow(this)'>";

            // 삭제하는 버튼이 담긴 dTd를 tr에 추가한다
            // dTd는 tr의 자식
            tr.appendChild(dTd);

            return tr;
        }



        // 삭제 버튼이 눌리면 delRow 함수가 실행
        // ele를 가지고 있음 (input 태그 값이 들어감)
        function delRow(ele){
            // parentNode를 두번 씀
            // 한번 거슬러 올라가면 td, 또 올라가면 tr이 됨
            // tr의 요소를 변수 delTr에 값으로 넣는다
            // 삭제를 하려면 그 칸 이외에도 행(tr)을 다 해야 하니까
            var delTr = ele.parentNode.parentNode; 

            // addtr를 찾아서 변수 tbody에 값으로
            var tbody = document.getElementById("addtr");

            // 위에서 찾은 것에서 delTr을 삭제
            tbody.removeChild(delTr);
        }



        // 추가 버튼 옆 삭제 버튼을 누르면 실행
        function deleteVal(){

            //addtr를 찾아서 변수 tbody에 값으로 넣는다
            var tbody = document.getElementById("addtr");

            // hasChildNodes() : 자식 요소가 있니?
            // tbody.hasChildNodes() : tbody에 자식 요소가 있니?
            while(tbody.hasChildNodes()){
                // tbody.lastChild : tbody 요소의 마지막 자식 노드
                // 자식 노드가 있으면 True라서 while로 계속 remove 자식 삭제
                tbody.removeChild(tbody.lastChild);
            }
        }
    </script>

</head>
<body>
    <form>
        <table id="intable">
            <!-- <tr> : 테이블의 행(row) 만들기 -->
            <tr>
                <!-- <td> : 데이터 셀(Data Cell) 만들기 -->
                <td>아이디 : </td>
                <td><input type="text" name="id"></td>
            </tr>
            <tr>
                <td>비밀번호 : </td>
                <td><input type="text" name="pw"></td>
            </tr>
            <tr>
                <td>주소 : </td>
                <td><input type="text" name="addr"></td>
            </tr>
            <tr>
                <td>전화번호 : </td>
                <td><input type="text" name="phone"></td>
            </tr>


        </table>
        <input type="button" value="추가" onclick="tableVal();"/>
        <input type="button" value="삭제" onclick="deleteVal();">

    </form>

    <div id="addtable">
        <table border="1" id="ctb">
            <!-- 열의 너비(폭) 각각 다르게 지정 -->
            <col width="100px"> 
            <col width="100px">
            <col width="300px">
            <col width="200px">
            <col width="100px">

            <!-- <thead> : 테이블의 헤더 부분(Header)을 그룹화 -->
            <thead>
                <tr> 
                    <!-- <th> : 테이블의 열(column)이나 행(row)의 제목을 정의 -->
                    <th>아이디</th>
                    <th>비밀번호</th>
                    <th>주소</th>
                    <th>전화번호</th>
                    <th>삭제</th>
                </tr>
            </thead>

            <!-- 마지막 테이블 body 부분은 일단 뭐가 없고 id만 있음 -->
            <tbody id="addtr">
            </tbody>

        </table> 
    </div>
</body>
</html>
```


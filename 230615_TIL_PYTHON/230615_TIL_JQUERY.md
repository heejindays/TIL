# javascript (06/15)

## 1) basic

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        img{
            width: 200px;
            height: 200px;
        }
    </style>

    <!-- src로 가져온 것에는 절대 내용 추가 하면 안됨 -->
    <script src="resources/js/jquery-3.7.0.min.js"></script>

    <script type="text/Javascript">

        /* jquery : 자바스크립트의 라이브러리
        
            기본 작성법 : css selector

            기능 구현 방법 2가지 (onload=function과 같은 의미)
            $(document).ready(function(){

            });

            $(function(){

            });
        */

        // 문서가 로드되면 함수가 실행
        $(document).ready(function(){
        $("#click").click(function(){
            alert("click!");
        });


        // click 이벤트가 발생하면 작동
        // this : 콜백 이벤트를 발생시킨 img
        // 이미 있는 img만 찾음 (처음 로드 될 때 이미지)
        $("img").click(function(){
            $(this).hide();
        })
       });


       function showImg() {
            $("img").show();
       }

    //    method chainning : 동일한 객체에 연속적으로 메서드 호출
       

       function resizeImg() {
            // $("img").css("width", "100px").css("height", "100px")
            $("img").css({"width":"100px", "height":"100px"})
       }

       function addImg() {
            $("img").last().after("<img src='resources/imgs/img01.png'>");
       }

       function toggleImg() {
            $("img").toggle();
        
       }

    </script>

</head>
<body>

    <!-- 만들어져 있는 걸 가져다 사용 -->
    <h1 id="click">JQuery : Javascript Library</h1>

    <button onclick="showImg();">이미지 보이기</button>
    <button onclick="resizeImg();">이미지 축소</button>
    <button onclick="addImg();">이미지 추가</button>
    <button onclick="toggleImg();">이미지 숨기기/보이기</button>
    <br/>
    <br/>
    <br/>
    <div>
        <img src="resources/imgs/img01.png" alt="">
    </div>
</body>
</html>
```



## 2) selector

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script src="resources/js/jquery-3.7.0.min.js"></script>

    <script>
        $(document).ready(function(){
            $("div:eq(0)").css({"border": "1px solid red", "width":"400px", "height":"200px"});
            $("#view").css({"border": "1px solid red", "width":"400px", "height":"100px"})
        });

        function test01(){
            $("span").css("color","red");
            $("#view").text('$("span").css("color","red")');
        }

        // id가 "t1"인 요소를 선택
        function test02(){
            $("#t1").css("color","blue");
            $("#view").text('$("#t1").css("color","blue")');
        }

        // class가 "t2"인 요소를 선택
        function test03() {
            $(".t2").css("color","orange");
            $("#view").text('$(".t2").css("color","orange")');
        }

        // "li span" : 하위에 있는 모든 자식들 선택
        function test04() {
            $("li span").css("color","violet");
            $("#view").text('$("li span").css("color","violet")');
        }

        // "li > span" : 내 밑에 있는 직계 자식만 선택
        function test05() {
            $("li > span").css("background-color","aquamarine");
            $("#view").text('$("li > span").css("background-color","aquamarine")');
        }

        function test06() {
            // n은 1번부터 시작 : (6)은 여섯번째
            $("li:nth-child(6)").css("background-color","yellow");
            $("#view").text('$("li:nth-child(6)").css("background-color","yellow");');
        }

        function test07() {
            // 첫번째 자식 찾기
            $("li:first-child").css("background-color","skyblue");
            $("#view").text('$("li:first-child").css("background-color","skyblue");');

        }

        function test08() {
            // 마지막 자식 찾기
            $("li:last-child").css({"background-color":"lime", "color":"white"});
            $("#view").text('$("li:last-child").css({"background-color":"lime", "color":"white"});');        
        }

        function cls(){
            $("*").css("color","").css("background-color", "");
            $("#view").text("");
        }

    </script>

</head>
<body>
    
    <h1 onclick="cls();">selector 표현식</h1>

    <div>
        <ul>
            <li><span>1) tag로 선택하기</span></li>
            <li id="t1">2) id로 선택하기</li>
            <li class="t2">3) class로 선택하기</li>
            <li><span>4) parent child로 선택하기</span></li>
            <li><b><span>5) parent &gt; child로 선택하기</span></b></li>
            <li>6) :nth-child로 선택하기</li>
            <li>7) :first-child로 선택하기</li>
            <li>8) :last-child로 선택하기</li>
        </ul>
    </div>

    <div>
        <button onclick="test01();">tab 선택</button>
        <button onclick="test02();">id 선택</button>
        <button onclick="test03();">class 선택</button>
        <button onclick="test04();">parent child</button>
        <button onclick="test05();">parent &gt; child</button>
        <button onclick="test06();">nth-child</button>
        <button onclick="test07();">first-child</button>
        <button onclick="test08();">last-child</button>

    </div>

    <h2>코드 내용</h2>
    <div id="view"></div>
</body>
</html>
```



## 3) input

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script src="resources/js/jquery-3.7.0.js"></script>

    <script>
        function inputTxt() {
            // text 타입의 input 태그 가져옴
            // val() : value의 값을 가져옴
            var txt = $("input:text").val();
            alert(txt);
        }

        function inputRdo() {
            var rdo = $("input:radio").val();
            alert(rdo);
        }

        function inputChk(){
            var chk = $("input:checkbox").val();
            alert(chk);
        }

        $(function(){
            $("select").change(function(){ 
                var selectOption = $("select > option:selected");
                // $("select > option") : 노드 리스트
                alert(selectOption.val() + "\n" + $("select > option").index(selectOption));
            });
        });
    </script>

</head>
<body>
    
    <form action="">
        <input type="text"/><br/>
        <input type="button" value="선택" onclick="inputTxt();"/>
        <br><br/>
        <input type="radio" value="radio value" onclick="inputRdo();"/>radio
        <br><br/>
        <input type="checkbox" value="check value" onclick="inputChk();"/>check
        <br><br/>
        <div id="a"></div>
        <select>
            <option value="one">1</option>
            <option value="two">2</option>
            <option value="three">3</option>
        </select>
    </form>
</body>
</html>
```



## 4) check

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script src="resources/js/jquery-3.7.0.min.js"></script>

    <script>
        $(function(){
            // submit 이벤트가 발생했을 때
            $("#signal").submit(function(){
                // 유효성 검사
                // 값이 null or "" 이라면
                if($(".infobox").val() == null || $(".infobox").val() == ""){
                    $(".error").show();
                    return false; // submit 이벤트를 막아줌
                }
            })

            $("#confirm").click(function(){
                // id가 "result"인 요소의 자식들을 다 지움 (초기화)
                $("#result").empty(); 

                // "chk"라는 이름을 가진 체크박스 중 선택된 체크박스의 개수가 0이라면
                // 아무것도 선택을 하지 않았다면
                if($("input[name=chk]:checked").length == 0) {
                    alert("하나 이상 체크해주세요");
                } else {
                    var total = 0;
                    // .each(function(i)) : 객체를 반복하여 일치하는 각 요소에 대해 함수를 실행
                    $("input[name=chk]:checked").each(function(i){
                        // eq() : 해당 체크박스 중 현재 순회하는 인덱스(i)에 해당하는 체크박스를 선택
                        // var chk = $("input[name=chk]:checked").eq(i);
                        var chk = $(this);
                        var book = chk.next().text(); // next() 바로 다음에 나오는 형제 태그 (여기에서는 b태그)
                        var price = chk.val();
                        $("#result").append(book + " -> 가격: " + price + "<br/>"); // .append() : 요소 세트 끝에 삽입
                        total += parseInt(price);
                    })
                    $("#result").append("총 합 : " + total)
                }
            })


            $("input[name=chk]").click(function(){
                // 1. name이 chk인 체크박스의 길이와 
                // name이 chk인데 체크되어 있는 체크박스의 길이가 같다면
                // 전체 선택이 되도록
                if($("input[name=chk]").length == $("input[name=chk]:checked").length) {
                    // 이름이 "all"인 체크박스의 checked 값을 true로 설정
                    $("input[name=all]").prop("checked", true);
                } else {
                    // 2. 그게 아니라면 전체 선택 해제
                    $("input[name=all]").prop("checked", false);
                }
            })
        })

        // 전체선택 버튼 눌렀을 때
        function allChk(bool){
            $("input[name=chk]").each(function(){
                console.log(this);
                // this.checked = bool;
                $(this).prop("checked", bool);
            });
        }

    </script>
</head>
<body>
    
    <form action="" id="signal" method="get">
        <div>
            <span class="label">User ID</span>
            <input type="text" class="infobox" name="userid">
            <span class="error" hidden style="color:red;">반드시 입력하세요!</span>
        </div>
        <input type="submit" class="submit" value="입력">
    </form>

    <hr/>

    <fieldset style="width: 300px">
        <legend>체크 여부 확인</legend>

        <input type="checkbox" name="all" onclick="allChk(this.checked);"/>전체선택
        <br/>
        <input type="checkbox" name="chk" value="20000" /><b>python</b><br/>
        <input type="checkbox" name="chk" value="25000" /><b>javascript</b><br/>
        <input type="checkbox" name="chk" value="30000" /><b>jquery</b><br/>

        <input type="button" value="확인" id="confirm"/><br>

        <span>선택한 책 가격</span>
        <div id="result"></div>
    </fieldset>

</body>
</html>
```



## 5) dom - 1

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script src="resources/js/jquery-3.7.0.min.js"></script>

    <script>
        $(function(){
            $("div > p").eq(0).click(function(){
                $("pre b").eq(0).toggle();
            });

            // slice(1, 2) 인덱스 1부터 2전까지
            $("div > p").eq(1).click(function(){
                $("pre b").slice(1, 2).toggle();
            });

            $("div > p").eq(2).click(function(){
                $("pre b").first().css("color", "red");
                $("pre b").eq(2).toggle();

                // end() : chaning 되던 걸 멈추고 처음부터 다시 이전 상태에서 작업
                // $("pre b").first().css("color","red").end().eq(2).toggle();
               
            });

            $("div > p").eq(3).click(function(){
                $("pre b").last().toggle();
            })

        });
    </script>

</head>
<body>
    
    <pre>
        <b>eq() : 인덱스로 탐색</b>
        <b>slice() : 인덱스 길이로 탐색</b>
        <b>first() : 첫번째 요소 탐색</b>
        <b>last() : 첫번째 요소 탐색</b>
    </pre>

    <div>
        <p>1. eq() 매서드</p>
        <p>2. slice() 매서드</p>
        <p>3. first() 매서드</p>
        <p>4. last() 매서드</p>
    </div>

</body>
</html>
```



## 6) DOM - 2

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script src="resources/js/jquery-3.7.0.min.js"></script>

    <script>
        // .find("b") : div 안에 자식 요소가 있으면 다 찾음
        $(document).ready(function(){
            $("div").find("b").css({"font-size":"30px", "color":"red"})
            $("div").children("#chd").text("2.children");
            console.log($("div").children());
            // jQuery는 배열도 한꺼번에 다 CSS 적용
            $("b").parent().css("background-color", "hotpink");
            $("p > b").parents("div").css("background-color", "Turquoise");
            $("p").eq(0).next().css({"font-size":"20px", "color" : "white"})
        });
    </script>

</head>
<body>
    
    <pre>
        <b>find("selector")
            자손들 중에 탐색
        </b>
        <b>children("selector")
            자식들 중에 탐색
        </b>
        <b> parent() / parents("selector")
            부모요소 / 조상
        </b>
        <b> next ("selector")
            다음에 나오는 요소       
        </b>
    </pre>

    <div>
        <p><b>1</b></p>
        <p id="chd">2</p>
        <p>3</p>
        <p>4</p>
        <p>5</p>
    </div>

</body>
</html>
```


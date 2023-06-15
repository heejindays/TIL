# javascript (06/15)

## 1) ajax

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>

    <script>

        /*
            ajax : Asynchronous Javascript And Xml
            서버에 요청한 후 응답을 기다리지 않고 다음 명령 수행
            화면의 일부분만 바뀜
            
            문서가 아닌 데이터를 받음
            비동기 요청으로 인해 화면이 새로고침되지 않는다
            주소창은 변하지 않고, 화면 안의 특정 내용만 바뀜
            
        */

        /*
            .xml 파일
            "확장 가능한 마크업 언어" (eXtensible Markup Language)
            데이터를 저장하고 전송하기 위해 사용되는 텍스트 기반 파일 형식
            사용자가 자신만의 태그를 정의하여 데이터를 구조화하는 데 사용할 수 있는 개방형 형식
        
        */

        function ajaxTest(){
            // XMLHttpRequest() : javascript object로서 http를 통한 데이터 송수신 지원
            var xhr = new XMLHttpRequest();
            
            // onreadystatechange : readystate가 change될 때 (callback)
            xhr.onreadystatechange = function(){
                // alert(xhr.readyState);
                if (xhr.readyState == 4) { //통신이 완료 되었을 때
                    if (xhr.status == 200) {
                        // alert(xhr.responseText);
                        // 이 부분에서 데이터를 테이블에 넣을 것
                        var respXML = xhr.responseXML; // 원래 문서 형식으로 받는데 XML 객체로 바꿔서 전달해줌
                        // console.log(respXML);

                        var table = document.getElementById("tb");

                        var rows = respXML.getElementsByTagName("ROW");
                        // console.log(rows);


                        var tr = document.createElement("tr");
                        for (var i = 0; i < rows[0].children.length; i++) {
                            var th = document.createElement("th");
                            th.appendChild(document.createTextNode(rows[0].children[i].nodeName));
                            tr.appendChild(th);
                        }
                        table.appendChild(tr);

                        for(var i = 0; i < rows.length; i++) {
                            
                            // 1. tr 만들어서
                            var tr = document.createElement("tr");

                            // 2. tr 안에 ROW 하나의 내부 값을 td로 저장하고 (자식)
                            for (var j=0; j < rows[i].children.length; j++) {
                                // console.log(rows[i].children[j].textContent);
                                var td = document.createElement("td");
                                td.appendChild(document.createTextNode(rows[i].children[j].textContent));
                                tr.append(td);
                            }

                            // 3. table에 append 하자
                            table.appendChild(tr);
                        }
                
                    } else {
                        
                    }
                }
            }

            // 어디에 어떻게 요청할 것인지
            // 요청방식 : GET 방식 / 경로 : "emplist.xml"
            // GET 방식 : URL에 데이터를 포함하여 서버로 보냄
            // POST 방식 : 데이터가 URL에 노출되지 않은 상태로 전송

            xhr.open("GET", "emplist.xml");
            xhr.send();
        }

        /*
            readystate
            0: uninitialized (대기)
            1: loading (요청할 준비)
            2: loaded (요청 다 됨)
            3: interactive (통신하는 중)
            4: complete (통신 완료)

            status (http 상태 코드)
            200 : 성공
            400 : bad request (서버가 요청을 이해 못함)
            401 : unauthorized
            403 : forbidden
            404 : not found
            500 : internal server error (서버가 처리 방법을 모름)
            
        */

    </script>
</head>
<body>

    <button onclick="ajaxTest();">ajax</button>

    <table border="1" id="tb">
    </table>

</body>
</html>
```


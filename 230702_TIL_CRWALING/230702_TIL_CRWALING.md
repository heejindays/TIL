## CRAWLING한 데이터 활용(DJANGO)



### 1) urls.py

- views.py의 어디로 연결을 할 것인지 

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("sido/", views.get_sido),
    path("gugun/", views.get_gugun),
    path("store/", views.get_store),
]
```



### 2) views.py

- urls로부터 요청 받은 뒤 다시 스타벅스 서버에서 데이터 받아서 화면을 보여줌
- 전체적인 흐름은 전국 스타벅스의 시도 선택 > 구군 선택 > 지점 정보 나오도록



- 상단에 필요한 것들 import 하기

```python
from django.http import JsonResponse
from django.shortcuts import render
import requests
```

- from django.http import JsonResponse
  - Django에서 JSON 형식의 응답을 반환하기 위해 사용
- from django.shortcuts import render
  - Django에서 템플릿을 사용하여 HTML 응답을 생성하는 데 사용
- import requests
  - Python에서 HTTP 요청을 보내기 위해 사용
  - 다양한 방식으로 HTTP 요청을 생성하고 보낼 수 있으며, 응답을 받아올 수 있음





```python
def index(request):
    return render(request, "index.html")
```

- index 요청이 들어오면 index.html 페이지로 응답





```python
def get_sido(request):

    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp_list = requests.post(url).json()["list"]
    sido_dict = dict(zip(list(map(lambda x: x["sido_cd"], resp_list)),
                         list(map(lambda x: x["sido_nm"], resp_list))))

    return JsonResponse(sido_dict)

```

- 스타벅스 매장이 있는 시/도를 받아오자
- 필요한 데이터 sido_cd, sido_nm 꺼내와서 딕셔너리 형식으로
- json 형태로 응답하자 (json도 문자열)
- JsonResponse(딕셔너리형태) : 딕셔너리를 넣으면 json 형태로 응답해줌





```python
def get_gugun(request):
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp_list = requests.post(url, data={"sido_cd": request.GET["sido_code"]}).json()["list"]
    gugun_dict = dict(zip(list(map(lambda x: x["gugun_cd"], resp_list)),
                          list(map(lambda x: x["gugun_nm"], resp_list))))

    return JsonResponse(gugun_dict)

```

- 스타벅스 매장이 있는 구/군을 받아오자
- 파라미터로 제공된 sido_code에 기반하여 "gugun" (구군) 이름의 리스트를 가져옴
- 가져온 리스트에서 "gugun_cd"와 "gugun_nm"에 해당하는 값들을 사용하여 
- "gugun_dict" 딕셔너리를 만듦
- 그 이후 JSON 형식으로 반환





```python
def get_store(request):
    url = "https://www.starbucks.co.kr/store/getStore.do"
    code = request.GET["code"]

    sido_cd = code if code == "17" else ""
    gugun_cd = "" if code == "17" else code

    data = {"ins_lat": "37.5092201",
            "ins_lng": "127.0349915",
            "p_sido_cd": sido_cd,
            "p_gugun_cd": gugun_cd,
            "in_biz_cd": "",
            "set_date": ""
    }

    resp_list = requests.post(url, data=data).json()["list"]
```

- requests.post() 함수를 사용하여 POST 요청을 url에 보냄
- 요청 데이터는 data 변수로 전달됨
- 응답은 JSON 형식으로 함





```python
    store_list = list()
    for store in resp_list:
        temp = dict()
        temp["s_name"] = store["s_name"]
        temp["doro_address"] = store["doro_address"]
        temp["lat"] = store["lat"]
        temp["lot"] = store["lot"]
        store_list.append(temp)

    store_dict = {"list": store_list}

    return JsonResponse(store_dict)
```

-  각 매장의 정보를 추출하여 store_list 리스트에 딕셔너리 형태로 저장
-  "s_name" (매장 이름), "doro_address" (도로 주소), "lat" (위도), "lot" (경도)를 추출
- 새로운 딕셔너리 temp에 저장하고, 이를 store_list에 추가
- store_list를 "list"라는 키로 갖는 딕셔너리 store_dict를 생성
- 이 store_dict를 JSON 형식으로 응답하기 위해 JsonResponse를 사용하여 반환





### 3) templates (index.html)



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script src="https://code.jquery.com/jquery-3.7.0.js"></script>

    <script>
        <!--BODY 내용이 다 완성된 이후에 스크립트 부분 만들어짐-->
        <!--이후 ajax 부분이 생김-->
        $(function(){
            $.ajax({
                url: "sido/", 
                dataType: "json", 
                // 응답받는 형식이 json
                success: function(msg){
                    msgKeys = Object.keys(msg);


                    var sido = $("#sido");
                    for (var i = 0; i < msgKeys.length; i++) {
                        sido.append($("<option>").val(msgKeys[i]).text(msg[msgKeys[i]]))
                    }
                }
            });

            $("#sido").change(function(){
                var sido = $(this).val();
                console.log(sido);
                if (sido == "17") {
                    // 세종시
                    getStore(sido);

                } else {
                    $.ajax({
                        url: "gugun/",
                        data: {"sido_code": sido},
                        dataType: "json",
                        success: function(msg){
                            // console.log(msg);
                            var msgKeys = Object.keys(msg);
                            var gugun = $("<select>").prop("id", "gugun").append($("<option>").val(0).text("구군선택"));

                            for (var i = 0; i < msgKeys.length; i++) {
                                gugun.append($("<option>").val(msgKeys[i]).text(msg[msgKeys[i]]))
                            }

                            $("#wrapper").append(gugun)
                        }
                    });
                }
            });

            // 주의) 원래 있던 태그의 자식 요소를 활용해서 이벤트를 걸어야 함
            $("#wrapper").on("change", "#gugun", function(){
                code = $(this).val();
                // console.log(code);
                getStore(code);
                // 구군코드가 변하면 getstore에 보냄
            });

        });


        function getStore(code){
            $.ajax({
                url: "store/",
                data: {"code": code},
                dataType: "json",
                success: function(msg){
                    // console.log(msg);
                    var store_list = msg.list
                    var table = $("#result");
                    for (var i = 0; i < 1; i++) {
                        var head_txt = Object.keys(store_list[i])
                        var $tr = $("<tr>")
                        for (var j = 0; j < head_txt.length; j++) {
                            $tr.append($("<th>").text(head_txt[j]))
                        }
                        table.append($tr)
                    }
                    for (var i = 0; i < store_list.length; i++){
                        var store_keys = Object.keys(store_list[i])
                        var $tr = $("<tr>")
                        for (var j = 0; j < store_keys.length; j++) {
                            $tr.append($("<td>").text(store_list[i][store_keys[j]]))
                        }
                        table.append($tr)
                    }
                }
            });
        }


    </script>

</head>
<body>

    <h1>starbucks</h1>

    <div id ="wrapper">
        <select id="sido">
            <option value="0">시도선택</option>
        </select>
    </div>

    <table id="result" border="1"></table>

</body>
</html>
```
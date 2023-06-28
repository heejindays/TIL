## 1. 크롤링 관련 용어 정리

| 구분     | 용어                   | 의미                                                         |
| :------- | :--------------------- | ------------------------------------------------------------ |
| crawling | 크롤링(crawling)       | 인터넷  상의 웹 페이지를 자동으로 탐색하고 데이터를 수집하는 과정, 웹 사이트의 구조를 따라가면서 링크를 따라 이동하고 페이지의 텍스트, 이미지, 링크 등 다양한 정보를 수집 |
| crawling | 뷰티풀 숩BeautifulSoup | HTML과  XML 문서를 파싱하고 데이터를 추출하는 데 사용되는 파이썬 라이브러리, 웹 페이지의 소스 코드를 파싱하여 객체로 만들고, 이를 활용하여 원하는 데이터를 추출 |
| crawling | 파싱(parsing)          | 주어진  문서(예: HTML, XML)를 구문 분석하여 문서의 구조를 이해하고 원하는 정보를 추출하는 과정, 프로그래밍 언어 코드를 파악하고 이해하는 작업 |
| crawling | 제이슨(json) 파일      | (JavaScript  Object Notation)은 데이터를 표현하기 위한 경량의 데이터 교환 형식, JSON 형식은 키-값 쌍(key-value pair)으로 구성된 데이터 객체를 표현 |
| crawling | 드라이버(driver)       | 웹 브라우저를 제어하고 웹 페이지와 상호작용하기 위한 프로그램 |
| crawling | ensure_ascii=False     | ASCII 이외의 문자를 그대로 유지                              |
| crawling | selenium               | 애플리케이션을  테스트하거나 자동화하기 위해 사용되는 도구,  웹 페이지의 로그인 폼에 자동으로 로그인하거나, 버튼을 클릭하거나 텍스트 필드에 값을 입력하는 등의 작업을 자동화할 수 있음 |
| crawling | robots.txt             | 웹  사이트 소유자가 크롤러에게 특정 페이지의 접근을 허용하거나 제한하는 지침을 제공, 지침을 따라야 하며, 접근이 금지된 페이지에는 접근하지 말아야 함 |





## 2. 크롤링 코드 복기



### 1) 네이버 웹소설 페이지 통합 랭킹과 제목 가져오기 (urllib.request)

```py
from bs4 import BeautifulSoup
import urllib.request

# BeautifulSoup이란?
# HTML과 XML 문서를 파싱하고 데이터를 추출하는 데 사용되는 파이썬 라이브러리
# 웹 페이지의 소스 코드를 파싱하여 객체로 만들고, 이를 활용하여 원하는 데이터를 추출

# [1단계]
url = "https://novel.naver.com/webnovel/weekday"

# 지정된 URL을 열어 웹페이지의 내용을 가져오는 함수
resp = urllib.request.urlopen(url)
# print(resp)


# [2단계]
soup = BeautifulSoup(resp, "html.parser")
# "html.parser" : .html 을 python에서 사용할 수 있도록 분석해서 객체로 변환하는 것
# 서버에 요청 한 뒤 서버에서 받은 것을 객체로 저장 (파싱)
# print(soup)


# 만약 네이버 웹소설 페이지의 통합 랭킹과 제목을 가지고 오고 싶다면?
# 그 찾고 싶은 내용이 들어있는 구역을 직접 찾아야 함
# 이 경우 <div class="component_section">

# find : 해당되는 내용 1개 가져옴
ranking_list = soup.find("div", class_="component_section")
# print(ranking_list)

# find_all : 리스트 형태로 전부 가져옴
item_list = ranking_list.find_all("li", class_="item")
# print(item_list)

# 어디에 들어 있는지 확인!
# title : span class="title"
# rank : em class="rank"

for item in item_list:
    rank = item.find("em", class_="rank").text.strip()
    title = item.find("span", class_="title").text

    # rank = item.p.text.strip()
    # title = item.find_all("p")[1].find("span", class_="title").text

    print(f"{rank}위 : {title}")
```



## 2) 네이버 웹소설 페이지 통합 랭킹과 제목 가져오기 (requests)

```py
from bs4 import BeautifulSoup
import requests

# [1단계] : 클라이언트가 서버에 요청했더니, 서버가 클라이언트에게 응답함
# 이번의 경우에는 novels02.py가 클라이언트인 상황
# 응답 받는 것은 문자열 text(str)
# requests를 활용해서 크롤링을 해보자

url = "https://novel.naver.com/webnovel/weekday"

# requests.get(url)은 지정된 URL에 GET 요청을 보내고,응답을 받아오는 함수
# 그 값을 resp 변수에 넣는다
resp = requests.get(url)
# print(resp)
# print(resp.text)


# [2단계] : 응답 받아온 것을 객체로 만들어야 함 (파싱)
# 문자열을 객체로 바꾸는 것을 파싱이라고 함
# 그걸 도와주는 것이 BeautifulSoup

# CSS 선택자로 찾는 방법
soup = BeautifulSoup(resp.text, "html.parser")
# print(soup)


# [3단계] : 내가 원하는 데이터만 가져오는 과정
# (이 단계는 계속 바뀜)

ranking_list = soup.find("div", class_="component_section")
# print(ranking_list)
item_list = ranking_list.find_all("li", class_="item")
# print(item_list)

# 우선 li 태그로 똑같이 가져오는 것 까지는 동일함
# .rank는 rank 클래스

for item in item_list:
    # rank = item.css.select(".rank")[0].text
    # title = item.css.select("span[class='title']")[0].text
    # print(f"{rank}위 : {title}")

    # 어디에 들어있나?
    # title : span class="title"
    # rank : em class="rank"

    title = item.css.select("span[class='title']")[0].text
    rank = item.css.select("em[class='rank']")[0].text
    # print(rank)

    print(f"{rank}위 : {title}")
```



### 3) 가져온 데이터를 json 형식으로 파일 저장까지

```py
from bs4 import BeautifulSoup
import requests
import json

url = "https://novel.naver.com/webnovel/weekday"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

# 이 2개 코드를 하나로 합치면?
# ranking_list = soup.find("div", class_="component_section")
# item_list = ranking_list.find_all("li", class_="item")

item_list = soup.find("div", class_="component_section").find_all("li", class_="item")

novel_list = list()

for item in item_list:
    rank = item.select(".rank")[0].text
    title = item.select(".title")[0].text
    # print(f"{rank} : {title}")

    temp = dict()

    # "rank"라는 키를 만들고 해당 키에 rank 변수를 값으로 넣음
    # 딕셔너리명["키이름"] = 값으로 넣을 변수 이름
    temp["rank"] = rank
    temp["title"] = title
    # print(temp)

    novel_list.append(temp)

# print(novel_list)

result_dict = dict()
result_dict["novels"] = novel_list
# print(result_dict)

    # novel_list를 만들고 그 안에 딕셔너리로 만든 것들을 추가
    # 그리고 그걸 다시 딕셔너리 형태로 만들어야 함
    # {"novels" : [{"rank": 1, "title": ...}, {"rank": 2, .....} {....} {......}]}

# json.dumps() 함수의 첫 번째 인자로 변환할 딕셔너리 객체인 result_dict를 전달
# 두 번째 인자로 ensure_ascii=False를 지정하여 
# ASCII 이외의 문자도 그대로 유니코드로 유지하도록 설정

# ensure_ascii=False 옵션 : ASCII 이외의 문자를 그대로 유지
result_json = json.dumps(result_dict, ensure_ascii=False)
print(result_json)
# print(type(result_json))

# json 파일로 저장하기
with open("novels.json", "w", encoding="utf-8") as file:
    file.write(result_json)
```



### 4) 네이버 수요 웹툰 별점과 타이틀 가져오기 (selenium)

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import json

url = "https://comic.naver.com/webtoon?tab=wed"

# 1. webdriver path를 가지고 service 생성
service = webdriver.chrome.service.Service("../chromedriver.exe")

# 2. webdriver를 가지고 Chrome 객체 생성
driver = webdriver.Chrome(service=service)
sleep(5)

# 3. driver에서 url로 요청
driver.get(url)

# 4. 5초 동안 기다렸다가
sleep(5)

# 5. 수요 웹툰에 있는 각각의 웹툰의 별점과 제목을 가져오기
# ul class="ContentList__content_list--q5KXY"
# title : span class= text [0]
# star : span class= text [1]

soup = BeautifulSoup(driver.page_source, "html.parser")
item_list = soup.find_all("div", class_="component_wrap")[1].find_all("li", class_="item")

dict_list = list()
for item in item_list:
    text = item.find_all("span", class_="text")
    title, star = text[0].text, text[1].text
    # print(f"{star}: {title}")

    temp_dict = dict()
    temp_dict["title"] = title
    temp_dict["star"] = star
    dict_list.append(temp_dict)

# 6. {"webtoons" : [{"title":"?", "star": "?"}, {}, {}, {}]} 형태로 만들기
result_dict = dict()
result_dict["webtoons"] = dict_list

# 7. json으로 변환 후 webtoon.json으로 저장하기
result_json = json.dumps(result_dict, ensure_ascii=False)
print(result_json)

with open("webtoons.json", "w", encoding="utf-8") as f:
    f.write(result_json)

driver.close()
```


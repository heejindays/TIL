### 1) 크롤링 관련 용어 정리



| 136  | crawling | 크롤링(crawling)       | 인터넷 상의 웹 페이지를  자동으로 탐색하고 데이터를 수집하는 과정, 웹 사이트의 구조를 따라가면서 링크를 따라 이동하고 페이지의 텍스트, 이미지, 링크 등 다양한 정보를 수집 |
| :--: | -------- | ---------------------- | ------------------------------------------------------------ |
| 137  | crawling | 뷰티풀 숩BeautifulSoup | HTML과  XML 문서를 파싱하고 데이터를 추출하는 데 사용되는 파이썬 라이브러리, 웹 페이지의 소스 코드를 파싱하여 객체로 만들고, 이를 활용하여 원하는 데이터를 추출 |
| 138  | crawling | 파싱(parsing)          | 주어진  문서(예: HTML, XML)를 구문 분석하여 문서의 구조를 이해하고 원하는 정보를 추출하는 과정, 프로그래밍 언어 코드를 파악하고 이해하는 작업 |
| 139  | crawling | 제이슨(json) 파일      | (JavaScript  Object Notation)은 데이터를 표현하기 위한 경량의 데이터 교환 형식,  JSON 형식은 키-값 쌍(key-value pair)으로 구성된 데이터 객체를 표현 |
| 140  | crawling | 드라이버(driver)       | 웹 브라우저를 제어하고 웹 페이지와 상호작용하기 위한 프로그램 |
| 141  | crawling | ensure_ascii=False     | ASCII 이외의 문자를 그대로 유지                              |
| 142  | crawling | selenium               | 애플리케이션을  테스트하거나 자동화하기 위해 사용되는 도구     웹 페이지의 로그인 폼에 자동으로 로그인하거나, 버튼을 클릭하거나,  텍스트 필드에 값을 입력하는 등의 작업을 자동화할 수 있음 |
| 143  | crawling | robots.txt             | 웹  사이트 소유자가 크롤러에게 특정 페이지의 접근을 허용하거나 제한하는 지침을 제공 지침을 따라야 하며, 접근이 금지된 페이지에는 접근하지 말아야 함 |



### 2) 크롤링 코드 복기

```py
from bs4 import BeautifulSoup
import urllib.request

# BeautifulSoup이란?
# HTML과 XML 문서를 파싱하고 데이터를 추출하는 데 사용되는 파이썬 라이브러리
# 웹 페이지의 소스 코드를 파싱하여 객체로 만들고, 이를 활용하여 원하는 데이터를 추출

# 서버에 요청 한 뒤 서버에서 받은 것을 객체로 저장 (파싱)

url = "https://novel.naver.com/webnovel/weekday"
resp = urllib.request.urlopen(url)
# print(resp)

soup = BeautifulSoup(resp, "html.parser")
# "html.parser" : .html 을 python에서 사용할 수 있도록 분석해서 객체로 변환하는 것
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

for item in item_list:
    rank = item.p.text.strip()
    title = item.find_all("p")[1].find("span", class_="title").text
    print(f"{rank}위 : {title}")
```



```py
from bs4 import BeautifulSoup
import requests
import json

url = "https://novel.naver.com/webnovel/weekday"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

item_list = soup.find("div", class_="component_section").find_all("li", class_="item")

novel_list = list()

for item in item_list:
    rank = item.select(".rank")[0].text
    title = item.select(".title")[0].text
    # print(f"{rank} : {title}")
    temp = dict()
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

# ensure_ascii=False 옵션 : ASCII 이외의 문자를 그대로 유지
result_json = json.dumps(result_dict, ensure_ascii=False)
print(result_json)

# json 파일로 저장하기
with open("novels.json", "w", encoding="utf-8") as file:
    file.write(result_json)
```


## 1. 공공데이터포털 활용

- https://www.data.go.kr/index.do

- 신청 후 승인되면 데이터 활용 가능

  

### 1) 시도별 코로나 누적 확진자수 (2023년)

```python
import requests
from xml.etree import ElementTree

# 지금 xml로 만들어져 있기 때문에 위 내용 임포트
# https://docs.python.org/3/library/xml.etree.elementtree.html

# 공공데이터포털 승인 시
# 일반인증키(Encoding) 확인
service_key = "u3qFi2sWBNZ%2B%2FKoJDO18TXVeQaoNsfLS0KM2lgFplGAhhX6djnAYkN56QSfrJnc8oGOrtEOMJ%2FzSrIvRtNk%2F2A%3D%3D"

# 키를 적용할 링크 확인
# End Point = http://apis.data.go.kr/1352000/ODMS_COVID_04

# 요청변수 확인
# ex) 서비스키 / 페이지번호 / 한 페이지 결과 수 / 데이터 유형
# url = f"http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api?serviceKey={service_key}&pageNo=1&numOfRows=500"
query_string = f"?serviceKey={service_key}&pageNo=1&numOfRows=500"
url = f"http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api{query_string}"

# 인증키를 가져와서 서버에 전달함
# 서버는 적합한 클라이언트인지 확인하고 전달해줌

# print(url)

resp = requests.get(url)
# print(resp.text)

tree = ElementTree.fromstring(resp.text)
# 문자열을 가지고 와서 객체로 만듦
# print(tree)

# 요청했을 때 response 라는 태그가 있고 그 안에 헤더와 바디가 있음

# print(tree.find("body"))
# print(tree.find("body").find("items"))
# print(tree[0][1])


# 년도가 2023년도인 경우 찾기
for item in tree[1][0]:
    # print(item.find("stdDay").text)
    if item.find("stdDay").text.split("-")[0] == "2023":
        print(f"{item.find('gubun').text} : {item.find('defCnt').text}")

```



###  2) 구분(연령 또는 성별)별 사망자 수 (2023년)

```python
import requests
from xml.etree import ElementTree

service_key = "u3qFi2sWBNZ%2B%2FKoJDO18TXVeQaoNsfLS0KM2lgFplGAhhX6djnAYkN56QSfrJnc8oGOrtEOMJ%2FzSrIvRtNk%2F2A%3D%3D"
query_string = f"?serviceKey={service_key}&pageNo=1&numOfRows=500"

url = f"http://apis.data.go.kr/1352000/ODMS_COVID_05/callCovid05Api{query_string}"

# print(url)

resp = requests.get(url)
tree = ElementTree.fromstring(resp.text)
# print(tree)

# item들 중에서 2023년 데이터만 가지고
# 출력 예시 : 2023-05-27 등록 : 70-79 -> 7892명 사망

# for item in tree.find("body").find("items"):
# for item in tree[1][0]:
#     if item.find("createDt").text.split("-")[0] == "2023":
#         print(f"{item.find('createDt').text} 등록 : {item.find('gubun').text} -> {item.find('death').text}명 사망")


for item in tree[1][0]:
    create_dt = item.find("createDt").text
    if create_dt.split("-")[0] == "2023":
        gubun = item.find("gubun").text
        death = item[3].text
        print(f"{create_dt} 등록 : {gubun} -> {death}명 사망")
```



### 3) '교육' 키워드 검색 시 1~10 페이지 내 타이틀 수집

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=2"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

# print(soup)

nav = soup.select(".pagination")[0]
print(nav)

nums = list()
for page in nav:
    # print(page["onclick"])
    print(page.text)
    if page.text.isdigit():  # 문자열 값이 숫자라면 (이전페이지 같은 문자열은 배제)
        nums.append(page.text)

print(nums)

# 위 주석 처리한 코드와 같은 내용
# map() : nav 리스트의 각 요소에 대해 람다 함수 적용
# x 요소의 text 값을 반환하되, 해당 값이 숫자로만 이루어져 있는 경우에만 반환, 그렇지 않은 경우 None 반환
# map() : nav 리스트의 각 요소에 대해 숫자 값 또는 None 값을 반환
# filter(None, ...): map() 함수의 결과에서 None 값 제거
# list(...): 필터링된 요소들을 리스트로 변환

nums = list(filter(None, map(lambda x: x.text if x.text.isdigit() else None, nav)))
print(nums)

for i in nums:
    sub_url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage={i}"

    sub_soup = BeautifulSoup(requests.get(sub_url).text, "html.parser")
    title_list = sub_soup.select("span[class='title']")
    for title in title_list:
        print(title.text.strip())
```



## 2. 인스타그램



### 1) 태그 입력 시 사진 가져오기

```python
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

# 이렇게 한 줄로 쓸 수도 있음
url = f"https://www.instagram.com/explore/tags/" + input("search tag : ")

# tag = input("search tag : ")
# url = f"https://www.instagram.com/explore/tags/{tag}"

# 1. driver 준비
service = webdriver.chrome.service.Service("../chromedriver.exe")

# 2. driver 가지고 browser 실행
driver = webdriver.Chrome(service=service)

# 3. driver로 server에 요청 (url)
driver.get(url)

# 4. 5초 쉬고
sleep(5)

# 5. 현재 browser가 가지고 있는 page 가져오기 (page_sourse 사용)
soup = BeautifulSoup(driver.page_source, "html.parser")

# 6. img 태그의 링크 가져와서 출력

# 찾아야 하는 것은?
# div class="_aagv" 의 url을 가져와야 함

# img_list = soup.find_all("div", class_="_aaq8")[0].find_all("div", class_="_aagv")[0].text
div_list = soup.find_all("div", class_="_aagv")
for div in div_list:
    print(div.find("img")["src"])
```



### 2) ID / PW 자동 입력

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input("id 입력 : ")
input_pw = input("pw 입력 : ")

service = webdriver.chrome.service.Service("../chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")
sleep(5)

# document.getElementsByName("username")
# 이걸 셀레니움으로 가져올 예정

# 셀레니움이 자바 스크립트 관련된 내용도 가능

# element는 1개, elements는 여러개

id = driver.find_element(By.NAME, "username")
id.send_keys(input_id)
sleep(3)

pw = driver.find_element(By.NAME, "password")
pw.send_keys(input_pw)
sleep(3)

submit_btn = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)")
submit_btn.click()
sleep(15)

# XPATH로 바로 진행할 수 있도록
later_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
later_btn.click()
sleep(5)

driver.close()
driver.quit()
```


## 1. FOLIUM

- 파이썬에서 사용되는 지도 시각화 라이브러리
- 구글 지도를 통해 우리집 위도, 경도를 확인 후 지도에 나오도록

```python
my_loc = folium.Map(location=[위도, 경도], zoom_start=18)

# html로 저장한 뒤 브라우저로 확인 가능
my_loc.save("visual01.html")
```



- 팝업이 뜨도록 할 수도 있음

```python
import folium

my_loc = folium.Map(location=[위도, 경도], zoom_start=18)

folium.Marker([위도, 경도], popup=folium.Popup("우리집",max_width=100)).add_to(my_loc)

my_loc.save("visual02.html")
```



- 우리집 근처 스타벅스 매장

```python
import folium
import json

starbucks_map = folium.Map(location=[위도, 경도], zoom_start=18)

with open("starbucks.json", "r", encoding="utf-8") as f:
    starbucks_json = json.load(f)

print(starbucks_json["starbucks"])

for starbucks in starbucks_json["starbucks"]:
    folium.Marker([starbucks["lat"], starbucks["lot"]], popup=folium.Popup(starbucks["s_name"], max_width=100)).add_to(starbucks_map)

starbucks_map.save("starbucks.html")
```


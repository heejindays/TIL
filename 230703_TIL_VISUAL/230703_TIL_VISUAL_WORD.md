## 1. WORD (CLOUD)



- 가장 별점이 높은 네이버 웹툰 타이틀을 클라우드화

```python
from wordcloud import WordCloud
import json

cloud = WordCloud(background_color="white", max_words=30, width=400, height=300, font_path="Goyang.ttf")

with open("webtoons.json", "r", encoding="utf-8") as f:
    webtoons = json.load(f)

# print(webtoons)

res = dict()
for webtoon in webtoons["webtoons"]:
    res[webtoon["title"]] = int(float(webtoon["star"]) * 100)

print(res)

visual = cloud.fit_words(res)
visual.to_image()
visual.to_file("cloud01.png")
```



- 특정한 그림 안에만 글자가 들어가도록 할 수도 있음

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json

with open("webtoons.json", "r", encoding="utf-8") as f:
    webtoons = json.load(f)

# print(webtoons)

res = dict()
for webtoon in webtoons["webtoons"]:
    res[webtoon["title"]] = int(float(webtoon["star"]) * 100)

# 아무 것도 없으면 0, 뭔가 있으면 1이 채워짐 (행렬)
# 1로 채워진 구역에만 글자를 넣자
masking_img = np.array(Image.open("kakao.png"))

cloud = WordCloud(font_path="Goyang.ttf", max_font_size=40, mask=masking_img, background_color="white").fit_words(res)

cloud.to_file("cloud02.png")
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()
```


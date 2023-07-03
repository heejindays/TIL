## 1. PLOTLY

- 데이터 시각화를 위한 오픈 라이브러리
-  사용자가 그래프를 마우스로 클릭하거나 드래그하면 해당 데이터를 확대 또는 축소 가능
- 추가 정보를 표시하거나 원하는 부분을 강조할 수도 있음



- 캐나다 몬트리올 시의 선거 결과를 샘플로 연습

```python
import plotly.express as px

df = px.data.election()
# print(df)

fig = px.bar(df, x="district", y=["Coderre", "Bergeron", "Joly"], barmode="group")
# fig.show()

# 파일로 저장한 뒤 브라우저로 열 수 있음
# fig.write_html("montreal.html")

# json 파일로도 저장해서 활용할 수 있음
fig.write_json("montreal.json")
```



- 여러 국가에서 수상한 메달의 정보로 연습
- "nation" 열이 "South Korea"인 행들만 선택하여 korea 변수에 할당
- South Korea의 매달 정보만 추출
- count" 열을 값(values)으로, "medal" 열을 이름(names)으로 설정하여 파이 차트를 생성

```python
import plotly.express as px
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df = px.data.medals_long()
# print(df)

korea = df[df["nation"] == "South Korea"]
print(korea)

fig = px.pie(korea, values="count", names="medal")
fig.show()
```


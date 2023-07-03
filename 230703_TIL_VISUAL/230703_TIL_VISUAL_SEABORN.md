## 1. SEABORN

- http://seaborn.pydata.org/
- 사용자가 통계 그래프를 쉽게 그릴 수 있도록 도와주는 라이브러리
- 시각화의 미적인 요소를 개선하여 보다 멋진 그래프를 생성할 수 있도록 함



### 1) car_crashes 데이터 활용

- car_crashes 데이터를 load 하여 연습해보자
- 색깔이 좀 더 화려하고 예쁨
- barplot  : 범주형 변수의 각 카테고리(또는 그룹)의 값들을 막대로 나타내 비교
- 주로 데이터의 평균, 합계, 빈도 등을 시각적으로 비교하는 데 사용

```python
import seaborn as sns
import matplotlib.pyplot as plt

car_crashes = sns.load_dataset("car_crashes")
# print(car_crashes)

plt.figure(figsize=(15, 10))

sns.barplot(data=car_crashes, x="abbrev", y="total")

plt.show()

"""
total : 전체 사고 건수
speeding : 과속 비율
alcohol : 음주 비율
not_distracted : 전방 주시 태만
no_previous : 이전에 사고가 없었던 운전자 비율
ins_premium : 자동차 보험료
ins_losses : 운전자 1인당 충돌사고로 보험사가 입은 손해
abbrev : 미국 주 약자
"""
```



- Lineplot : 연속형 변수의 변화를 선으로 나타냄

-  ascending="False" : 내림차순으로 정렬
- inplace=True : 정렬하고나서 그 결과를 원본 데이터프레임에 바로 적용
- facecolor : 그래프의 배경 색 (채우는 색)
- edgecolor : 테두리 색

```python
import seaborn as sns
import matplotlib.pyplot as plt

car_crashes = sns.load_dataset("car_crashes")

car_crashes.sort_values("total", ascending=False, inplace=True)

plt.figure(figsize=(15, 10))

sns.barplot(x="abbrev", y="total", data=car_crashes, facecolor="w", edgecolor="black")

sns.lineplot(x="abbrev", y="speeding", data=car_crashes, linewidth=3, color="r", label="speeding")
sns.lineplot(x="abbrev", y="alcohol", data=car_crashes, linewidth=3, color="g", label="alcohol")
sns.lineplot(x="abbrev", y="no_previous", data=car_crashes, linewidth=3, color="b", label="no_previous")

plt.xlim(-1, 51)
plt.show()
```



- alpha : 투명도를 설정해서 겹치게 만들 수 있음

```python
import seaborn as sns
import matplotlib.pyplot as plt

car_crashes = sns.load_dataset("car_crashes")
car_crashes.sort_values("total", ascending=False, inplace=True)

plt.figure(figsize=(15, 10))

sns.barplot(data=car_crashes, x="abbrev", y="total", facecolor="w", edgecolor="black")

sns.barplot(data=car_crashes, x="abbrev", y="no_previous", color="b", alpha=0.3, label="no_previous")
sns.barplot(data=car_crashes, x="abbrev", y="speeding", color="r", alpha=0.3, label="speeding")
sns.barplot(data=car_crashes, x="abbrev", y="alcohol", color="g", alpha=0.3, label="alcohol")

plt.xlim(-1, 51)
plt.show()
```



### 2) penguins 데이터 활용

- 종(species) 별로 다르게 그릴 수 있음
- histplot : 주어진 데이터의 분포를 히스토그램으로 시각화
- hue : 데이터를 그룹화 함, 지정된 열의 고유한 값에 따라 데이터가 서로 다른 색상으로 표시됨
- multiple : 여러개의 그룹을 겹쳐서 표시할지, 채우기 모드로 표시할지 결정
  - 기본값은 multiple="layer" (겹치게 표현)
  - multiple="fill" 로 설정하면 히스토그램이 겹치지 않고 영역을 채움

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
# print(penguins)
print(penguins.columns)

sns.histplot(penguins["body_mass_g"])
sns.histplot(data=penguins, y="body_mass_g")
sns.histplot(data=penguins, x="body_mass_g", bins=50)
sns.histplot(data=penguins, x="body_mass_g", binwidth=100)

sns.histplot(data=penguins, x="body_mass_g", hue="species", multiple="fill")


plt.show()
```



- 펭귄의 종 별로 박스 플롯 그리기

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

sns.boxplot(data=penguins, x="species", y="body_mass_g", hue="species")

plt.show()
```



- Swarmplot : 각 범주에 해당하는 데이터 포인트를 연속형 변수의 값에 따라 점으로 나타냄

- x, y 를 각각 쓰면 따로 종별로 박스 플롯을 따로 그릴 수 있음

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

sns.swarmplot(data=penguins, x="body_mass_g", y="species", color="black", alpha=0.5)
sns.boxplot(data=penguins, x="body_mass_g", y="species", hue="sex")

plt.show()
```



- scatterplot : 연속형 변수 간의 관계를 시각화하기 위해 사용됨

- 마커 모양을 다양하게 바꿀 수도 있음
  - `'.'` : 작은 점 모양
  - `','` : 픽셀 모양
  - `'o'` : 원 모양
  - `'v'` : 아래쪽 삼각형
  - `'^'` : 위쪽 삼각형
  - `'<'` : 왼쪽 삼각형
  - `'>'` : 오른쪽 삼각형
  - `'1'` : 아래쪽 피라미드 모양
  - `'2'` : 위쪽 피라미드 모양
  - `'s'` : 사각형
  - `'p'` : 오각형
  - `'*'` : 별 모양
  - `'+'` : 플러스 모양
  - `'x'` : 엑스 모양

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

markers = {"Male": "P", "Female": "o"}
sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm",
                hue="species", style="sex", markers=markers)

plt.show()
```



- violinplot : 커널 밀도 추정 그래프와 상자그림(box plot)을 결합한 형태
- split=True : 좌우 반전할 수 있음

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# split=True 좌우 반전됨
sns.violinplot(data=penguins, x="body_mass_g", y="species", hue="sex", split=True)
sns.swarmplot(data=penguins, x="body_mass_g", y="species", hue="sex", color="black")

plt.show()
```



- regplot : 산점도와 추세선을 함께 보여주는 함수

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

sns.regplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")

plt.show()
```



- ecdfplot : 누적 분포 함수

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

sns.ecdfplot(data=penguins, x="body_mass_g")

plt.show()
```



- pairplot : 변수 간의 산점도와 분포를 한 번에 시각화, 한번에 데이터 전체 볼 수 있음
- penguins 데이터는 총 7개지만, 3개 컬럼은 문자열이라서 4개 컬럼만 나옴
- corner=True : 아래쪽 부분만 출력하게도 가능

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# 3개 컬럼은 문자열이라서, 4개 컬럼만 나옴
sns.pairplot(penguins, hue="sex")
sns.pairplot(penguins, hue="species")

# reg : scatter + 추세선 (kind에 들어갈 속성 찾아보기)
sns.pairplot(penguins, kind="reg")

# corner=True : 아래쪽 부분만 출력됨
sns.pairplot(penguins, corner=True)


plt.show()
```



- 처음에 도화지를 나눌 때 맨 처음을 기준으로 나눔

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins= sns.load_dataset("penguins")

fig = plt.figure(figsize=(10, 7))

# 도화지를 기준으로 각각 분할함
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(2, 2, 2)
ax03 = fig.add_subplot(2, 2, 4)

sns.histplot(data=penguins, x="body_mass_g", ax=ax01)

sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", ax=ax02)

sns.boxplot(penguins["body_mass_g"])

plt.tight_layout()
plt.show()
```


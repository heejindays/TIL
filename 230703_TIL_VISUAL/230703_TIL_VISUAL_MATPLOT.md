## 1. matflot

- 데이터 시각화를 위한 가장 널리 사용되는 라이브러리

- 2D 그래프를 그리는 데 사용됨
- 선 그래프, 산점도, 막대 그래프, 히스토그램, 파이 차트 등 다양한 종류의 그래프를 생성

- 별칭을 plt라고 씀



### 1) plot(선그래프)

- 주어진 데이터를 가지고 선 그래프(line plot)를 그림

- 선 그래프를 그림
- x값, y값을 각각 따로 입력했을 경우

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

fig = plt.figure() # 피규어(fig) > 도화지 생성 (그래프 전체의 밑바탕)
ax = fig.subplots() # subplot > 도화지 나누기 (그래프 몇 개를 어떻게 그릴 건지)

ax.plot(x, y)

plt.show() # 그래프 출력
```



- x값만 입력했을 경우에도 가능

```python
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.subplots()

# [1, 2, 3, 4, 5]: x축에 해당하는 값으로 사용
# y축 값도 동일한 1, 2, 3, 4, 5로 설정
ax.plot([1, 2, 3, 4, 5])

plt.show()
```



- 그래프 색깔을 지정하거나
- 라벨(범례)을 설정할 수도 있음
- 도화지를 한 번에 만들고 나누는 것도 코드 한 줄로 가능 (fig, ax = plt.subplots()

```python
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.subplots()

fig, ax = plt.subplots()


x = [1, 2, 3, 4, 5]
y01 = list(map(lambda x: x**2, x)) # x의 제곱 그래프
y02 = list(map(lambda x: x**3, x)) # x의 세제곱 그래프

ax.plot(x, y01, color="red", label="pow2")
ax.plot(x, y02, color="blue", label="pow3")

# 왼쪽 상단에 라벨로 표시
plt.legend()

plt.show()
```



- figsize=() 사용하려 도화지의 크기를 조절하거나 
- fig.add_subplot()으로 분할하고 위치를 조절할 수도 있음
- label로 범례를 추가할 때에는 그래프 각각 추가
- set_title() 그래프별로 타이틀 지정 가능

```python
import matplotlib.pyplot as plt

# 해당 도화지 크기 조절
fig = plt.figure(figsize=(10, 5))

# 도화지 분할 (1줄, 2칸, 왼쪽에서부터 순서)
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(1, 2, 2)

x = [1, 2, 3, 4, 5]
y01 = list(map(lambda x: x**2, x))
y02 = list(map(lambda x: x**3, x))

ax01.plot(x, y01, color="r", label="pow2")
ax02.plot(x, y02, color="b", label="pow3")

# label 범례 추가 (그래프 하나씩 추가)
ax01.legend()
ax02.legend()

ax01.set_title("x**2")
ax02.set_title("x**3")

plt.show()
```



### 2) scatter (산점도/점그래프)

- 랜덤으로 숫자를 만들어서 산점도 그려보기
- fig.tight_layout() : 레이아웃이 서로 겹치지 않도록 자동으로 조율
- 랜덤으로 나온 숫자라서 분포에 의미 없음

```python
import matplotlib.pyplot as plt
import random

# fig = plt.figure()
# ax01 = fig.add_subplot(2, 2, 1)
# ax02 = fig.add_subplot(2, 2, 2)
# ax03 = fig.add_subplot(2, 2, 3)
# ax04 = fig.add_subplot(2, 2, 4)

fig, ax = plt.subplots(2, 2, figsize=(10, 10))

x = list(range(50))
# 랜덤으로 숫자를 만들어줌
y01 = list(random.randint(0, 50) for i in range(50))
y02 = list(random.randint(0, 50) for i in range(50))
y03 = list(random.randint(0, 50) for i in range(50))
y04 = list(random.randint(0, 50) for i in range(50))

print(x)
print(y01)
print(y02)
print(y03)
print(y04)

# scatter 함수는 점으로 찍히는 함수
ax[0, 0].scatter(x, y01, color="red") #(2, 2, 1)
ax[0, 1].scatter(x, y02, color="green") #(2, 2, 2)
ax[1, 0].scatter(x, y03, color="blue") #(2, 2, 3)
ax[1, 1].scatter(x, y04, color="yellow") #(2, 2, 4)

ax[0, 0].set_title("y01")
ax[0, 1].set_title("y02")
ax[1, 0].set_title("y03")
ax[1, 1].set_title("y04")

# 레이아웃이 서로 겹치지 않도록 조율
fig.tight_layout()

plt.show()
```



### 3) 히스토그램

- x = list(randint(0, 10) for i in range(100))  
- 0부터 10 사이의 난수를 100개 생성하여 리스트 x에 저장

```python
import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots()

x = list(randint(0, 10) for i in range(100))

ax.hist(x, bins=10)

plt.xticks(list(range(0, 11)))
plt.yticks(list(range(0, 101, 5)))

plt.xlim(0, 10)
plt.ylim(0, 100)

plt.show()
```



- cumulative 활용하여 누적 표현도 가능 (True / False)

```python
import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots()

x = list(randint(0, 10) for i in range(100))

# cumulative : 누적(그 이전까지 다 더함)
ax.hist(x, bins=10, cumulative=True)
ax.hist(x, bins=10, cumulative=False)

plt.xticks(list(range(1, 11)))
plt.yticks(list(range(0, 101, 5)))

# limit
plt.xlim(1, 10)
plt.ylim(1, 100)

plt.show()
```



### 4) boxplot

- 박스(Box): 박스 플롯의 중심 부분으로서, 데이터의 중앙값(Q2)을 나타냄
- 박스의 윗부분은 Q3(상위 사분위수), 박스의 아랫부분은 Q1(하위 사분위수)
- 이상치 : 박스 플롯에서 독립적으로 표시될 수도 있고, 점 또는 다른 표시 방법 사용 가능
- 평균(mean)과 중위값(median) 구하기
- limit : 범위

```python
import matplotlib.pyplot as plt
from random import randint
import numpy as np

fig, ax = plt.subplots()

x = list(randint(0, 1000) for i in range(10))

print(x)
print(f"평균 : {np.mean(x)}")
print(f"중위값 : {np.median(x)}")

ax.boxplot(x)

plt.show()
```



### 5) pie

- 랜덤으로 숫자를 골라 파이 그래프 만들기
- autopct="%1.1f%%" : 각 부채꼴(pie wedge) 영역에 대한 백분율 레이블을 지정
- startangle=90 : 시작 각도를 90도로
- counterclock=False : 그래프의 회전 방향을 지정(반시계방향)

```python
import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots()
ages = list(randint(1, 100) for i in range(100))

# 숫자가 랜덤으로 나오지만 그 안에서 구분됨
child = list(x for x in ages if x < 19)
young = list(x for x in ages if 19 <= x < 50)
middle = list(x for x in ages if 50 <= x < 70)
wise = list(x for x in ages if x >= 70)

print(child)
print(young)
print(middle)
print(wise)

labels = ["child", "young", "middle", "wise"]
count = [len(child), len(young), len(middle), len(wise)]

# 파이 그래프에서 몇 % 를 차지하고 있는지도 알려줌
# 90도 부터 시작하게 할 수도 있고, 순서를 시계방향으로 할 수도 있음
ax.pie(count, labels=labels, autopct="%1.1f%%", startangle=90, counterclock=False)

plt.show()

```



### 6) bar / barh

- 그래프를 위로 올라가게도
- 오른쪽으로 뻗어나가게도 할 수 있음

```python
import matplotlib.pyplot as plt
from random import randint

fig = plt.figure()
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(1, 2, 2)

x = [1, 2, 3, 4, 5]
y = list(randint(1, 100) for i in range(5))

# 위로 올라감
ax01.bar(x, y, color='r')

# 오른쪽으로 늘어남
ax02.barh(x, y, color='b')

plt.show()
```


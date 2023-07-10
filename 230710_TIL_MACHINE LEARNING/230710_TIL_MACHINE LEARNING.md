## 선형 회귀 분석 하는 법

**null값/na값이 있는지 확인 (결측치)**

boston.isnull().sum()
boston.isna().sum()



**데이터 준비**

문제 : x (넣을 값)
정답 : y (알고 싶은 값)
x = df[["RM"]]
y = df[["PRICE"]]



**데이터 분할 (import 되어 있어야 함)**

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)



**모델 선택 (import 되어 있어야 함)**

from sklearn.linear_model import LinearRegression

model = LinearRegression() 



**모델 학습**

model.fit(x_train, y_train)



**예측**

predict = model.predict(x_test)
predict



**정확도 평가**

model.score(x_test, y_test["PRICE"])



**어느정도 오차가 있는지 궁금하다면**
result = y_test
result["predict"] = predict
result



**그래프 그리기**

import matplotlib.pyplot as plt

plt.plot(x, y, 'o')
plt.plot(x_test, predict)
plt.show()





<hr>



### 다항 회귀 분석하는 법



**산점도로 한번 확인해보자**

plt.plot(x, y, 'o')
plt.show()



**데이터 준비**

x = tips[["total_bill", "size"]]
y = tips[["tip"]]



**다항식 만들기(import 필요)**

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3) 



**데이터 학습 후 변경**

poly.fit(x)
x_poly = poly.transform(x)



**데이터 분할**

x_train, x_test, y_train, y_test = train_test_split(x_poly, y, test_size=0.3, random_state=1)



**모델 선택 및 학습**

model = LinearRegression()
model.fit(x_train, y_train)



**예측**

predict = model.predict(x_test)
predict



**정확도 평가**

model.score(x_test, y_test)


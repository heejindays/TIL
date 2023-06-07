# 04. Python function

> `함수(def)` : 기능을 구현한 뒤 호출해서 사용


## 1) 기본 구조


- 함수 호출하는 방법 : `함수이름()`

```python
def hello01():
    print("hello, world!")

hello01()

------------------------------

hello, world!
```

- `return` : 값을 돌려줘야 하는 경우가 있다면 사용

- 없다면 `return 생략 가능`


```python
def hello02():
    return "hello, return!"

print(hello02())

------------------------------

hello, return!
```
- `key : value` 형태도 출력 가능


```python
def hello03():
    return {"name" : "heejin", "age" : "100"}

print(hello03())

------------------------------

{'name': 'heejin', 'age': '100'}
```


- return이 여러개 : `맨 처음 return 출력 후 종료`

```py
def hello05():
    return 1
    return 2
    return 3

print(hello05())

------------------------------

1 # return 1만 출력됨
```

- 기본 연산 및 문자열 출력 가능

```py
def sum(a, b):
    result = a + b
    return result
print(sum(1, 2))

------------------------------

3
```
```py
def say():
    return "hi"
print(say())

------------------------------

hi
```

```py
def sum(a, b):
    print(f"{a}, {b}의 합은 {a+b}입니다.")
sum(1, 5)

------------------------------

1, 5의 합은 6입니다.
```

```py
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1, 2, 3, 4, 2, 5))


------------------------------

17
```

```py
def sum_many(*args):

    sum = 0
    for i in args:
        sum += i    # sum에 i를 더하겠다
    return sum

print(sum_many(1, 2, 3, 4, 2, 5))
------------------------------

17
```
___

## 2) Arguments 와 Parameter

- `arguments` : 함수 외부에서 파라미터에게 전달하는 "값"

- `parameter` : 함수 외부에서 전달되는 값을 받아서 함수 내부에서 사용하기 위한 변수

- x : 파라미터

- 2 : arguments (args)

```py
def sum2(x):
    return x + 2
print(sum2(2))

------------------------------

4
```

- 값이 2개인 경우도 가능

```py
def sum_x_y(x, y):
    result = x + y
    return result

print(sum_x_y(2,1))

------------------------------

3
```
- 값이 여러개면 `튜플`로 만들어 줌

```py
def my_x_y(x, y):
    return x+y, x-y

print(my_x_y(7,6))
print(type(my_x_y(7,6)))

------------------------------

(13, 1)
<class 'tuple'>
```

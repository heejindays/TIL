# python quiz 예상 문제 (6/15)

## 1) 용어 정리

| No.  | 구분       | 용어명                                         | 설명                                                         |
| ---- | ---------- | ---------------------------------------------- | ------------------------------------------------------------ |
| 1    | python     | Null                                           | 값이 없음 (값이 뭔지 알 수가 없음)                           |
| 2    | python     | 주석                                           | #을 사용하여 프로그램 작성 시 코드를  설명하기 위해 사용하는 것 (코드로 인식되지 않음) |
| 3    | python     | 상수                                           | 어떤 숫자를 변수에 할당한 후에  프로그램이 끝날 때까지 값을 변경하지 않고 사용하는 변수 |
| 4    | python     | 모듈(module)                                   | 상수, 변수, 함수, 클래스를 포함하는  코드가 저장된 파일      |
| 5    | python     | 내장 모듈                                      | 개발 환경을 설치할 때 함께 설치되는  모듈                    |
| 6    | python     | 임포트(import)                                 | 다른 파일에 있는 걸 사용하겠다는 의미                        |
| 7    | python     | 패스(pass)                                     | 코드가 실행되기는 하지만 아무 일도  일어나지 않음 (전체적인 구조를 먼저 잡을 때 사용) |
| 8    | python     | 브레이크(break)                                | for문이나 while문에서  break를 만나면 바로 반복문을 빠져나옴 |
| 9    | python     | 컨티뉴(continue)                               | 반복문에서 continue를 만나면 그  이후의 코드는 실행하지 않고 반복문의 처음으로 되돌아감 |
| 10   | python     | readline()                                     | 파일의 문자열 한 줄을 읽음 (또  사용하면 그 다음줄을 읽음)   |
| 11   | python     | pickle(dump)                                   | 객체를 파일로 바로 저장할 수 있음                            |
| 12   | python     | unpickle (load)                                | 파일에 저장되어 있는 객체를 다시  코드로 가져올 수 있음      |
| 13   | python     | 튜플(tuple)                                    | 여러 개의 데이터를 하나로 묶는 데  사용함, 순서 있고 중복도 가능하나 변경은 불가능 () |
| 14   | python     | 세트(set)                                      | 여러 개의 데이터를 수학의 집합 개념으로 묶는 것, 데이터의 순서가 없고 중복이  불가능 함 {} |
| 15   | python     | 딕셔너리(dictionary)                           | 여러 개의 데이터의 묶음으로  키(key)와 밸류(value)의 조합인 쌍으로 구성되어 있음 {} |
| 16   | python     | 리스트(list)                                   | 여러 개의 데이터의 묶음으로 순서가  있고 중복이 가능하다 []  |
| 17   | python     | 문자열(str)                                    | 문자열 : 리스트처럼 순서가 정해진  형태로 정리됨             |
| 18   | python     | 불(bool)                                       | 논리 연산을 위한 데이터 타입으로  TRUE와 FALSE가 있음        |
| 19   | python     | 시퀀스(Sequence)                               | 순서가 있는 값들을 가진 객체                                 |
| 20   | python     | mutable                                        | list, set, dictionary  (값이 변하는 것들)                    |
| 21   | python     | immutable                                      | numbers, tuple, str,  frozenset, bool, int (값이 변하지 않는 것들) |
| 22   | python     | 컬렉션(collections)                            | list, tuple, set,  dict 등 여러 데이터가 모여있는 묶음       |
| 23   | python     | 기능, 매서드(method)                           | 클래스에서 정의한 함수를 객체를 생성한  이후에 이용할 때 (클래스에서 정의한 함수) |
| 24   | python     | 클래스(class)                                  | 객체의 공통된 속성과 기능을 변수와  함수로 정의한 것         |
| 25   | python     | singleton                                      | 객체를 하나만 만든다                                         |
| 26   | python     | 객체(object)                                   | 클래스를  가지고 메모리에 구현해서 만들어지며 속성과 기능으로 이루어진 대상     속성은 변수로 구현하고 기능은 함수로 구현함 |
| 27   | python     | 인스턴스(instance)                             | 클래스로부터 만들어진 객체                                   |
| 28   | python     | 객체 지향 프로그래밍 언어                      | 객체를 만들고 이용할 수 있는 기능을  제공하는 프로그래밍 언어 |
| 29   | python     | 클래스 변수(class  variable)                   | 클래스  내에 있지만 함수 밖에서 정의한 변수     클래스에서 생성한 모든 객체가 공통으로 사용 가능     해당 클래스 타입 전체가 사용할 수 있는 변수 |
| 30   | python     | 인스턴스 변수 (instance  variable)             | 각 인스턴스(객체)에서 개별적으로  정의하여 사용하는 변수     |
| 31   | python     | 인스턴스 매서드 (instance  method)             | 각 객체에서 개별적으로 동작하는 함수를  만들고자 할때 사용 (첫 인자로 self가 필요) |
| 32   | python     | 정적  메서드 (static method)     @staticmethod | 클래스  안에 있지만 클래스나 클래스의 인스턴스(객체)와는 무관하게      독립적으로 동작하는 함수 (self를 사용하지 않음) |
| 33   | python     | 클래스  매서드 (class method)     @classmethod | 클래스 변수를 사용하기 위한 함수  (상속받는 환경에서 인자로 cls가 필요함) |
| 34   | python     | `__init__`                                     | 객체가 생성될 때 인스턴스 변수 초기화                        |
| 35   | python     | 패키지(package)                                | 여러 모듈을 체계적으로 모아둔 것                             |
| 36   | python     | 함수                                           | 어떤 기능을 수행할 수 있도록 작성된  코드의 묶음 (명령문들의 집합) |
| 37   | python     | 파라미터(parameter)                            | 함수 외부에서 전달되는 값을 받아서  함수 내부에서 사용하기 위한 변수 |
| 38   | python     | 아규먼트(arguments)                            | 함수 외부에서 전달되는  "값"                                 |
| 39   | python     | *arg                                           | 별(*)이  하나 붙어 있으면 콤마로 나열해서 입력한      여러개의 asgs 들이 하나씩 들어올거고 그걸 다 받겠다는 의미     몇 개가 들어올지 모르고 어떤 형태가 들어올지 모름      (만들때는 모르니까 일단 써두자 뭐가 몇 개 들어올지 모름) |
| 40   | python     | **kwargs (keyword  arguments)                  | key  : value 형태로 들어간다     몇 개가 들어올지 모르고 어떤 형태가 들어올지 모름      (만들때는 모르니까 일단 써두자 뭐가 몇 개 들어올지 모름) |
| 41   | python     | 전역 변수(global scope)                        | 해당 파일 스크립트 전체에서 접근할 수  있도록 하는 변수      |
| 42   | python     | 지역 변수                                      | 해당 함수 안에서 사용 가능한 함수                            |
| 43   | python     | 추상화                                         | 큰  개념으로 묶어서 공통적인 걸 하나로 묶어서 미리 만들어 두는 것      (자식 개념이 나머지를 만들 수 있도록) |
| 44   | python     | 상속                                           | 부모  클래스에 있는 것들을 자식 클래스에서 모두 사용할 수 있음      (단 __로 묶어둔 것은 사용하지 못함) |
| 45   | python     | 예외 처리                                      | 에러 발생했을 때, 프로그램이  비정상적으로 종료되는 것을 방지 |
| 46   | python     | lazy evaluation                                | 실행(호출)될 때 연산 / 당장하는  것이 아님                   |
| 47   | python     | 리터레이터 (iterator)                          | 반복해서 값을 순서대로 꺼낼 수 있는  객체                    |
| 48   | python     | yield                                          | 호출될 때 생성할 것                                          |
| 49   | python     | 스레드(thread)                                 | 프로그램 안에 있는 작업 단위                                 |
| 50   | python     | 콜백 (callback)                                | 지금 당장 실행되는게 아니고 특정  이벤트가 발생했을 때 실행되는 것 |
| 51   | python     | 코루틴(coroutine)                              | 메인 루틴과 독립적으로 실행되는 것  (메인, 서브와 별개로 같이 돌고 있는 루틴 개념) |
| 52   | python     | yield from                                     | 내가 받은 제너레이터 요청을 다른  제너레이터에게 다시 전달함 |
| 53   | python     | 고수준 실행                                    | 사람에게 가까움 (추상화가 잘  되어있다)                      |
| 54   | python     | 저수준 실행                                    | 컴퓨터에 가까움 (명령어들을 많이  사용할 수 있다)            |
| 55   | python     | 정수 (int)                                     | 정수를 나타내는 데이터 타입                                  |
| 56   | python     | 부동소수 (float)                               | 소수점 이하의 값을 가지는 실수 데이터  타입                  |
| 57   | python     | dir()                                          | 객체의 속성, 매서드 확인                                     |
| 58   | python     | 클로저                                         | 함수와 그 함수가 접근하는 비로컬  변수들로 이루어진 패키지   |
| 59   | jQuery     | jquery                                         | 빠르고 간편한 웹 개발을 위한 오픈  소스 JavaScript 라이브러리 |
| 60   | jQuery     | $ 함수                                         | jQuery 객체를 생성                                           |
| 61   | javascript | ajax                                           | Asynchronous  Javascript And Xml     서버에 요청한 후 응답을 기다리지 않고 다음 명령 수행     비동기 요청으로 인해 화면이 새로고침되지 않는다     주소창은 변하지 않고, 화면 안의 특정 내용만 바뀜 |
| 62   | javascript | .xml 파일                                      | "확장  가능한 마크업 언어" (eXtensible Markup Language)     데이터를 저장하고 전송하기 위해 사용되는 텍스트 기반 파일 형식     사용자가 자신만의 태그를 정의하여 데이터를 구조화하는 데 사용할 수 있는 개방형 형식 |
| 63   | javascript | GET 방식                                       | URL에 데이터를 포함하여 서버로 보냄                          |
| 64   | javascript | POST 방식                                      | 데이터가 URL에 노출되지 않은 상태로  전송                    |
| 65   | javascript | readystate                                     | 0:  uninitialized (대기)     1: loading (요청할 준비)     2: loaded (요청 다 됨)     3: interactive (통신하는 중)     4: complete (통신 완료) |
| 66   | javascript | status (http 상태 코드)                        | 200  : 성공     400 : bad request (서버가 요청을 이해 못함)     401 : unauthorized     403 : forbidden     404 : not found     500 : internal server error (서버가 처리 방법을 모름) |
| 67   | javascript | textContent                                    | 태그 포함해서 그냥 문자열이 됨                               |
| 68   | javascript | isNaN                                          | 숫자 아닌게 맞니? 숫자가 아닌 것이  들어가야 true가 됨       |
| 69   | javascript | 프로퍼티 (property)                            | 객체(Object) 내에서 값을  저장하거나 접근하기 위한 변수 (이름(키)과 값으로 구성) |
| 70   | javascript | 매서드 체이닝 (method  chainning)              | 객체  지향 프로그래밍에서 동일한 객체에 연속적으로 메서드를 호출하는 것     코드가 간결하고 가독성이 높아지며, 여러 단계의 작업을 한 줄로 표현할 수 있게 됨 |
| 71   | html       | HTTP                                           | 클라이언트와 서버 사이에서 어떤 식으로  소통할지 통신 규약을 정해둔 것 (Hyper Text Transfer Protocol) |
| 72   | html       | web                                            | 클라이언트로부터 요청이 들어오면 요청에  맞는 문서를 응답해줄 것 |
| 73   | CSS        | CSS                                            | Cascading  Style Sheets     웹 페이지의 디자인과 레이아웃을 담당하는 스타일 시트 언어      HTML과 XHTML 같은 마크업 언어로 작성된 문서의 스타일을  지정하여 웹 페이지를 꾸밀 수 있음 |



## 2) 객관식 및 OX 퀴즈

 

- 여러 개의 값을 콤마로 구분하여 할당하면 튜플로 인식 (튜플로 패킹)



- 튜플을 개별 변수로 분리 (언패킹)

  f = 1, 2, 3

  g, h, i = f

  print(g) > 1

  print(h) > 2

  print(i) > 3



- a, b = b, a 으로 값 바꾸는 것 가능



- 리스트 길이의 타입 : **int**

  print(type(len(b))) 

  **<class 'int'>**



- 문자열(str)은 문자들의 시퀀스로 구성
  각 문자는 순서를 가지고 위치를 나타냄
  ex) 단어를 set으로 생성하면 알파벳별로 나뉨



- 이스케이프 시퀀스(escape sequence)
  - 작은 따옴표까지 나오게 :  `\'python\'`
  - 줄바꿈 : `\n`



- raw string (그대로 출력) i = r'쓰고싶은 내용'

  

- 문자열도 * 2가 됨 print('hello' * 2 + "python!") hellohellopython! 

  

- 집합처럼 순서도 중복도 없는 것 : SET

  

- set은 순서가 없으니까 출력할 때마다 순서 바뀜 

  ex) print(a.pop()) 하나 뽑아도 뭐가 나올지 모름

  

- frozenset : 변경할 수 없는 set

  중복은 안 됨, 타입은 <class 'frozenset'>

  

- 괄호 모양

  - 리스트 : [ ]

  - 튜플 : ( )

  - 셋, 딕셔너리 : { }

    

- 딕셔너리도 순서 있음 (3.7 버전부터)

  key는 중복 안되고, value는 중복 가능

  

- 딕셔너리 만드는 법

  dict05 = {"a":1, "c":2, "b":3}

  dict02 = dict(a=1, c=2, b=3)

  

- list, set, dictionary (값이 변하는 것들)

  내용 추가해서 값은 변해도 주소값은 같음

  

- numbers, tuple, str, frozenset, bool, int  (값이 변하지 않는 것들)

  값은 변하지 않아도 주소값이 다름

  

- 소수점 있는거에 int() 씌우면 버림

  a = int(1.9)

  print(a) 1이 됨

  

- int(True) : 숫자 1

  

- str(문자열)은 str(문자열)이랑만 더할 수 있음
  

- print()

  sep = " " 한 칸 띄어쓰기 옵션이 기본 (변경 가능)

  end = \n 줄바꿈 옵션이 기본 (변경 가능)
  

- f-string

  name = "엘리스"

  age = 25

  print(f"제 이름은 {name} 이고, 제 나이는 {age} 입니다.")
  

- a = 10

  b = 20

  print(f"{a}와 {b}의 합계는 {a+b}이다.")
  

- 거듭제곱 : print(a ** b)

  몫 : print(a // b)

  나머지 : print(a % b)
  

- 파이썬에서 같다는 의미는 == 로 표현
  

- 비교

  and : 둘 다 True 일때만 True

  or : 둘 중 하나만 True 이면 True
  

- range : 해당 범위의 숫자를 생성

  range(stop) : 0 ~ stop-1

  print(range(10)) : 0부터 9까지

  range(10, 20)) : 10부터 19까지

  range(1, 10, 2) : 1부터 9까지 2간격으로 증가

  range(10, 0, -1) : 10부터 1까지 -1씩 증가

  ** range(0, 10, -1) 이건 만들어질 수 없음

- 슬라이싱

  [start : stop] : start 부터 stop-1 까지

  [start : stop : step] : start부터 stop-1까지 step 간격으로

  

- hello = "hello, wolrd!"

  world 만 출력하려면?

  print(hello[7:12])
  

- input()으로 입력한 값 : 'str' 문자열
  

- 딕셔너리에 키:값 추가

  score = dict()

  score['name'] = name

  비어있는거 만들고 키:값 추가
  

- if ~ elif : if절이 참이면 바로 끝
  

- if ~ elif ~ else : 위 모든 조건에 해당하지 않으면
  else로 나머지 모든 조건

- TRUE / FALSE

  False : 비어있는 문자열, 괄호, 0, None

  True : 채워진 문자열, 1
  

- _ : 값을 사용하고 싶지 않을 때



- `enumerate()` 함수 

  (iterable) 객체를 입력 받아 인덱스와 값을 순차적으로 반환
  

- match : if처럼 순차적으로 판별하지 않고 점프해서 바로 그 값으로 감
  

- for _ in range(3):

  그냥 3번 반복 (_로 변수 사용 가능)
  

- break : 반복문 종료 후 다음 명령을 수행

  

- continue : 아래의 명령문을 무시하고 다음 반복으로 넘어가서 진행



- 반복문의 마지막 else : 반복문이 다 끝나고 나서 실행 

  (중간에 break로 반복문이 멈추면 안 나옴)
  

- 리스트 안에 튜플로 묶여 있을 때 : 튜플 맨 앞 숫자 기준 정렬
  

- raise : 강제로 발생시킨다
  

- `__init__(self, end):`

  인스턴스 변수 초기화
  

- `__iter__(self):`
   iterable한 객체로 바꿈
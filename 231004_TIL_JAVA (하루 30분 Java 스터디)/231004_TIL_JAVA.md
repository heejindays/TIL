## Java

- **method 선언 방법**
  - 접근제한자 / 메모리영역 / 리턴타입 / 메소드이름(파라미터) {}

<br>

- **method 호출 방법**
  - method();
  - static인 경우 : class.method();
  - non-static인 경우 : 
    - class 변수 = new class();
    - 변수.method();

<br>

- **리턴 타입**

  - void : 리턴되는 값이 없다

  - python 에서는 리턴되는 값이 없으면 None
  - 파라미터(parameter) : 외부에서 전달된 값을 받아서 내부에서 사용하기 위한 '변수'
  - 아규먼트(argument) : 외부에서 전달되는 '값'

<br>

- 상수인 경우 대문자로 표기 (암묵적인 합의)
  - ex) **private** **static** **final** **int** **TEN** = 10;

<br>

- **증감 연산**
  - ++, -- 
  - 변수의 앞뒤에 증감연산자를 붙이게 되면, 변수가 가진 값을 1씩 증감 
  - 전위 연산자 : 연산자를 변수 앞에 붙여 연산을 먼저 하고, 값을 나중에 리턴
  - 후위 연산자 : 연산자를 변수 뒤에 붙여서 값을 먼저 리턴하고, 연산을 나중에 

<br>

- **논리 연산**

  - & (and 연산) : true 이고 true 이면 true가 리턴

  - && : 왼쪽 조건이 false면 오른쪽 조건 확인 안 함 (안해도 false)
  - | (or 연산) : false 이고 false 이면 그때만 false 이고 나머지는 true 
  - || : 왼쪽 조건이 true면 오른쪽 조건 확인 안 함 (안해도 true)

<br>

- **삼항 연산**
  - String s = (a<b)?"a가 b보다 작다.":"a가 b보다 크다.";
  - (조건)? 참일 때 리턴 : 거짓일 때 리턴
  - 여러개의 조건을 연결할수도 있음
    - int i = (a>b)? a-b : (a<b)? a+b : a*b (많이 사용되진 않음)

<br>

- **비트 연산**
  -  &, |, ^, ~, <<, >> 
  - 수치를 0,1 비트 상태에서 연산 후, 연산 결과를 리턴
  - int는 4byte = 32bit

<br>

- **program의 주 진입점**
  - public static void main(String[] args)
  - 접근제한자 : public (어디서든 접근 가능)
  - 메모리영역 : static (static 영역에 저장되어 java가 실행될 때 한번만 호출)
  - 리턴타입 : void (리턴하는 값 없음)
  - 메소드명 : main
  - 파라미터 : String[] (문자열 배열)

<br>

- **body 작성하는 방법**

  - python에서는 들여쓰기로 body를 지정

  - java에서는 중괄호 {} 로 body를 지정

  - python 

    - if i > 0 :
          print("")

  - java

    - if i > 0 {

      ​    System.out.println("");
      }

<br>

- **조건문**

  - python : elif

  - java : else if

  - if (true == true) {

    }

    if (true) {
    }

  - if (ring == true) 이렇게 쓸 필요 없음 바로 if(ring) 으로 써야 좋은 코드

  - 바로 참인지 아닌지 알 수 있기 때문에


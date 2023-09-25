## Java

- **기본타입**
  - 타입변수 = 값;
  - 값을 가지고 있는 > 값을 넣어두거나 값을 가져오는 것만
  - ex) int
- **참조타입**
  - 타입변수 = 객체; (해당 객체가 저장되어있는 주소값)
  - 주소값을 가지고 있는 > 주소값에 있는 값을 기능 추가할 수 있음
  - ex) Interger

- char : 문자
- String : 문자열 = character sequence (문자 배열, 문자들의 집합)
- boolean : 논리 (true / false)

<br>

- 파이썬은 모든 게 다 객체라서 대문자 (True / False)
- 소문자면 기본타입, 대문자면 참조타입

<br>

- 묵시적 형변환 (upCasting : 작은 타입에서 큰 타입으로 - promotion)

  - ​		**byte** b1 = (**byte**) 100;

    ​		**int** i1 = b1;

    ​		System.**out**.println(i1);

- 명시적 형변환 (downCasting : 큰 타입에서 작은 타입으로 - casting)

  - ​		**int** i2 = 100;

    ​		**byte** b2 = (**byte**)i2;

    ​		System.**out**.println(b2);

<br>

- print
  - System.out.print() - 줄 바꿈 없음 
  - System.out.println() - 줄 바꿈 포함
  - System.out.printf() - 'f' : formatter (자리 or 형식)

<br>

class Hello {

// main method : 프로그램의 주 진입점

// **접근제한자 메모리영역 리턴타입 메소드명 (파라미터)**

public static void main (String[] args){

}

}

<br>

- **method : 종속적임 (class에 종속적임)**
  - class.method와 같은 방식으로 호출됨
  - 같은 클래스 내에서는 class. 을 생략 가능함
- function : 독립적임

<br>

- 전역변수 : 클래스 밖에는 변수를 만들 수 없고 안에 있어야 함

<br>

- **접근제한자**
  - public : 
    - 어디서나 접근, 참조 가능 (+)
  - protected : 
    - 상속일 경우 상속된 곳에서 가능
    - 상속이 아닌 경우 같은 패키지 내에서 (#)
  - (defalut) : 
    - 같은 패키지 내에서 사용 가능
    - 접근제한자가 생략되면 default method
    - 실제로 키워드를 사용하지 않음 (~)
  - pritave : 
    - 현재 클래스 내에서만 (-)

<br>

- private method : not visible (있긴 있는데 못 본다는 의미)

- undefined (애초에 없음)

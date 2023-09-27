## Java

- **매소드 선언 방법**
  
  - 접근제한자 메모리영역 리턴타입 매소드명 (파라미터) {
  
    }

- 접근제한자
  - public : 
    - 상속인 경우 상속된 곳에서(클래스) 
    - 상속이 아닌 경우 같은 패키지 내에서
  - (default) : 같은 패키지 내에서
  - private : 같은 클래스 내에서만

<br>

- os가 java에게 메모리를 주면 static / stack / heap 영역으로 나눔
- **static** 
  - class, static으로 선언된 매서드나 변수가 들어감
  - 자바가 실행될 때 딱 1번 호출됨
- **stack**
  - 변수가 들어감
- **heap**
  - 객체, 값이 들어감

- 자바 > 클래스 > 실행

<br>

- non-static : 객체를 만들어야 사용 가능 (heap 영역)

- 객체 생성 방법
  - type 변수 = new Type();

- 우리가 만든 class는 참조 타입
  - 변수.method(); 로 호출할 수 있음

<br>

- diagram

![image-20230927084144019](C:\Users\heeji\AppData\Roaming\Typora\typora-user-images\image-20230927084144019.png)

<br>

- **import** multi.test01.MethodTest01;
  - 다른 패키지에 있는 클래스를 사용하고 싶을 때
  - 해당 클래스의 매서드를 사용하겠다고 선언해야 함
  - 패키지 : 서로 관련이 있는 클래스들의 집합
  - 관련이 있는 클래스들을 패키지로 묶어야 다른 곳에서 쓸 수 있음
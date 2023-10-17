## Java

- 예외처리 
  - 개발자가 의도하지 않은 프로그램의 비정상적인 종료를 막기 위해 필요
  - 자바에서는 예외를 처리하기 위해 `try`, `catch`, `finally`, `throw`, `throws` 등의 키워드를 사용

<br>

- 예외처리
  - try 
    - 예외가 발생할 수 있는 코드
  - catch() 
    - 특정 예외가 발생했을 때 실행됨
    - 여러 `catch` 블록을 사용하여 여러 예외를 처리할 수 있음
  - finally  
    - 예외 발생 여부와 관계없이 항상 실행
  - throw 
    - 메서드에서 발생한 예외를 직접 처리하지 않음
    - 호출한 쪽으로 예외를 던질 수 있음

<br>

- lambda : 익명함수 (일회용으로 간결하게 사용하기 위한 함수)
- stream : lambda나 functional interface 등을 가지고 연결
- **@functionalinferface** 
  - 해당 인터페이스의 매서드가 한 개라는 걸 알려줌
  - 반드시 하나의 추상 메서드만 가져야함
  - 그렇지 않으면 컴파일러가 오류를 발생시킴

```java
@FunctionalInterface
public interface MyFunctionalInterfaceError {
    void myMethod(); // 올바른 함수형 인터페이스

    void anotherMethod(); // 오류: 두 개 이상의 추상 메서드를 가짐
}
```

<br>

- lambda로 구현 가능
  - 명령어 하나 일때만 중괄호랑 return 생략 가능

- Operator : 파라미터 받아서 연산해서 리턴해줌
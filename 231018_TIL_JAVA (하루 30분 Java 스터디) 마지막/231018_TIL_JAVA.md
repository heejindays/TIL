## Java

- java.util.function 공식문서 확인하기

<br>

- Operator : apply() -> 값을 받아서 처리하고 값을 리턴해줌

- Function : apply() -> 값을 받아서 처리하고 값을 리턴해줌

- Function과 Operator의 차이 : type

- predicate : 값을 받아서 조건을 판별하고 T/F를 리턴함

  - interface Predicate<T> {

    ​	public boolean test(T);

    }

<br>

- **Supplier와 Consumer**

- Java.util.function 패키지에 속하는 함수형 인터페이스(Functional Interface)
-  주로 람다 표현식을 사용하여 함수를 정의하고 전달하는 데 사용
- 함수형 인터페이스들은 Java 8에서 추가됨

- supplier : 값을 만들어서 리턴해줌
- consumer : 값을 받아서 처리하고 리턴하지 않음

<br>

- JAVA 기본 강의 마무리!
- 추후 실무에서 사용할 일이 있다면 추가적으로 공부할 것!
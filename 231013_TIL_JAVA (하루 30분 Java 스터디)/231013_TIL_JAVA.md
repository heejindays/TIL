## Java

- java는 하나의 클래스만 상속할 수 있음
- Python : 다중 상속 시, 부모의 메소드 호출 순서를 MRO 에다가 저장 (자바는 없음)
- 인터페이스
  - 모든 메서드가 추상 매서드이다
  - 바디가 없는 메서드만 있음
  - 인터페이스는 여러개 상속 가능

<br>

- extends : 같은 모양 (class - class, interface - interface)
- implements : 다른 모양 (class-implements)

- interface에서의 body가 있는 매서드들은 default 키워드 작성
- 접근제한자의 default는 키워드를 작성하지 않음

<br>

- Python : dataclass > getter / setter
- Java : record type

<br>

- class 클래스명 {

  // field (속성)

  // 클래스 변수 : class에서 사용할 수 있는 변수 (static)

  // 인스턴스 변수 : class를 가지고 만들어진 객체 하나가 가질 수 있는 변수

  

  // constructor (생성자)

  // 객체 생성, 필드 초기화

  

  // method (기능)

  // getter / setter

  }

<br>

- 추상 클래스 : 
  - 부분적으로 구현된 메서드를 가질 수 있어 일부 공통 동작을 제공
  - 하위 클래스에서 필요한 메서드를 구현하도록 할 수 있음
- 인터페이스 : 
  - 모든 매서드가 추상 매서드인 클래스
  - 서로 다른 클래스들 간에 공통된 동작을 정의하고 싶을 때
  - 다중 상속을 지원할 때 유용함

<br>

- class는 하나만 상속 가능, interface는 다중 상속 가능
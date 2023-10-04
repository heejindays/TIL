## Java

- **switch**

  - if는 순차적으로 모든 코드를 읽어들임
  - switch는 해당 case로 jumping하기 때문에 컴파일러가 작업하는데 수월
  - java 7버전 이후부터 문자열 사용 가능

<br>

- **do while**

  - 일단 do의 명령부터 실행함
  - 그 다음에 조건을 확인
  - ex) 게임을 한번 하고 나서 그 다음에 다시 할지 물어보고 싶을 때 사용

- **do ~ while문 예시**

  - do {
    	System.out.println(i);
    	i++;
    } while (i == 10);

    // 1 출력하고 끝남

- **i가 1부터 10 전까지 출력**

  - }while(i < 10);

    ​		//i == 10 이면 안되는 이유! false라서

    ​		System.**out**.println("do while이 종료된 후의 i 값 : " + i);

    ​	}

<br>

- while(true){
  }
  - 무한루프를 만들어 둔 뒤
  - if로 조건문을 넣어서 조건에 해당하면 멈추도록 할 수 있음

<br>

- fot (초기값 ; 조건식 ; 증감식) {
  // 명령문
  }
  - 조건을 만족할 때까지 명령문 수행한 뒤 증감식 반영함

<br>

- **vararg (가변인수)**
  - 메서드가 임의의 개수의 인자를 받을 수 있도록 허용
  - 호출 시에는 인자의 개수를 동적으로 지정할 수 있음
  - 파라미터에 ... 붙임
  - total(int ... data)
  - data 변수는 배열
  - python 에서 args, kwargs와 비슷

<br>

- **array (배열) : 같은 타입만 가질 수 있음**

  - 배열 : 같은 타입의 여러 개의 값을 효과적으로 관리할 수 있는 객체
  - **int**[] : int type만 가질 수 있는 배열을 만들겠다는 의미
  - python의 리스트는 다른 타입도 넣을 수 있음
  - 자바의 배열은 같은 타입만 넣을 수 있음

  <br>

  - int [] 변수 ;
    a = new int [size];
  - int type만 가질 수 있는 배열을 만들 예정 (사이즈 못 바꿈)

  - size를 꼭 지정해야 함 = 고정 크기 (배열은 크기가 고정됨)

<br>

- 중괄호로 입력값을 넣을 경우
  - **int**[] yourNum = **new** **int** [] {5, 4, 3, 2, 1};
  - 5칸 배열이 자동으로 만들어짐

<br>

- 선언 초기화
  - String[] hello = {"have", "a", "nice", "day"};

<br>

- **import** java.util.Arrays;
  - 만들어져 있는 함수도 사용 가능
  - System.**out**.println(Arrays.*toString*(yourNum));
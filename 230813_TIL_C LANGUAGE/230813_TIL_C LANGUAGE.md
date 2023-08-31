### 배열

- 같은 크기의 기억 공간을 연속적으로 나열해둔 것
- 같은 자료형의 변수를 연속적으로 묶어 놓은 저장 공간
- 배열의 선언
  - int a [5] ;  이렇게 표현하면 a[0], a[1], a[2], a[3], a[4] 이렇게 5개 만들어짐

- 이차원 배열
- 같은 자료형의 변수를 행과 열의 연속적인 공간으로 묶어 놓은 것
  - int a [2] [3] ;



char msg[50] : 1글자 들어갈 공간을 0부터 49까지 50개 만든다



### 포인터

- 메모리의 위치를 표현한 기호
- int *a; 
  - a를 만들건데 이건 포인터 변수고 주소값을 가지고 있다
- *a = 10; 
  - a가 가지고 있는 주소의 값에 10을 넣어라

- printf("%d", a);
  - a가 가지고 있는 주소값을 출력해라 (102번지)
- printf("%d", *a);
  - a 값이 아니라 a가 가리키고 있는 102번지의 값을 출력해라(10)
- a = &b;
  - a에다가 b가 가지고 있는 주소 값을 넣어라



**#include<stdid.h>**

- 여러 함수들이 들어있기 때문에 이걸 선언하면 여러 함수 사용 가능



**scanf**

- 사용자의 키보드로 입력받을 때 사용하는 함수
- 형식 ) scanf("%d", 변수의주소);
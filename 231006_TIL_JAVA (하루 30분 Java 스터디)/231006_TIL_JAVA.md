## Java

- array : 같은 타입의 여러 개의 값을 효과적으로 관리하기 위한 객체
- ex) int [] [] a = new int [3] [2];

<br>

- 배열 만드는 방법

  ```java
  	public static void main(String[] args) {
  		// 방법 1
  		int [][] a = new int[3][2];
  		a[0][0] = 1;
  		a[0][1] = 2;
  		a[1][0] = 3;
  		a[1][1] = 4;
  		a[2][0] = 5;
  		a[2][1] = 6;
  		
  		a[1][0] = 9;
  
  		// 방법 2
  		int[][]b = new int[3][];
  		b[0] = new int[3];
  		b[1] = new int[5];
  		b[2] = new int[1];
  		
  		// 방법 3
  		int[][] c = new int[][] {{1, 2},{3,4,5},{6},{7,8,9,10}};
  	
  		// 방법 4
  		int[][] d = {{1,2,3,4},{5},{6,7},{8}};
  ```

  

<br>

- **얕은 값 복사 (ShallowCopy)**

  - 주소 값 복사 (같은 객체를 가리킴)

  - 똑같은 걸 같이 가리키게 됨
  - 같이 가리키고 있던 값이 변하면 같이 바뀜
  - hashCode : 객체의 주소값

- **깊은 값 복사 (DeepCopy)**
  - 객체 복사 (다른 객체가 만들어짐)
  - 새로 복사해서 하나 만들고 값을 복사해서 넣음
  - 카피한 배열의 값을 바꿔도 오리지널에 반영되지 않음

<br>

- **original clone**
  - 카피하고 값 복사해서 가져오는 과정을 다 만들어둔 것
  - 자동으로 다른 배열을 카피해줌

<br>

- **System class 사용**
  - System.arrayCopy(원본 배열 객체, 원본 시작 위치, 
    복사 배열 객체, 복사 시작 위치, 복사 갯수)
    - System.*arraycopy*(original, 0, copyThree, 1, 2);

<br>

- foreach / 향상된 fot문

  - people 안에 있는 값들을 하나씩 가져와서 person에 넣음

  - **for** (**var** person : people) {

    ​			System.out.println(person.age);
    }

## Java

- Collection (framework)
  - 여러개의 데이터를 효과적으로 관리하기 위한 객체

<br>

List	Set	Map

중복	O	X	(k:X, v:O)

순서	O	X	X

<br>

- Iterator : collection framework를 조회하는 공식적인 방법
- List<type>
- Set<type>
- Map <key, value>
- <> : generics (타입을 강제)

<br>

- Map.entrySet() -> entry들을 set으로 관리
- Map은 Key를 통해서 Value를 사용하자 (key를 모르면 value 사용 못함)
- Map.Entry 는 key와 value가 각각 사용 가능함
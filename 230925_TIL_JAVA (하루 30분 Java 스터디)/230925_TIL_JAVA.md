## Java

- type 변수 = 값;
- 기본 (primitive type)
  - 1바이트는 8비트로 구성
  - 정수 : byte(1), short(2), int(4), long(8)
  - 실수 : float(4), double(8)
  - 문자 : char
  - 문자열 : string (참조 타입이지만, 기본타입처럼 사용)
  - 논리 : boolean
- 참조(reference type, class type)
  - 모든 클래스
  - 배열

<br>

- 형변환 : 변환해주지 않으면 정수형의 기본은 int

<br>

- int
- fortran 언어에서 i ~ n 까지는 정수로 취급했던 것이 관습적으로 내려옴
- 물리/수학에선 iterator, index 등의 뜻으로 i 사용
- long인 경우 literal의 뒤에 l

<br>

- 0b : 2진수
  - System.**out**.println(0b10);

- 00 : 8진수
  - System.**out**.println(0010);

- 0x : 16진수
  - System.**out**.println(0x10);

<br>

- float인 경우 literal의 뒤에 f, F 붙임
- double : 이진수의 근사치 저장 (정확하지 않음)
  - 정확한 값은 BigDecimal 사용

<br>

- 홑따옴표('') : 문자(char)
- 쌍따옴표("") : 문자열(string)

<br>

- 기본 데이터 타입(primitive data types)	->	래퍼 클래스(wrapper classes) 
  - byte		->	Byte
  - short 	->	Short
  - int		->	Integer
  - long		->	Long
  - float		->	Float
  - double	->	Double
  - char		->	Character
  - boolean	->	Boolean

<br>

- byte의 범위 : -128 ~ 127

- short의 범위 : -32768 ~ 32767

- int의 범위 : -2147483648 ~ 2147483647

- long의 범위 : -9223372036854775808 ~ 9223372036854775807

- float의 범위 : 1.4E-45 ~ 3.4028235E38

- doulbe의 범위 : 4.9E-324 ~ 1.7976931348623157E308

- char의 크기 : 16

- boolean 참 : true
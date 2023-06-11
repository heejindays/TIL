# javascript (6/11)

## 기본 개념

- script
    - 소프트웨어에 실행시키는 처리 절차를 문자(텍스트)로 기술한 것

- script language
    - 응용 소프트웨어를 제어하는 언어

- 자바와 자바스크립트는 완전히 다른 언어

- 널널한 문법 + 좀 특이함

- html 및 css와의 비교

    - HTML : the Skeleton

    - CSS : the Skin

    - JAVASCRIPT : the Brain (논리 설계 가능) / 프로그래밍 언어

<br>


## 1) 변수

- 상자 안에 값을 담는 개념

- a = 1 : 1을 a에 넣는다

- a == 1 : a는 1과 같다

- var a = 1

- let a = 1
변수에 값을 넣는 일반적인 방식

<br>

## 2) 함수

```javascript
function myFunction(x) {
    let temp = 2*x +3
    return temp
}

myFunction()

function add(x,y) {
    let temp = x + y;
    return temp

}

add(1, 2)

((x,y) => {return x+y}) (1,2)

```

- 입력, 출력 없을 수 있음
- 함수 = 마법 = 코드 묶음

<br>

## 3) 조건문

- 만약 5,000원 이상 있으면 택시를 탄다

```javascript
if(money > 5000) {
    rideTaxi();
}
```
```javascript
let money = 6000
if(money > 5000){
    console.log("택시를 탄다")
}
```

- 돈이 5000원 이상 있으면 택시를 타고, 없으면 걷는다

```javascript
if (money > 5000) {
    rideTaxi(); 
    // 참일때의 조건
} else{
    walk();
    // 거짓일때의 조건
}
```

- 5000원 이상 있으면 택시를 타고

- 2000원 이상 있으면 버스를 타고

- 2000 미만으로 있으면 걷는다

```javascript
if(money > 5000) {
    rideTaxi();
} else if(money > 2000) {
    elseBus();
} else {
    walk();
}
```

<br>

## 4) 반복문

- 나무를 10번 찍는다

```javascript
for (let i=0; i < 10; i++>) {
    console.log("나무 찍기" + i)
}
```
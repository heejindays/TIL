## ORACLE

**DCL**

- transacrion : 최소한의 작업 단위
- commit : 현재까지의 작업을 database에 영구적으로 저장
- rollback : 가장 마지막 commit 부분으로 작업을 되돌림



**순서가 있는 값을 생성해주는 객체**
create sequence dcl_seq;



**예제 테이블 만들기**
create table table_dcl(
id number,
name varchar2(50)
);



**commit 해보기!**

insert into table_dcl values(dcl_seq.nextval, 'admin');
commit;



select * from table_dcl;

insert into table_dcl values(dcl_seq.nextval, 'hong-gd');
insert into table_dcl values(dcl_seq.nextval, 'kin-sd');
insert into table_dcl values(dcl_seq.nextval, 'hong-gd');

**롤백했어도 dcl_seq의 currval은 3임!**
**그래서 새롭게 행을 하나 추가해 보면 롤백을 했어도 2가 아니라 4가 됨!**



**function**

왼쪽 빈칸을 별표로 채워서 오른쪽 정렬처럼 만들기
select lpad(ename, 7, '*') from emp;

오른쪽 빈칸을 별표로 채워서 왼쪽 정렬처럼 만들기
select rpad(ename, 10, '*') from emp;



**LTRIM**
x이거나 y이거나 z면 왼쪽에서 지우겠다
안 지워지는 것을 만나면 거기서부터 다 출력함
select ltrim('xyxzyyTech6 327', 'xyz') from dual;
결과 : Tech6 327



**RTRIM**
오른쪽부터 숫자는 다 지우고
숫자가 아닌 것을 만나면 거기서부터 다 출력함
select rtrim('xyxzyyTech6 327', '0123456789') from dual;
결과 : xyxzyyTech6



**TRIM**
양쪽에서 x를 지워줌
x가 아닌 걸 만나면 그 이후로는 쭉 출력함
select trim ('x' from 'xyxzyyTech6 327xyxxzxxx') from dual;
결과 : yxzyyTech6 327xyxxz



**양 옆으로 여러개를 지울 수 있을까?**
ORA-30001: 트림 설정은 하나 문자만 가지고 있어야 합니다
select trim ('xyz' from 'xyxzyyTech6 327xyxxzxxx') from dual;
결과 : 에러 발생



**사원 테이블에서 사원 이름, 사원 이름의 앞 2글자를 출력해보자**
**그리고 사원 이름의 가장 마지막 글자를 출력하자**

**0부터 시작하든 1부터 시작하든 결과가 같음**

select ename, substr(ename,0,2), substr(ename,1,2), substr(ename, -1, 1)
from emp; 



**instr : 찾는 문자열의 위치를 알려줌**
index + str
select ename, instr(ename, 'S', 1, 1) from emp;
SMITH : 1
JAMES : 5



인덱스는 무조건 앞에서부터 셈
select ename, instr(ename, 'L', -1, 2) from emp;
ALLEN : 2
MILLER : 3



**length : 길이(개수)**
**lengthb : 바이트수**

select length('a'), lengthb('a'), length('ㄱ'), lengthb('ㄱ') from dual;

LENGTH('ㄱ') : 1
LENGTHB('ㄱ') : 3
utf-8 기준, 한글 3byte



**round : 반올림**
**trunc : 버림**
select round(123.456), round(123.456,1), trunc(123.456,1), trunc(123.456, -1) from dual;

ROUND(123.456) : 123
ROUND(123.456, 1) : 123.5
TRUNC(123.456,1) : 123.4
TRUNC(123.456,-1) : 120



**CEIL : 올림**
**FLOOR : 버림**
select ceil(123.456) from dual;
CEIL(123.456) : 124

select floor(123.456, 1) from dual;
ORA-00909: 인수의 개수가 부적합합니다
자리수를 지정할 수가 없음

select sal, ceil(sal/1000), floor(sal/1000) from emp;



**입사한 지 20년이 되는 달을 구하자**

**add_months : 개월수를 추가해 줌**
select ename, hiredate, add_months(hiredate, 240) from emp;



**00년 1월 1일을 기준으로 10년 이상 근무한 사람의 이름, 직업, 입사일, 근무년을 구하자**
**months_between (날짜1, 날짜2)**

select ename, job, hiredate, trunc(months_between('2000/01/01', hiredate)/12)
from emp
where months_between('2000/01/01', hiredate) > 120;

날짜 1 > 날짜 2 : 양수
날짜 1 < 날짜 2 : 음수



select 
months_between('2000/01/01', sysdate), 
months_between(sysdate, '2000/01/01')
from dual;

MONTHS_BETWEEN('2000/01/01',SYSDATE) : -283.88618
MONTHS_BETWEEN(SYSDATE,'2000/01/01') : 283.886179



**숫자를 문자로 바꾸기**

select 
to_char(1234, '99999'), 
to_char(1234, '00000'),
to_char(1234, 'L9999'), 
to_char(1234, '9,9999') 
from dual;



to_char(1234, '99999') : 1234
to_char(1234, '00000') : 01234
to_char(1234, 'L9999') : ￦1234
to_char(1234, '9,9999') : 1234



**날짜를 문자로 바꾸기**
**to_char(sysdate)**
**date형 타입을 문자로 변환**

select 
to_char(sysdate, 'hh24:mi:ss'),
to_char(sysdate, 'mon dy, yyyy'),
to_char(sysdate, 'yyyy-fmmm-dd day'),
to_char(sysdate, 'yyyy-mm-dd'),
to_char(sysdate, 'year, q')
from dual;

11:26:46
8월  월, 2023
2023-8-28 월요일
2023-08-28
twenty twenty-three, 3


select to_date('20200101', 'yyyymmdd') from dual;
20/01/01

select to_char(to_date('20100101', 'yyyymmdd'), 'yyyy, mon') from dual;
결과 : 2010, 1월



**to_number**
**문자 타입을 숫자 타입으로 바꾸기**
**사원의 이름과 입사한 년도, 입사한 월을 출력하자** 
**(+1을 써서 숫자인지 확인)**

select
ename,
hiredate,
to_number(substr(hiredate, 1, 2)) + 1,
to_number(substr(hiredate, 4, 2)) +1
from emp;

**decode (칼럼이나 문자열, 비교값, 같을 때 반환값)**
select ename, job, decode(job, 'MANAGER', '0') from emp;



**job이 PRESIDENT면 P / MANEGER면 0 / 이외에는 1 출력**

select ename, job, decode(job, 'PRESIDENT', 'P', 'MANAGER', '0', '1')
from emp;



위와 같은 코드 내용
select ename, job, 
case when job = 'PRESIDENT' then 'P' 
when job = 'MANAGER' then '0' 
else '1' end
from emp;




select count(*) from emp;
select count(comm), count(nvl(comm,0)) from emp;

nvl이 아니면 0으로 바꿔서 리턴해라



COUNT(COMM) : 4
COUNT(NVL(COMM,0)) : 14



**연산에서 null은 제외됨**
**집계 함수에 조건문을 사용할 경우 where 대신에 having 사용**



select comm, nvl(comm, -1) from emp;

최대 / 최소 / 합계 / 평균
select max(sal), min(sal), sum(sal), avg(sal) from emp;




select a, b, 집계 함수

from 테이블
group by rollup (a, b);

select job, deptno, avg(sal)
from emp
group by rollup(job, deptno);



**ROWID / ROWNUM : 식별자로 사용 (수정 불가)**

create table rowtest(
no number
);



insert into rowtest values(111);
insert into rowtest values(222);
insert into rowtest values(333);



select * from rowtest;



select no, rowid, rownum from rowtest;



ROWID에는 각각 다른 값이 들어감
ROWNUM에도 1, 2, 3 숫자가 들어감



삭제하면 ROWID는 기존에 붙인 것과 같게 나옴
반면 ROWNUM은 행을 삭제하면 달라짐
no333인 것이 ROWNUM이 2가 됨
delete from rowtest where no=222;



**Top n Query**

select ename, sal, rownum
from emp
order by sal desc;



**ROWNUM 순서대로 정렬하고 싶을 때 서브쿼리 사용**
select ename, sal, rownum
from 
(select ename, sal 
from emp
order by sal desc);



**급여가 가장 높은 상위 3명을 출력하고 싶을 때**
select ename, sal, rownum
from 
(select ename, sal 
from emp
order by sal desc)
where rownum < 4;



select ename, sal, rownum
from 
(select ename, sal 
from emp
order by sal desc)
where rownum >=3 and rownum <=5;
에러 : 선택된 레코드가 없습니다.



**rownum는 갯수니까 and를 기준으로**
**앞 뒤로 나눠서 생각해보면 논리적으로 맞지 않음**



**'as rn'으로 별칭을 주면** 
**가상테이블의 컬럼이 되어서 사용 가능**

select *
from
(select ename, sal, rownum as rn
from
(select ename, sal
from emp
order by sal desc))
where rn >= 3 and rn <= 5;

**위 내용으로 쿼리를 짜면** 
**급여 3위에서 5위까지 추릴 수 있음**



**RANK vs DENSE RANK**

select ename, sal,
rank() over (order by sal desc) as rank,
dense_rank() over (order by sal desc) as dense,
row_number() over (order by sal desc) as rownb
from emp;



**rank() : 등수가 같으면 누적**
**dense_rank() : 등수가 같으면 그 다음 숫자**
**row_number() : 같은 등수여도 다르게 나옴**



**JONES보다 더 많은 월급을 받는 사원의 이름과 월급을 출력하자**



**1) JONES가 얼마 받는지 알아보자**
select sal
from emp
where ename = 'JONES';

**2) 그보다 더 많이 받는 사람들을 알아보자**
select * 
from emp
where sal >
(select sal
from emp
where ename = 'JONES');



**부하직원이 없는 사원의**
**사원번호와 이름을 출력하자**

**부하직원이 없다 = mgr 컬럼에 내 empno가 없다**

select * 
from emp
where empno not in
(select nvl(mgr,0) from emp);



**직업이 SALESMAN인 사원과 같은 부서에서 근무하고**
**직업이 SALESMAN인 사원과 같은 월급을 받는 사원들의**
**이름, 월급, 부서번호를 출력하자**

select *
from emp
where
deptno in (select deptno from emp where job = 'SALESMAN')
and
sal in (select sal from emp where job = 'SALESMAN');



**위 쿼리에서 겹치는 부분을 중복해서 쓰지 않으려면?**

select *
from emp
where (deptno, sal) 
in (select deptno, sal from emp where job = 'SALESMAN');



**사원테이블과 부서테이블을 join**

select *
from emp join dept on emp.deptno = dept.deptno;



**academy 테이블 만들고 값 넣기**
create table academy(
id number,
class varchar2(5)
);

insert into academy values(1, 'de');
insert into academy values(2, 'ds');
insert into academy values(3, 'web');
insert into academy values(4, 'cloud');

select * from academy;



**student 테이블 만들고 값 넣기**
create table student(
id number,
name varchar2(10),
class char(2)
);

insert into student values(1, 'hong-gd', 'de');
insert into student values(1, 'kim-sd', 'ds');
insert into student(id, name) values(3, 'lee-ss');

select * from student;



**cross join**

모든 경우의 수를 다 join

select * from academy cross join student;



**outer join**

select * from academy left outer join student using (class);



select * from academy, student where academy.class = student.class(+);

left outer join의 경우, 오른쪽 테이블.컬럼에 (+)를 붙인다



select * from academy right outer join student using(class);

select * from academy, student where academy.class(+) = student.class;

select * from academy full outer join student using(class);



select ename, sal, grade from emp join salgrade on (sal between losal and hisal);

select ename, sal, grade from emp, salgrade where sal between losal and hisal;
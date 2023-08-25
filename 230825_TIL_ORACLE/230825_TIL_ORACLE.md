## ORACLE

- DDL : create alter drop

- DML : select insert update delete

- DCL : grant revoke commit rollback

- TCL : (commit rollback)



**테이블 만들기(기본)**

create
create table student(
	name varchar2(100),
	age number,
	addr varchar2(2000)
);



**테이블 세부 정보 보기**

desc student;



**alter** 

alter table student add (phone varchar2(13));

alter table student modify (name varchar2(50));

alter table student drop column age;



**drop**

drop table student;



**sequence : (mysql) auto_increment / (postgresql) serial**

create sequence sequence_test;

select sequence_test.nextval from dual;
select sequence_test.nextval from dual;
select sequence_test.nextval from dual;



**현재 올라간 값을 알려줌**

select sequence_test.currval from dual;
select sequence_test.currval from dual;
select sequence_test.currval from dual;

**dual : 가상 임시 테이블**



**where 1 = 2;**
**조건을 False로 만들어서, 데이터의 출력을 0개로 만든다.**


select * from emp where 1=2;

constraint / not null
create table table_notnull01(
	id char(3) not null,
	name varchar2(20)
);



**not null 이면 꼭 값이 있어야 함**

insert into table_notnull01 values('111', 'oracle');
insert into table_notnull01 values('222', 'mongo');
insert into table_notnull01(name) values('postgre');
--ORA-01400: NULL을 ("C##MULTI"."TABLE_NOTNULL01"."ID") 안에 삽입할 수 없습니다



**unique**

create table table_unique01(
	id char(3) unique,
	name varchar2(20)
);



insert into table_unique01 values('111', 'oracle');
insert into table_unique01 values('112', 'mongo');
insert into table_unique01 values('112', 'postgre');
--ORA-00001: 무결성 제약 조건(C##MULTI.SYS_C008318)에 위배됩니다



**테이블 레벨에서 not null 제약조건을 걸면 안됨**

create table table_unique02(
	id char(3),
	name varchar2(20),
	constraint tu02_id_unq unique (id)
);



**제약 조건 이름을 지정할 수 있음**

insert into table_unique02 values('111', 'oracle');
insert into table_unique02 values('112', 'mongo');
insert into table_unique02 values('112', 'postgre');
--ORA-00001: 무결성 제약 조건(C##MULTI.TU02_ID_UNQ)에 위배됩니다



**unique(id, name) 세트로만 유니크하게**

create table table_unique03(
	id char(3),
	name varchar2(20),
	constraint tu03_id_nm_unq unique(id, name)
);

insert into table_unique03 values('111', 'oracle');
insert into table_unique03 values('112', 'mongo');
insert into table_unique03 values('112', 'postgre');
insert into table_unique03 values('112', 'postgre');
--ORA-00001: 무결성 제약 조건(C##MULTI.TU03_ID_NM_UNQ)에 위배됩니다

**id와 name이 쌍으로 unique 제약조건에 걸림**



**primary key : unique + not null > 식별자**



**id가 pk인 상황**

create table table_pk01(
	id char(3) primary key,
	name varchar2(20)
);

insert into table_pk01 values('111', 'oracle');
insert into table_pk01 values('112', 'mongo');
insert into table_pk01 values('112', 'postgre');
--ORA-00001: 무결성 제약 조건(C##MULTI.SYS_C008321)에 위배됩니다
insert into table_pk01 values(null, 'mysql');
--ORA-01400: NULL을 ("C##MULTI"."TABLE_PK01"."ID") 안에 삽입할 수 없습니다



create table table_pk02(
	id char(3),
	name varchar2(20),
	constraint tp02_id_pk primary key (id)
);

insert into table_pk02 values('111', 'oracle');
insert into table_pk02 values('112', 'mongo');
insert into table_pk02 values('112', 'postgre');
--ORA-00001: 무결성 제약 조건(C##MULTI.TP02_ID_PK)에 위배됩니다
insert into table_pk02 values(null, 'mysql');
--ORA-01400: NULL을 ("C##MULTI"."TABLE_PK02"."ID") 안에 삽입할 수 없습니다



create table table_pk03(
	id char(3),
	name varchar2(20),
	constraint tu03_id_name_pk primary key (id, name)
);

insert into table_pk03 values('111', 'oracle');
insert into table_pk03 values('112', 'mongo');
insert into table_pk03 values('112', 'postgre');
insert into table_pk03 values(null, 'mysql');
--ORA-01400: NULL을 ("C##MULTI"."TABLE_PK03"."ID") 안에 삽입할 수 없습니다



**foreign key**

**참조 제약조건 (references)**

create table table_fk01(
	id char(3),
	name varchar2(20),
	pkid char(3) references table_pk01(id)
);

insert into table_fk01 values('111', 'oracle', '111');
insert into table_fk01 values('112', 'mongo', '112');
insert into table_fk01 values('112', 'postgre', '112');
insert into table_fk01 values(null, 'mysql', null);

select * from table_pk01;



insert into table_fk01 values('113', 'mysql', '113');
--ORA-02291: 무결성 제약조건(C##MULTI.SYS_C008324)이 위배되었습니다- 부모 키가 없습니다




create table table_fk02(
	id char(3),
	name varchar2(20),
	pkid char(3),
	constraint tf02_pkid_fk foreign key (pkid) references table_pk02(id)
);

insert into table_fk02 values('111', 'oracle', '111');
insert into table_fk02 values('112', 'mongo', '112');
insert into table_fk02 values('112', 'mysql', '112');
insert into table_fk02 values(null, 'mysql', null);

insert into table_fk02 values('113', 'oracle', '113');
--ORA-02291: 무결성 제약조건(C##MULTI.TF02_PKID_FK)이 위배되었습니다- 부모 키가 없습니다



**check 제약 조건** **/ 대소문자를 구분함**

create table table_check01(
	id char(3),
	name varchar2(20),
	marriage char(1) check (marriage in ('y', 'n'))
);

insert into table_check01 values('111', 'oracle', 'y');
insert into table_check01 values('112', 'mongo', 'n');
insert into table_check01 values('113', 'postgre', 'Y');
-- ORA-02290: 체크 제약조건(C##MULTI.SYS_C008326)이 위배되었습니다



create table table_check02(
	id char(3),
	name varchar2(20),
	marriage char(1),
	constraint tc02_mg_ck check (marriage in ('y', 'n'))
);

insert into table_check02 values('111', 'oracle', 'y');
insert into table_check02 values('112', 'mongo', 'n');
insert into table_check02 values('113', 'postgre', 'Y');
-- ORA-02290: 체크 제약조건(C##MULTI.TC02_MG_CK)이 위배되었습니다



DML
emp 테이블의 모든 컬럼과 모든 데이터를 출력하자.
select * from emp;



`SET LINESIZE`: 한 행에 출력되는 문자의 최대 수를 지정

이를 통해 텍스트가 화면에 보다 잘 맞도록 조절



`SET PAGESIZE`: 출력 결과를 페이지 단위로 나눌 때 각 페이지에 출력되는 행 수를 지정

 

set linesize 120;

각 행에 최대 120개의 문자를 출력



set pagesize 20;

한 페이지에 20개의 행을 출력



**job이 'SALESMAN' 인 사원들의 모든 정보를 출력**
select *
from emp
where job='SALESMAN';



**select에 컬럼명 다 써주는 것이 좋은 경우도 있음**

select empno, ename, job, mgr, hiredate, sal, comm, deptno
from emp
where job='SALESMAN';



**sal (월급)이 1500 이상 인 사원들의 사원번호와 이름과 직업과 월급을 출력하자.**
select empno, ename, job, sal
from emp
where sal >= 1500;



**job이 SALESMAN 이고 월급이 1500 이상인 사원들의 전체 정보를 출력**
select *
from emp
where job = 'SALESMAN'
	and sal >= 1500;



**월급을 많이 받는 사람부터 출력**
select *
from emp
order by sal desc;



**부서별 인원을 출력 (부서번호 - deptno)**
select deptno, count(*), ename
from emp
group by deptno
order by 1;
-- ORA-00979: GROUP BY 표현식이 아닙니다.



**부서별 월급 평균 출력**
select deptno, avg(sal)
from emp
group by deptno;



**10번 부서를 제외한 부서별 월급 평균 출력**
select deptno, avg(sal)
from emp
where deptno != 10
group by deptno;



**<> : 같지 않다(제외한다)**

select deptno, avg(sal)
from emp
where deptno <> 10
group by deptno;



**월급 평균이 2000 이상인 부서별 월급 평균 출력**
**집계 함수에 조건을 걸 때는 where 대신 having**

select deptno, avg(sal)
from emp
group by deptno
having avg(sal) >= 2000;



**합집합 (중복 제거)**
select deptno from dept 
union 
select deptno from emp;



**합집합 (중복 허용)**
select deptno from dept 
union all
select deptno from emp;



**교집합**
select deptno from dept
intersect
select deptno from emp;



**차집합**
select deptno from dept
minus
select deptno from emp;



**현재 날짜 확인**
select sysdate from dual;



**insert**
insert into emp values(7777, 'hong-gd', 'ANALYST', null, sysdate, 4000, null, null);


insert into emp(empno, ename, sal) values (7778, 'kim-sd', 3500);



**update**
update emp 
set sal=4000
where ename='kim-sd';



**delete**
delete from emp 
where sal = 4000;
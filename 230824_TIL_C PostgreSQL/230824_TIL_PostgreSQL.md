## PostgreSQL

**2019년 8월 24일에 사용 내역**

select usedate, amount, main_cate, sub_cate, store
from card
where usedate = '2019-08-24';



**2019년 전체 사용 내역**

select *
from card
where usedate >= '2019-01-01' and usedate <= '2019-12-31';



select *
from card
where usedate between '2019/01/01' and '2019/12/31';



**금액이 가장 큰 값부터 10개만**

select *
from card
order by amount desc
limit 10;



**대분류가 쇼핑인 데이터의 갯수**

select main_cate, count(*)
from card
where main_cate='쇼핑'
group by main_cate;



**대분류의 데이터 개수가 100개 이상인 대분류와 갯수 출력**

**단, 갯수가 높은 순으로 출력**

select main_cate, count(*)
from card
group by main_cate
having count(*) >= 100
order by 2 desc;



**distinct**

select distinct main_cate
from card;



**like**

select distinct store
from card
where store like '%커피%';



**like : 대소문자 구분 없이 검색**



**split_part**

select
	split_part(usedate::varchar, '-', 1),
	split_part(usedate::varchar, '-', 2),
	split_part(usedate::varchar, '-', 3),
	usedate
from card
limit 10;



**2019년도 사용 내역**

select *
from card
where split_part(usedate::varchar, '-', 1) = '2019';



**년도별 금액 총 합**

select split_part(usedate::varchar, '-', 1), sum(amount)
from card
group by split_part(usedate::varchar, '-', 1)
order by 1;



**rank, dense_rank**

select main_cate, sub_cate,
	rank() over (order by amount desc),
	dense_rank() over (order by amount desc),
	amount
from card
where main_cate = '문화'
limit 10;



**partition by**

select store, amount,
rank() over (partition by store order by amount desc)
from card
where sub_cate = '치킨';
emp dept
select *
from emp join dept on emp.deptno = dept.deptno;
select *
from emp join dept using(deptno);



**outer**

select *
from emp left join dept using(deptno);

select *
from emp right join dept using(deptno);

select *
from emp full outer join dept using(deptno);



**cross join**

select * from emp cross join dept;



### 문제 스스로 만들고 풀어보기!

1. **MANAGER인 직원들의 평균 급여는 얼마일까?**
    select avg(sal) 
    from emp
    where job = 'MANAGER';
****



2. **부서별로 직원 수가 몇 명일까?**
    select deptno, count(empno)
    from emp
    group by deptno;



3. **매니저별 관리하는 직원 수가 몇 명일까?**
    select mgr, count(empno)
    from emp
    group by mgr;



4. **년도 상관 없이 2월에 입사한 직원들의 정보는?**
    select * 
    from emp 
    where split_part(hiredate::varchar,'-',2) = '02';



5. **가장 연봉이 높은 사람과 가장 낮은 사람의 금액은 얼마일까?**
    select max(sal), min(sal)
    from emp;

  


6. **부서번호가 30인 직원들의 평균 급여는 얼마일까?**
    select avg(sal)
    from emp
    where deptno = 30;

  


7. **부서 번호별 평균 급여가 높은 순으로 정렬하면?**
    select deptno, round(avg(sal),2) as avg_sal 
    from emp 
    group by deptno 
    order by avg_sal desc;

  


8. **매니저(manager)가 없는 사람의 이름은?**
    select ename
    from emp
    where mgr is null;

  


9. **job이 CLERK인 사람들을 골라서 그 사람들의 정보를 연봉 순으로 정렬하면?**
    select *
    from emp
    where job = 'CLERK'
    order by sal desc;

  


10. **커미션(comm)을 받은 사람들의 이름을 입사날짜가 빠른 순으로 정렬하면?**
    select ename
    from emp
    where comm is not null
    order by hiredate asc;

    


11. **KING 보다 먼저 입사한 사람들의 이름을 입사날짜가 빠른 순으로 정렬하면?**
    select ename
    from emp
    where hiredate < (select hiredate
    from emp
    where ename = 'KING');

    


12. **직원 이름이 가장 짧은 사람부터 긴 사람 순서로 나열하면?**
    **(이름 알파벳 수가 같으면 오름차순)**
    select ename
    from emp
    order by length(ename), ename asc;

    


13. **급여가 제일 높은 직원이랑 제일 낮은 직원의 차이는 얼마인가?**
select max(sal) - min(sal)
from emp;
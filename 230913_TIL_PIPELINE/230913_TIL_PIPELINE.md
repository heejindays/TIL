## PIPELINE

- sudo service mysql status 
  - active (running) 인 상태
- sudo mysql -u root
- use mysql;

- AWS로 할 때 비밀번호 설정할 때 쉽게 설정하면 안 됨!

<br>

- **비밀번호 바꾸기**
  - alter user 'root'@'localhost' identified with mysql_native_password by '**';
- **어디서든 관리자 계정 접근**
  - create user 'root'@'%' identified by '**';
- **권한**
  - grant all privileges on *.* to 'root'@'%' with grant option;
  - grant all privileges on *.* to 'root'@'localhost' with grant option;

<br>

- **테스트 테이블 만들기** 
  - flush privileges;
  - create table test(id int, name varchar(30));
  - insert into test values(1, "hadoop");
  - insert into test values(2, "spark");
  - select * from test;

<br>

- **Connector/J 8.1.0 다운로드**
  - wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j_8.1.0-1ubuntu22.04_all.deb
  - sudo dpkg -i mysql-connector-j_8.1.0-1ubuntu22.04_all.deb
  - cd /usr/share/java
  - ls
  - /urs/share/java/mysql-connector-j-8.1.0.jar 로 경로가 만들어져 있는 상황

<br>

​	**vim spark-defaults.conf 설정하기**

- cd $SPARK_HOME/conf
  - vim spark-defaults.conf
    - spark.jars        /urs/share/java/mysql-connector-j-8.1.0.jar

<br>

- **파이스파크 실행하기**
  - cd
  - start-all.sh
  - jps
  - hdfs dfsadmin -report
  - pyspark

<br>

- user="root"
- password="**"
- url="jdbc:mysql://localhost:3306/mysql"
- driver="com.mysql.cj.jdbc.Driver"
  - jdbc : java + database + connection
- dbtable="test"
- test_df 에 넣기 (아래 두 코드는 스타일만 다르고 내용은 같음)
  - test_df = spark.read.format("jdbc").option("user",user).option("password",password).option("url", url).option("driver",driver).option("dbtable",dbtable).load()
  - test_df = spark.read.format("jdbc").options(user=user, password=password, url=url, driver=driver, dbtable=dbtable).load()

- test_df.show()
  - +---+------+
    | id|  name|
    +---+------+
    |  1|hadoop|
    |  2| spark|
    +---+------+

<br>

- **테이블에 추가하기**
  - test_insert = [(3, "mysql"), (4, "zeppelin")]
  - insert_df = sc.parallelize(test_insert).toDF(["id", "name"])
  - insert_df.show()
    - +---+--------+
      | id|    name|
      +---+--------+
      |  3|   mysql|
      |  4|zeppelin|
      +---+--------+

<br>

- **추가한 내용을 저장하기 (append)**
  - insert_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user":user, "password":password})
  - test_df.show()
  - 원래 테이블에는 1, 2만 들어있었는데 3, 4를 추가함
  - mysql에서 가져온 데이터 테이블이랑 같은 형식으로 추가해서 저장함
  - exit() 로 나간 뒤 mysql에서 확인해보자

<br>

- **mysql로 들어가서 테이블 다시 확인하기**
  - mysql -u root -p
  - use mysql;
  - select * from test;
    - +------+----------+
      | id   | name     |
      +------+----------+
      |    1 | hadoop   |
      |    2 | spark    |
      |    3 | mysql    |
      |    4 | zeppelin |
      +------+----------+
  - exit; 
    - mysql에서도 테이블 잘 합쳐져 있는지 확인 후 종료

## SPARK

- **json 파일 가져오기**
  - json_file = spark.read.format("json").load("data/card_data/json/202010.json")
  - json_file.printSchema()
    - root
       |-- list: array (nullable = true)
       |    |-- element: struct (containsNull = true)
       |    |    |-- 결제일: string (nullable = true)
       |    |    |-- 금액: string (nullable = true)
       |    |    |-- 대분류: string (nullable = true)
       |    |    |-- 소분류: string (nullable = true)
       |    |    |-- 이용일: string (nullable = true)
       |    |    |-- 중분류: string (nullable = true)
       |    |    |-- 포인트리금액: string (nullable = true)
  - json_file.show()
    - +-------------------------+
      |                     list|
      +-------------------------+
      |[{, 2990, 생활, 웰빙마...|
      +-------------------------+
  - from pyspark.sql.functions import explode, col
  - json_temp = json_file.select(explode(col("list")).alias("temp"))
  - json_temp.printSchema()
    - root
       |-- **temp: struct (nullable = true)**
       |    |-- 결제일: string (nullable = true)
       |    |-- 금액: string (nullable = true)
       |    |-- 대분류: string (nullable = true)
       |    |-- 소분류: string (nullable = true)
       |    |-- 이용일: string (nullable = true)
       |    |-- 중분류: string (nullable = true)
       |    |-- 포인트리금액: string (nullable = true)
  - json_temp.show()
    - 한 줄씩 json 으로 묶여진 걸 temp로 모아서 만듦
  - json_df = json_temp.select("temp.*")
  - json_df.printSchema()
  - json_df.show()
    - +------+-----+------+----------+--------+------+------------+
      |결제일| 금액|대분류|    소분류|  이용일|중분류|포인트리금액|
      +------+-----+------+----------+--------+------+------------+
      |      | 2990|  생활|  웰빙마트|20201001|  마트|            |
      |      |17100|  식사|카페부부스|20201002|  카페|            |
      |      |18000|  식사|          |20201002|  구이|            |
      |      | 2990|  생활|  웰빙마트|20201003|  마트|            |
      |      |21900|  식사|          |20201003|  족발|            |
      |      | 4100|  생활|        CU|20201005|편의점|            |
      |      | 1500|  식사| 카페7그램|20201005|  카페|          15|
      |      | 7000|  유흥|          |20201005|    술|            |
      |      | 1900|  생활|        CU|20201006|편의점|            |
      |      | 8700|  생활|        CU|20201006|편의점|            |
      |      | 7000|  식사|          |20201006|  한식|            |
      |      | 1500|  식사| 카페7그램|20201006|  카페|          15|
      |      | 8500|  식사|          |20201007|돈까스|          60|
      |      |14000|  식사|          |20201007|  순대|            |
      |      | 3000|  생활|        CU|20201007|편의점|            |
      |      | 7250|  식사|          |20201007|디저트|            |
      |      | 2900|  생활|        CU|20201008|편의점|            |
      |      |16000|  식사|          |20201008|  한식|            |
      |      | 1500|  식사| 카페7그램|20201008|  카페|          15|
      |      |40900|  교통|          |20201009|  택시|            |
      +------+-----+------+----------+--------+------+------------+

<br>

- **json 파일로 저장하고 다시 열어보기**
  - json_df.write.format("json").mode("overwrite").save("/json")
  - exit()
  - hdfs dfs -ls /json/
    - -rw-r--r--   1 ubuntu supergroup          0 2023-09-11 09:15 /json/_SUCCESS
      -rw-r--r--   1 ubuntu supergroup      15175 2023-09-11 09:15 /json/part-00000-9a74c1ac-2e37-4cbe-8541-5cda8110986a-c000.json
  - hdfs dfs -cat /json/part-*.json
    - {}{}{}{}.json 확장자가 json으로 되어있지만 json이 아님
    - {} 이 한 줄 한 줄이 json이기 때문에
    - {"결제일":"","금액":"8000","대분류":"식사","소분류":"","이용일":"20201030","중분류":"한식","포인트리금액":""}
      {"결제일":"","금액":"1900","대분류":"생활","소분류":"CU","이용일":"20201030","중분류":"편의점","포인트리금액":""}
      {"결제일":"","금액":"5600","대분류":"생활","소분류":"CU","이용일":"20201030","중분류":"편의점","포인트리금액":""}
      {"결제일":"","금액":"9000","대분류":"식사","소분류":"","이용일":"20201030","중분류":"디저트","포인트리금액":""}

<br>

- rdd 를 쓰려면 from pyspark import SparkContext
- sc = SparkContext

<br>

- cat spark_app.py

- from pyspark.sql import SparkSession

  if __name__ == '__main__':

  `#sparkSession 생성

  ​    spark = SparkSession.builder.master("local").appName("myCount").getOrCreate()

  `#1 ~ 1000까지 모두 더하는 프로그램

  ​    print("\n**********\n", spark.range(1,1001).selectExpr("sum(id)").collect(), "\n**********\n")

<br>

- 우리가 만들어둔 파일이 파이썬 파일이니까 python spark_app.py로 하면 실행이 되어야 함
- 그런데 지금 pyspark 모듈을 실행하지 않았으니까 실행이 안 됨
- pip install pyspark==${SPARK_VERSION}
- **반드시 spark 버전과 pyspark는 동일한 버전을 사용해야 함**

<br>

- **스파크 버전 낮추기 (3.2.4로 변경)**

- wget https://dlcdn.apache.org/spark/spark-3.2.4/spark-3.2.4-bin-without-hadoop.tgz
- tar xvzf spark-3.2.4-bin-without-hadoop.tgz
- ln -s spark-3.2.4-bin-without-hadoop spark
  - 이렇게만 설정하면 계속 예전 높은 버전으로 되어있음
  - spark-3.4.1-bin-without-hadoop
- ls -l 으로 심볼릭 링크 확인
  - ln -nfs spark-3.2.4-bin-without-hadoop spark
  - spark-3.2.4-bin-without-hadoop로 변경됨
  - 바로가기를 변경해야 함

<br>

- cd $SPARK_HOME/conf
- ls
- spark-3.2.4 conf 버전을 살펴보면 ?
  - 바로가기가 바뀌어서 기존에 작업한 것들이 없어짐
  - 바로가기(즐겨찾기)를 잘 설정해둬야 하는 이유
- cp workers.template workers
  - workers 템플릿을 복사해서 붙여 넣음
- cp spark-env.sh.template spark-env.sh
  - spark-env 템플릿을 복사해서 붙여 넣음

<br>

- **vim spark-env.sh 설정하기**
  - export JAVA_HOME=/home/ubuntu/java
  - export HADOOP_CONF_DIR=/home/ubuntu/hadoop/etc/hadoop
  - export YARN_CONF_DIR=/home/ubuntu/hadoop/etc/hadoop
  - export SPARK_DIST_CLASSPATH=$(/home/ubuntu/hadoop/bin/hadoop classpath)
  - export PYSPARK_PYTHON=/usr/bin/python3
  - export PYSPARK_DRIVER_PYTHON=/usr/bin/python3

<br>

- vim spark-defaults.conf 설정하기
- cp spark-defaults.conf.template spark-defaults.conf
- vim spark-defaults.conf
  - spark.master	yarn

<br>

- **재플린**
  - 대화형 웹 인터페이스를 통한 협업 도구
  - 데이터를 시각화하고 분석하며, 협업하고 문서화하는 데 사용됨
  - 주피터 노트북과 유사한 대화형 환경에서 코드를 작성하고 실행
  - Spark, Python, SQL, R, 그리고 기타 데이터 처리 및 분석 도구와 통합
  - 다양한 시각화 라이브러리를 지원
  - 여러 사용자가 실시간으로 공동 작업하고 결과를 공유
  - 데이터베이스, 클라우드 스토리지, 분산 파일 시스템 등을 지원
  - 보안 및 접근 제어 기능을 포함함

<br>

- **재플린 설치하기**
  - wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-netinst.tgz
  - tar xvzf zeppelin-0.10.1-bin-netinst.tgz
  - ln -s zeppelin-0.10.1-bin-netinst/ zeppelin
  - ls -l (파일 확인)

<br>

- **sudo vim ~/.bashrc 설정하기**
  - export ZEPPELIN_HOME=/home/ubuntu/zeppelin
  - export PATH=$PATH:$ZEPPELIN_HOME/bin

- source ~/.bashrc

<br>

- **vim zeppelin-env.sh 설정하기**
  - cd $ZEPPELIN_HOME/conf
  - ls
  - cp zeppelin-env.sh.template zeppelin-env.sh
  - vim zeppelin-env.sh
  - 19번째 라인 주석 해제 : export JAVA_HOME=/home/ubuntu/java
  - 79번째 라인 : export SPARK_HOME=/home/ubuntu/spark
  - 89번째 라인 : export HADOOP_CONF_DIR=/home/ubuntu/hadoop/etc/hadoop

<br>

- **vim zeppelin-site.xml 설정하기**

  - cp zeppelin-site.xml.template zeppelin-site.xml

  - vim zeppelin-site.xml

  - 0.0.0.0 = 모든 ip

    <property>
      <name>zeppelin.server.addr</name>
      <value>0.0.0.0</value>
      <description>Server binding address</description>
    </property>

  - 8080 : http port (web)

    - 8080을 8987 포트로 바꿈 (비어있는 포트)

<br>

- **재플린 실행 후 웹에서 설정하기**
  - zeppelin-daemon.sh start
    - 잘 실행되면 아래와 같은 메시지 나옴
    - Zeppelin start                                             [  OK  ]
  - Zeppelin을 웹 페이지에서 보려면?
    - IP주소 : 8987
  - anonymous > Interpreters > spark 검색 > edit
    - 아래 설정들을 확인 후 수정해야 사용 가능
    - %spark, %sql, %pyspark, %ipyspark, %r, %ir, %shiny, %kotlin
    - spark.master : yarn으로 변경
    - spark.submit.deployMode : client로 변경
    - PYSPARK_PYTHON : python3
    - PYSPARK_DRIVER_PYTHON : python3
    - **설정을 변경한 다음엔 변동 사항 꼭 save 해야 함!**
    - Create New Note로 새로 만들기

<br>

- **새로운 재플린 파일에 테스트 파일 만들기**
  - %pyspark
  - test = [1, 2, 3, 4, 5]
  - test_rdd = sc.parallelize(test)
  - test_rdd.collect()

<br>

- **재플린 종료하기**
  - zeppelin-daemon.sh stop

<br>

- **전체 파이프라인 만들기**
  - 파이프라인(pipeline)이라는 가상머신을 새로 만들어서
  - hadoop > spark > zeppelin > mysql > mongodb
  - 재플린에서 연결할 예정
  - airflow로 나중에 추가

<br>

- **airflow**
  - 데이터 파이프라인을 자동화하고 관리하기 위한 오픈 소스 플랫폼
  - 파이썬 코딩으로 조작 가능
  - 워크플로우 작성 및 실행, 작업 스케줄링, 모니터링, 오류 처리, 재시도 및 병렬 처리를 해줌

<br>

- **Elasticsearch**
  - 검색 및 분석을 위한 오픈 소스 분산 검색 엔진
  - 색인된 데이터에 대한 실시간 검색을 지원
  - ELK 스택 (Elasticsearch, Logstash, Kibana)와 함께 사용
  - 로그 및 이벤트 데이터를 수집, 분석 및 시각화
  - Kibana : 데이터 시각화와 대시보드 작성

<br>

- **card 데이터를 재플린 노트북에서 확인해보기**
  - %pyspark
    card = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("data/card_data/csv/202010.csv")
  - %pyspark
    card.printSchema()
  - %pyspark
    card.createOrReplaceTempView("card")
  - %sql
    select * from card

<br>

- **lang 설치**
  - wget https://dlcdn.apache.org//commons/lang/binaries/commons-lang-2.6-bin.tar.gz
  - tar xvzf commons-lang-2.6-bin.tar.gz
  - cd commons-lang-2.6/
  - ls
  - cp commons-lang-2.6.jar $SPARK_HOME/jars/
  - cd $SPARK_HOME/jars
  - ls | grep commons
    - commons-lang-2.6.jar
    - commons-lang3-3.12.0.jar
    - 두개 들어가있는 걸 확인

<br>

- **재플린 노트북 다시 실행하기**
  - zeppelin-daemon.sh restart

<br>

- **mysql 설치하기**
  - sudo apt install mysql-server -y
  - sudo service mysql start
  - sudo systemctl enable mysql
  - sudo service mysql status
    - Active: active (running)로 되어있는지 확인
    - 이렇게 되어있어야 mysql이 실행중인 상태
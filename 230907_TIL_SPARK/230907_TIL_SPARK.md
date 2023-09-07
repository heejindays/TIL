## SPARK

- 스파크 실행하면 나오는 메시지 의미
  - Spark context available as 'sc' 	# rdd
  - SparkSession available as 'spark'    # dataframe
  - master = yarn    # spark 작업을 hadoop (yarn)이 관리함

<br>

- avengers 예제
  - member = ["CaptainAmerica", "Thor", "Hulk", "IronMan", "BlackWidow", "Hawkeye", "Hulk"]
    avengers = sc.parallelize(member, 2)
    avengers = avengers.distinct()
    avengers = avengers.coalesce(1)
    avengers.glom().collect()
- nums = sc.parallelize([1, 4, 2, 3, 7, 6, 5], 1)
  - Python 리스트 `[1, 4, 2, 3, 7, 6, 5]`를 분산 컬렉션으로 변환
  - 1은 파티션 수 : 하나의 파티션으로 데이터 분할
- nums.collect() : [1, 4, 2, 3, 7, 6, 5]
- nums.sortBy(lambda x: x).collect()
  - 람다 함수 `lambda x: x`를 통해 각 요소를 그대로 유지하고 오름차순으로 정렬

<br>

- action 함수 : rdd의 값을 value로 바꿔주는 함수
- avengers.first() : 첫번 째 값
- nums.max() : 7
- nums.min() : 1
- nums.mean() : 3.9999999999999996
- nums.variance() : 4.000000000000001
- nums.stdev() : 2.0

<br>

- nums.stats()
  - 기초 통계 내용 정리
  - (count: 7, mean: 3.9999999999999996, stdev: 2.0, max: 7.0, min: 1.0)
- avengers.take(3)
  - `avengers` 데이터 세트의 첫 번째 3개의 요소 출력
- avengers.takeOrdered(3)
  - 알파벳 오름차순으로 정렬 후 3개 출력
  - ['BlackWidow', 'CaptainAmerica', 'Hawkeye']
- avengers.top(3)
  - 알파벳 내림차순으로 정렬 수 3개 출력
  - ['Thor', 'IronMan', 'Hulk']

<br>

- chars = sc.parallelize(['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd'])
- chars.countByValue()
  - defaultdict(<class 'int'>, {'a': 3, 'b': 2, 'c': 4, 'd': 1})
  - RDD 내에서 각 요소의 등장 횟수를 세어서 결과를 딕셔너리 형태로 반환 
  - 반환된 딕셔너리의 키는 요소 값이고, 값은 해당 요소의 등장 횟수

<br>

- rdd01 = sc.range(0, 1000, 2)
  - 0부터 999까지 2씩 늘어나도록
- rdd01.collect()
- rdd01.getNumPartitions()
  - 파티션 몇 개로 만들어져 있는지 > 2개
- rdd01.glom().collect()
  - 파티션 별로 배열로 나타내줌

<br>

- 합계 구하기
  - rdd01.sum() : 249500
  - rdd01.reduce(lambda x, y: x+y) : 249500
    - `reduce` 함수는 RDD의 모든 요소를 순차적으로 람다 함수를 적용하고 그 결과를 누적하여 반환
    - 파티션 1을 다 더하고 파티션 2를 다 더하고 그 둘을 합침

- rdd01.fold(0, max)
  -  `rdd01`의 모든 요소 중에서 가장 큰 값을 찾음
- aggregate (기본값, 파티션 단위 연산, 전체 연산)
  - rdd01.aggregate(0, max, lambda x, y: x+y)
  - rdd01 = [ [0 ~ 498], [500 ~ 998] ]
  - 498 + 998
  - 1496이 출력됨

<br>

- avengers에서 가장 긴 단어를 찾고 싶다면?

  - 먼저 함수를 만들고 나서 reduce로 함수 적용함

  - def longvengers(x, y):

    ​    if len(x) > len(y):

    ​        return x

    ​    else:

    ​        return y

  - avengers.reduce(longvengers)

<br>

- avengers에서 가장 짧은 단어를 찾고 싶다면?
  - avengers.reduce(lambda x, y: y if len(x) > len(y) else x)
  -  두 문자열 `x`와 `y`의 길이를 비교하여 긴 문자열을 선택

<br>

- 만들어진 내용 저장하기
  - avengers.saveAsTextFile("/avengers")
  - 스파크 종료하고 들어가서 확인 hdfs dfs -ls /avengers
  - hdfs dfs -cat /avengers/part-00000
  - 마스터를 yarn으로 지정해서 경로가 hadoop으로 잡힘
  - 스탠다드로 하면 로컬 경로로 저장됨

<br>

- 하둡에 있는 데이터를 가지고 오기
  - result = sc.textFile("/avengers/part-*")
  - `"part-*"`는 와일드카드 문자
  - 해당 디렉토리에서 `"part-"`로 시작하는 모든 파일을 읽어옴
  - 파티션별로 나뉘어져 있는 것 다 가지고 오겠다는 의미
  - result.collect()

<br>

- result_upper = result.map(lambda x: x.upper())
  - `result` RDD의 각 요소를 대문자로 변환한 새로운 RDD인 `result_upper`를 생성
- result.keyBy(lambda x: x[0]).mapValues(lambda x: len(x)).collect()
  -  `result` RDD의 각 요소를 처리하여 키-값 쌍 형태로 변환
  -  그 다음 각 요소의 길이를 계산하여 새로운 RDD를 생성
  -  먼저 `keyBy` 함수를 사용하여 각 요소의 첫 번째 문자를 키로 지정
  -  그런 다음 `mapValues` 함수를 사용하여 각 요소의 길이를 값으로 변환
  -  마지막으로 `collect` 함수를 사용하여 결과를 수집
- [('I', 7), ('B', 10), ('H', 4), ('C', 14), ('T', 4), ('H', 7)]

<br>

- lineage

- localhost:8088
- AWS에서 접속할 때는 내 IP :8088

<br>

- avengers = result

- **key_val = avengers.keyBy(lambda x: x[0])**
- key_val.collect()
- **[('I', 'IronMan'), ('B', 'BlackWidow'), ('H', 'Hulk'), ('C', 'CaptainAmerica'), ('T', 'Thor'), ('H', 'Hawkeye')]**
- 각 문자열의 첫 번째 문자를 키로 사용하여 RDD의 요소를 그룹화
- 키와 해당 요소를 튜플로 반환하는 방식으로 `keyBy` 함수가 작동

<br>

- key_val.mapValues(lambda x: list(x)).collect()
- [('I', ['I', 'r', 'o', 'n', 'M', 'a', 'n']), ('B', ['B', 'l', 'a', 'c', 'k', 'W', 'i', 'd', 'o', 'w']), ('H', ['H', 'u', 'l', 'k']), ('C', ['C', 'a', 'p', 't', 'a', 'i', 'n', 'A', 'm', 'e', 'r', 'i', 'c', 'a']), ('T', ['T', 'h', 'o', 'r']), ('H', ['H', 'a', 'w', 'k', 'e', 'y', 'e'])]
- `mapValues` 함수를 사용하여 각 요소의 값을 리스트로 변환
- 결과는 각 키와 해당 값을 리스트로 포함하는 튜플의 형태로 출력
- [(key, [values]), (key, [values]) (key, [values])...]

<br>

- key_val.flatMapValues(lambda x: list(x)).collect()
- [('I', 'I'), ('I', 'r'), ('I', 'o'), ('I', 'n'), ('I', 'M'), ('I', 'a'), ('I', 'n'), ('B', 'B'), ('B', 'l'), ('B', 'a'), ('B', 'c'), ('B', 'k'), ('B', 'W'), ('B', 'i'), ('B', 'd'), ('B', 'o'), ('B', 'w'), ('H', 'H'), ('H', 'u'), ('H', 'l'), ('H', 'k'), ('C', 'C'), ('C', 'a'), ('C', 'p'), ('C', 't'), ('C', 'a'), ('C', 'i'), ('C', 'n'), ('C', 'A'), ('C', 'm'), ('C', 'e'), ('C', 'r'), ('C', 'i'), ('C', 'c'), ('C', 'a'), ('T', 'T'), ('T', 'h'), ('T', 'o'), ('T', 'r'), ('H', 'H'), ('H', 'a'), ('H', 'w'), ('H', 'k'), ('H', 'e'), ('H', 'y'), ('H', 'e')]
- [ (k, [1, 2, 3, 4]), .... ] > [ (k, 1), (k, 2), (k, 3), (k, 4) ... ]
- 키를 밸류 하나씩한테 각각 나눠줘서 펼침
- `key_val` RDD의 각 값(value)에 대해 문자열을 문자 단위로 분해하여 
- 키-값 쌍을 생성하고, 이를 하나의 평면화된 RDD로 수집

<br>

- key_val.groupByKey().mapValues(list).collect()

- [('C', ['CaptainAmerica']), ('I', ['IronMan']), ('B', ['BlackWidow']), ('H', ['Hulk', 'Hawkeye']), ('T', ['Thor'])]

- RDD를 그룹화하고 그룹별로 값을 리스트로 변환하는 작업
  - `groupByKey()` 함수는 RDD를 키별로 그룹화
  - 여기서는 `key_val` RDD를 키별로 그룹화합니다.
  - `mapValues(list)` 함수는 각 그룹에 속한 값을 리스트로 변환
  - 이 부분에서 각 키에 대한 값들이 리스트로 변환됩니다.
  - `collect()` 함수를 사용하여 변환된 결과를 로컬 컬렉션으로 수집

<br>

- reduseByKey를 이용하여 [... ('H', 'Hawkeye, Hulk')] 형태로 출력
  - key_val.reduceByKey(lambda x, y: x+","+y).collect()
  - [('C', 'CaptainAmerica'), ('I', 'IronMan'), ('B', 'BlackWidow'), ('H', 'Hulk,Hawkeye'), ('T', 'Thor')]

<br>

- key_val.countByKey()
  - defaultdict(<class 'int'>, {'I': 1, 'B': 1, 'H': 2, 'C': 1, 'T': 1})
  - 각 키(key)의 빈도를 세는 작업을 수행하는 메서드
  - 이 메서드는 키-값 쌍의 RDD에서 각 키의 발생 횟수를 계산
  - Python의 `collections` 모듈에서 제공하는 `defaultdict` 형태로 반환

<br>

- vim wordcount.py

- spark-submit wordcount.py /user/ubuntu/data/shakespeare.txt /result

- hdfs -ls /result

<br>

- input_file = sc.textFile("data/shakespeare.txt")
- input_file.take(5)

<br>

- DataFrame
  - pandas의 데이터프레임과 유사함
  - 2차원 형태
- nums = spark.range(1000).toDF("nums")
  - 0부터 999까지의 숫자로 구성된 DataFrame을 생성
  - 이 DataFrame은 "nums"라는 하나의 컬럼을 가지며
  - 각 레코드는 숫자 값을 가지고 있음

- nums.head(10)
  - [Row(nums=0), Row(nums=1), Row(nums=2), Row(nums=3), Row(nums=4), Row(nums=5), Row(nums=6), Row(nums=7), Row(nums=8), Row(nums=9)]
- nums.tail(10)
  - [Row(nums=990), Row(nums=991), Row(nums=992), Row(nums=993), Row(nums=994), Row(nums=995), Row(nums=996), Row(nums=997), Row(nums=998), Row(nums=999)]
- nums.show()
  - +----+
    |nums|
    +----+
    |   0|
    |   1|
    |   2|
    |   3|
    |   4|
    |   5|
    |   6|
    |   7|
    |   8|
    |   9|
    |  10|
    |  11|
    |  12|
    |  13|
    |  14|
    |  15|
    |  16|
    |  17|
    |  18|
    |  19|
    +----+
    only showing top 20 rows

- evens = nums.where("num % 2 == 0")
- evens.head(5)
- evens.tail(5)
- evens.show()

<br>

- card202010 = spark.read.csv("data/card_data/csv/202010.csv")
- card202010.printSchema()
- card202010.take(5)
  - [Row(_c0='이용일', _c1='결제일', _c2='금액', _c3='포인트리금액', _c4='대분류', _c5='중분류', _c6='소분류'), Row(_c0='20201001', _c1=None, _c2='2990', _c3=None, _c4='생활', _c5='마트', _c6='웰빙마트'), Row(_c0='20201002', _c1=None, _c2='17100', _c3=None, _c4='식사', _c5='카페', _c6='카페부부스'), Row(_c0='20201002', _c1=None, _c2='18000', _c3=None, _c4='식사', _c5='구이', _c6=None), Row(_c0='20201003', _c1=None, _c2='2990', _c3=None, _c4='생활', _c5='마트', _c6='웰빙마트')]

- card_column = spark.read.option("header", "true").csv("data/card_data/csv/202010.csv")
- card_column.printSchema()
- card_column.take(5)
- card_column.show()
  - 데이터베이스 표처럼 나옴

<br>

- card = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("data/card_data/csv/202010.csv")
  - `card = spark.read.format("csv")`: 
    - SparkSession `spark`를 사용하여 CSV 파일을 읽음 
    - `format("csv")`는 데이터의 형식을 CSV로 지정
  - `.option("header", "true")`: 
    - CSV 파일의 첫 번째 행을 헤더로 처리
    - 이 옵션을 설정하면 첫 번째 행의 데이터가 컬럼 이름으로 사용됨
  - `.option("inferSchema", "true")`: 
    - 데이터 형식을 자동으로 추론해서 지정
    - 이 옵션을 설정하면 Spark가 각 컬럼의 데이터 형식을 자동으로 감지
  - `.load("data/card_data/csv/202010.csv")`: 
    - 실제 CSV 파일을 로드
    - 파일 경로는 `"data/card_data/csv/202010.csv"`로 지정
- card.printSchema()
  - root
     |-- 이용일: integer (nullable = true)
     |-- 결제일: integer (nullable = true)
     |-- 금액: integer (nullable = true)
     |-- 포인트리금액: integer (nullable = true)
     |-- 대분류: string (nullable = true)
     |-- 중분류: string (nullable = true)
     |-- 소분류: string (nullable = true)
- card.show()
  - +--------+------+-----+------------+------+------+----------+
    |  이용일|결제일| 금액|포인트리금액|대분류|중분류|    소분류|
    +--------+------+-----+------------+------+------+----------+
    |20201001|  null| 2990|        null|  생활|  마트|  웰빙마트|
    |20201002|  null|17100|        null|  식사|  카페|카페부부스|
    |20201002|  null|18000|        null|  식사|  구이|      null|
    |20201003|  null| 2990|        null|  생활|  마트|  웰빙마트|
    |20201003|  null|21900|        null|  식사|  족발|      null|
    |20201005|  null| 4100|        null|  생활|편의점|        CU|
    |20201005|  null| 1500|          15|  식사|  카페| 카페7그램|
    |20201005|  null| 7000|        null|  유흥|    술|      null|
    |20201006|  null| 1900|        null|  생활|편의점|        CU|
    |20201006|  null| 8700|        null|  생활|편의점|        CU|
    |20201006|  null| 7000|        null|  식사|  한식|      null|
    |20201006|  null| 1500|          15|  식사|  카페| 카페7그램|
    |20201007|  null| 8500|          60|  식사|돈까스|      null|
    |20201007|  null|14000|        null|  식사|  순대|      null|
    |20201007|  null| 3000|        null|  생활|편의점|        CU|
    |20201007|  null| 7250|        null|  식사|디저트|      null|
    |20201008|  null| 2900|        null|  생활|편의점|        CU|
    |20201008|  null|16000|        null|  식사|  한식|      null|
    |20201008|  null| 1500|          15|  식사|  카페| 카페7그램|
    |20201009|  null|40900|        null|  교통|  택시|      null|
    +--------+------+-----+------------+------+------+----------+
    only showing top 20 rows

- card.show(5)
  - 5개만 보여줌 (기본은 20개 보여줌)
  - +--------+------+-----+------------+------+------+----------+
    |  이용일|결제일| 금액|포인트리금액|대분류|중분류|    소분류|
    +--------+------+-----+------------+------+------+----------+
    |20201001|  null| 2990|        null|  생활|  마트|  웰빙마트|
    |20201002|  null|17100|        null|  식사|  카페|카페부부스|
    |20201002|  null|18000|        null|  식사|  구이|      null|
    |20201003|  null| 2990|        null|  생활|  마트|  웰빙마트|
    |20201003|  null|21900|        null|  식사|  족발|      null|
    +--------+------+-----+------------+------+------+----------+
    only showing top 5 rows

- card.sort("이용일")
  - DataFrame[이용일: int, 결제일: int, 금액: int, 포인트리금액: int, 대분류: string, 중분류: string, 소분류: string]
  - 데이터프레임 객체로 반환됨
  - card.sort("이용일").show() 으로 볼 수 있음

<br>

- execution plan (실행 계획) > 명령 실행 순서 (lazy)

- card.sort("이용일").explain()
  -  `explain()` 함수는 DataFrame의 실행 계획을 확인하는 메서드
  - 실행 계획은 Spark의 논리적 및 물리적 실행 계획을 포함 
  - DataFrame의 각 단계와 데이터 셔플, 파티셔닝 등에 대한 정보를 제공함

<br>

### SparkSQL

- card.createOrReplaceTempView("card")
- 한글 사용할 때는 백틱 사용
- card_table = spark.sql("SELECT `이용일`, `금액`, `대분류`, `중분류`, `소분류` FROM card")
- card_table.show()

<br>

- spark 사용법
  - 함수 사용
  - 쿼리 사용

<br>

- df이 가지고 있는 groupBy 함수를 사용하는 것과 spark.sql을 통해 쿼리로 group by 하는 것이 결과가 똑같음

- df = card.groupBy("이용일").count()
- sql = spark.sql("SELECT `이용일`, count(*) FROM card GROUP BY `이용일`")

<br>

- df.explain()
- sql.explain()

<br>

- 이용일 count()
  - df.show(3)
  - sql.show(3)
  - +--------+-----+
    |  이용일|count|
    +--------+-----+
    |20201010|    4|
    |20201008|    3|
    |20201002|    2|
    +--------+-----+

<br>

- from pyspark.sql.functions import max
- 금액 최대값 보기
  - df function : card.select(max("`금액`")).show()
  - spark.sql : spark.sql("select max(`금액`) from card").show()
  - +---------+
    |max(금액)|
    +---------+
    |    90000|
    +---------+

<br>

- 대분류 / 중분류 / 소분류 / 금액으로 컬럼 나눠서 보기
  - card.select("`대분류`", "`중분류`", "`소분류`", "`금액`").show()
  - spark.sql("select `대분류`, `중분류`, `소분류`, `금액` from card").show()
  - +------+------+----------+-----+
    |대분류|중분류|    소분류| 금액|
    +------+------+----------+-----+
    |  생활|  마트|  웰빙마트| 2990|
    |  식사|  카페|카페부부스|17100|
    |  식사|  구이|      null|18000|
    |  생활|  마트|  웰빙마트| 2990|
    |  식사|  족발|      null|21900|
    |  생활|편의점|        CU| 4100|
    |  식사|  카페| 카페7그램| 1500|
    |  유흥|    술|      null| 7000|
    |  생활|편의점|        CU| 1900|
    |  생활|편의점|        CU| 8700|
    |  식사|  한식|      null| 7000|
    |  식사|  카페| 카페7그램| 1500|
    |  식사|돈까스|      null| 8500|
    |  식사|  순대|      null|14000|
    |  생활|편의점|        CU| 3000|
    |  식사|디저트|      null| 7250|
    |  생활|편의점|        CU| 2900|
    |  식사|  한식|      null|16000|
    |  식사|  카페| 카페7그램| 1500|
    |  교통|  택시|      null|40900|
    +------+------+----------+-----+
    only showing top 20 rows

<br>

- expr(표현식)
- col : column을 의미함

<br>

- from pyspark.sql.functions import expr, col

  - PySpark의 `pyspark.sql.functions` 모듈에서 `expr`과 `col` 함수를 가져옴

  

  컬럼명 바꾸기

  - card.select(expr("`대분류` as category"), col("금액")).show()
  - card.select(expr("`대분류`").alias("category"), col("금액")).show()
  - spark.sql("select `대분류` as category, `금액` from card").show()
  - 동일한 결과 (대분류 > category로 변경)

<br>

- selectExpr : select + expr
  - card.selectExpr("`대분류` as category", "`금액`").show()
- card.selectExpr("*", "`금액` > 15000").show()

- spark.sql("SELECT *, `금액` > 15000 FROM card").show()
  - true랑 false로 결과가 나옴

<br>

- card.selectExpr("avg(`금액`)").show()
- spark.sql("select avg(`금액`) from card").show()
  - +------------------+
    |         avg(금액)|
    +------------------+
    |10393.419047619047|
    +------------------+

<br>

- withColumn(컬럼, 표현식) : 추가되는 컬럼의 이름 변경
- card.withColumn("up4", expr("`금액` > 40000")).show()
- 변경한 내용을 저장(반영)해야 함

- spark.sql("select *, (`금액` > 40000) as up4 from card").show()

<br>

- withColumnRenamed : 컬럼명 변경
- 대분류 컬럼명을 category로 바꾸자
- card.withColumnRenamed("대분류", "category").show()

- spark.sql("select `이용일`, `결제일`, `금액`, `포인트리금액`, `대분류` as category, `중분류`, `소분류`from card").show()

<br>

- card.drop("결제일").show()
- card.drop("포인트리금액").show()

<br>

- filter와 where의 차이점
  - where()는 filter()의 별칭
- 10,000원 보다 적게 쓴 내역만 보자
- card.filter(col("금액") < 10000).show()
- card.where("`금액` <10000").show()
- spark.sql("select * from card where `금액` <10000").show()

<br>

- 5000보다 크고 10000보다 작은 사용액 찾기

- card.where(col("금액") < 10000).where(col("금액") > 5000).show()

- spark.sql("select * from card where `금액` < 10000 and `금액` > 5000").show()

<br>

- 중복 제거하기
- card.select("대분류").distinct().show()
- spark.sql("select distinct(`대분류`) from card").show()
  - +------+
    |대분류|
    +------+
    |  교통|
    |  생활|
    |  의료|
    |  기타|
    |  식사|
    |  쇼핑|
    |  통신|
    |  유흥|
    |  문화|
    +------+

<br>

- "대분류"와 "중분류" 컬럼의 고유한 조합이 출력
  - card.select("대분류", "중분류").distinct().show()
  - spark.sql("SELECT `대분류`, `중분류` FROM card group by `대분류`, `중분류`").show()
  - spark.sql("SELECT DISTINCT `대분류`, `중분류` FROM card").show()
    - 중분류는 중복이 가능하기 때문에 이렇게 쓰면 안 됨
  - 아래처럼 묶으면 안 됨(구조체)
  - spark.sql("select distinct(`대분류`, `중분류`) from card").show()
    - +--------------------------------------------+
      |named_struct(대분류, 대분류, 중분류, 중분류)|
      +--------------------------------------------+
      |                                  {유흥, 술}|
      |                              {식사, 디저트}|
      |                                {식사, 분식}|
      |                              {식사, 돈까스}|
      |                                {의료, 약국}|
      |                             {교통, 버스 17}|
      |                                {문화, 도서}|
      |                                {식사, 순대}|
      |                                {식사, 한식}|
      |                                {식사, 카페}|
      |                                {식사, 족발}|
      |                                {식사, 중식}|
      |                              {식사, 햄버거}|
      |                              {생활, 편의점}|
      |                          {기타, 포인트사용}|
      |                             {교통, 버스 26}|
      |                                {통신, null}|
      |                                {교통, 택시}|
      |                                {생활, 마트}|
      |                                {식사, 구이}|
      +--------------------------------------------+

<br>

- from pyspark.sql import Row

- schema = card.schema
  - 구조 정보를 복사해왔다는 의미

- new_rows = [Row (20230907, None, 13000, None, '생활', '편의점', None), Row(20230907, None, 15000, None, '식사', '카페', '컴포즈커피')]
- new_card = spark.createDataFrame(new_rows, schema)
- new_card.show()
  - +--------+------+-----+------------+------+------+----------+
    |  이용일|결제일| 금액|포인트리금액|대분류|중분류|    소분류|
    +--------+------+-----+------------+------+------+----------+
    |20230907|  null|13000|        null|  생활|편의점|      null|
    |20230907|  null|15000|        null|  식사|  카페|컴포즈커피|
    +--------+------+-----+------------+------+------+----------+

<br>

- 새로 만든 DF를 기존 card랑 합치기
  - cards = card.union(new_card)
  - cards.show(cards.count())
  - 마지막에 새로 추가한 2행이 들어감
    - |20230907|    null| 13000|        null|  생활|    편의점|      null|
      |20230907|    null| 15000|        null|  식사|      카페|컴포즈커피|

<br>

- sort / orderby
  - card.sort("금액").show()
  - card.sort("금액", ascending=False).show()
  - card.orderBy(col("금액").asc()).show()
  - card.orderBy(col("금액").desc()).show()
  - spark.sql("select * from card order by `금액` desc").show()

<br>

- 이용일은 오름차순, 금액은 내림차순으로 5개만 출력
  - from pyspark.sql.functions import asc, desc
  - 아래 5가지가 다 같은 내용이므로 원하는 스타일로 작성하면 됨
    - card.orderBy(asc("이용일"), desc("금액")).show(5)
    - card.orderBy(["이용일", "금액"], ascending=[1, 0]).show(5)
    - card.orderBy(col("이용일").asc(), col("금액").desc()).show(5)
    - card.sort(["이용일", "금액"], ascending=[1, 0]).show(5)
    - card.sort(col("이용일").asc(), col("금액").desc()).show(5)

<br>

- from pyspark.sql.functions import instr
- store_filter = instr(col("소분류"), "마트") >= 1
- pay_filter = col("금액") <10000

<br>

- card.where(store_filter & pay_filter).where(col("이용일") >= 20201010).where(col("이용일") <= 20201020).show()
- spark.sql("select * from card where instr(`소분류`, '마트') >=1 and `금액` <10000 and `이용일` > 20201010 and `이용일` <20201020").show()
  - +--------+------+----+------------+------+------+--------+
    |  이용일|결제일|금액|포인트리금액|대분류|중분류|  소분류|
    +--------+------+----+------------+------+------+--------+
    |20201011|  null|2000|        null|  생활|  마트|웰빙마트|
    |20201017|  null|7970|        null|  생활|  마트|웰빙마트|
    +--------+------+----+------------+------+------+--------+

<br>

- 1만원이 넘으면 비싸다고 표시하기 (컬럼)
- expensive_filter = col("금액") > 10000
- card.withColumn("비쌈", expensive_filter).show()
- 비쌈 컬럼이 true 인 것만 표시하고 싶다면
  - card.withColumn("비쌈", expensive_filter).where(col("비쌈")).show()

<br>

- from pyspark.sql.functions import round
- pay_filter = col("금액") / 1000
- card.select(pay_filter, round(pay_filter)).show()
- spark.sql("select `금액` / 1000, round(`금액`/1000) from card" ).show()
  - +-------------+-----------------------+
    |(금액 / 1000)|round((금액 / 1000), 0)|
    +-------------+-----------------------+
    |         2.99|                    3.0|
    |         17.1|                   17.0|
    |         18.0|                   18.0|
    |         2.99|                    3.0|
    |         21.9|                   22.0|
    |          4.1|                    4.0|
    |          1.5|                    2.0|
    |          7.0|                    7.0|
    |          1.9|                    2.0|
    |          8.7|                    9.0|
    |          7.0|                    7.0|
    |          1.5|                    2.0|
    |          8.5|                    9.0|
    |         14.0|                   14.0|
    |          3.0|                    3.0|
    |         7.25|                    7.0|
    |          2.9|                    3.0|
    |         16.0|                   16.0|
    |          1.5|                    2.0|
    |         40.9|                   41.0|
    +-------------+-----------------------+
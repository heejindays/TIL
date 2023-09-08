## SPARK

- **파일 불러오기**
  - input_file = "data/shakespeare.txt"
    - PySpark를 사용하여 `shakespeare.txt` 파일을 읽고
  - wordcount = sc.textFile(input_file)
    - `wordcount` RDD (Resilient Distributed Dataset) 만들기
  - wordcount.take(10)

<br>

- **공백 없애기**
  - wordcount = wordcount.filter(lambda x: len(x) > 0)
    - '' 으로만 들어가 있는 것들을 없앰
    - wordcount.take(10)

<br>

- **단어로 분할하기**

  - import re
    - 정규 표현식을 사용하기 위해 파이썬에서 필요한 모듈을 가져오는 명령

  - wordcount = wordcount.flatMap(lambda x: re.split('\W+', x))
    - 정규 표현식을 사용하여 단어로 분할
    - 문자열 `x`를 정규 표현식 `\W+` (비알파벳 문자 하나 이상)을 사용하여 단어로 분할
    - 다시 공백이 생길 수 있기 때문에 확인 후 다시 한 번 공백 없애야 함

<br>

- **(단어, 1) 형태로 만들기**
  - wordcount = wordcount.map(lambda x: (x.lower(), 1))
  - [('the', 1), ('sonnets', 1), ('by', 1), ('william', 1), ('shakespeare', 1), ('from', 1), ('fairest', 1), ('creatures', 1), ('we', 1), ('desire', 1)]
  - 이 형태로 만든 뒤 같은 단어들이 있으면 count를 높여야 함

<br>

- **키값 기준으로 밸류값 더하기 = 단어 기준으로 +1**
  - wordcount = wordcount.reduceByKey(lambda x, y:x+y)

<br>

- **(단어, 숫자) > (숫자, 단어)의 형태로 바꾸기**
  - wordcount = wordcount.map(lambda x: (x[1], x[0]))
  - [(13, 'take'), (26, 'new'), (370, 'of'), (287, 'thy'), (17, 'mind'), (22, 'these'), (1, 'offices'), (121, 'as'), (235, 'thou'), (22, 'look')]

<br>

- **키를 기준으로 내림차순으로 정리하기**
  - wordcount = wordcount.sortByKey(ascending=False)
  - [(490, 'and'), (432, 'the'), (414, 'to'), (393, 'my'), (370, 'of'), (351, 'i'), (323, 'in'), (323, 'that'), (287, 'thy'), (235, 'thou')]

<br>

- **카드 데이터 가지고 오기**
  - card = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("data/card_data/csv/202010.csv")
  - card.show()
  - card.createOrReplaceTempView("card")
  - spark.sql("select * from card").show()

<br>

- **소분류 체인점일 경우 '치환' 컬럼 만들어서 '체인점'이라고 만들기**
  - from pyspark.sql.functions import col, regexp_replace
  - chain = "파머스빈|빽다방|바나프레소|카페7그램|스타벅스"
  - card.select(col("소분류"), regexp_replace(col("소분류"), chain, "체인점").alias("치환")).where(col("중분류") == "카페").show()
  - spark.sql("select `소분류`, regexp_replace(`소분류`, '파머스빈|빽다방|바나프레소|카페7그램|스타벅스', '체인점') as `치환` from card where `중분류` = '카페'").show()
  - col("소분류"), chain, "체인점") 소분류가 chain이라면 체인점으로 바꾸겠다
    - +----------+----------+
      |    소분류|      치환|
      +----------+----------+
      |카페부부스|카페부부스|
      | 카페7그램|    체인점|
      | 카페7그램|    체인점|
      | 카페7그램|    체인점|
      |  스타벅스|    체인점|
      | 카페7그램|    체인점|
      | 카페7그램|    체인점|
      |  파머스빈|    체인점|
      |  파머스빈|    체인점|
      | 카페7그램|    체인점|
      |  파머스빈|    체인점|
      | 카페7그램|    체인점|
      | 카페7그램|    체인점|
      |  파머스빈|    체인점|
      |바나프레소|    체인점|
      | 카페7그램|    체인점|
      | 카페7그램|    체인점|
      | 카페7그램|    체인점|
      |    빽다방|    체인점|
      |  파머스빈|    체인점|
      +----------+----------+

<br>

- **'스벅그프다' 문자를 각각 12345로 바꾸기**
- 스 > 1, 벅 > 2, 그 > 3, 프 > 4 , 다 >5
- from pyspark.sql.functions import translate
- card.select(col("소분류"), translate(col("소분류"), "스벅그프다", '12345').alias("치환")).where(col("중분류") == "카페").show()
- spark.sql("select `소분류`, translate(`소분류`, '스벅스프다', '12345') as `치환` from card where `중분류` = '카페'").show()
  - +----------+---------+
    |    소분류|     치환|
    +----------+---------+
    |카페부부스|카페부부1|
    | 카페7그램| 카페73램|
    | 카페7그램| 카페73램|
    | 카페7그램| 카페73램|
    |  스타벅스|    1타21|
    | 카페7그램| 카페73램|
    | 카페7그램| 카페73램|
    |  파머스빈|  파머1빈|
    |  파머스빈|  파머1빈|
    | 카페7그램| 카페73램|
    |  파머스빈|  파머1빈|
    | 카페7그램| 카페73램|
    | 카페7그램| 카페73램|
    |  파머스빈|  파머1빈|
    |바나프레소|바나4레소|
    | 카페7그램| 카페73램|
    | 카페7그램| 카페73램|
    | 카페7그램| 카페73램|
    |    빽다방|    빽5방|
    |  파머스빈|  파머1빈|
    +----------+---------+

<br>

- from pyspark.sql.functions import regexp_extract
- `regexp_extract` :주어진 문자열에서 정규 표현식을 사용하여 일치하는 부분을 추출하는 데 사용됨
- extract_str = "카페|다방"
- card.select(regexp_extract(col("소분류"), extract_str, 0).alias("치환"), col("소분류")).where(col("중분류") == "카페").show()

- +----+----------+
  |치환|    소분류|
  +----+----------+
  |카페|카페부부스|
  |카페| 카페7그램|
  |카페| 카페7그램|
  |카페| 카페7그램|
  |    |  스타벅스|
  |카페| 카페7그램|
  |카페| 카페7그램|
  |    |  파머스빈|
  |    |  파머스빈|
  |카페| 카페7그램|
  |    |  파머스빈|
  |카페| 카페7그램|
  |카페| 카페7그램|
  |    |  파머스빈|
  |    |바나프레소|
  |카페| 카페7그램|
  |카페| 카페7그램|
  |카페| 카페7그램|
  |다방|    빽다방|
  |    |  파머스빈|
  +----+----------+

<br>

- from pyspark.sql.functions import instr

- contains01 = instr(col("소분류"), "카페") >= 1
- contains02 = instr(col("소분류"), "다방") >= 1

- card.withColumn("카페다방포함", contains01 | contains02).select("소분류", "카페다방포함").where(col("중분류") == "카페").show() 
  - +----------+------------+
    |    소분류|카페다방포함|
    +----------+------------+
    |카페부부스|        true|
    | 카페7그램|        true|
    | 카페7그램|        true|
    | 카페7그램|        true|
    |  스타벅스|       false|
    | 카페7그램|        true|
    | 카페7그램|        true|
    |  파머스빈|       false|
    |  파머스빈|       false|
    | 카페7그램|        true|
    |  파머스빈|       false|
    | 카페7그램|        true|
    | 카페7그램|        true|
    |  파머스빈|       false|
    |바나프레소|       false|
    | 카페7그램|        true|
    | 카페7그램|        true|
    | 카페7그램|        true|
    |    빽다방|        true|
    |  파머스빈|       false|
    +----------+------------+

<br>

- **오늘 날짜 및 시간을 표현**
- from pyspark.sql.functions import current_date, current_timestamp
- date_df = spark.range(1).withColumn("mydate", current_date()).withColumn("mytimestamp", current_timestamp())
- date_df.show(1, False)
- date_df.show(truncate=False)
  - +---+----------+--------------------------+
    |id |mydate    |mytimestamp               |
    +---+----------+--------------------------+
    |0  |2023-09-08|2023-09-08 10:34:19.700917|
    +---+----------+--------------------------+

<br>

- **5일 전 날짜와 5일 수 날짜를 알아보자**
  - from pyspark.sql.functions import date_sub, date_add
  - date_df.createOrReplaceTempView("date_table")
  - `date_sub(mydate, 5)`: `mydate` 컬럼의 값을 5일 전으로 줄임
  - `date_add(mydate, 5)`: `mydate` 컬럼의 값을 5일 후로 늘림
  - date_df.select(date_sub(col("mydate"), 5), date_add(col("mydate"), 5)).show()
  - spark.sql("select date_sub(mydate, 5), date_add(mydate, 5) from date_table").show()
  - +-------------------+-------------------+
    |date_sub(mydate, 5)|date_add(mydate, 5)|
    +-------------------+-------------------+
    |         2023-09-03|         2023-09-13|
    +-------------------+-------------------+

<br>

-  **날짜 간 차이를 계산 (날짜 차이 : 7일)**
- from pyspark.sql.functions import datediff, months_between, to_date
- date_df.withColumn("week_ago", date_sub(col("mydate"), 7)).select(datediff(col("week_ago"), col("mydate"))).show()
  - +--------------------------+
    |datediff(week_ago, mydate)|
    +--------------------------+
    |                        -7|
    +--------------------------+

<br>

- **두 날짜 사이의 월 수를 계산하기**
- lit : literal (값 자체)
- from pyspark.sql.functions import lit

- date_df.select(to_date(lit("2023-09-08")).alias("today"), to_date(lit("2023-10-31")).alias("end")).select(months_between(col("today"), col("end"))).show()
  - `to_date(lit("2023-09-08")).alias("today")`: 
    - "2023-09-08" 문자열을 날짜 형식으로 변환
    - "today"라는 이름의 새로운 컬럼을 생성
    - "today" 컬럼에는 2023년 9월 8일의 날짜가 들어갑니다.
  - `to_date(lit("2023-10-31")).alias("end")`: 
    - "2023-10-31" 문자열을 날짜 형식으로 변환
    -  "end"라는 이름의 새로운 컬럼을 생성
    - "end" 컬럼에는 2023년 10월 31일의 날짜가 들어감
  - `months_between(col("today"), col("end"))`: 
    - "today"와 "end" 컬럼 사이의 월 수를 계산
    - 즉, 두 날짜 사이의 월 차이를 계산
    - +--------------------------------+
      |months_between(today, end, true)|
      +--------------------------------+
      |                     -1.74193548|
      +--------------------------------+
  - spark.sql("select datediff(mydate, date_sub(mydate, 7)) as `datediff`, months_between('2023-09-08', '2023-10-31') as `months_between` from date_table").show()
    - +--------+--------------+
      |datediff|months_between|
      +--------+--------------+
      |       7|   -1.74193548|
      +--------+--------------+

<br>

- **만약에 존재하지 않는 날짜를 입력한다면?**
  - date_df.select(to_date(lit("2023-12-32")), to_date(lit("2023-13-01"))).show()
  - +-------------------+-------------------+
    |to_date(2023-12-32)|to_date(2023-13-01)|
    +-------------------+-------------------+
    |               null|               null|
    +-------------------+-------------------+

<br>

- spark context > sc, 저수준 api (RDD)

- spark session > spark, 고수준 api (dataframe) 

<br>

- simpleDateFormat : 날짜의 포맷 지정

- date_format = "yyyy-MM-dd"

- format_df = spark.range(1).select(to_date(lit("2022-12-25"), date_format).alias("format1"), to_date(lit("2022-25-12"), "yyyy-dd-MM").alias("format2"))
  - spark.range(1) : 데이터프레임 하나 만들어놓고 이걸 바탕으로 select
- format_df.show()
  - +----------+----------+
    |   format1|   format2|
    +----------+----------+
    |2022-12-25|2022-12-25|
    +----------+----------+

<br>

- from pyspark.sql.functions import to_timestamp

- format_df.select (to_date(col("format1"), "yyyy-MM-dd HH:mm:ss").alias("date"), to_timestamp(col("format1"),"yyyy-MM-dd HH:mm:ss").alias("timestamp")).show()

- "to_date" 함수를 사용하여 "format1" 열의 날짜를 추출

  - 아무리 yyyy-MM-dd HH:mm:ss 으로 시간을 잡아줘도 날짜만 나옴

- "to_timestamp" 함수를 사용하여 타임스탬프를 추출

  - 시간까지 다 필요하다면 to_timestamp로 잡아야 함

  - +----------+-------------------+
    |      date|          timestamp|
    +----------+-------------------+
    |2022-12-25|2022-12-25 00:00:00|
    +----------+-------------------+

- spark.sql("SELECT to_date(format1, 'yyyy-MM-dd HH:mm:ss') AS date, to_timestamp(format1, 'yyyy-MM-dd HH:mm:ss') AS timestamp FROM format_table").show()

<br>

- card 이용일 컬럼 값을 날짜로 바꾼 뒤 출력
  - card.printSchema()
  - root
     |-- 이용일: integer (nullable = true)
     |-- 결제일: integer (nullable = true)
     |-- 금액: integer (nullable = true)
     |-- 포인트리금액: integer (nullable = true)
     |-- 대분류: string (nullable = true)
     |-- 중분류: string (nullable = true)
     |-- 소분류: string (nullable = true)
  - card.select(to_date(col("이용일").cast("string"), "yyyyMMdd")).show()
    - 먼저 문자로 바꾼 다음에 날짜로 바꿔야 함
  - +-----------------------------------------+
    |to_date(CAST(이용일 AS STRING), yyyyMMdd)|
    +-----------------------------------------+
    |                               2020-10-01|
    |                               2020-10-02|
    |                               2020-10-02|
    |                               2020-10-03|
    |                               2020-10-03|
    |                               2020-10-05|
    |                               2020-10-05|
    |                               2020-10-05|
    |                               2020-10-06|
    |                               2020-10-06|
    |                               2020-10-06|
    |                               2020-10-06|
    |                               2020-10-07|
    |                               2020-10-07|
    |                               2020-10-07|
    |                               2020-10-07|
    |                               2020-10-08|
    |                               2020-10-08|
    |                               2020-10-08|
    |                               2020-10-09|
    +-----------------------------------------+

<br>

- 데이터베이스에서의 null = 파이썬에서의 None
- name / phone / address 테이블 만들기
  - from pyspark.sql import Row
  - null_df = sc.parallelize([Row(name="You", phone="010-0000-0000", address="Seoul"), Row(name="Shine", phone="010-1111-1111", address=None), Row(name="Kang", phone=None, address=None)]).toDF()
  - null_df.show()
  - null_df.createOrReplaceTempView("null_table")
  - +-----+-------------+-------+
    | name|        phone|address|
    +-----+-------------+-------+
    |  You|010-0000-0000|  Seoul|
    |Shine|010-1111-1111|   null|
    | Kang|         null|   null|
    +-----+-------------+-------+

<br>

- from pyspark.sql.functions import coalesce
  - coalesce (rdd) : repartition (파티션 축소)
  - coalesce (sql / df) : null을 제외한 첫번째 값
- null_df.select(coalesce(col("address"), col("phone")).alias("coalesce")).show()
  - address랑 phone 중에서 null이 아닌 첫 번째 값들이 나옴
  - 순서는 address부터 살펴보기 시작함
  - +-------------+
    |     coalesce|
    +-------------+
    |        Seoul|
    |010-1111-1111|
    |         null|
    +-------------+

<br>

- spark에는 없고 query로만 존재하는 것들
  - ifnull : 첫 번째 값이 null이면 두번째 값 리턴
  - nullif : 두 값이 같으면 null
  - nvl : 첫 번째 값이 null이면 두 번째 값 리턴
  - nvl2 : 첫번째 값이  null이면 두 번째 값 / 아니면 세 번째 값

- spark.sql("select ifnull(null, 'value'), nullif('same','same'), nvl('not null', 'value1'), nvl(null, 'value1'), nvl2('notnull', 'value1', 'value2'), nvl2(null, 'value1', 'value2')").show()

<br>

- **na : null값을 처리하기 위한 DateFrameNaFunction을 리턴**
  - DataFrameNaFunction : drop, fill, replace
  - null_df.show()
  - null_df.na.drop().show()
  - +----+-------------+-------+
    |name|        phone|address|
    +----+-------------+-------+
    | You|010-0000-0000|  Seoul|
    +----+-------------+-------+

<br>

- **all : 모든 컬럼의 값이 null이면 row 제거**
- **any  : 컬럼 중 하나라도 null이면 row 제거**
  - null_df.na.drop("all", subset=["phone"]).show()
  - null_df.na.drop("all", subset=["phone","address"]).show()
  - +-----+-------------+-------+
    | name|        phone|address|
    +-----+-------------+-------+
    |  You|010-0000-0000|  Seoul|
    |Shine|010-1111-1111|   null|
    +-----+-------------+-------+
  - null_df.na.drop("any", subset=["phone","address"]).show()
  - +----+-------------+-------+
    |name|        phone|address|
    +----+-------------+-------+
    | You|010-0000-0000|  Seoul|
    +----+-------------+-------+

<br>

- null_df.na.fill("n/a").show()
- null_df.na.fill("n/a", subset=["phone"]).show()
  - phone만 바꿀 수도 있음
  - +-----+-------------+-------+
    | name|        phone|address|
    +-----+-------------+-------+
    |  You|010-0000-0000|  Seoul|
    |Shine|010-1111-1111|   null|
    | Kang|          n/a|   null|
    +-----+-------------+-------+

- null_df.na.fill("n/a", subset=["phone", "address"]).show()

  - phong이랑 address만 바꿀 수 있음
  - +-----+-------------+-------+
    | name|        phone|address|
    +-----+-------------+-------+
    |  You|010-0000-0000|  Seoul|
    |Shine|010-1111-1111|    n/a|
    | Kang|          n/a|    n/a|
    +-----+-------------+-------+

  <br>

- na인 값들을 기본 값으로 바꾸려면
  - defalut_value = {"phone": "010-7777-7777", "address": "street"}
  - null_df.na.fill(defalut_value).show()
  - +-----+-------------+-------+
    | name|        phone|address|
    +-----+-------------+-------+
    |  You|010-0000-0000|  Seoul|
    |Shine|010-1111-1111| street|
    | Kang|010-7777-7777| street|
    +-----+-------------+-------+

<br>

- seoul을 서울로 바꾸려면
  - null_df.na.replace(["seoul"], ["서울"], "address").show()

<br>

- 구조체 : dataframe 안에 dataframe
  - card.selectExpr("(`이용일`, `금액`) as complex", "*").show()
  - card.selectExpr("struct(`이용일`, `금액`) as complex", "*").show()

- from pyspark.sql.functions import struct
- complex_df = card.select(struct("이용일", "금액").alias("complex"))
- complex_df.show()
  - +-----------------+
    |          complex|
    +-----------------+
    | {20201001, 2990}|
    |{20201002, 17100}|
    |{20201002, 18000}|
    | {20201003, 2990}|
    |{20201003, 21900}|
    | {20201005, 4100}|
    | {20201005, 1500}|
    | {20201005, 7000}|
    | {20201006, 1900}|
    | {20201006, 8700}|
    | {20201006, 7000}|
    | {20201006, 1500}|
    | {20201007, 8500}|
    |{20201007, 14000}|
    | {20201007, 3000}|
    | {20201007, 7250}|
    | {20201008, 2900}|
    |{20201008, 16000}|
    | {20201008, 1500}|
    |{20201009, 40900}|
    +-----------------+
- complex_df.createOrReplaceTempView("complex_table")
- complex_df.select("complex.`이용일`").show()
- complex_df.select(col("complex").getField("이용일")).show()

- spark.sql("select complex.`이용일` from complex_table").show()
  - +--------+
    |  이용일|
    +--------+
    |20201001|
    |20201002|
    |20201002|
    |20201003|
    |20201003|
    |20201005|
    |20201005|
    |20201005|
    |20201006|
    |20201006|
    |20201006|
    |20201006|
    |20201007|
    |20201007|
    |20201007|
    |20201007|
    |20201008|
    |20201008|
    |20201008|
    |20201009|
    +--------+
- complex_df.select("complex.*").show()
- spark.sql("select complex.* from complex_table").show()
  - +--------+-----+
    |  이용일| 금액|
    +--------+-----+
    |20201001| 2990|
    |20201002|17100|
    |20201002|18000|
    |20201003| 2990|
    |20201003|21900|
    |20201005| 4100|
    |20201005| 1500|
    |20201005| 7000|
    |20201006| 1900|
    |20201006| 8700|
    |20201006| 7000|
    |20201006| 1500|
    |20201007| 8500|
    |20201007|14000|
    |20201007| 3000|
    |20201007| 7250|
    |20201008| 2900|
    |20201008|16000|
    |20201008| 1500|
    |20201009|40900|
    +--------+-----+

<br>

- **배열로 split 하기**
- from pyspark.sql.functions import split
- card.select(split(col("중분류"), " ")).where(col("대분류") == "교통").show()
- spark.sql("select split(`중분류`, ' ') from card where `대분류` = '교통' ").show()
  - +--------------------+
    |split(중분류,  , -1)|
    +--------------------+
    |              [택시]|
    |          [버스, 17]|
    |          [버스, 26]|
    +--------------------+

- **잘라 놓은 것에서 [0]만 가져오기**
  - card.select(split(col("중분류"), " ").alias("arraycolumn")).selectExpr("arraycolumn[0]").where(col("대분류") == "교통").show()
  - spark.sql("select split(`중분류`, ' ')[0] from card where `대분류` == '교통'").show()
  - +-----------------------+
    |split(중분류,  , -1)[0]|
    +-----------------------+
    |                   택시|
    |                   버스|
    |                   버스|
    +-----------------------+

<br>

- **사이즈(개수)도 알 수 있음**
  - from pyspark.sql.functions import size
  - card.select(split(col("중분류"), " "), size(split(col("중분류"), " ")).alias("split_size")).where(col("대분류") == "교통").show()
  - +--------------------+----------+
    |split(중분류,  , -1)|split_size|
    +--------------------+----------+
    |              [택시]|         1|
    |          [버스, 17]|         2|
    |          [버스, 26]|         2|
    +--------------------+----------+

<br>

- **자른 단어 중에서 버스가 있는지 확인**
  - from pyspark.sql.functions import array_contains
  - card.select(array_contains(split(col("중분류"), " "), "버스")).where(col("대분류") == "교통").show()
  - +------------------------------------------+
    |array_contains(split(중분류,  , -1), 버스)|
    +------------------------------------------+
    |                                     false|
    |                                      true|
    |                                      true|
    +------------------------------------------+

<br>

- **"중분류" 열을 공백을 기준으로 분할하고,** 
- **"대분류"가 "교통"인 행만 선택하여 "중분류"와 분할된 "splitted" 컬럼을 출력**
  - from pyspark.sql.functions import explode
  - card.withColumn("splitted", split(col("중분류"), " ")).select("중분류", "splitted").where(col("대분류") == "교통").show()
  -  +-------+----------+
    | 중분류|  splitted|
    +-------+----------+
    |   택시|    [택시]|
    |버스 17|[버스, 17]|
    |버스 26|[버스, 26]|
    +-------+----------+

<br>

- **splitted 배열 안에 들어있는 값 하나당 하나의 row를 각각 만들기**
  - card.withColumn("splitted", split(col("중분류"), " ")).withColumn("exploded", explode(col("splitted"))).select("중분류", "splitted", "exploded").where(col("대분류") == "교통").show()
  - +-------+----------+--------+
    | 중분류|  splitted|exploded|
    +-------+----------+--------+
    |   택시|    [택시]|    택시|
    |버스 17|[버스, 17]|    버스|
    |버스 17|[버스, 17]|      17|
    |버스 26|[버스, 26]|    버스|
    |버스 26|[버스, 26]|      26|
    +-------+----------+--------+

<br>

- **맵 (key > value)**
-  **"이용일"과 "금액"을 이용하여 복합 맵(complex map)을 생성**
- 이를 "complexmap"이라는 별칭으로 만들기
- `create_map` 함수는 열의 값을 키와 값의 쌍으로 매핑하여 맵을 생성
- from pyspark.sql.functions import create_map
- card.select(create_map(col("이용일"), col("금액")).alias("complexmap")).show()
- spark.sql("select map(`이용일`, `금액`) as complexmap from card").show()
  - +-------------------+
    |         complexmap|
    +-------------------+
    | {20201001 -> 2990}|
    |{20201002 -> 17100}|
    |{20201002 -> 18000}|
    | {20201003 -> 2990}|
    |{20201003 -> 21900}|
    | {20201005 -> 4100}|
    | {20201005 -> 1500}|
    | {20201005 -> 7000}|
    | {20201006 -> 1900}|
    | {20201006 -> 8700}|
    | {20201006 -> 7000}|
    | {20201006 -> 1500}|
    | {20201007 -> 8500}|
    |{20201007 -> 14000}|
    | {20201007 -> 3000}|
    | {20201007 -> 7250}|
    | {20201008 -> 2900}|
    |{20201008 -> 16000}|
    | {20201008 -> 1500}|
    |{20201009 -> 40900}|
    +-------------------+

<br>

- card.select(create_map(col("이용일"), col("금액")).alias("complexmap") ).selectExpr("complexmap['20201002']").show()
- spark.sql("select map(`이용일`, `금액`)['20201002'] from card").show()

- +--------------------+
  |complexmap[20201002]|
  +--------------------+
  |                null|
  |               17100|
  |               18000|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  |                null|
  +--------------------+

<br>

- **explode** 
  - 배열에서는 배열 요소 각각을 row로
  - 맵에서는 key 따로 value 따로
- card.select(create_map(col("이용일"), col("금액")).alias("complexmap")).selectExpr("explode(complexmap)").show()
- spark.sql("select explode(map(`이용일`, `금액`)) from card").show()
  - +--------+-----+
    |     key|value|
    +--------+-----+
    |20201001| 2990|
    |20201002|17100|
    |20201002|18000|
    |20201003| 2990|
    |20201003|21900|
    |20201005| 4100|
    |20201005| 1500|
    |20201005| 7000|
    |20201006| 1900|
    |20201006| 8700|
    |20201006| 7000|
    |20201006| 1500|
    |20201007| 8500|
    |20201007|14000|
    |20201007| 3000|
    |20201007| 7250|
    |20201008| 2900|
    |20201008|16000|
    |20201008| 1500|
    |20201009|40900|
    +--------+-----+

<hr>

- **csv directory에 있는 모든 데이터 가져오기**
- card_all = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("data/card_data/csv/*.csv")
- card_all.createOrReplaceTempView("card_all")
- card_all.count()

<br>

- **전체 카드 데이터 가져오기**
  - from pyspark.sql.functions import count
  - card_all.select(count("*")).show
  - spark.sql("select count(*) from card_all").show()
  - +--------+
    |count(1)|
    +--------+
    |    3039|
    +--------+

<br>

- **이용일에서 중복되지 않는 값들의 수**
  - from pyspark.sql.functions import countDistinct, col
  - card_all.select(countDistinct(col("이용일"))).show()
  - spark.sql("select count(Distinct(`이용일`)) from card_all").show()
  - +----------------------+
    |count(DISTINCT 이용일)|
    +----------------------+
    |                  1160|
    +----------------------+

<br>

- **"card_all" 테이블에서 "이용일" 열의 첫 번째(first) 값과 마지막(last) 값 출력**
  - from pyspark.sql.functions import first, last
  - card_all.select(first(col("이용일")), last(col("이용일"))).show()
  - spark.sql("select first(`이용일`), last(`이용일`) from card_all").show()
  - +-------------+------------+
    |first(이용일)|last(이용일)|
    +-------------+------------+
    |     20190902|    20200331|
    +-------------+------------+

<br>

-  **"card_all" 테이블에서 "금액" 열의 최솟값(min)과 최댓값(max)을 선택하여 출력**
  - from pyspark.sql.functions import max, min
  - card_all.select(min("`금액`"), max(col("금액"))).show()
  - spark.sql("select min (`금액`), max(`금액`) from card_all").show()
  - +---------+---------+
    |min(금액)|max(금액)|
    +---------+---------+
    |  -191860|  4326850|
    +---------+---------+

<br>

-  **"card_all" 테이블에서 "금액" 열의 합계(sum)를 계산하고 출력**
  - from pyspark.sql.functions import sum
  - card_all.select(sum(col("금액"))).show()
  - spark.sql("select sum(`금액`) from card_all").show()
  - +---------+
    |sum(금액)|
    +---------+
    | 53019959|
    +---------+

<Br>

- **결제 건수 및 금액 평균**
  - from pyspark.sql.functions import avg, mean
  - card_all.select(count(col("금액")), sum(col("금액")), avg(col("금액")), mean(col("금액"))).show()
  - +-----------+---------+------------------+------------------+
    |count(금액)|sum(금액)|         avg(금액)|         avg(금액)|
    +-----------+---------+------------------+------------------+
    |       3039| 53019959|17446.514972030272|17446.514972030272|
    +-----------+---------+------------------+------------------+

<br>

- 분산/표준편차

- 모집단 : 전체 집단
- 표본집단 : 그 중에서 선택된 일부 집단
- var_pop : 모분산
- stddev_pop : 모표준편차
- var_samp : 표본분산
- stddev_samp : 표본 표준편차

<br>

- **"금액" 열의 통계적 지표들 계산**
  - from pyspark.sql.functions import var_pop, stddev_pop, var_samp, stddev_samp
  - card_all.select(var_pop(col("금액")).alias("varpop"), var_samp(col("금액")).alias("varsamp"), stddev_pop(col("금액")).alias("stddev_pop"), stddev_samp(col("금액")).alias("stddevsamp")).show()
  - spark.sql("select var_pop(`금액`), var_samp(`금액`), stddev_pop(`금액`), stddev_samp(`금액`) from card_all").show()

<br>

- **공분산 상관관계**
  - from pyspark.sql.functions import covar_pop, covar_samp, corr
  - card_all.select(covar_pop(col("이용일"), col("금액")), covar_samp(col("이용일"), col("금액")), corr(col("이용일"), col("금액"))).show()
  - +-----------------------+------------------------+--------------------+
    |covar_pop(이용일, 금액)|covar_samp(이용일, 금액)|  corr(이용일, 금액)|
    +-----------------------+------------------------+--------------------+
    |      6865.962989131605|       6931.981864027101|0.048078139390917436|
    +-----------------------+------------------------+--------------------+

<br>

- card_all.groupBy(col("대분류"), col("중분류")).count().show()
  - spark.sql("select `대분류`, `중분류`, count(*) from card_all group by `대분류`, `중분류`").show()
  - +------+----------+-----+
    |대분류|    중분류|count|
    +------+----------+-----+
    |  유흥|        술|    2|
    |  식사|    디저트|    5|
    |  식사|      분식|    3|
    |  식사|    돈까스|    3|
    |  의료|      약국|    1|
    |  교통|   버스 17|    1|
    |  문화|      도서|    1|
    |  식사|      순대|    3|
    |  식사|      한식|    8|
    |  식사|      카페|   21|
    |  식사|      족발|    2|
    |  식사|      중식|    3|
    |  식사|    햄버거|    2|
    |  생활|    편의점|   29|
    |  기타|포인트사용|    1|
    |  교통|   버스 26|    1|
    |  통신|      null|    1|
    |  교통|      택시|    1|
    |  생활|      마트|    5|
    |  식사|      구이|    1|
    +------+----------+-----+

<br>

- **date" 열을 추가하고 "to_date" 함수를 사용하여 "이용일" 열의 문자열을 날짜 형식으로 변환**
- from pyspark.sql.functions import to_date

- date_df = card_all.withColumn("date", to_date(col("이용일").cast("string"), "yyyyMMdd"))
- date_df.show()
- date_df.createOrReplaceTempView("date_table")
- spark.sql("select * from date_table").show()
- +--------+------+-----+------------+------+------+----------+----------+
  |  이용일|결제일| 금액|포인트리금액|대분류|중분류|    소분류|      date|
  +--------+------+-----+------------+------+------+----------+----------+
  |20201001|  null| 2990|        null|  생활|  마트|  웰빙마트|2020-10-01|
  |20201002|  null|17100|        null|  식사|  카페|카페부부스|2020-10-02|
  |20201002|  null|18000|        null|  식사|  구이|      null|2020-10-02|
  |20201003|  null| 2990|        null|  생활|  마트|  웰빙마트|2020-10-03|
  |20201003|  null|21900|        null|  식사|  족발|      null|2020-10-03|
  |20201005|  null| 4100|        null|  생활|편의점|        CU|2020-10-05|
  |20201005|  null| 1500|          15|  식사|  카페| 카페7그램|2020-10-05|
  |20201005|  null| 7000|        null|  유흥|    술|      null|2020-10-05|
  |20201006|  null| 1900|        null|  생활|편의점|        CU|2020-10-06|
  |20201006|  null| 8700|        null|  생활|편의점|        CU|2020-10-06|
  |20201006|  null| 7000|        null|  식사|  한식|      null|2020-10-06|
  |20201006|  null| 1500|          15|  식사|  카페| 카페7그램|2020-10-06|
  |20201007|  null| 8500|          60|  식사|돈까스|      null|2020-10-07|
  |20201007|  null|14000|        null|  식사|  순대|      null|2020-10-07|
  |20201007|  null| 3000|        null|  생활|편의점|        CU|2020-10-07|
  |20201007|  null| 7250|        null|  식사|디저트|      null|2020-10-07|
  |20201008|  null| 2900|        null|  생활|편의점|        CU|2020-10-08|
  |20201008|  null|16000|        null|  식사|  한식|      null|2020-10-08|
  |20201008|  null| 1500|          15|  식사|  카페| 카페7그램|2020-10-08|
  |20201009|  null|40900|        null|  교통|  택시|      null|2020-10-09|
  +--------+------+-----+------------+------+------+----------+----------+

<br>

- **대분류 / 날짜별 금액의 순위 출력**
-  "대분류" 열을 기준으로 내림차순으로 정렬된 윈도우(Window)를 정의하고, 현재 행부터 시작하여 해당 파티션(Partition) 내의 모든 행을 포함하도록 설정

- from pyspark.sql.window import Window
- from pyspark.sql.functions import desc
- window_function = Window.partitionBy(col("대분류")).orderBy(desc(col("date"))).rowsBetween(Window.unboundedPreceding, Window.currentRow)

<br>

- **"대분류" 열을 기준으로 오름차순으로 정렬한 다음,** 
- **"대분류", "date", "금액", "win_dense", "win_rank" 열을 선택하여 상위 10개 출력**

- from pyspark.sql.functions import dense_rank, rank
- win_dense = dense_rank().over(window_function)
- win_rank = rank().over(window_function)
- date_df.orderBy(col("대분류")).select(col("대분류"), col("date"), col("금액"), win_dense, win_rank).show(10)
- spark.sql("select `대분류`, date, rank() over (partition by `대분류` order by date), dense_rank() over (partition by `대분류` order by date) from date_table").show()

<br>

- rollup_df = card_all.rollup("`이용일`", "`대분류`").agg(avg("`금액`").alias("avgpay")).selectExpr("`이용일`", "`대분류`", "avgpay").orderBy("이용일")
- rollup_df.show()
- spark.sql("select `이용일`, `대분류`, avg(`금액`) from card_all group by rollup(`이용일`, `대분류`) order by `이용일`").show()

- +--------+------+------------------+
  |  이용일|대분류|            avgpay|
  +--------+------+------------------+
  |    null|  null|10393.419047619047|
  |20201001|  생활|            2990.0|
  |20201001|  null|            2990.0|
  |20201002|  식사|           17550.0|
  |20201002|  null|           17550.0|
  |20201003|  null|           12445.0|
  |20201003|  생활|            2990.0|
  |20201003|  식사|           21900.0|
  |20201005|  생활|            4100.0|
  |20201005|  유흥|            7000.0|
  |20201005|  null|            4200.0|
  |20201005|  식사|            1500.0|
  |20201006|  null|            4775.0|
  |20201006|  식사|            4250.0|
  |20201006|  생활|            5300.0|
  |20201007|  생활|            3000.0|
  |20201007|  null|            8187.5|
  |20201007|  식사| 9916.666666666666|
  |20201008|  생활|            2900.0|
  |20201008|  null|            6800.0|
  +--------+------+------------------+

<br>

- cube_df = card_all.cube("`이용일`","`대분류`").agg(avg("`금액`").alias("avgpay")).selectExpr("`이용일`", "`대분류`", "avgpay").orderBy("이용일")

- cube_df.show()

- +--------+------+------------------+
  |  이용일|대분류|            avgpay|
  +--------+------+------------------+
  |    null|  기타|           -3622.2|
  |    null|  교통|           52700.0|
  |    null|  통신|           21710.0|
  |    null|  null|10393.419047619047|
  |    null|  유흥|            7000.0|
  |    null|  쇼핑| 33591.42857142857|
  |    null|  식사| 9789.607843137255|
  |    null|  문화|           60000.0|
  |    null|  의료|            4000.0|
  |    null|  생활|3447.0588235294117|
  |20201001|  생활|            2990.0|
  |20201001|  null|            2990.0|
  |20201002|  식사|           17550.0|
  |20201002|  null|           17550.0|
  |20201003|  null|           12445.0|
  |20201003|  식사|           21900.0|
  |20201003|  생활|            2990.0|
  |20201005|  null|            4200.0|
  |20201005|  생활|            4100.0|
  |20201005|  유흥|            7000.0|
  +--------+------+------------------+

<br>

- grouping set : spark 함수에 없음

<br>

- from pyspark.sql.functions import substring
  - rollup_df.where(substring(col("이용일"), 1, 6) == '202010').show()
  - +--------+------+-----------------+
    |  이용일|대분류|           avgpay|
    +--------+------+-----------------+
    |20201001|  생활|           2990.0|
    |20201001|  null|           2990.0|
    |20201002|  식사|          17550.0|
    |20201002|  null|          17550.0|
    |20201003|  null|          12445.0|
    |20201003|  식사|          21900.0|
    |20201003|  생활|           2990.0|
    |20201005|  생활|           4100.0|
    |20201005|  유흥|           7000.0|
    |20201005|  null|           4200.0|
    |20201005|  식사|           1500.0|
    |20201006|  null|           4775.0|
    |20201006|  식사|           4250.0|
    |20201006|  생활|           5300.0|
    |20201007|  null|           8187.5|
    |20201007|  식사|9916.666666666666|
    |20201007|  생활|           3000.0|
    |20201008|  null|           6800.0|
    |20201008|  생활|           2900.0|
    |20201008|  식사|           8750.0|
    +--------+------+-----------------+

<br>

- 새로운 데이터 만들기
  - heroes.show()
  - +---+---------------+----+------+
    | id|           name|team|   job|
    +---+---------------+----+------+
    |  1|       iron man|   1|   [1]|
    |  2|         batman|   3|   [1]|
    |  3|captain america|   1|   [1]|
    |  4|       deadpool|   2|[1, 2]|
    |  5|       superman|   3|   [1]|
    |  6|   harley quinn|   4|   [2]|
    |  7|          dooly|   0|   [0]|
    +---+---------------+----+------+

<br>

- 새로운 데이터 만들기
  - teams.show()
  - +---+-------------------+------+
    | id|               team|comics|
    +---+-------------------+------+
    |  1|           avengers|marvel|
    |  2|            x-force|marvel|
    |  3|     justice league|    dc|
    |  4|      suicide squad|    dc|
    |  5|guardians of galaxy|marvel|
    +---+-------------------+------+

<Br>

- 새로운 데이터 만들기
  - jobs.show()
  - +---+-------+
    | id|    job|
    +---+-------+
    |  1|   hero|
    |  2|villain|
    +---+-------+

<br>

- **join (=inner join)**
  - **join_condition = heroes["team"] == teams["id"]**
  - spark.sql("SELECT * FROM heroes JOIN teams ON heroes.team = teams.id").show()
  - heroes.join(teams, join_condition).show()
  - +---+---------------+----+------+---+--------------+------+
    | id|           name|team|   job| id|          team|comics|
    +---+---------------+----+------+---+--------------+------+
    |  1|       iron man|   1|   [1]|  1|      avengers|marvel|
    |  3|captain america|   1|   [1]|  1|      avengers|marvel|
    |  4|       deadpool|   2|[1, 2]|  2|       x-force|marvel|
    |  2|         batman|   3|   [1]|  3|justice league|    dc|
    |  5|       superman|   3|   [1]|  3|justice league|    dc|
    |  6|   harley quinn|   4|   [2]|  4| suicide squad|    dc|
    +---+---------------+----+------+---+--------------+------+

<br>

- **inner join**
  - heroes.join(teams, join_condition, "inner").show()
  - spark.sql("select * from heroes inner join teams on (heroes.team = teams.id)").show()
  - +---+---------------+----+------+---+--------------+------+
    | id|           name|team|   job| id|          team|comics|
    +---+---------------+----+------+---+--------------+------+
    |  1|       iron man|   1|   [1]|  1|      avengers|marvel|
    |  3|captain america|   1|   [1]|  1|      avengers|marvel|
    |  4|       deadpool|   2|[1, 2]|  2|       x-force|marvel|
    |  5|       superman|   3|   [1]|  3|justice league|    dc|
    |  2|         batman|   3|   [1]|  3|justice league|    dc|
    |  6|   harley quinn|   4|   [2]|  4| suicide squad|    dc|
    +---+---------------+----+------+---+--------------+------+

- **full outer join**
  - heroes.join(teams, join_condition, "outer").show()
  - +----+---------------+----+------+----+-------------------+------+
    |  id|           name|team|   job|  id|               team|comics|
    +----+---------------+----+------+----+-------------------+------+
    |   7|          dooly|   0|   [0]|null|               null|  null|
    |   1|       iron man|   1|   [1]|   1|           avengers|marvel|
    |   3|captain america|   1|   [1]|   1|           avengers|marvel|
    |   4|       deadpool|   2|[1, 2]|   2|            x-force|marvel|
    |   5|       superman|   3|   [1]|   3|     justice league|    dc|
    |   2|         batman|   3|   [1]|   3|     justice league|    dc|
    |   6|   harley quinn|   4|   [2]|   4|      suicide squad|    dc|
    |null|           null|null|  null|   5|guardians of galaxy|marvel|
    +----+---------------+----+------+----+-------------------+------+

<br>

- **left outer join**
  - heroes.join(teams, join_condition, "left_outer").show()
  - +---+---------------+----+------+----+--------------+------+
    | id|           name|team|   job|  id|          team|comics|
    +---+---------------+----+------+----+--------------+------+
    |  1|       iron man|   1|   [1]|   1|      avengers|marvel|
    |  3|captain america|   1|   [1]|   1|      avengers|marvel|
    |  2|         batman|   3|   [1]|   3|justice league|    dc|
    |  7|          dooly|   0|   [0]|null|          null|  null|
    |  5|       superman|   3|   [1]|   3|justice league|    dc|
    |  4|       deadpool|   2|[1, 2]|   2|       x-force|marvel|
    |  6|   harley quinn|   4|   [2]|   4| suicide squad|    dc|
    +---+---------------+----+------+----+--------------+------+

<br>

- **right outer**
  - heroes.join(teams, join_condition, "right_outer").show()
  - +----+---------------+----+------+---+-------------------+------+
    |  id|           name|team|   job| id|               team|comics|
    +----+---------------+----+------+---+-------------------+------+
    |   3|captain america|   1|   [1]|  1|           avengers|marvel|
    |   1|       iron man|   1|   [1]|  1|           avengers|marvel|
    |   4|       deadpool|   2|[1, 2]|  2|            x-force|marvel|
    |null|           null|null|  null|  5|guardians of galaxy|marvel|
    |   2|         batman|   3|   [1]|  3|     justice league|    dc|
    |   5|       superman|   3|   [1]|  3|     justice league|    dc|
    |   6|   harley quinn|   4|   [2]|  4|      suicide squad|    dc|
    +----+---------------+----+------+---+-------------------+------+

<br>

- **left semi : 오른쪽과 일치하는 왼쪽 데이터만 출력**
  - heroes.join(teams, join_condition, "left_semi").show()
  - spark.sql("SELECT * FROM heroes LEFT SEMI JOIN teams ON heroes.team = teams.id").show()
  - +---+---------------+----+------+
    | id|           name|team|   job|
    +---+---------------+----+------+
    |  1|       iron man|   1|   [1]|
    |  3|captain america|   1|   [1]|
    |  4|       deadpool|   2|[1, 2]|
    |  5|       superman|   3|   [1]|
    |  2|         batman|   3|   [1]|
    |  6|   harley quinn|   4|   [2]|
    +---+---------------+----+------+

<br>

- **left anti : 오른쪽과 일치하지 않는 왼쪽 데이터만**
  - heroes.join(teams, join_condition, "left_anti").show()
  - spark.sql("select * from heroes left anti join teams on (heroes.team = teams.id)").show()
  - +---+-----+----+---+
    | id| name|team|job|
    +---+-----+----+---+
    |  7|dooly|   0|[0]|
    +---+-----+----+---+

<br>

- **cross join**
  - heroes.join(teams).show()
  - 모든 경우의 수가 다 나옴
  - +---+---------------+----+------+---+-------------------+------+
    | id|           name|team|   job| id|               team|comics|
    +---+---------------+----+------+---+-------------------+------+
    |  1|       iron man|   1|   [1]|  1|           avengers|marvel|
    |  1|       iron man|   1|   [1]|  2|            x-force|marvel|
    |  2|         batman|   3|   [1]|  1|           avengers|marvel|
    |  2|         batman|   3|   [1]|  2|            x-force|marvel|
    |  3|captain america|   1|   [1]|  1|           avengers|marvel|
    |  3|captain america|   1|   [1]|  2|            x-force|marvel|
    |  1|       iron man|   1|   [1]|  3|     justice league|    dc|
    |  1|       iron man|   1|   [1]|  4|      suicide squad|    dc|
    |  1|       iron man|   1|   [1]|  5|guardians of galaxy|marvel|
    |  2|         batman|   3|   [1]|  3|     justice league|    dc|
    |  2|         batman|   3|   [1]|  4|      suicide squad|    dc|
    |  2|         batman|   3|   [1]|  5|guardians of galaxy|marvel|
    |  3|captain america|   1|   [1]|  3|     justice league|    dc|
    |  3|captain america|   1|   [1]|  4|      suicide squad|    dc|
    |  3|captain america|   1|   [1]|  5|guardians of galaxy|marvel|
    |  4|       deadpool|   2|[1, 2]|  1|           avengers|marvel|
    |  4|       deadpool|   2|[1, 2]|  2|            x-force|marvel|
    |  5|       superman|   3|   [1]|  1|           avengers|marvel|
    |  5|       superman|   3|   [1]|  2|            x-force|marvel|
    |  6|   harley quinn|   4|   [2]|  1|           avengers|marvel|
    +---+---------------+----+------+---+-------------------+------+

<br>

- **배열 데이터 조인**
  - from pyspark.sql.functions import array_contains
  - heroes.join(jobs, array_contains(heroes.job, jobs.id)).show()
  - spark.sql("SELECT * FROM heroes JOIN jobs ON array_contains(heroes.job, jobs.id)").show()
  - +---+---------------+----+------+---+-------+
    | id|           name|team|   job| id|    job|
    +---+---------------+----+------+---+-------+
    |  1|       iron man|   1|   [1]|  1|   hero|
    |  2|         batman|   3|   [1]|  1|   hero|
    |  3|captain america|   1|   [1]|  1|   hero|
    |  4|       deadpool|   2|[1, 2]|  1|   hero|
    |  5|       superman|   3|   [1]|  1|   hero|
    |  4|       deadpool|   2|[1, 2]|  2|villain|
    |  6|   harley quinn|   4|   [2]|  2|villain|
    +---+---------------+----+------+---+-------+

<br>

- **스키마를 미리 지정하고 데이터를 가져올 수 있음**

  - from pyspark.sql.types import *

    eng_colums = StructType([
        StructField('postdate', IntegerType(),True),
        StructField('transdate', IntegerType(),True),
        StructField('amount', IntegerType(),True),
        StructField('pointree', IntegerType(),True),
        StructField('maincategory', StringType(),True),
        StructField('subcategory', StringType(),True),
        StructField('store', StringType(),True),
    ])

  - card = spark.read.format("csv").option("header", "true").schema(eng_colums).load("data/card_data/csv/202010.csv")

  - card.printSchema()



- **파일 다시 저장하기**
  - card.write.format("csv").mode("overwrite").save("/tmp/csv")
  - hdfs dfs -ls /tmp/csv

<br>

- **Json 파일로 가져오기**
  - json_file = spark.read.format("json").load("data/card_data/json/202010.json")
  - json_file.show()
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

<br>

- from pyspark.sql.functions import explode, col

- json_temp = json_file.select(explode(col("list")))

- json_temp.show()

- +--------------------------+
  |                       col|
  +--------------------------+
  |{, 2990, 생활, 웰빙마트...|
  | {, 17100, 식사, 카페부...|
  |    {, 18000, 식사, , 2...|
  |{, 2990, 생활, 웰빙마트...|
  |    {, 21900, 식사, , 2...|
  |    {, 4100, 생활, CU, ...|
  | {, 1500, 식사, 카페7그...|
  |    {, 7000, 유흥, , 20...|
  |    {, 1900, 생활, CU, ...|
  |    {, 8700, 생활, CU, ...|
  |    {, 7000, 식사, , 20...|
  | {, 1500, 식사, 카페7그...|
  |    {, 8500, 식사, , 20...|
  |    {, 14000, 식사, , 2...|
  |    {, 3000, 생활, CU, ...|
  |    {, 7250, 식사, , 20...|
  |    {, 2900, 생활, CU, ...|
  |    {, 16000, 식사, , 2...|
  | {, 1500, 식사, 카페7그...|
  |    {, 40900, 교통, , 2...|
  +--------------------------+

<br>

- json_df = json_temp.select("col.*")

- json_df.show()

- json_df.write.format("json").mode("overwrite").save("/tmp/json")

<br>

- **제대로 json으로 저장되었는지 확인**
  - hdfs dfs -ls /tmp/json/
  - hdfs dfs -cat /tmp/json/*.json
  - 이렇게 확인을 해보면 row별로 json이 만들어져 있음 > 그래서 권장하지 않음

<br>

- **그 외 type**
  - parquet : spark 컬럼 기반 데이터 저장 방식
  - orc : hadoop 기반 데이터 저장 방식
  - db : (oracle, ..., mongodb, ..., hive, ...)
## SPARK

- **RDD(R esilient D istributed D atasets)**
  - Apache Spark에서 사용되는 기본적인 데이터 구조 중 하나 
  - RDD는 분산 환경에서 데이터를 나타내고 처리하는 데 사용 

<br>

- **RDD 특징**

1. **분산 데이터 구조**: 
   - RDD는 데이터를 여러 노드에 분산하여 저장하고 처리할 수 있는 분산 데이터 구조 
   - 이를 통해 대용량 데이터를 효율적으로 처리할 수 있음
2. **불변성 (Immutable)**: 
   - RDD는 한 번 생성되면 수정할 수 없음
   - 새로운 RDD를 생성하거나 변환 연산을 수행하여 데이터를 변경해야 함 
   - 이러한 불변성은 데이터 무결성을 유지하는 데 도움이 됨
3. **재계산 가능성 (Resilience)**: 
   - RDD는 여러 노드에 분산되어 저장됨 
   - 일부 노드의 장애가 발생해도 데이터의 손실을 방지할 수 있음
   - 장애 발생 시 RDD는 원본 데이터나 이전 단계의 RDD를 기반으로 재계산 가능
4. **병렬 처리**: 
   - RDD는 다수의 노드에서 동시에 처리될 수 있으므로 병렬 처리를 지원
   - 이를 통해 대규모 데이터 집합을 효율적으로 처리할 수 있음
5. **다양한 연산 지원**: 
   - RDD는 다양한 연산을 지원
   - 맵, 필터, 리듀스와 같은 함수형 프로그래밍 스타일의 연산을 포함
   - 데이터 변환 및 조작을 수행할 수 있음
6. **지연 연산 (Lazy Evaluation)**: 
   - RDD는 지연 연산의 개념을 적용함
   - 연산이 실행되지 않고, 필요한 경우에만 실제로 실행되도록 하는 것을 의미함 
   - 이로 인해 최적화와 성능 향상이 가능

<br>

- 최근 버전의 Spark에서는 DataFrame 및 Dataset과 같은 고수준의 데이터 추상화도 제공되지만, RDD는 **여전히 낮은 수준의 데이터 처리와 관련된 경우에 유용함**

<br>

- **저수준 (Low-Level)**:

  - **하드웨어 중심**: 
    - 컴퓨터 하드웨어와 밀접하게 관련된 개념 
    - CPU, 메모리, 레지스터 등과 직접적으로 상호 작용하는 작업
  - **비트 조작**: 
    - 메모리 주소, 레지스터 값 등과 같은 하드웨어 수준의 세부 사항을 다룸
  - **성능 최적화**: 
    - 성능 최적화 및 자원 효율성을 고려하는 경우가 많음
  - **프로그래밍 언어**: 
    - 어셈블리 언어(Assembly language)와 C 언어는 대표적 저수준 프로그래밍 언어

  <br>

- **고수준 (High-Level)**:

  - **추상화**: 
    - 고수준은 주로 추상화(abstraction)된 개념과 작업
    - 하드웨어 세부 사항을 숨겨서 프로그래머가 더 높은 수준에서 문제를 해결할 수 있음
  - **사용자 편의성**: 
    - 프로그래머가 더 쉽게 코드를 작성하고 읽을 수 있도록 함
  - **프로그래밍 언어**: 
    - Python, Java, C#, JavaScript 등은 고수준 언어
    - 이러한 언어는 높은 수준의 추상화와 편의성을 제공
  - **응용 프로그램 개발**: 
    - 고수준 언어 및 환경은 응용 프로그램 개발에 주로 사용됨
    - 웹 개발, 앱 개발, 데이터베이스 관리, 인공 지능 등 다양한 분야에서 활용

<br>

- SPARK 공식 문서 (RDD 파트)
  - https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html#pyspark.RDD

<br>

- SPARK 실행 시 나오는 메시지 중 체크해야 할 것
  - Spark context availableas 'sc' : RDD
  - SparkSession available as 'spark': DataFrame

<br>

- 0부터 999까지 총 1000개, 1씩 증가, partition 2개
  - rdd01 = sc.range(0, 1000, 1, 2)
  - 파티션을 분할하여 각각 처리

<br>

- PythonRDD[1] at RDD at PythonRDD.scala:53
  - 자바 기반 scala로 바뀜
  - 컴파일러 : 사람이 만든 코드를 컴퓨터가 이해할 수 있도록 바꾸는 것 (번역기)

<br>

- 파티션이 몇 개 인지 확인하고 싶을 때
  - rdd01.getNumPartitions()

<br>

- RDD의 모든 요소를 수집
  - rdd01.collect()

<br>

- RDD 개수

  - rdd01.count()

  

<br>

- 0부터 4까지 5개

  - rdd01.take(5)

  

<br>

- transformation : rdd > rdd
- action : rdd > value

<br>

- filter
  - 특정 값을 걸러줄 수 있는 함수가 있음
  - 주어진 조건에 맞는 요소만 남기는 데 사용
  - rdd02 = rdd01.filter(lambda x: x % 2) : 홀수

<br>

- 멤버 리스트 만들기
  - member = ["CaptainAmerica", "Thor", "Hulk", "IronMan", "BlackWidow", "Hawkeye", "Hulk"]
  - avengers = sc.parallelize(member, 2) : 파티션 2개로 저장
  - avengers.collect()

<br>

- 중복 삭제하기(Hulk)
  - avengers = avengers.distinct()

<br>

- 각각의 요소를 순회하면서 다 대문자로 바꾸기
  - avengers_upper = avengers.map(lambda x: x.upper())
  - avengers_upper.collect()

<br>

- 스펠링 하나씩 따로
  - avengers_upper = avengers.map(lambda x: list(x))
  - [['C', 'a', 'p', 't', 'a', 'i', 'n', 'A', 'm', 'e', 'r', 'i', 'c', 'a'], ['T', 'h', 'o', 'r'], ['H', 'u', 'l', 'k'], ['I', 'r', 'o', 'n', 'M', 'a', 'n'], ['B', 'l', 'a', 'c', 'k', 'W', 'i', 'd', 'o', 'w'], ['H', 'a', 'w', 'k', 'e', 'y', 'e']]

<br>

- flatMap
  - [[], [], [], []... ] > [, , , , ] 평평하게 1차원으로 펼침
  - avengers_flatMap = avengers.flatMap(lambda x: list(x))
  - avengers_flatMap.collect()

<br>

- cnt = sc.range(1, avengers.count()+1)
- cnt.collect()



<br>

- 2개의 rdd를 하나로 합치기
  - avengers_cnt = cnt.zip(avengers)
  - 파티션의 개수가 서로 다르기 때문에 value error 발생
  - ValueError: Can not deserialize PairRDD with different number of items in batches: (3, 5)

<br>

- 파티션 별로 어떻게 묶여있는지 확인하고 싶을 때
  - avengers.glom().collect()
  - cnt.glom().collect() : [[1, 2, 3], [4, 5, 6]]

<br>

- avengers = avengers.coalesce(1) : [['IronMan', 'BlackWidow', 'Hulk', 'CaptainAmerica', 'Thor', 'Hawkeye']]
- avengers.glom().collect()
- cnt = cnt.repartition(1)
- cnt.glom().collect() : [[4, 5, 6, 1, 2, 3]]

<br>

- **coalesce와 repartition의 차이점?**

- `coalesce`와 `repartition`은 데이터를 재분할(reshuffle)하기 위한 두 가지 메서드

  - **coalesce**:
    - `coalesce`는 데이터를 재분할할 때 데이터 셔플(shuffle)을 최소화하는 데 주로 사용
    - 즉, `coalesce`는 현재 파티션 수를 줄이거나 줄이지 않는 방향으로 데이터를 재분할
    - 데이터의 재배치 없이 파티션을 합치므로 셔플 비용이 발생하지 않음
    - 일반적으로 `coalesce`는 파티션 수를 줄이는 목적으로 사용
    - 데이터를 더 적은 파티션으로 재분할
  
  - **repartition**:
    - `repartition`은 데이터를 새로운 파티션으로 재분할
    - 즉, `repartition`은 파티션 수를 늘리거나 줄이는 데 사용됨
    - 파티션 수를 늘리는 경우, 데이터를 더 많은 파티션으로 분할하므로 셔플 비용이 발생
    - 일반적으로 `repartition`은 파티션 수를 변경하고 데이터를 셔플하는 목적으로 사용

<br>

-  `coalesce`는 주로 파티션 수를 줄이는 데 사용되며, 데이터 셔플을 최소화 
-  `repartition`은 파티션 수를 변경하고 데이터를 셔플하는 데 사용되며 파티션 수를 늘리거나 줄일 수 있음 
- 데이터 분산 및 처리 성능에 영향을 미칠 수 있으므로 적절한 메서드를 선택하는 것이 중요

<br>

- 다시 zip 으로 묶어보기
  - avengers_cnt = cnt.zip(avengers)
  - avengers_cnt.collect()
  - 이제는 개수가 맞아서 잘 합쳐짐 (파티션을 1개씩으로 묶었기 때문)
  - [(4, 'IronMan'), (5, 'BlackWidow'), (6, 'Hulk'), (1, 'CaptainAmerica'), (2, 'Thor'), (3, 'Hawkeye')]
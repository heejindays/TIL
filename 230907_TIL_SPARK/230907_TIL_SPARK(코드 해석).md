-  PySpark를 사용하여 워드 카운트 작업을 수행하는 Python 스크립트
-  입력 파일 경로와 출력 디렉터리를 받아서 실행



**import sys, re**

Python의 `sys` 모듈을 가져옴

이 모듈은 시스템과 관련된 기능을 제공하며, 명령줄 인수를 다루는 데 사용

**from pyspark import SparkContext**

SparkContext는 Spark 애플리케이션을 초기화함

Spark 클러스터와 상호 작용하는 데 사용

<br>

**sc = SparkContext()**

SparkContext 객체를 만들겠다

이제 RDD를 생성하고 작업을 수행할 수 있다

<br>

**if len(sys.argv) != 3:**

명령줄의 입력값을 살펴봐서 만약에 3이 아니라면

​    **print('wordcount.py inputFile outputDir 형태로 실행해 주세요')**

​    **sys.exit(0)**

​    위 메시지를 출력하고 스크립트를 종료한다

**else:**
    **inputFile = sys.argv[1]**
    **outputDir = sys.argv[2]**

만약 입력값이 3이라면

입력값의 1번 인덱스를 inputFile 변수에 넣고

입력값의 2번 인덱스를 outputDir 변수에 넣는다 

<br>

- 위 과정을 통해서 입력값의 개수가 옳게 들어갔는지 확인할 수 있음
-  `sys.argv`라는 리스트를 통해 스크립트를 실행할 때 
- 명령줄에 입력된 인수들을 문자열로 저장
- 스크립트 내에서 이 인수들을 활용할 수 있음

<br>

**wordcount = sc.textFile(inputFile)\ **

inputFile 경로에서 텍스트 파일을 RDD로 읽어옴 

​              **.repartition(10)\ ** 

​			  RDD를 10개의 파티션으로 다시 만듦

​              **.filter(lambda x: len(x) > 0)\ ** 

​			  RDD 각 줄에서 비어있지 않은 문자열을 필터링해서 유지

​              **.flatMap(lambda x: re.split('\W+', x))\ **

​              각 줄을 공백이나 특수 문자를 기준으로 분할하여 단어를 추출함

​              **.filter(lambda x: len(x) > 0)\ **

​              비어있지 않은 단어만 필터링해서 유지

​              **.map(lambda x: (x.lower(), 1))\ **

​              각 단어를 소문자로 바꾸고 (단어, 1) 형태로 만들어둠

​              **.reduceByKey(lambda x, y: x + y)\ **

​              동일한 단어를 그룹화하고 각 단어의 출현 횟수를 합산함

​              각 단어가 key이고 해당 단어의 출현 횟수가 value가 됨

​              **.map(lambda x: (x[1], x[0]))\ **

​               출현 횟수를 key로 하고 단어를 value로 하는 튜플로 만들기

​              **.sortByKey(ascending=False)\ **

​              출현 횟수를 기준으로 내림차순으로 정렬

​              즉, 가장 많이 나타난 단어부터 정렬

​              **.persist()**

​               RDD를 메모리에 지속적으로 저장하여 재사용 가능하게 함

<br>

- 최종적으로 텍스트 파일에서 단어를 추출하고 각 단어의 출현 횟수를 계산
- 그 이후 정렬된 형태로 결과를 wordcount RDD에 저장함

<br>

**wordcount.saveAsTextFile(outputDir)**

wordcount RDD의 결과를 텍스트 파일로 저장

outputDIR은 출력 디렉토리의 경로

각 단어와 해당 단어의 출력 횟수가 저장된 텍스트 파일이 만들어짐

<br>

**top10 = wordcount.take(10)**

wordcount RDD에서 상위 10개 항목을 가져와서

top10 변수에 저장함

<br>

**result = []**

결과를 저장할 빈 리스트 만들고

<br>

**for counts in top10:**
    **result.append(counts[1])**

top10 리스트에 들어있는 항목들 반복문 돌리는데

각 항목에서 1번 인덱스(단어)를 result 리스트에 추가해서 저장함

<br>

**print(result)** 

최종 상위 10개 단어를 출력함
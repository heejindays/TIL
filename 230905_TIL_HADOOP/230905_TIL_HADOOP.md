## HADOOP



- Hadoop Distributed File System (HDFS) 컴포넌트를 시작
  - start-dfs.sh

- Hadoop YARN (Yet Another Resource Negotiator) 컴포넌트를 시작
  - start-yarn.sh

- Hadoop 클러스터의 모든 핵심 컴포넌트를 한 번에 시작
  - start-all.sh

- 컴포넌트 시작했을 때 시작되어야 하는 것들
  - Starting namenodes on [localhost]
    Starting datanodes
    Starting secondary namenodes [localhost]
    Starting resourcemanager
    Starting nodemanagers

<br>

- jps 명령어를 통해 잘 실행되고 있는지 확인
  - 3172 ResourceManager
    2711 DataNode
    2568 NameNode
    3289 NodeManager
    2907 SecondaryNameNode

<br>

- ResourceManager
  - Hadoop 클러스터에서 작업 관리와 자원 할당을 담당하는 중요한 컴포넌트
  - 클러스터 내의 자원 (CPU, 메모리 등)을 관리
  - 클러스터에서 실행 중인 애플리케이션의 자원 요청에 대한 스케줄링을 수행

<br>

- DataNode 
  - Hadoop HDFS에서 데이터를 저장하는 물리적인 노드
  - 클러스터의 데이터 블록을 관리하고, 데이터를 저장하며, 데이터 블록을 읽고 쓰는 작업을 처리

<br>

- NameNode
  - Hadoop HDFS의 메타데이터와 파일 시스템 구조를 관리하는 중심 노드
  - 모든 파일과 디렉토리의 메타데이터와 블록 위치를 추적하고 유지

<br>

- NodeManage 
  - ResourceManager와 함께 작업을 관리하는 컴포넌트
  - 데이터 노드에서 실행되는 컨테이너를 관리하고 감시하여 자원 사용량을 보고

<br>

- SecondaryNameNode
  - NameNode의 체크포인트 작업을 보조하는 보조 데몬
  - 메타데이터를 주기적으로 백업하고, 이를 통해 빠른 복구와 데이터 손실 방지를 도와줌

<br>

- hdfs dfsadmin -report
  - Live datanodes (1): 잘 나오는지 확인

<br>

- 깃헙에서 링크로 압축 파일 다운로드
  - wget + 깃헙 다운로드 주소

- 압축을 해제함
  - unzip master.zip

<br>

- 같은 위치에 있는 파일 이름을 변경
  - mv data-master data
  - 결국 이름만 변경됨

<br>

- hdfs 명령어들 알아보기
- hdfs : Hadoop Distributed File System

<br>

- data 폴더 만들기
  - hdfs dfs -mkdir /data

<br>

- data 폴더로 업로드
  - hdfs dfs -put ~/data/shakespeare.txt /data
  - hdfs dfs -ls /data (잘 업로드 되었는지 확인)
  - hdfs dfs -head /data/shakespeare.txt

<br>

- 로컬 파일 시스템에서 HDFS로 파일을 복사
  - hdfs dfs -copyFromLocal ./data/card_data /data/card
  - hdfs dfs -ls /data/card

  <br>

- **hdfs dfs -put**

  - 이 명령어는 로컬 파일 시스템의 파일 또는 디렉토리를 HDFS로 복사하거나 이동하는 데 사용됨
  - 따라서 로컬 파일 시스템의 파일이나 디렉토리가 HDFS로 업로드 됨

- **hdfs dfs -copyFromLocal** 

  - 이 명령어도 로컬 파일 시스템의 파일을 HDFS로 복사하는 데 사용됨
  - 명령어 이름에서 알 수 있듯이 주로 로컬 파일 시스템에서 HDFS로 파일을 복사하는 데에 특화되어 있음
  - 결과적으로 로컬 파일 시스템의 파일이 HDFS로 복사됨

<br>

- 요약하면, 핵심 차이점은 명령어의 이름과 사용법에서 나타남
- 두 명령어는 모두 로컬 파일 시스템의 파일을 HDFS로 복사하는 데 사용되며, 선택적으로 사용할 수 있음

<br>

- localhost:9870

- 다운로드 받는 방법 (하둡경로 먼저 > 로컬경로 나중에)
  - hdfs dfs -get /data/shakespeare.txt ~/shakes
- -copyToLocal
  - HDFS에 저장된 파일이나 디렉토리를 HDFS에서 로컬 파일 시스템으로 가져옴
  - hdfs dfs -copyToLocal [HDFS 경로] [로컬 경로]

<br>

- 원래 명령어(좀 더 넓은 개념) : hadoop fs

- 우리가 사용한 명령 : hdfs dfs

- 위 두 명령어는 사실상 동일한 명령어도 같은 결과를 제공

<br>

- **맵리듀스(MapReduce)란?**
  - 대규모 데이터를 처리하는 데 사용되는 분산 컴퓨팅 프로그래밍 모델

<br>

1. **맵(Map)**:

   - 데이터를 나누고 각 부분에 동일한 작업을 수행하는 과정
   - 예) 텍스트 문서에서 단어를 추출하는 작업을 모든 문서의 일부에 적용하는 것

   <br>

2. **리듀스(Reduce)**:

   - 맵 단계에서 생성된 결과를 수집하고, 요약하거나 필터링하는 과정
   - 예를 들어, 모든 맵에서 얻은 단어 수를 합산하여 총 단어 수를 계산하는 것

   <br>

3. **분산 컴퓨팅**:

   - 여러 컴퓨터 또는 노드를 활용하여 데이터 처리를 병렬로 수행하는 방식
   - 빠르고 효율적인 대용량 데이터 처리를 가능하게 함

   <br>

4. **자동 병렬화**:

   - 맵리듀스 프레임워크는 작업을 자동으로 분할하고 병렬로 처리
   - 개발자는 병렬 처리에 대한 복잡한 로직을 작성할 필요가 없음

   <br>

5. **용도**:

   - 데이터 분석, 로그 처리, 검색 엔진, 웹 크롤링 등 다양한 분야에서 사용
   - 구글에서 처음 개발되었으며, Hadoop과 같은 오픈 소스 프로젝트로 유명

<br>

- 맵리듀스는 큰 문제를 작은 부분으로 나누고, 
- 각 부분을 동시에 처리한 다음 결과를 모아서 
- 원하는 결과를 얻는 방식으로 대용량 데이터 처리를 수행하는 프로그래밍 모델

<br>

- pi 추정해보자 (1,000개의 샘플로 10개의 맵)

- 준난수 몬테카를로 방법으로 파일을 추정

- hadoop jar /home/big/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar pi 10 1000
  - `hadoop jar`: Hadoop JAR 파일을 실행하는 명령어
  - `/home/big/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar`: Hadoop의 예제 JAR 파일 경로. 이 JAR 파일은 Hadoop 예제 작업을 실행하는 데 사용됨
  - `pi`: 실행할 Hadoop 예제 작업의 이름 또는 식별자 
    이 경우 "pi" 작업을 실행하려고 함
  - `10`: 몬테카를로 방법을 사용하여 추정할 원 내에 무작위로 생성되는 점의 개수. 이 값은 원주율 추정의 정확도에 영향을 미치며 더 많은 점을 생성하면 추정이 더 정확해질 수 있음
  - `1000`: 각 맵 태스크에서 생성할 점의 수. 맵리듀스 작업을 여러 맵 태스크로 분할하여 병렬로 처리하며, 각 맵 태스크는 이 수의 점을 생성하여 추정에 사용

<br>

- 워드 카운트 (wordcount)

- hadoop jar /home/big/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar wordcount /data/shakespeare.txt /output

<br>

- HDFS의 `/output` 디렉토리 안에 있는 파일 및 하위 디렉토리의 목록을 나열
  - hdfs dfs -ls /output

<br>

-  `/output` 디렉토리에 있는 특정 파일인 "part-r-*" 의 내용을 출력
  - hdfs dfs -cat /output/part-r-*
  - 와일드카드를 사용하여 여러 파일을 선택할 수 있음

<br>

- 로컬에 따로 저장하기
  - hdfs dfs -cat /output/part-r-* >> result.txt

<br>

- 하둡 STOP 종료하기
  - stop-all.sh
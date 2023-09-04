## LINUX

- vim test01

- 문서 만들기
  - echo "test shell script"
  - echo 명령어 : 주어진 텍스트나 변수 값을 화면에 출력하는 역할

- 외부에서 문서 보기
  - cat test01

- 현재위치에서 test01 열기
  - ./test01

- 소유자에게 실행 권한 부여하기
  - sudo chmod u+x test01

<br>

- vim test02
- echo "user id : $USER"
  - $USER : 현재 사용자 계정 이름을 담고 있는 변수

- echo "home dir : $HOME"
  - $HOME : 현재 사용자의 home directory 경로를 담고 있는 변수

- 권한 부여하는 또 다른 방법
  - sudo chmod 764 test02 (764 : -rwxrw-r--)

<br>

- vim test03
- #!/bin/bash
  - 가장 윗줄에 shellscript가 실행된 shell을 정의
  - name=hong-gd
  - age=100
  - addr=seoul

- echo "$name is $age years old"
- echo "$name lives in $addr"
- rwxr-xr-x 형태로 권한 부여 (숫자 사용)
- sudo chmod 755 test03
  - r (read) = 4
  - w (write) = 2
  - x (execute) = 1
  - 이 세 가지 권한을 조합하여 각각의 권한 그룹 (소유자, 그룹, 기타) 에 대한 숫자를 할당
  - 소유자 (owner): rwx = 4 (read) + 2 (write) + 1 (execute) = 7
  - 그룹 (group): r-x = 4 (read) + 0 (write) + 1 (execute) = 5
  - 기타 (others): r-x = 4 (read) + 0 (write) + 1 (execute) = 5
  - 따라서 "rwxr-xr-x" 권한은 숫자로 "755"로 표현

<br>

- vim test04.sh
  - 리눅스는 확장자가 중요하지 않지만 사용 가능
  - .sh : 쉘 스크립트를 의미함

- backtick
  - "backtick" (`)은 명령어 치환을 수행하는 데 사용

- today=`date`
  - today: 현재 날짜와 시간

- format01=$(date +%Y)
  - format01: 현재 연도 (4자리)

- format02=$(date +%y-%m)
  - format02: 현재 연도와 월 (YY-MM)

- format03=$(date +%Y/%m/%d)
  - format03: 현재 연도, 월, 일 (YYYY/MM/DD)

- time01=$(date +%T)
  - time01: 현재 시간 (HH:MM:SS)

- time02=$(date +%r)
  - time02: 현재 시간 (AM/PM 표기)

- echo "today : $today"
  echo "year : $format01"
  echo "year month : $format02"
  echo "today : $format03"
  echo "time24 : $time01"
  echo "time12 : $time02"

- expr 1 + 2
  이건 3으로 결과가 잘 나옴
  expr 3 * 4
  이건 *가 모든 것을 의미하니까 실행이 안됨
  expr 3 \* 4
  별표 앞에 역슬래시를 붙이면 곱하기로 잘 실행됨

<br>

- vim test05.sh

- 대괄호 안에 넣으면 역슬래시 없어도 동작함
  result=$[(1 + 2) * 4]
  echo $result

- 제어문
  마지막에 if를 거꾸로 쓴 fi를 써야 함
  if [ $USER = "big" ]
  then
  echo "big is data"
  fi

- if [ $USER = "test" ]
  then
  echo "$USER is test user"
  else
  echo "welcome $USER"
  fi

- if [ $USER = "test" ]
  then
  echo "$USER is test user"
  elif [ $USER = "big" ]
  then
  echo "welcom $USER"
  echo "(multicampus user)"
  else
  echo "this user is nor resistered"
  fi

<br>

- vim test06.sh

- if sudo grep $USER /etc/passwd
  then
  echo "$USER is exists passwd file"
  fi

- if [ -d $HOME/java ]
  then
  echo "java directory is exists"
  else
  echo "java directory is not exists"
  fi

- 아래 조건을 직접 넣을수도 있음
  - -e : 파일 존재 확인
  - -d : 파일 존재 및 디렉토리 인지 확인
  - -f : 파일 존재 및 파일 인지 확인
  - -r : 파일이 읽기 가능한지
  - -w : 파일이 쓰기 가능한지
  - -x : 파일이 실행 가능한지
  - -O : 파일이 현재 사용자 소유인지
  - -G : 파일이 현재 사용그룹 인지

- file=$HOME/test05.sh
  if [ -f $file ] && [ -w $file ] ; then
  echo "$file is file"
  echo "$file is writable"
  fi

<br>

- vim test07.sh

- file=~/test06.sh
  if [ -d $file ] || [ -r $file ] ; then
  echo "$file is directory"
  echo "$file is readable"
  fi

- ~ : 현재 사용자의 home directory

- echo -n "input name :"
  read name
  echo "hello, $name!"

- -n : 커서가 다음줄로 넘어가는 것 방지
- read : 사용자 입력을 읽어줌

<br>

- vim test09.sh

- case $USER in
  root )
  echo "$USER is administrator user" ;;
  big | multi )
  echo "welcome $USER" ;;
  * )
  echo "$USER is not resistreted" ;;
  esac

- 명령 뒤에 세미콜론 2개(;;) 붙여야 함

- big인 상태에서 하면?
  welcome big

- sudo ./test09.sh로 하면?
  root is administrator user

<br>

- vim test10.sh

- echo "keep study? (y/n)"
  read answer

- case $answer in
  Y | y | yes ) 
  echo "go study!!" ;;
  N | n | no)
  echo "so rest..." ;;
  *)
  echo "invalid input" ;;
  esac

<br>

- vim test11.sh

- for i in  1 2 3 4 5
  do
  echo $i
  done

<br>

- list="6 7 8 9 10"
  for i in $list
  do
  echo $i
  done

<br>

- for i in {1..10}
  do
  echo -n "$i "
  done

<br>

- for (( i=0 ; i<10 ; i++ ))
  do
  echo -n "$i "
  done

<br>

- for i in {1..10}
  do
  if [ $[ $i % 2 ] -eq 0 ] ; then
  continue
  fi
  echo "$i"
  done

<br>

- for i in {1..20..2}
  do
  echo "$i"
  done

<br>

- 아래 조건을 사용할 수 있음
  - -eq : 두 숫자가 같다
  - -ne : 같지 않다
  - -ge : 크거나 같다
  - -gt : 크다
  - -le : 작거나 같다
  - -lt : 작다

<br>

- 구구단 만들기
  for ((i = 2; i < 10; i++)); do
      echo "$i 단"

  ​	for ((j = 1; j <= 9; j++)); do
  ​    	echo "$i * $j = $((i * j))"
  ​	done

  done > gugu.txt

  echo "gugudan"

<br>

- vim test12.sh

- for file in ~/java/*
  do
  echo ${file}
  done

<br>

- vim test13.sh

- 파일인지 디렉토리인지 확인
  파일이면 [f], 디렉토리면 [d]

- for file in ~/java/*
  do
  if [ -d $file ]
  then 
  echo "[d] $file"
  elif [ -f $file ]
  then
  echo "[f] $file"
  fi
  done

<br>

- vim test14.sh

- echo -n "input num : "
  read num
  while [ $num -gt 0 ]
  do
  echo $num
  num=$[ $num - 1 ]
  done

<br>

- vim test15.sh

- echo -n "input num : "
  read num
  until [ $num -gt 0 ]
  do
  echo $num
  num=$[ $num - 1 ]
  done

- until은 while과 반대로 작동함
  until은 조건이 거짓일 때 반복

<br>

- vim test16.sh

- echo -n "input num : "
  read num

- until [ $num -eq 0 ]
  do
  echo $num
  num=$[ $num - 1 ]
  done

<br>

- 입력되는 파라미터를 알고 싶을 때
  vim test17.sh

- echo "first param : $1"
  echo "second param : $2"
  echo "zero param(filename / command) : $0"
  echo "param count : $#"
  echo "all params : $@"

<br>

- ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
  - `-t rsa`: RSA 암호화 알고리즘을 사용하여 SSH 키 쌍을 생성하도록 지정
  - `-P ''`: 비밀번호를 지정하지 않음
  - `-f ~/.ssh/id_rsa`: 생성된 SSH 키 쌍을 `~/.ssh/id_rsa` 경로와 파일 이름으로 저장

- cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
  - `~/.ssh/id_rsa.pub`: 이 파일은 현재 사용자의 공개 SSH 키를 저장하는 곳
    공개 키는 원격 서버에서 해당 사용자를 식별하는 데 사용됨
  - `~/.ssh/authorized_keys`: 원격 서버에 접근을 허용할 사용자의 공개 키 목록을 포함하는 파일. 
    원격 서버에 접속할 때 해당 사용자의 공개 키가 이 파일에 있는지 확인하고, 맞으면 접근을 허용

<br>

## HADOOP

- tar xvzf hadoop 설치 및 압축 해제

- 즐겨찾기로 이름 변경 (심볼릭)
  - ln -s hadoop-3.3.6 hadoop

- path / user 설정
  - sudo vim ~/.bashrc

- hadoop
  - export HADOOP_HOME=/home/big/hadoop
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

- hadoop user
  - export HDFS_NAMENODE_USER=big
    export HDFS_DATENODE_USER=big
    export HDFS_SECONDARYNAMENODE_USER=big
    export YARN_RESOURCEMANAGER_USER=big

- source ~/.bashrc

- vim hadoop-env.sh

  <br>

- vim core-site.xml
  - <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>

<br>

- vim hdfs-site.xml
  - <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
  - <property>
        <name>dfs.namenode.name.dir</name>
        <value>/home/big/hadoop/namenode_dir</value>
    </property>
  - <property>
        <name>dfs.datanode.data.dir</name>
        <value>/home/big/hadoop/datanode_dir</value>
    </property>
  - <property>
        <name>dfs.namenode.secondary.http-address</name>
        <value>localhost:9868</value>
    </property>

<br>

- vim mapred-site.xml
  - <property>
        <name>mapred.framework.name</name>
        <value>yarn</value>
    </property>
  - <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
    </property>
  - <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
    </property>
  - <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
    </property>

<br>

- vim yarn-site.xml
  - <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
    </property>
  - <property>
    <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>

<br>

- HDFS 네임노드와 데이터노드 포맷
  - hdfs namenode -format
    hdfs datanode -format

-  파일을 소유자만 읽고 쓸 수 있도록 함
  - chmod 0600 ~/.ssh/authorized_keys

- start-dfs.sh
  start-yarn.sh

<br>

- sudo apt install openssh-server-y

- hdfs dfsadmin -report

- Live datanodes (1):
  데이터 노드가 잘 올라갔다는 의미

- "HDFS 웹"
  - Hadoop 분산 파일 시스템 (HDFS)의 웹 인터페이스를 의미
  - HDFS 웹 인터페이스는 Hadoop 클러스터에서 실행 중인 
  - HDFS의 상태 및 정보를 검토하고 관리하는 데 사용

- localhost:9870
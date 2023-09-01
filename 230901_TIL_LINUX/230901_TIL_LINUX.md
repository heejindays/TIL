## LINUX

- 컴퓨터 운영체제의 한 종류
- 이 운영체제는 Unix 계열의 운영체제로서 개발되었으며, 오픈 소스 소프트웨어로 배포됨
- Linux는 다양한 하드웨어 플랫폼에서 실행할 수 있음 
- 개인 컴퓨터부터 서버, 임베디드 시스템, 스마트폰, 태블릿, IoT 디바이스 등 다양한 환경에서 사용

<br>

- 사용 가능한 package 정보 업데이트
  - sudo apt update

<br>

- 업그레이드 가능한 패키지들 업그레이드
  - sudo apt upgrade

<br>

- update 한 이후에, 업그레이드도 진행
  - sudo apt update && sudo apt upgrade -y

<br>

- 사용자(계정) 생성 : multi  생성
  - sudo adduser multi

<br>

- 현재 접속된 사용자의 home directory 확인
  - cd

<br>

- 현재 경로 확인
  - pwd (print working directory)

<br>

- 유저 바꾸기 (switch user)
  - su multi

<br>

- 계정@host
  - host : ip / computer 

<br>

- ~ : 나의 home directory

<br>

- 사용자를 시스템에 추가
  - sudo adduser test

<br>

- sudo : superuser do (슈퍼 유저로 일하겠다)

- superuser = root
- superuser = adminstrator = "root"

<br>

- 내 계정에 대한 정보 확인
  - id

<br>

- multi 계정에 sudo group 추가
  - sudo usermod -aG sudo multi

<br>

- 현재 디렉토리에 있는 파일과 디렉토리의 목록을 나열
  - ls

<br>

- 현재 접속되어 있는 계정 이름이 알고 싶을 때
  - whoami

<br>

- file 생성
  - touch multi01

<br>

- 디렉토리 만들기
  - mkdir test

<br>

- 복사하기 cp (copy)
  - cp multi01 multi02

<br>

- 이동하기 mv (move)
  - mv multi01 ../multi01

<br>

- 현재 위치로 mv하면 파일 이름이 변경됨
  -  현재 디렉토리에서 "multi01" 파일을 "multi"로 이름을 변경
  - mv ./multi01 ./multi

<br>

-  "multi" 파일을 "abc"로 이름을 변경
  - mv ./multi ./abc

<br>

-  "abc" 파일을 "test" 디렉토리 아래의 "def" 디렉토리로 이동
  - mv abc test/def

<br>

-  rm 파일 또는 디렉토리를 삭제
  - rm def ( "rm" 명령어를 사용하면 삭제한 파일 또는 디렉토리를 복구할 수 없음)
  - rm -i multi02 (-i : 진짜 삭제할 건지 물어보는 옵션)
  - rm: remove regular empty file 'multi02'? 
  - dir의 경우 -r 옵션 필수 ( -r 옵션은 "재귀적으로" 디렉토리 내부의 파일 및 하위 디렉토리를 삭제)
  - -rf 옵션을 사용하면 다음과 같이 디렉토리를 강제로 삭제
  - rm -rf test

<br>

- 권한

  <br>

- 아래 메시지를 해석해보면 : -rw-rw-r-- 1 multi multi test0
  - -: directory가 아니다
  - rw- : 해당 파일의 소유자가 read, write 가능
  - rw- : 해당 파일의 소유그룹이 read, write 가능
  - r-- : 타그룹은 read 가능
  - multi : 소유자
  - multi : 소유그룹

<br>

- 이 메시지를 해석해보면 : drwxr-xr-x 2 root  root  4096  9월  1 14:30 test01
  - d : directory가 맞다
  - rwx : 소유자는 read, write, execute 다 가능하다
  - r-x : 소유 그룹은 read, excute만 가능하다
  - r-x : 타그룹은 read, execute만 가능
  - 소유자 : root
  - 소유그룹 : root

<br>

- chmod  : 권한을 부여하거나 회수
- 소유자에게 x권한 부여 : 파일은 readme.txt
  - chmod u+x readme.txt

- 소유그룹에게 w권한 회수 : readme.txt
  - chmod g-w readme.txt

<br>

- chmod 400 P-team01.pem
- 해석해 보면?
  - 4 : r--
  - 0 : ---
  - 0 : ---
  - -r-------- P-team01.pem



- -rwxr--r-- : 744
- chmod 755 readme.txt : -rwxr-xr-x

<br>

- 소유자를 바꿈 (big으로)
  - sudo chown big readme.txt

<br>

- 소유그룹을 바꿈 (big으로)
  - sudo chown :big readme.txt

<br>

- 소유자:소유그룹으로 한 번에 바꿈
  - sudo chown big:big test

<br>

- 헐리우드 모드 (정신 없는 화면)
  - sudo apt install hollywood

<br>

- vim 이란?
  - 텍스트 편집기 중 하나
  - 터미널 환경에서 작동하며
  - 텍스트 파일을 효율적으로 편집할 수 있는 다양한 기능과 명령어를 제공

<br>

- vim 설치 : sudo apt install vim -y
- vim 나가고 싶을 때 : [esc]wq!
- 밖에서 구경하고 싶을 때 : cat multi.txt

<br>

- 리눅스에서는 확장자가 중요하지 않음

<br>

- 파일 압축하기
  - tar -cvzf multi.txt.tar.gz multi.txt

<br>

- 파일을 옮기고 싶을 때 (mv)
  - sudo mv multi.txt.tar.gz ../test

- 압축 해제 하는 방법
  - tar -xvzf multi.txt.tar.gz

<br>

- 위에서 10줄만 보여주기
  - sudo head /etc/sudoers

<br>

- 위에서 5줄만 보여주기

  - sudo head -n 5 /etc/sudoers

    

<br>

- 아래에서 10줄만 보여주기
  - sudo tail /etc/sudoers

<br>

- 아래에서 10줄만 보여주기
  - sudo tail -n 5 /etc/sudoers
## MongoDB (pymongo)



- 새로운 가상환경 만들어서 파이참에서 MongoDB 사용하기
- 몽고디비 데이터베이스 서버에 클라이언트 코드를 만들어서 접속
  - client = MongoClient("localhost", 27017)
  - db = client.test
  - score = db.score

<br>

- **pymongo.cursor.Cursor란?**
  - PyMongo 라이브러리를 통해 MongoDB에서 데이터를 쿼리하거나 검색한 결과를 나타내는 객체
  - pymongo.cursor.Cursor 객체는 데이터베이스 쿼리의 결과로 반환되는 반복 가능한 객체
  - 이 객체를 통해 검색된 문서(document)를 반복하고 접근할 수 있음
  - 주로 `find()` 메서드 등으로 데이터를 조회한 후에 반환되는 객체

<br>

- **pprint** 
  - "pretty print"의 줄임말
  - 복잡한 데이터 구조나 중첩된 데이터를 보기 좋게 출력해주는 기능을 제공하는 파이썬의 모듈
  - 주로 딕셔너리나 리스트와 같은 중첩된 데이터 구조를 가진 데이터를 가독성 좋게 출력할 때 사용

<br>

- **find**
  - 컬렉션(collection) 내에서 매칭되는 여러 문서(document)를 검색할 때 사용
  - 이 메서드는 지정한 조건에 맞는 모든 문서를 찾아 반환
  - 검색 결과는 `pymongo.cursor.Cursor` 객체로 반환됨
  - 이 객체를 통해 검색 결과를 순회하거나 필요한 작업을 수행할 수 있음

<br>

- **find_one**
  - 컬렉션 내에서 매칭되는 첫 번째 문서만 검색할 때 사용 
  - 이 메서드는 단일 문서를 반환하며, 검색 결과가 없는 경우 `None`을 반환

<br>

- **score.count_documents({})**
  - MongoDB의 `score` 컬렉션 내에 있는 모든 문서의 개수를 반환하는 코드
  - 이 코드는 MongoDB 데이터베이스 내의 `score` 컬렉션에 대해 빈 필터(`{}`)를 사용하여 
  - 모든 문서를 검색하고, 이렇게 검색된 문서의 개수를 반환함

<br>

- **insert_many()** 

  - 여러 개의 문서를 한 번에 컬렉션에 삽입할 때 사용

  - 리스트 형태로 문서들을 전달하여 여러 개의 문서를 한 번에 추가할 수 있음

    

<br>

- **update_one()**
  - 컬렉션 내에서 조건에 맞는 첫 번째 문서를 업데이트할 때 사용 
  - 이 메서드를 사용하여 문서의 필드를 업데이트하거나 변경할 수 있음

<br>

- **matched_count**
  - 업데이트 작업 시 적용된 필터 조건과 일치하는 문서의 수
  - 즉, 업데이트가 적용될 조건과 일치하는 문서의 수

<br>

- **modified_count**
  - 실제로 업데이트된 문서의 수
  - `update_many()` 메서드에서 `update` 파라미터에 `$set` 또는 
  - 다른 업데이트 연산자를 사용하여 업데이트한 필드가 있는 경우에만 증가

<br>

- pymongo.command_cursor.CommandCursor
  - PyMongo 라이브러리를 사용하여 MongoDB에서 실행하는 명령의 결과를 다루기 위한 도구
  - MongoDB에서 명령을 실행하면 그 결과로 반환되는 객체
  - 이 객체를 사용하여 명령의 실행 결과를 가져올 수 있음
  - 즉 명령을 실행한 후 그 결과를 확인하고 처리하는 데 사용되는 객체 
  - 이 객체는 MongoDB 서버에 특정 작업을 요청하고 그 결과를 받아올 때 사용됨

<br>

### GeoJSON 형태로 입력하기

- 기본 코드 형식
  - 아래 형식으로 넣어야 편하게 바로 입력 가능
  - location: {
          type: "Point",
          coordinates: [-73.856077, 40.848447]
    }

<br>

- 중요한 포인트 
  - list the **longitude** first, and then **latitude**.

<br>

- geospatial query 사용
- db.mongobucks02.createIndex({location: "2dsphere"})
  - MongoDB 데이터베이스에서 `mongobucks02` 컬렉션에 대해 
  - 2D 공간 인덱스를 생성하는 작업을 수행
  - 지리 위치 정보를 효율적으로 저장하고 검색하기 위한 인덱스
  - `db.mongobucks02`: "mongobucks02"라는 컬렉션
  - `createIndex({location: "2dsphere"})`:  "mongobucks02" 컬렉션에 대한 인덱스를 생성
  - `location`이라는 필드에 대해 2D 공간 인덱스를 생성하겠다는 의미
  - `"2dsphere"`: 생성하려는 인덱스의 유형 
  - `"2dsphere"`는 MongoDB에서 지리 공간 데이터를 인덱싱하기 위해 사용되는 유형 중 하나
  - 2D 공간 인덱스는 위도와 경도와 같은 지리 위치 정보를 효율적으로 인덱싱하여 
  - 검색 및 분석에 사용할 수 있게 해주는 역할을 함
  - 이렇게 생성된 인덱스를 사용하면 지리 위치 기반의 쿼리를 효율적으로 수행할 수 있음
  - (예: 주변의 위치 찾기, 지리 범위 내의 위치 찾기 등)

<br>



**세종대학교 국제캠퍼스 위치를 기준으로 예제 만들기 **

**[127.0736345, 37.5518018]**

<br>

- 내 위치와 가까운 순서대로 나열

- $near : 내 위치랑 가까운 순서대로

- $geometry : 이 위치가 내 위치야
  - db.mongobucks02.find({
        location: {
            $near: {
                $geometry: { type: "Point", coordinates: [127.0736345, 37.5518018] }
            }
        }
    })

<br>

- 거리 순서대로 나열하되, 실제 거리까지 나오도록
  - db.mongobucks02.aggregate([
        {
            $geoNear: {
                near: { type: "Point", coordinates: [127.0736345, 37.5518018] },
                spherical: true,
                query: { s_name: /역/ }, 
                distanceField: "distance"
            }
        }
    ])

<br>

- 아래 3개 지점을 삼각형으로 만들었을 때, 그 위치 안에 들어있는 지점들을 알아보고 싶을 때

- 강변역 127.094695, 37.535098
- 서울숲역 127.044703, 37.543655
- 군자역 127.079415, 37.557193

- **주의사항! 다각형을 그릴 땐, 처음 위치로 다시 돌아와야 함**
  - db.mongobucks02.find({
        location: {
            $geoIntersects: {
                $geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [127.094695, 37.535098],
                            [127.044703, 37.543655],
                            [127.079415, 37.557193],
                            [127.094695, 37.535098]
                        ]
                    ]
                }
            }
        }
    })

<br>

- **중심 주변 안에 있는 지점들을 알고 싶을 때 (원 형태)**
  - `mongobucks02` 컬렉션에서 
  - 중심 좌표 `[127.0736345, 37.5518018]` 주변의 반경 0.5 마일 내에 있는 문서들을 검색
  - db.mongobucks02.find({
        location: {
            $geoWithin: {
                $centerSphere: [
                    [127.0736345, 37.5518018],
                    0.5 / 3963.2
                ]
            }
        }
    })


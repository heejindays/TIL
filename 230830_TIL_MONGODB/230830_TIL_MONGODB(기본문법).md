## MongoDB



- NoSQL 데이터베이스 시스템의 하나

- 문서 지향적인 데이터 저장 방식을 사용하여 구조화되지 않은 데이터를 저장하고 처리

- 오픈 소스 데이터베이스

- 자바스크립트 기반의 언어를 사용함

- 자바스크립트처럼 함수를 만들어서 사용할 수 있음

  function test(){
  print("mongodb");
  }

  test();





- **mongodb는 collection을 따로 만들지 않아도 insert를 할 때 바로 만들어짐**

  - db.jstest.insertOne({name:"mongo", class:"ds"})
  - db.jstest.insertOne({name:"postgre", age:100, class:"de"})

  

  



- **하나 추가하고 싶을 때**
- db.collection.insertOne( document )
  - db.multi.insertOne({name:"hong-gd", class:"de", midterm: {Kor:100, eng:60, math:80}})





- **여러 개 추가하고 싶을 때**

  - db.collection.insertMany( [  document, document, ...      ]  )
  
  - db.multi.insertMany([
  
     { name: "kim-sd", class: "ds", kor: 100, eng: 100, math: 40 },
  
      { name: "kang-hd", class: "de", kor: 80, eng: 50, math: 70 }
  
      { name: "you-js", class: "de", kor: 96, eng: 40, math: 100 }
  
    ]);
  
  



- **multi라는 collection에서 document들을 출력하겠다**
  **(MongoDB에서 컬렉션은 관계형 데이터베이스(RDBMS)의 테이블과 유사한 개념)**
  
  



- **날짜도 자바스크립트처럼 가능**

  - var today = new Date();

  

  

- **이미 만들어진 collection에 추가하는 것도 가능**
  
  - db.multi.insertOne({name : 'shin-dy', kor:90, eng:100, math:60})
  
  



- **. (마침표) : 참조연산자 (~안에)**
  
  - db.jstest : db안에 jstest라는 collection을 만들겠다는 의미
  
  



- **multi 라는 collection에서 document들을 출력**
  
- db.multi.find()
  

  
  
  
- show dbs
  
- // admin   40.00 KiB > root database
  
- // config  72.00 KiB > shard 정보 저장 database
  
- // local   40.00 KiB > 복제되지 않는 database 
  
  - (여기에 만든 collection들은 shard에 복제되지 않음)
  
- // test    72.00 KiB > 연습 database
  
  



- **BSON : Binary JSON**
  - MongoDB에서 사용되는 이진 형식의 데이터 표현 방식
  
  - BSON은 JSON(JavaScript Object Notation)의 확장된 형태
  
  - MongoDB의 데이터를 직렬화하고 저장하기 위해 사용
  
    



- **쿼리(조건)는 딱히 지정하지 않고 비워둘 수 있음**
  
  - db.multi.find({}, {name:1})
  
  



- **id는 안보이게 하고 name만 보고 싶다면**
  
  - db.multi.find({}, {_id:0, name:1})
  
  



- **class가 없으면 안보임(보여줄 수 있는 만큼만 보임)**
  
  - db.multi.find({}, {_id:0, name:1, class:1})
  
  



- **midterm이 없으면 없는대로 가져와서 출력해줌**
  
  - db.multi.find({}, {_id:0, midterm:1})
  
  



- **클래스가 'de'인 것만 출력**
  
  - db.multi.find({class:'de'})
  
  



- **midterm이라는 필드가 존재하는 document 들만 출력**
  
  - (해당 필드의 존재 여부에 대한 검색)
  - db.multi.find({midterm:{$exists:true}})
  
  



- **midterm 필드 안의 kor 값이 50보다 크거나 같은 document 출력**
  
  - gte : Greater Than or Equal
  - db.multi.find({"midterm.kor": {$gte: 50}})
  
  



- **kor 값이 80보다 작거나 같은 document 출력**
  
  - db.multi.find({kor: {$lte:80}})
  
  



- **100점보다 작고 80점보다 크거나 같은 document 출력**
  
  - 조건이 여러개면 $and로 묶어야 함
  - db.multi.find({ $and: [ {kor: {$lt: 100}}, {kor: {$gte: 80}} ] })
  
  



- **k가 중간에 들어가는 것들 출력 (like '%k%')**
  
  - 정규표현식 사용해야 함
  - db.multi.find({ name: {$regex:'k'} })
  - db.multi.find({ name: {$regex:/k/} })
  - db.multi.find({ name: { $regex: /k/ } }, { _id: 0, name: 1 })
  
  



- **정렬 : 1(asc) / -1(desc)**
  
- db.multi.find().sort({name:1})
  
  
  
  
  
- **아래 두 쿼리는 같은 의미(정렬)**
  
  - select * from multi order by name desc;
  - db.multi.find().sort({name:-1})
  
  



-  **_id 필드를 제외하고 name과 kor 필드만을 반환**
  
-  **kor 필드를 기준으로 내림차순으로 정렬**
  
-  **최대 2개의 결과만 반환**
  
  -  db.multi.find({}, { _id: 0, name: 1, kor: 1 }).sort({ kor: -1 }).limit(2)
  

  

  
- **영어 점수 가장 높은 사람**

  -  db.multi.find({}, { _id: 0, name: 1, eng: -1 }).sort({ eng: -1 }).limit(1)
  -  db.multi.find().sort({eng:-1}).limit(1)

  



- **영어 점수 가장 낮은 사람**
  
  - db.multi.find().sort({ eng: 1 }).limit(1)
  
  



- **id 필드를 제외한 모든 필드를 반환**
  
  - 첫 번째 문서를 건너뛰고 나머지 문서들을 반환
  - db.multi.find({}, {_id:0}).skip(1)
  
  



- **update 하고 싶을 때**
  
  - db.multi.updateOne({name:/hong/}, {$set: {name: "홍길동"}})
  
  



- **update 이후 잘 바뀌었는지 확인**
  
  - db.multi.find({}, {_id:0})
  
  



- **update와 replace의 차이**
  
  - db.multi.replaceOne({midterm: {$exists:true}}, {name:"hong-gd", kor:100, eng:0, math:0})
  - db.multi.replaceOne({ midterm: { $exists: true }, name: "hong-gd" }, { name: "hong-gd"kor: 100, eng: 0, math: 0 })
  - db.multi.updateMany({kor: {$lte:90}}, {$set: {kor:0}})
  
  
  
  


- matchedCount : 내가 바꾸려는 갯수

- modifiedCount : 변경된 것들의 갯수

  

  

- updateOne : 조건에 맞는거 찾아서 1개 바꾸기 (field)
  
- updateMany : 조건에 맞는거 찾아서 다 바꾸기 (field)
  
- replaceOne : 조건에 맞는거 찾아서 문서 변경 (document)
  
  

  
  
- **hong-gd 하나를 지우고 싶음**
  
  
- db.multi.deleteOne({name:'hong-gd'})
  - deletedCount: 1

  
  
  
  
- **class 있는 걸 다 지우고 싶음**
  
  
- db.multi.deleteMany({class: {$exists: true}})
  - deletedCount: 3

  
  
  
  
- **delete로 지우면 아직 남아있음**
  

  - db.multi.deleteMany({})

  
  
  
  
- **drop으로 지우면 collection까지 다 사라짐**
  

  - db.multi.drop()

  
  
  
  
- **두 개의 문서를 두 개의 다른 방식으로 myfriends 컬렉션에 추가할 수 있음**
  
  
  - (방법1) db.myfriends.insert({name:'아이언맨', buddy: ['토르', '헐크', '호크아이']})
  - (방법2) db.myfriends.insertOne({name: '슈퍼맨', buddy: ['배트맨', '원더우먼', '아쿠아맨', '조커']})
  
  



- **name이 아이언맨인 문서에 추가 하기**
  
  - db.myfriends.updateOne({name:'아이언맨'}, {$push: {buddy : {$each: ['캡틴아메리카', '블랙위도우']}}})
  
  



- **삭제 (pull도 가능)**
  
  - db.myfriends.updateOne({name:'슈퍼맨'}, {$pop: {buddy:1}})
  
  



- **aggregate :**

  - MongoDB에서 복잡한 데이터 처리 작업을 수행하기 위해 사용되는 
  - 집계(aggregation) 파이프라인

  

  - 예시

    db.multi.aggregate([
      { $match: { kor: { $gt: 50 } } },
      { $project: { kor: 1 } },
      { $group: { _id: 'test', 'average': { $avg: '$kor' } } }
    ]);

  

  1. `$match`: "kor" 필드가 50보다 큰 값을 가진 문서를 필터링
  2. `$project`: 결과 문서에서 "kor" 필드만을 유지
  3. `$group`: 결과 문서들을 하나의 그룹으로 묶고, "kor" 필드의 평균을 계산





- **새로운 collection 추가**

  

  - db.score.insertMany([
       {name:"홍길동",kor:90,eng:80,math:98,test:"midterm"},
       {name:"이순신",kor:100,eng:100,math:76,test:"final"},
       {name:"김선달",kor:80,eng:55,math:67,test :"midterm"},
       {name:"강호동",kor:70,eng:69,math:89,test:"midterm"},   
       {name:"유재석",kor:60,eng:80,math:78,test:"final"},
       {name:"신동엽",kor:100,eng:69,math:89,test:"midterm"},
       {name:"조세호",kor:75,eng:100,math:100,test:"final"}
    ])

    

  - db.score.aggregate(
    	{$project: {_id:0, name:1, kor:1, eng:1, math:1}}
    	)_

    

  - db.score.aggregate(
    	{$group: {_id:'$test', average: {$avg: '$kor'}}}
    	)





 - **(문제) test가 final인 document들만 가지고 eng 필드만 사용하여 eng 필드 평균을 출력**

 - 결과형태 : _id : 'test'. average:

  

  - db.score.aggregate(
    {$match: {test:'final'}},
    {$project: {eng:1}},
    {$group: {_id:'test', average: {$avg: '$eng'}}}
    )
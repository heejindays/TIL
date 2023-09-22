## Elasticsearch

- **데이터 복사**
  - /var/lib/mysql-files/ 밑에 데이터 복사하면 
  - mysql에서 table에 데이터 입력 가능
  - sudo cp data/card_data/csv/202009.csv /var/lib/mysql-files/card.csv

<br>

- **mysql 실행하기**
  - mysql -u root -p

<br>

- **mysql에 테이블 만들기**

  - use mysql;

    CREATE TABLE card (
        postdate VARCHAR(8),
        transdate VARCHAR(8),
        amount INTEGER,
        pointree VARCHAR(100),
        maincategory VARCHAR(100),
        subcategory VARCHAR(100), 
        store VARCHAR(100)
    );

    LOAD DATA INFILE '/var/lib/mysql-files/card.csv'
    INTO TABLE card
    FIELDS TERMINATED BY ','
    IGNORE 1 rows;

  

- **elasticsearch 다운로드**

  - wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.10.0-linux-x86_64.tar.gz

  - 압축 해제 및 즐겨찾기 지정
    - tar xvzf elasticsearch-8.10.0-linux-x86_64.tar.gz
    - ln -s elasticsearch-8.10.0 elastic

<br>

- **logstatch 다운로드**
  - wget https://artifacts.elastic.co/downloads/logstash/logstash-8.10.0-linux-x86_64.tar.gz
  - 압축 해제 및 즐겨찾기 지정
    - tar xvzf logstash-8.10.0-linux-x86_64.tar.gz
    - ln -s logstash-8.10.0 logstash

<br>

- **kibana 다운로드**
  - wget https://artifacts.elastic.co/downloads/kibana/kibana-8.9.2-linux-x86_64.tar.gz
  - 압축 해제 및 즐겨찾기 지정
    - tar xvzf kibana-8.9.2-linux-x86_64.tar.gz
    - ln -s kibana-8.9.2 kibana

<br>

- 설정하기
- sudo apt install vim -y
- sudo vim ~/.bashrc
  - export ELASTIC_HOME=/home/ubuntu/elastic
  - export LOGSTASH_HOME=/home/ubuntu/logstash
  - export KIBANA_HOME=/home/ubuntu/kibana
  - export PATH=$PATH:$ELASTIC_HOME/bin:$LOGSTASH_HOME/bin:$KIBANA_HOME/bin

<br>

- 전체 출력 (10개만 보여줌)
  - get card/_search

<br>

- 전체 카운트
  - get card/_count

<br>

- id를 가지고 데이터 하나 선택
  - id -> document_id
  - get card/_doc/1

<br>

- field의 type 확인
  - get card/_mapping

<br>

- maincartegory가 "식사"인 데이터만 출력
  - get card/_search
    {
    	"query": {
    		"term": {
    			"maincategory": {
    				"value": "식사"
    			}
    		}
    	}
    } 

<br>

- 위와 동일한 코드
  - get card/_search
    {
    	"query": {
    		"bool": {
    			"must": [
    				{
    					"match": {
    						"maincategory": "식사"
    					}
    				}
    			]
    		}
    	}
    } 

<br>

- filter
  - get card/_search
    {
    	"query": {
    		"bool": {
    			"filter": [
    				{
    					"term": {"maincategory": "식사"}
    				}
    			]
    		}
    	}
    }

<br>

- match + filter

- maincategory가 식사이면서 subcategory가 분식인
  - get card/_search
    {
    	"query": {
    		"bool": {
    			"must": [
    				{
    					"match": {"maincategory": "식사"}
    				}
    			],
    			"filter": [
    				{
    					"term": {"subcategory": "분식"}
    				}
    			]
    		}
    	}
    }

<br>

- subcategory가 카페인 데이터들 중에 amount가 5000 이상인 데이터만
  - get card/_search
    {
    	"query": {
    		"bool": {
    			"must": [
    				{"match": {"subcategory": "카페"}}
    			],
    			"filter": [
    				{"range": {"amount": {"gte": 5000}}}
    			]
    		}
    	}
    }

<br>

- must : and

- should : or
  - get card/_search
    {
    	"query": {
    		"bool": {
    			"should": [
    				{"match": {"subcategory": "카페"}},
    				{"match": {"subcategory": "도서"}}
    			]
    		}
    	}
    }

<br>

- operator를 통한 조건 연결
  - get card/_search
    {
    	"query": {
    		"match": {
    			"subcategory": {
    				"query": "카페 도서",
    				"operator": "or"
    			}
    		}
    	}
    }

<br>

- 집계 : aggs

- maincategory로 groupby
  - get card/_search
    {
    	"aggs": {
    		"maincate": {
    			"terms": {
    				"field": "maincategory.keyword"
    			}
    		}
    	}
    }

<br>

- min
  - get card/_search
    {
    	"aggs": {
    		"min_amount": {
    			"min": {"field": "amount"}
    		}
    	}
    }

<br>

- amount가 0보다 크면서 가장 작은 값은?
  - get card/_search
    {
    	"query": {
    		"bool": {
    			"filter": [
    				{"range": {"amount": {"gte": 0}}}
    			]
    		}
    	},
    	"aggs": {
    		"min_amount": {
    			"min": {
    				"field": "amount"
    			}
    		}
    	}
    }

<br>

- histogram
  - get card/_search
    {
    	"aggs": {
    		"histogram_aggs": {
    			"histogram": {
    				"field": "amount",
    				"interval": 10000
    			}
    		}
    	}
    }

<br>

- sql로 검색
  - get _sql?format=txt
    {
    	"query": """
    		select * from card
    		"""
    }

<br>

- 여러가지 형태 가능
  - get _sql?format=csv
    {
    	"query": """
    		select postdate, maincategory, subcategory, store, amount
    		from card
    		"""
    }
  - get _sql?format=json
    {
    	"query": """
    		select postdate, maincategory, subcategory, store, amount
    		from card
    		"""
    }

<br>

- cursor를 이용해 다음 데이터를 가져올 수 있음
  - get _sql?format=json
    {
    	"query": """
    		select postdate, maincategory, subcategory, store, amount
    		from card
    		order by postdate
    		""",
    	"fetch_size": 5
    }
  - get _sql?format=json
    {
    	"query": """
    		select postdate, maincategory, subcategory, store, amount
    		from card
    		order by postdate
    		""",
    	"fetch_size": 5,
    	"cursor": ""
    }

<br>

- 변환 (sql -> query dsl)
  - get _sql/translate
    {
    	"query": """
    		select postdate, maincategory, subcategory, store, amount
    		from card
    		order by postdate
    		"""
    }
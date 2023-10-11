## **감성분석**

- 문서의 주관적인 감성/의견/감정/기분등을 파악하기 위한 방법
- 소셜 미디어, 여론조사, 온라인 리뷰, 피드백 등의 분야에서 활용됨
- 문서 내 텍스트가 나타내는 여러 가지 주관적인 단어와 문맥을 기반으로 감성(Sentiment) 수치를 계산함
- 긍정 감성 지수와 부정 감성 지수로 구성됨




```python
# 1. 지도학습 기반 감성 분석

import pandas as pd
```

- id : 각 데이터의 id
- sentiment : 영화평(review)의 Sentiment 결과값 (1은 긍정 / 0은 부정)
- review : 영화평의 텍스트 내용


```python
review_df = pd.read_csv('C:\workspaces\Sentiment Analysis\labeledTrainData.tsv', header=0, sep="\t", quoting=3)
review_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>sentiment</th>
      <th>review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>"5814_8"</td>
      <td>1</td>
      <td>"With all this stuff going down at the moment ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>"2381_9"</td>
      <td>1</td>
      <td>"\"The Classic War of the Worlds\" by Timothy ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>"7759_3"</td>
      <td>0</td>
      <td>"The film starts with a manager (Nicholas Bell...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>"3630_4"</td>
      <td>0</td>
      <td>"It must be assumed that those who praised thi...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"9495_8"</td>
      <td>1</td>
      <td>"Superbly trashy and wondrously unpretentious ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>24995</th>
      <td>"3453_3"</td>
      <td>0</td>
      <td>"It seems like more consideration has gone int...</td>
    </tr>
    <tr>
      <th>24996</th>
      <td>"5064_1"</td>
      <td>0</td>
      <td>"I don't believe they made this film. Complete...</td>
    </tr>
    <tr>
      <th>24997</th>
      <td>"10905_3"</td>
      <td>0</td>
      <td>"Guy is a loser. Can't get girls, needs to bui...</td>
    </tr>
    <tr>
      <th>24998</th>
      <td>"10194_3"</td>
      <td>0</td>
      <td>"This 30 minute documentary Buñuel made in the...</td>
    </tr>
    <tr>
      <th>24999</th>
      <td>"8478_8"</td>
      <td>1</td>
      <td>"I saw this movie as a child and it broke my h...</td>
    </tr>
  </tbody>
</table>
<p>25000 rows × 3 columns</p>
</div>




```python
print(review_df['review'][0])
```

    "With all this stuff going down at the moment with MJ i've started listening to his music, watching the odd documentary here and there, watched The Wiz and watched Moonwalker again. Maybe i just want to get a certain insight into this guy who i thought was really cool in the eighties just to maybe make up my mind whether he is guilty or innocent. Moonwalker is part biography, part feature film which i remember going to see at the cinema when it was originally released. Some of it has subtle messages about MJ's feeling towards the press and also the obvious message of drugs are bad m'kay.<br /><br />Visually impressive but of course this is all about Michael Jackson so unless you remotely like MJ in anyway then you are going to hate this and find it boring. Some may call MJ an egotist for consenting to the making of this movie BUT MJ and most of his fans would say that he made it for the fans which if true is really nice of him.<br /><br />The actual feature film bit when it finally starts is only on for 20 minutes or so excluding the Smooth Criminal sequence and Joe Pesci is convincing as a psychopathic all powerful drug lord. Why he wants MJ dead so bad is beyond me. Because MJ overheard his plans? Nah, Joe Pesci's character ranted that he wanted people to know it is he who is supplying drugs etc so i dunno, maybe he just hates MJ's music.<br /><br />Lots of cool things in this like MJ turning into a car and a robot and the whole Speed Demon sequence. Also, the director must have had the patience of a saint when it came to filming the kiddy Bad sequence as usually directors hate working with one kid let alone a whole bunch of them performing a complex dance scene.<br /><br />Bottom line, this movie is for people who like MJ on one level or another (which i think is most people). If not, then stay away. It does try and give off a wholesome message and ironically MJ's bestest buddy in this movie is a girl! Michael Jackson is truly one of the most talented people ever to grace this planet but is he guilty? Well, with all the attention i've gave this subject....hmmm well i don't know because people can be different behind closed doors, i know this for a fact. He is either an extremely nice but stupid guy or one of the most sickest liars. I hope he is not the latter."



```python
# 태그, 영어가 아닌 숫자나 특수문자는 모두 공란으로 변경해야 함
# 정규표현식 사용

import re
```


```python
# <br> html 태그가 있다면 공백으로 replace 하기
review_df['review'] = review_df['review'].str.replace('<br/>', ' ')
```


```python
# re를 이용해서 영어 문자열이 아니면 모두 공백으로 바꾸기
review_df['review'] = review_df['review'].apply(lambda x: re.sub("[^a-zA-Z]", " ", x))
```


```python
# 결정 값 클래스인 sentiment 칼럼을 별도로 추출한 뒤 결정값 데이터 세트 만들기
from sklearn.model_selection import train_test_split

class_df = review_df["sentiment"]
```


```python
# 원본 데이터 세트에서 id와 sentiment 칼럼 삭제 해서 피터 데이터 세트 만들기
feature_df = review_df.drop(['id', 'sentiment'], axis=1, inplace=False)
```


```python
X_train, X_test, y_train, y_test = train_test_split(feature_df, class_df, test_size=0.3, random_state=156)

# 학습용 데이터는 17,500개의 리뷰
# 테스트용 데이터는 7,500개의 리뷰
X_train.shape, X_test.shape
```




    ((17500, 1), (7500, 1))




```python

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# CountVectorizer : 문서 집합을 토큰으로 나누고, 토큰의 출현 빈도를 세어 Bag of Words를 만듦
# TfidfTransformer : TF-IDF(Term Frequency-Inverse Document Frequency)를 계산하여 단어에 가중치 부여 (단어의 상대적 중요성)


from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

```

<br>

### 1) Count 벡터화를 적용해서 예측 성능 측정


```python
# Pipeline 클래스를 사용하여 텍스트 데이터를 처리하고 분류 모델을 적용하는 파이프라인을 만듦
# ngram_range=(1,2) : 최소 길이가 1이고 최대 길이가 2인 n-gram을 사용
# C : 로지스틱 회귀 모델의 규제 매개변수 (C=10은 중간 정도의 규제)
pipeline = Pipeline([
    ('cnt_vect', CountVectorizer(stop_words='english', ngram_range=(1,2))),
    ('lc_clf', LogisticRegression(solver='liblinear', C=10))
])

pipeline.fit(X_train['review'], y_train)
pred = pipeline.predict(X_test['review'])

# 이진 분류 문제이므로  [:, 1]는 모든 행(:)에 대해 두 번째 열(인덱스 1)을 선택
# 모델이 예측한 각 샘플이 클래스 1에 속할 확률을 나타내는 값들의 배열을 생성
pred_probs = pipeline.predict_proba(X_test['review'])[:,1]

print(f'예측 정확도 : {accuracy_score(y_test, pred)}')
print(f'ROC-AUC : {roc_auc_score(y_test, pred_probs)}')
```

    예측 정확도 : 0.8869333333333334
    ROC-AUC : 0.9505469639198725

<br>

### 2) TF-IDF 벡터화를 적용해 예측 성능 측정


```python
# C : 로지스틱 회귀 모델의 규제 매개변수 (C=10은 중간 정도의 규제)
pipeline = Pipeline([
    ('tfidf_vect', TfidfVectorizer(stop_words='english', ngram_range=(1,2))),
    ('lc_clf', LogisticRegression(solver='liblinear', C=10))
])

pipeline.fit(X_train['review'], y_train)
pred = pipeline.predict(X_test['review'])
pred_probs = pipeline.predict_proba(X_test['review'])[:,1]

print(f'예측 정확도 : {accuracy_score(y_test, pred)}')
print(f'ROC-AUC : {roc_auc_score(y_test, pred_probs)}')
```

    예측 정확도 : 0.8932
    ROC-AUC : 0.9600004979512861

<br>

### 비지도 학습 기반 감성 분석

- Lexicon을 기반으로 함
- 감성 사전은 긍정(positive) 감성 또는 부정(Negative) 감성의 정도를 의미하는 수치를 가침
- 이를 감성 지수(Polarity score)라고 함
- 이 감성 기수는 단어의 위치나 주벼 단어, 문맥, POS(Part of Speech) 등을 참고하여 결정됨

<br>

### 1) SentiWordNet을 이용한 감성 분석


```python
import nltk
nltk.download('all')
```

    True


```python
from nltk.corpus import wordnet as wn

term = 'present'

# 'present' 라는 단어로 wordnet의 synset 생성
# synsets: WordNet에서 특정 단어의 동의어 세트(synset)를 나타내는 객체들의 리스트
# 동일한 단어가 여러 의미를 가질 수 있기 때문에 하나의 단어에 대해 여러 synset이 존재
synsets = wn.synsets(term)
print('synsets() 반환 type :', type(synsets))
print('synsets() 반환값 개수 type :', len(synsets))
print('synsets() 반환값 :', synsets)
```

    synsets() 반환 type : <class 'list'>
    synsets() 반환값 개수 type : 18
    synsets() 반환값 : [Synset('present.n.01'), Synset('present.n.02'), Synset('present.n.03'), Synset('show.v.01'), Synset('present.v.02'), Synset('stage.v.01'), Synset('present.v.04'), Synset('present.v.05'), Synset('award.v.01'), Synset('give.v.08'), Synset('deliver.v.01'), Synset('introduce.v.01'), Synset('portray.v.04'), Synset('confront.v.03'), Synset('present.v.12'), Synset('salute.v.06'), Synset('present.a.01'), Synset('present.a.02')]

```python
for synset in synsets :
    print('#### Synset name :', synset.name(), '####') # synset.name(): 현재 synset의 이름
    print('POS:', synset.lexname()) # synset.lexname(): 현재 synset의 품사(POS)
    print('Definition:', synset.definition()) # synset.definition(): 현재 synset의 정의
    print('Lemmas:', synset.lemma_names()) # synset.lemma_names(): 현재 synset에 속하는 단어의 기본형
```

    #### Synset name : present.n.01 ####
    POS: noun.time
    Definition: the period of time that is happening now; any continuous stretch of time including the moment of speech
    Lemmas: ['present', 'nowadays']
    #### Synset name : present.n.02 ####
    POS: noun.possession
    Definition: something presented as a gift
    Lemmas: ['present']
    #### Synset name : present.n.03 ####
    POS: noun.communication
    Definition: a verb tense that expresses actions or states at the time of speaking
    Lemmas: ['present', 'present_tense']
    #### Synset name : show.v.01 ####
    POS: verb.perception
    Definition: give an exhibition of to an interested audience
    Lemmas: ['show', 'demo', 'exhibit', 'present', 'demonstrate']
    #### Synset name : present.v.02 ####
    POS: verb.communication
    Definition: bring forward and present to the mind
    Lemmas: ['present', 'represent', 'lay_out']
    #### Synset name : stage.v.01 ####
    POS: verb.creation
    Definition: perform (a play), especially on a stage
    Lemmas: ['stage', 'present', 'represent']
    #### Synset name : present.v.04 ####
    POS: verb.possession
    Definition: hand over formally
    Lemmas: ['present', 'submit']
    #### Synset name : present.v.05 ####
    POS: verb.stative
    Definition: introduce
    Lemmas: ['present', 'pose']
    #### Synset name : award.v.01 ####
    POS: verb.possession
    Definition: give, especially as an honor or reward
    Lemmas: ['award', 'present']
    #### Synset name : give.v.08 ####
    POS: verb.possession
    Definition: give as a present; make a gift of
    Lemmas: ['give', 'gift', 'present']
    #### Synset name : deliver.v.01 ####
    POS: verb.communication
    Definition: deliver (a speech, oration, or idea)
    Lemmas: ['deliver', 'present']
    #### Synset name : introduce.v.01 ####
    POS: verb.communication
    Definition: cause to come to know personally
    Lemmas: ['introduce', 'present', 'acquaint']
    #### Synset name : portray.v.04 ####
    POS: verb.creation
    Definition: represent abstractly, for example in a painting, drawing, or sculpture
    Lemmas: ['portray', 'present']
    #### Synset name : confront.v.03 ####
    POS: verb.communication
    Definition: present somebody with something, usually to accuse or criticize
    Lemmas: ['confront', 'face', 'present']
    #### Synset name : present.v.12 ####
    POS: verb.communication
    Definition: formally present a debutante, a representative of a country, etc.
    Lemmas: ['present']
    #### Synset name : salute.v.06 ####
    POS: verb.communication
    Definition: recognize with a gesture prescribed by a military regulation; assume a prescribed position
    Lemmas: ['salute', 'present']
    #### Synset name : present.a.01 ####
    POS: adj.all
    Definition: temporal sense; intermediate between past and future; now existing or happening or in consideration
    Lemmas: ['present']
    #### Synset name : present.a.02 ####
    POS: adj.all
    Definition: being or existing in a specified place
    Lemmas: ['present']

```python
# path_similarity() 를 이용해 'tree','lion', 'tiger', 'cat', 'dog' 단어의 상호 유사도 알아보기

tree = wn.synset('tree.n.01')
lion = wn.synset('lion.n.01')
tiger = wn.synset('tiger.n.01')
cat = wn.synset('cat.n.01')
dog = wn.synset('dog.n.01')

entities = [tree, lion, tiger, cat, dog]
similarities = []
entity_names = [entity.name().split('.')[0] for entity in entities]
```


```python
# 다른 단어의 synset과 유사도를 측정
for entity in entities:
    similarity = [round(entity.path_similarity(compared_entity), 2)
                for compared_entity in entities]
    similarities.append(similarity)

# 유사도를 데이터 프레임으로 저장
similarity_df = pd.DataFrame(similarities, columns=entity_names, index=entity_names)
similarity_df
```



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }


    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tree</th>
      <th>lion</th>
      <th>tiger</th>
      <th>cat</th>
      <th>dog</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>tree</th>
      <td>1.00</td>
      <td>0.07</td>
      <td>0.14</td>
      <td>0.08</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>lion</th>
      <td>0.07</td>
      <td>1.00</td>
      <td>0.08</td>
      <td>0.25</td>
      <td>0.17</td>
    </tr>
    <tr>
      <th>tiger</th>
      <td>0.14</td>
      <td>0.08</td>
      <td>1.00</td>
      <td>0.09</td>
      <td>0.17</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>0.08</td>
      <td>0.25</td>
      <td>0.09</td>
      <td>1.00</td>
      <td>0.20</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>0.12</td>
      <td>0.17</td>
      <td>0.17</td>
      <td>0.20</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
import nltk
from nltk.corpus import sentiwordnet as swn

senti_synsets = list(swn.senti_synsets('slow'))
print('senti_synsets() 반환 type :', type(senti_synsets))
print('senti_synsets() 반환값 개수:', len(senti_synsets))
print('senti_synsets() 반환값 :', senti_synsets)
```

    senti_synsets() 반환 type : <class 'list'>
    senti_synsets() 반환값 개수: 11
    senti_synsets() 반환값 : [SentiSynset('decelerate.v.01'), SentiSynset('slow.v.02'), SentiSynset('slow.v.03'), SentiSynset('slow.a.01'), SentiSynset('slow.a.02'), SentiSynset('dense.s.04'), SentiSynset('slow.a.04'), SentiSynset('boring.s.01'), SentiSynset('dull.s.08'), SentiSynset('slowly.r.01'), SentiSynset('behind.r.03')]


- sentisynset 객체는 단어의 감성을 나타내는 감성지수와 객관성을 나타내는 객관성 지수가 있음
- 감성 지수는 다시 긍정 지수와 부정 지수로 나뉨


```python
# father(아버지)와 fabulous(멋진) 두 개 단어의 감성 지수와 객관성 지수 살펴보기

import nltk
from nltk.corpus import sentiwordnet as swn

father = swn.senti_synset('father.n.01')
print('father 긍정 지수 :', father.pos_score())
print('father 부정 지수 :', father.neg_score())
print('father 객관성 지수 : ', father.obj_score())
print('\n')
fabulous = swn.senti_synset('fabulous.a.01')
print('fabulus 긍정 지수:', fabulous.pos_score())
print('fabulus 부정 지수:', fabulous.neg_score())
print('fabulus 객관성 지수:', fabulous.obj_score())
```

    father 긍정 지수 : 0.0
    father 부정 지수 : 0.0
    father 객관성 지수 :  1.0
    fabulus 긍정 지수: 0.875
    fabulus 부정 지수: 0.125
    fabulus 객관성 지수: 0.0


​    

<br>

### SentiWordNet을 이용해 감성 분석을 수행하는 순서

- 문서(document)를 문장(Sentence) 단위로 분해
- 다시 문장을 단어(Word) 단위로 토큰화하고 품사 태깅
- 품사 태깅된 단어 기반으로 synset 객체와 senti_synset 객체를 생성
- senti_synset 객체에서 긍정 감성/부정 감성 지수를 구함
- 이를 모두 합산하여 특정 값 이상일 때 긍정 감성으로, 아닐 때 부정 감성으로 결정


```python
from nltk.corpus import wordnet as wn

# WordNet 기반의 품사 태그로 변환

def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startwith('N'):
        return wn.NOUN
    elif tag.startwith('R'):
        return wn.ADV
    elif tag.startwith('V'):
        return wn.VERB

```


```python
# polarity score 합산하기
# 다 더한 감성지수가 0 이상일 경우 긍정, 아닐 경우 부정 감성으로 예측하자

from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

# Penn Treebank 품사 태그를 WordNet 품사로 변환
def penn_to_wn(tag):
    if tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('V'):
        return wn.VERB
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('J'):
        return wn.ADJ
    return None

def swn_polarity(text):
    # 초기화
    sentiment = 0.0
    tokens_count = 0

    lemmatizer = WordNetLemmatizer()
    raw_sentences = sent_tokenize(text)

    for raw_sentence in raw_sentences:
        tagged_sentence = pos_tag(word_tokenize(raw_sentence))
        for word, tag in tagged_sentence:
            wn_tag = penn_to_wn(tag)
            if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                continue

            lemma = lemmatizer.lemmatize(word, pos=wn_tag)
            if not lemma:
                continue

            synsets = wn.synsets(lemma, pos=wn_tag)
            if not synsets:
                continue

            # 모든 단어에 대해 긍정은 +로 부정은 -로 합산해 총점 계산
            synset = synsets[0]
            swn_synset = swn.senti_synset(synset.name())
            sentiment += (swn_synset.pos_score() - swn_synset.neg_score())
            tokens_count += 1

    if not tokens_count:
        return 0
    
    # 총 score가 0 이상일 경우 긍정(positive) 1, 아닐 경우 부정(negative) 0 반환
    if sentiment >= 0:
        return 1

    return 0


```


```python
# DataFrame에 'preds' 열 추가
review_df['preds'] = review_df['review'].apply(lambda x: swn_polarity(x))

# 예측값과 실제값 가져오기
y_target = review_df['sentiment'].values
preds = review_df['preds'].values
```

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score
import numpy as np


```python
print(confusion_matrix(y_target, preds))
print("정확도:", np.round(accuracy_score(y_target, preds), 4))
print("정밀도:", np.round(precision_score(y_target, preds), 4))
print("재현율:", np.round(recall_score(y_target, preds), 4))
```

    [[7669 4831]
     [3644 8856]]
    정확도: 0.661
    정밀도: 0.647
    재현율: 0.7085


- 정확도가 약 66%이고 재현율이 약 70.9%임
- 정확도 지표를 포함한 전반적인 성능 평가 지료는 만족스러울만한 수치는 아님

<br>

## 최종 정리

- Natural Language Toolkit (NLTK)를 사용하여 주어진 텍스트의 감성 지수를 계산

- 해당 텍스트가 긍정적인지 혹은 부정적인지 예측하는 함수를 정의

<br>

- Penn Treebank 품사 태그를 WordNet 품사로 변환하는 함수 정의 (penn_to_wn)

- Penn Treebank에서 사용되는 품사 태그를 WordNet에서 사용되는 품사로 변환하는 함수

    - 감성 분석에 사용될 단어의 품사를 정확히 지정하기 위해서

<br>

- 감성 지수 계산 및 예측 함수 정의 (swn_polarity)

    - 주어진 텍스트를 문장으로 나눔

    - 각 문장을 단어로 토큰화하고 각 단어의 품사를 태깅

    - 각 단어에 대해 WordNet 품사로 변환하고, 해당 단어의 기본형을 얻음

    - 기본형 단어에 대한 WordNet Synset을 찾음

    - Synset이 존재하면, 해당 단어의 긍정 및 부정 감성 점수를 계산하고 총 감성을 업데이트

    - 최종적으로, 모든 단어에 대한 긍정 및 부정 감성 점수를 합산한 총 감성 점수를 반환

    - 총 감성 점수가 0 이상인 경우, 함수는 1을 반환하여 긍정적인 감성으로 예측

    - 그렇지 않으면 0을 반환하여 부정적인 감성으로 예측

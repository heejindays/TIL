# HTML (6/11)

## 1) title

```html
<h1>제목</h1>
    <h2>글자</H2>
    <h3>크기</h3>
    <h4>지정</h4>
    <h5>하는</h5>
    <h6>태그</h6>

    <div>영역을 정의</div> 
    <!--div는 영역을 정의-->
    <div>
        <p>단락을 정의</p> 
        <!--영역 안에서 단락을 정의-->
        <p>단락을 정의</p>
    </div>
```

## 2) TEXT

```html
<h1>Text</h1>

    <!--웹 접근성 태그들 : strong, em, ...-->

    <p>
        <b>진하게 (&lt;b&gt;)</b><br/>
        <strong>강하게 (&lt;strong&gt;)</strong><br/>

        <i>기울임(&lt;i&gt;)</i><br/>
        <em>강조하여(&lt;em&gt;)</em><br/>

        <small>작은 텍스트, 코멘트 (&lt;small&gt;)</small><br/>
        
        위<sup>첨자</sub>(&lt;sup&gt;)<br/>
        아래<sub>첨자</sub>(&lt;sub&gt;)<br/>

        <ins>내용 추가(&lt;ins&gt;)</ins><br/>
        <del>내용 삭제(&lt;del&gt;)</del><br/>
    </p>
```

## 3) image

```html
<h1>img</h1>

    <img src="resourses/images/image.png" 
         alt="이미지"
         width="400px"
         height="400px">
    <!-- src = 현재 이미지 파일 경로-->
    <!-- alt = 제대로 나오지 않을 때 메시지-->

    <!--
        pt : 포인트 (1pt = 0.72인치)
        px : 픽셀 (해상도 별 상대 크기)
        %, em : 지정 / 상속 등에 대한 백분율 (상대 크기)
    -->

    <a href="index.html">
        <img src="resourses/images/image.png" width="200px" height="200px">
    </a>

    <img src="resourses/images/image.png"
        width="200px" height="200px" usemap="#my">

    <map name="my">
        <area shape="rect" coords="25, 25, 175, 175" href="index.html"/>

        <!-- map : 그림 내 일부 구역을 클릭했을 때 이동할 수 있도록 하는 기능 -->
    </map>

```

## 4) ANCHOR

```html
 <h1>&lt;a&gt;</h1> 
    
    <!-- 다른 페이지(링크)로 이동 -->
    <a href="http://lc.multicampus.com/k-digital"> mlp</a>
    <br/>

    <a href="#a">1번으로</a><br>
    <a href="#b">2번으로</a><br>
    <a href="#c">3번으로</a><br>

    <!-- 같은 페이지 내에서 이동이 가능하다 -->
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

    <p id="a">1번</p>

    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

    <p id="b">2번</p>

    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

    <p id="c">3번</p>

    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
```

## 5) LIST


```html
    <!-- ordered list -->

    <ol>
        학원 오는 순서
        <li>눈을 뜬다</li>
        <li>일어나서 씻는다</li>
        <li>버스정류장으로 간다</li>
            <ol>
                <li>171번 버스를 기다린다</li>
                <li>버스를 타고 목적지 근처에서 내린다</li>
            </ol>
        </li>
        <li>걷는다</li>
    </ol>


    <!-- unordered list -->
    <ul>
        점심 메뉴
        <li>달걀</li>
        <li>한식
            <ul>
                <li>양념게장</li>
                <li>닭갈비</li>
                <li>김밥</li>
                <li>갈비찜</li>
                <li>계란찜</li>
            </ul>
        </u1>
        <li>양식
            <ul>
                <li>피자</li>
                <li>햄버거</li>
            </ul>
        </li>
    </u1>

    <!-- definition or description list (들여쓰기로 구분)-->

    <dl>
        <dt>학원 커리큘럼</dt>
        <dd>python</dd>
        <dd>html, css, js, jq</dd>
        <dd>django</dd>
        <dd>crawling</dd>
        <dd>
            <dl>
                <dt>science</dt>
                <dd>ml</dd>
                <dd>dl</dd>
            </dl>
            <dl>
                <dt>engineer</dt>
                <dd>hadoop</dd>
                <dd>spark</dd>
            </dl>
        </dd>
    </dl>
```

## 6) TABLE

```html
    <h1>table</h1>

    <h2>기본테이블</h2>
    <table>
        <tr> 
            <!-- th는 볼드처리, 가운데 정렬 -->
            <th>컬럼1</th>
            <th>컬럼2</th>
        </tr>
        <tr>
            <td>데이터1</td>
            <td>데이터2</td>
        </tr>
        <tr>
            <td>데이터3</td>
            <td>데이터4</td>
        </tr>
    </table>

    <h2>추가</h2>
    <table border="1">
        <caption>테이블 제목</caption>
        <!-- 캡션 : 테이블 제목을 가운데 정렬로 -->
        <colgroup>
                <col width="100px" />
                <col width="300px" />
                <col width="400px" />
                <!-- col : 각 컬럼에 적용 -->
        </colgroup>

        <thead>
            <tr>
                <th>컬럼1</th>
                <th>컬럼2</th>
                <th>컬럼3</th>
                <!-- 가운데 정렬 & 볼드 처리 -->
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
            </tr>
            <tr>
                <td>4</td>
                <td>5</td>
                <td>6</td>
            </tr>
            <tr>
                <td>7</td>
                <td>8</td>
                <td>9</td>
            </tr>
        </tbody>
        <tfoot><tr><td>foot1</td><td>foot2</td><td>foo3</td></tr></tfoot>
        <!-- 위치와 관계 없이 테이블 제일 아래에 -->
    </table>



    <h2>셀 병합</h2>

    <table border="1">
        <col width="200px">
        <col width="200px">
        <col width="200px">
        <col width="200px">
        <tr>
            <th>컬럼1</th>
            <th>컬럼2</th>
            <th>컬럼3</th>
            <th>컬럼4</th> 
        </tr>
        <tr>
            <td rowspan="2">1 (행 합치기)</td>
            <!-- rawspan : 행 2개를 하나로 합친다 -->
            <td>2</td>
            <td>3</td>
            <td>4</td>
        </tr>
            <td>6</td>
            <td colspan="2">7 (열 합치기)</td>
            <!-- colspan : 열 2개를 하나로 합친다 -->
      
        <tr>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
        </tr>
        <tr>
            <td colspan="4" align="center"> 행 4개 다 합치기</td>
        </tr>
    </table>
```

## 7) LAYOUT 1
```html
    <style>
        *{
            padding: 0px;
            margin: 0px;
        }
        div{
            border: 1px dashed blue;
            margin: 10px;
        }
        #body{
            height: 400px;
        }
        #left{
            width: 48%;
            height: 90%;
            float: left;
        }
        #right{
            width: 48%;
            height: 90%;
            float: right;
        }
    </style>
</head>
<body>
    
    <div id="header">
        <h1>제목</h1>
        <div>
            <span><a href="#">메뉴1</a></span>
            <span><a href="#">메뉴2</a></span>
            <span><a href="#">메뉴3</a></span>
            <span><a href="#">메뉴4</a></span>
        </div>
    </div>

    <div id="body">

        <div id="left">
            <p>내용1</p>
        </div>
        <div id="right">
            <p>내용2</p>
        </div>
    </div>

    <div id="footer">
        <address>copyright&copy; all right...</address>
    </div>
```

## 8) LAYOUT2

```html
<style>
        *{
            padding: 0px;
            margin: 0px;
        }
        .html5{
            border: 1px dotted red;
            margin: 10px;
        }
        section{
            height: 400px;
        }

        #left{
            width: 48%;
            height: 90%;
            float: left;
        }
        #right{
            width: 48%;
            height: 90%;
            float: right;
        }
    </style>

</head>
<body>
    
    <header class="html5">
        <h1>제목</h1>

        <nav class="html5">
            <span><a href="#">메뉴1</a></span>
            <span><a href="#">메뉴2</a></span>
            <span><a href="#">메뉴3</a></span>
            <span><a href="#">메뉴4</a></span>
        </nav>
    </header>

    <section class="html5">
        <article class="html5" id="left">
            <p>내용1</p>
        </article>
        <article class="html5" id="right">
            <p>내용2</p>
        </article>
    </section>

    <footer class="html5">
        <address>copyright&copy; all rights resered ...</address>
    </footer>
```

## 9) FORM
```html
    <form action="html10-form-res.html" method="get">
        <fieldset>
            <legend>회원가입</legend>

            <p>ID : <input type="text" name="id"></p>
            <p>pw : <input type="password" name="pw"></p>
            <p>이메일 수신 여부
                <input type="radio" name="rdo" value="y">y<br>
                <input type="radio" name="rdo" value="n">n<br>
            </p>
            <p>
                관심분야
                <input type="checkbox" name="web" value="web">WEB<br>
                <input type="checkbox" name="ai" value="ds">AI<br>
                <input type="checkbox" name="eng" value="de">Engineer<br>
            </p>
            <P>
                하고싶은 말
                <textarea name="etc" cols="30" rows="10"></textarea>
            </P>
            <p>
                <input type="button" value="그냥 버튼"><br/>
                <input type="submit" value="전송"><br/>
                <input type="reset" value="취소"><br/>
            </p>
        </fieldset>
    </form>
```

## 10) SELECT
```html
 <h1>select</h1>

    <form action="html10-form-res.html" method="get">
        <p>점심
            <select name="lunch">
                <option value="kimbab">김밥</option>
                <option value="bulgogi">불고기</option>
                <option value="samkubsal">삼겹살</option>
                <option value="ddukbokki">떡볶이</option>
            </select>
        </p>
        <p>저녁
            <select name="dinner">
                <optgroup label="한식">
                    <option value="dakbokumtang">닭볶음탕</option>
                    <option value="jeyukbokem">제육볶음</option>
                    <option value="kimchijjigae">김치찌개</option>
                    <option value="kimchibokumbab">김치볶음밥</option>
                    <option value="a-gu-jjim">아구찜</option>
                    <option value="miyortkguk">미역국</option>
                </optgroup>
                <optgroup label="한식">
                    <option value="steak">스테이크</option>
                    <option value="pasta">파스타</option>
                    <option value="puagra">푸아그라</option>
                </optgroup>
            </select>
        </p>
        <P>
            <input type="submit" value="선택">
        </P>
    </form>
```
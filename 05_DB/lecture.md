# 05. Database

| 분류                   | 개념                                                         | 예시                                        |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| DDL - 데이터 정의 언어 | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE<br />DROP<br />ALTER                 |
| DML - 데이터 조작 언어 | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 언어          | INSERT<br />SELECT<br />UPDATE<br />DELETE  |
| DCL - 데이터 제어 언어 |                                                              | GRANT<br />REVOKE<br />COMMIT<br />ROLLBACK |



### CREATE statement

```bash
$ sqlite3 tutorial.sqlite3 # SQLite 파일 생성
> .database #데이터 베이스 생성
> .mode csv
> .import hellodb.csv examples # hellodb.csv 파일을 examples 테이블로 넘김
> .tables
examples
> .headers on
> .mode column
```

```sqlite
CREATE TABLE TABLE_NAME 
(value1 value1_type PRIMARY KEY,
value2 value2_type NOT NULL,
value3 value3_type NOT NULL);
```



### DROP statement

```sqlite
DROP TABLE_NAME;
```



### INSERT statement (C)

```sqlite
INSERT TABLE_NAME (COLUMN1, COLUMN2 ...) VALUES (VALUE1, VALUE2 ...);
```



### SELECT statement (R)

* SELECT
  * 테이블에서 데이터를 조회
  * SELECT문은 SQLite에서 가장 복잡한 문이며 다양한 절(clause)와 함께 사용
* LIMIT
  * 쿼리에서 반환되는 행 수를 제한
  * 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
* WHERE
  * 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정 

* DISTINCT
  * 조회 결과에서 중복행을 제거
  * SELECT 바로 뒤에 작성한다.
* OFFSET
  * 동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지의 위치 변화량을 나타내는 정수형

```sqlite
SELECT COLUMN1, COLUMN2, .... FROM TABLE_NAME;
SELECT COLUMN1, COLUMN2, .... FROM TABLE_NAME LIMIT NUMBER;
SELECT COLUMN1, COLUMN2, .... FROM TABLE_NAME LIMIT Number OFFSET NUMBER;
SELECT COLUMN1, COLUMN2, .... FROM TABLE_NAME WHERE C;
SELECT DISTINCT COLUMN FROM TABLE_NAME;
```



### DELETE statement (D)

```sqlite
 DELETE FROM Table_name WHERE Condition
```

* 삭제하고 나서
* SQLite 에서는 기본적으로 id값을 재활용한다

* AUTOINCREMENT (장고에서는 기본적으로 사용되는 column 속성)

  * SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용 하는 것을 방지

    



### UPDATE statement (U)

* 기존 행의 데이터를 수정
* SET clause에서 테이블의 각 열에 대해 새로운 값을 설정

```sqlite
UPDATE TABLE_NAME SET COLUMN1=VALUE1, COLUMN2=VALUE2 ... WHERE CONTIDIONs;
```



### WHERE

```sqlite
SELECT COLUMN1, COLUMN2, .... FROM TABLE_NAME WHERE C;
----------------------------------------------------------
ex)
SELECT * FROM users WHERE age >= 30;
SELECT age, first_name FROM users WHERE age>=30 and last_name='김';
```



### SQLite Aggregate Function (집계함수)

* COUNT(*), AVG, SUM, MIN, MAX

  ```sqlite
  SELECT COUNT(COLUMN_NAME) FROM TABLE_NAME;
  
  SELECT AVG(COLUMN_NAME) FROM TABLE_NAME WHERE CONDITIONS;
  
  SELECT COLUMN_NAME1, MAX(COLUMN_NAME2) FROM TABLE_NAME;
  
  SELECT AVG(COLUMN_NAME) FROM TABLE_NAME WHERE CONDITIONS;
  ```

  

### LIKE

* wildcards
  * % (percent sign) : 이자리에 문자열이 있을 수도, 없을 수도 있다.
  * _ (underscore): 반드시 이 자리에 한개의 문자가 존재해야 한다.

```sqlite
SELECT * FROM TABLE_NAME WHERE COLUMN_NAME LIKE 'WILDCARD_PATTERN';
```



### ORDER BY clause

* ORDER BY
  * 조회 결과 집합을 정렬
  * SELECT 문에 추가하여 사용
  * 정렬 순서를 위한 2개의 keyword 제공
    * ASC - 오름차순 (default)
    * DESC - 내림차순

```sqlite
SELECT * FROM TABLE_NAME ORDER BY COLUMN_NAME ASC;
SELECT * FROM TABLE_NAME ORDER BY COLUMN_NAME1, COLUMN_NAME2 DESC;
```



### GROUP BY clause

* GROUP BY
  * 행 집합에서 요약 행 집합을 만듦
  * SELECT 문의 optional 절
  * 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
  * 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 와야 함

```sqlite
SELECT COLUMN_NAME, AGGREGATE_FUNCTION(COLUMN_NAME2) FROM TABLE_NAME GROUP BY COLUMN_NAME1, COLUMN_NAME2;
```



### ALTER TABLE

* ALTER TABLE의 3가지 기능
  1. table 이름 변경
  2. 테이블에 새로운 column 추가
  3. column 이름 수정
  4. column 삭제

```sqlite
ALTER TABLE TABLE_NAME RENAME TO NEW_TABLE_NAME;

-- 새로운 컬럼 추가
ALTER TABLE TABLE_NAME ADD COLUMN NEW_COLUMN_NAME TEXT NOT NULL; -- 에러 발생 (기존 데이터는 널값이기 때문에)

-- 1. NOT NULL 설정 없이 추가하기
ALTER TABLE TABLE_NAME ADD COLUMN NEW_COLUMN_NAME TEXT;

-- 2. NOT NULL 설정 유지하면서 추가하기
ALTER TABLE TABLE_NAME ADD COLUMN NEW_COLUMN_NAME TEXT NOT NULL DEFAULT DEFAULT_VALUE;

-- 컬럼 이름 바꾸기
ALTER TABLE TABLE_NAME RENAME COLUMN COLUMN_NAME TO NEW_COLUMN_NAME:

-- 컬럼 지우기
ALTER TABLE TABLE_NAME DROP COLUMN COLUMN_NAME;
```


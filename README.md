# Python 언어 practice
## 기초
* 변수와 리터럴
> a=100; b='good morning' a,b는 변수/ 100은 정수 리터럴, good morning은 문자열 리터럴

* 숫자형
    * 정수형(integer) : 100
    * 부동 소수점 숫자형(float) : 3.14, 314E-2

* 문자열
    * 작은 따움표로 묶어준다. 'good \n morning' 
    > good

    morning

    * 순문자열의 경우 -> r'good \n morning'과 같이 r을 써준다.
    > good \n morning

* 자료형 ★ => type(변수)으로 확인해준다.
1. 정수형(int)
2. 실수형(float)
3. 문자열(str)
4. 튜플(tuple)
5. 리스트(list)★
6. 딕셔너리(dict)★

* 논리적, 물리적 명령행
    * 한 줄에 여러 명령 작성 시 ';' 사용
    * 여러 줄에 하나의 명령 작성 시 줄 바뀔 때 '\n'사용

* 들여쓰기

## 연산자와 수식
* 연산자

|연산자|결과|
|:--:|:--:|
|10/2|5|
|10%2|0|
|10%3|1|
|10//2|5 -> 몫 반환|
|==(같은)|비교할 때|
|=(대입)|값 대입할 때|

## 사용자 입력과 출력
### 사용자 입력
* input() 사용
> tip! 여러개 한 번에 입력 받고 싶다면?
>> a,b = input().**split()**  자료형 지정하고 싶다면
 a,b = ***map***(float,input().split())


### 사용자 출력
* print() 사용
> tip! 같은 자료형끼리 '+'로 묶을 수 있지만 다른 자료형끼리는 묶을 수 없다!  다른 자료형끼리는 ','로 묶는다.

* print() 사용 예시

 ```py

name = 'parkminuk'; age = 22
print(f.'{name}은 {age}살 입니다.') #혹은
print('{}은 {}살 입니다. '.format(name,age))
```

## 리스트


## 딕셔너리 


## if문


## 반복문(for문/while문)



## 함수



# Python 언어 practice
## 기초
* 변수와 리터럴
> a=100; b='good morning' a,b는 변수/ 100은 정수 리터럴, good morning은 문자열 리터럴

* 숫자형
    * 정수형(integer) : 100
    * 부동 소수점 숫자형(float) : 3.14, 314E-2

* 문자열
    * 작은 따움표로 묶어준다. 'good \n morning' 
    > good\
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
```py
a = [1,2,3,'a','b']
``` 
* '[]'(대괄호)를 사용하여 감싸 주고 각 요소값은 쉼표로 구분해준다.
* 리스트 안 요소에 또 다른 리스트가 올 수 있다. (2차원,3차원~~가능)
* 리스트 안 요소가 모두 같은 자료형일 필요는 없다.


## 딕셔너리 
```py
b = {'kor':93,'eng':88,'math':90} # 하나의 요소(?)가 key값과 value값으로 만들어짐
c = {'park':[93,88,72],'kim':[80,74,69],'hong':[99,100,66]} # value값에 리스트가 올 수 있다.
```
* 딕셔너리 요소 추가와 삭제
> 추가는 **dict_name[KEY] = Value**로 한다.
> 삭제는 **del dict_name[KEY]**로 한다.


## if문
* X in s : s안에 X가 있으면 참, 없으면 거짓
* X not in s : s안에 X가 없으면 참, 있으면 거짓

* 한 줄 if문 사용 예제
 ```py
#1
# score = int(input('점수는 : '))
# if score >=80:
#     print('합격')
# else:
#     print('불합격')

# 한 줄 if문으로 변경
score = int(input('점수는 : '))
# print('합격') if score>=80 else print('불합격') 
result = '합격' if score>=80 else '불합격'

print(result)
```


## 반복문(for문/while문)
### for문 

* **range(시작:끝:증감)** 을 사용한 반복문
    * 시작은 생략하면 0, 끝((ex)len(리스트))
* 리스트 내포(comprehension)★
    * 리스트 안에서 for문 사용


### while문
* while(조건문):

    * while(1(무한반복))

    
## 함수
* 함수 작성의 필요성 : 
    * 반복해서 코딩해야 하는 부분을 함수로 만들어 호출한다.
    * 흐름을 알아보기 쉽게 하기 위해서이다.

* 함수 구조
```py
def funtion_name(매개변수): # 매개변수 : 값을 전달받는 변수
    <처리할 문장1>
    <처리할 문장2>

    return 반환값 # 반환하지 않아도 된다.
```

* 입력값(매개변수)과 결과값(반환값)에 따른 함수의 형태
> 단!! 입력값 != 매개변수★


    * 1. 입력값 o, 반환값 o 
    ```py
    def caculate(x,y):
        sum = x + y
        mul = x * y

        return sum,mul # 반환값 : sum,mul

    a,b = input('연살할 값 두 개를 입력하세요. ').split()
    sum,mul = caculate(a,b) # 입력값 : a,b
    ```


    * 2. 입력값 x, 반환값 o
    ```py
    def string():
        hello = '안녕하세요!!'

        return hello # 반환값 : hello
    
    hi = string() # 입력값 : x
    print(hi) # 안녕하세요!!
    ```
    

    * 3. 입력값 o, 반환값 x
    ```py
    def my_data(name,age,major):
        print(f'{name}의 나이는 {age}이고 전공은 {major}입니다. ')

    a = 'parkminuk'
    b = 23
    c = 'datacomunication'

    my_data(a,b,c) # 입력값 : a,b,c
    ```

    * 4. 입력값 x, 반환값 x
    ```py
    def direct():
        print('입력값이 없고 반환값도 없습니다. ')

    direct()
    ```
    
## lambda 함수
* 한 줄로 된 함수
* 함수 구조
```py
add = lambda a,b:a+b # add(함수명) = lambda a,b(매개변수):a+b(반환값)
sum = add(5,4)
print(sum)
```


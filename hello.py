# a=0;b=4

'''print(a+b,a+10,a-b);print(a*b,a/b,a//b)
print(3//2,5//2,a%3)
print(a**2,a**3)'''

'''
name = input('이름을 입력하세요. '); age = int(input('나이를 입력하세요. ')) # input은 문자열로 받는다!!!!!

print(f'{name}의 나이는 {age}입니다.')
print('{}의 나이는 {}입니다. '.format(name,age))

print('%s의 나이는 %d입니다. ' %(name,age))
'''



# name = '박민욱'; score = 76.521

# print('{:>5}의 성적은{:.2f}입니다. '.format(name,score))


'''
name = []

for i in range(5) : 
    na = input("이름을 입력하세요. ")
    name.append(na)
    
print(name)
'''

'''
name = [input("이름입력 : ") for i in range(5)]

print(name)
'''
 #d4=dict(d2,**d3) #**의 뜻은??

'''
a = {}
b = []

for i in range(3) :
    name = input('이름을 입력하세요 : ') 
    score = input('점수를 입력하세요. ')
    a[name]=score

print(a) # 딕셔너리 만들기

# 딕셔너리 key, value 분리하기
print(list(a.keys())) 
print(list(a.values()))

name_1 = list(a.keys())
score_1 = list(a.values())

# 리스트 만들기
for i,j in zip(name_1,score_1) :
    b.append([i,j])
    
print(b)
'''

# say = "\"Python is very easy.\" he says." # \사용하여 큰 따옴표 문자열 포함시키기

# name_score = [["박민욱",85],["홍길동",75]]
# name=[]
# score =[]

# for i,j in name_score :
#     name.append(i)
#     score.append(j)
    

# for i in range(len(name)):
#     print(name[i],score[i])
    


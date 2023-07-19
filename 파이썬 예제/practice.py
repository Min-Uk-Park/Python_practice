name,age,score = input('이름, 나이, 점수를 입력하세요. ').split()

print('1',name,age,score)
print('2 {}의 나이는 {}살 입니다. '.format(name,age))
print('3 {}의 성적은 {:.2f}점 입니다. '.format(name,score)) # 안되는 이유는?? ans) input으로 받은 데이터는 자료형이 str이다!!





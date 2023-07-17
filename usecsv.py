import csv,re,os

def opencsv(filename):
    # newline = ''필요한가????????????★
    with open(filename,'r',encoding='cp949',newline='') as f: # 파일을 읽기/쓰기 형태로 f로 연다(가져온다.)
        reader = csv.reader(f) # f를 읽는다
        output= []
        # output = list(reader) 첫 번째 방식
        for i in reader:
            output.append(i) 
    # with open() as 변수 => close(변수) 해서 return 하기 전 파일 닫아주는 함수 안 써도 된다.
    return output
    

def writecsv(filename,data):
    with open(filename,'w',newline='',encoding='Euc-KR') as f:
        a = csv.writer(f,delimiter=',') # 리스트 형태의 요소를 하나씩 쓰므로 구분기호를 ','로 해줌
        a.writerows(data) #data는 리스트 형태 
        
def switch(listname):
    for i in listname:
        for j in i:
            try:
                i[i.index(j)] = (float)(re.sub(',','',j))
            except:
                pass
    return listname

        

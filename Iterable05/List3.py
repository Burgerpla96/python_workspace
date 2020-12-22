print('[리스트 표현식(축약,내포) 미 사용]')
a= []
for i in range(5):
    a.append(i)
print(a)
print('[리스트 표현식(축약,내포) 사용 첫번째]')
#순서:range(5) -> for문 안의 i -> for문 앞의 식 :i
#설명:숫자 0부터 4까지 생성(range(5))하여 for문 안의 i에 담고 그 i를 이용해서 식을 만들고
#그 식에 따라 리스트의 요소가 하나씩 생성된다
a = [i for i in range(5)]
print(a)
a=[i+2 for i in range(5)]
print(a)
a=[i > 1 for i in range(5)]
print(a)#[False, False, True, True, True]
print('[리스트 표현식(축약,내포) 사용 두번째]')
a=list(i+2 for i in range(5))
print(a)
a=list(i > 1 for i in range(5))
print(a)
print('[리스트 표현식(축약,내포) 사용 세번째]')
#순서:range(5) -> for문 안의 i -> for문 다음의 if문 ->if문이 참인 경우 식이 실행되서 요소가 하나 만들어진다
#설명:숫자 0부터 9까지 생성하여 i에 저장하고 그 i가 2의 배수이면 for문 앞의 식이 실행되서 요소가 만들어진다
a=[i for i in range(10) if i % 2 ==0]
print(a)
#이중 for문과 같다
#for i in range(2,10)는 바깥 for문 .for k in range(1,10)는 안쪽 for문이 된다

a=[i * k for i in range(2,10)  for k in range(1,10) ]
print(a)#[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
#위 리스트 표현식은 아래와 같다
b=[]
for i in range(2,10):
    for k in range(1, 10):
        #print(i * k,end=',')
        b.append(i*k)
print(b)

a=[i * k for i in range(2,10) if i==9  for k in range(1,10) if k==9 ]
print(a)
#위 표현식은 아래와 같다
b=[]
for i in range(2,10):
    if i == 9:
        for k in range(1, 10):
            if k == 9:
                b.append(i*k)
print(b)

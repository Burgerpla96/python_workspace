#리스트는  a=[표현식] 혹은 a=list(표현식)
#튜플은   a=tuple(표현식)형식으로 하자
#a=(표현식)은 튜플이 아니고 <generator object <genexpr> at 0x00D15DB0>즉 제너레이터객체 반환
print('[튜플 표현식(축약,내포) 미 사용]')
a = (i for i in range(5))
print('객체:{},타입:{}'.format(a,type(a)))
print(dir(a))
print(tuple(a))
'''
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
'''
#print(a.__next__())#StopIteration
print('[튜플 표현식(축약,내포) 사용 첫번째:tuple()생성자]')
a = tuple(i for i in range(5))
print('객체:{},타입:{}'.format(a,type(a)))
print('[튜플 표현식(축약,내포) 사용 두번째]')
a=tuple(i+2 for i in range(5))
print(a)
a=tuple(i > 1 for i in range(5))
print(a)
print('[리스트 표현식(축약,내포) 사용 세번째]')
a=tuple(i for i in range(10) if i % 2 ==0)
print(a)
a=tuple(i * k for i in range(2,10) if i==9  for k in range(1,10) if k==9)
print(a)
#위 표현식은 아래와 같다
b=[]
for i in range(2,10):
    if i == 9:
        for k in range(1, 10):
            if k == 9:
                b.append(i*k)
#리스트를 튜플로 변환
print(tuple(b))


'''
파이썬에는 switch문이 없다
딕션너리 와 사용자 정의 함수를 이용해서 switch문 효과를 낼수 있다
'''
kor = 99;eng=60;math=95
avg =(kor+eng+math)//30
#학점을 반환하는 함수:switch
'''
print('[첫번째 방법]')
def switch(key):
    #문자열 반환
    return {
        10:'A학점',9:'A학점',8:'B학점',7:'C학점',6:"D학점"
    }.get(key,'F학점')
print('평균:{},학점:{}'.format(avg,switch(avg)))
'''
print('[두번째 방법]')
def switch(key):
    #함수 반환
    return {
        10:lambda : print('A학점'),
        9: lambda: print('A학점'),
        8: lambda: print('B학점'),
        7: lambda: print('C학점'),
        6: lambda: print('D학점'),
        5: lambda: print('F학점'),
        4: lambda: print('F학점'),
        3: lambda: print('F학점'),
        2: lambda: print('F학점'),
        1: lambda: print('F학점'),
        0: lambda: print('F학점'),
    }[key]
'''
f=switch(avg)
print('value :%s,type:%s' % (f,type(f)))
#반환한 함수 호출해야 학점이 출력됨
f()
'''
#아래처럼 한키에
switch(avg)()


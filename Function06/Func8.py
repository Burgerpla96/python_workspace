print('[지역변수]')#함수안에서 선언된 변수:지역변수
def add(*args):
    total =0
    for i in args:
        total+= i

    print('{}부터 {}까지 누적합:{}'.format(args[0],args[len(args)-1],total))

add(1,2,3,4,5,6,7,8,9,10)
#print(total)#NameError: name 'total' is not defined
print('[전역변수]')#스크립트 파일(.py) 전체에서 사용할 수 있는 변수
a = 10
def add2():
    total = 0;
    a = int(input('숫자 입력?'))+1#a는 지역변수
    for i in range(1,a+1):
        total+=i
    print('{}부터 {}까지 누적합:{}'.format(1,10, total))
add2()
print('함수밖의 a출력:',a)

for i in range(a):#i는 전역변수
    pass
print('for문이 끝난 후 i : ',i)
print('[global 키워드 사용하기]')
#global 키워드는 쓰지말자.함수가 외부변수에 의존하니까
def global_():
    global b#b는 함수 밖에서도 사용할 수 있는 전역변수
    print('b의 주소(함수 안):', id(b))
    for _ in range(b):
        print('GLOBAL')
#함수 호출
b = 5
print('b의 주소(.py파일 안):',id(b))
global_()


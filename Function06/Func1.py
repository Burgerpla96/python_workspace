#함수 정의 하기전에 함수 호출하기
#파이썬은 코드를 순차적으로 실행하기 때문에 함수 정의전에 호출하면
#name 'helloPython' is not defined에러 발생
#helloPython()
#함수 정의하기
def helloPython():
    print('Hello Python')
#함수 호출하기
helloPython()
#빈 함수 정의하기
def empty():
    pass
print(empty())#None
#함수 독스트링 사용하기
def printMessage(msg):
    #함수 독스트링은 함수의 맨 첫줄에 와야 한다.
    #그래야 함수명.__doc__으로 출력된다
    '''
    함수 독스트링:주석처럼 사용할 수 있으나 하나의 명령문이다
    문자열을 입력받아 출력하는 함수
    :param msg:입력받은 문자열
    '''
    msg='입력값 : {}'.format(msg)
    '''
    아래 print(msg)는 입력값을 출력하기위한 출력문이다(주석처럼 사용하는 스트링)
    '''
    print(msg)


printMessage('Hello Python')
print('[함수 독스트링 출력하기]')
print(printMessage.__doc__)
print('[help(함수명) 내장함수(Built-In Function)로 함수 정보 출력하기')
help(printMessage)

#함수의 결과값 반환하기
def add(a,b):
    result = a+b
    return result#함수는 return문을 만나면 모든 실행을 종료하고 빠져 나간다 즉 아래 코드는 실행되지 않는다
    print('return문 이후 출력문')#return문 이후의 코드는 실행되지 않는다

#result = add(10,20)#함수의 결과값 저장
#print(result)
print(add(10,20))#혹은 바로 print(add(10,20))해도 결과는 같다
#return 키워드 응용하기
def entrance(age):
    if not (20 <=age <=40):
        print('입장불가')
        return
    print('즐거운 시간 보내세요')

entrance(10)
entrance(30)
entrance(45)

#하나의 스크립트 파일(.py)안에서 같은 이름의 함수 여러개 정의시
#아래 기술한 함수가 호출된다
def add(x,y):
    c = x+y
    return c,x,y#(c,x,y)와 같다 즉 튜플을 반환

r=add(10,20)
print(r)
z,x,y = add(100,200)
print('{} + {} = {}'.format(x,y,z))

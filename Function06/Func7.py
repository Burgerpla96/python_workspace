#남다 표현식(함수)
print('[람다함수를 사용하지 않고 def 키워드로 함수 정의하여 사용하기]')
def plus100(arg):
    return arg+100
print('value:{},type:{}'.format(plus100,type(plus100)))#<function plus100 at 0x0000013840C7F040>,type:<class 'function'>
#리스트 [1,2,3,4,5]의 각 요소에 plus100이라는 함수 적용 즉 각 요소를 plus100의 인자로 전달
print(list(map(plus100,[1,2,3,4,5])))#map의 첫번째 전달 인자인 함수는 매개변수(인자) 하나를 갖는 함수 여야한다
print('[람다 함수 정의하여 사용하기]')
#lambda 입력 : 출력(함수바디)
lambda_func = lambda arg : arg +100
print('value:{},type:{}'.format(lambda_func,type(lambda_func)))#value:<function <lambda> at 0x00000193181FADC0>,type:<class 'function'>
print(lambda_func(100))
print(list(map(lambda_func,[1,2,3,4,5])))
print(list(map(lambda arg : arg +100,[1,2,3,4,5])))#람다함수를 직접 인자로 전달
print('[람다표현식을 리스트의 요소로 사용하기]')
list_ = [lambda a,b : a+b,lambda  a,b:a-b,lambda a,b:a*b,lambda a,b:a/b]
print('value:{},type:{}'.format(list_[0],type(list_[0])))
print(list_[0](10,20))
print('{} + {} ={}'.format(10,20,list_[0](10,20)))
print('{} - {} ={}'.format(10,20,list_[1](10,20)))
print('{} * {} ={}'.format(10,20,list_[2](10,20)))
print('{} / {} ={}'.format(10,20,list_[3](10,20)))
print('[람다함수를 직접 호출하기]')
print((lambda  a : a)(100))

#lambda  a : a= a*2#SyntaxError: cannot assign to lambda
#print((lambda  a : a+b)(100))#NameError: name 'b' is not defined

b = 10
print((lambda  a : a+b)(100))#[o]
print('[매개변수에 초기값을 지정한 람다함수]')
lambda_ = lambda  a,b=10 : a +b
print(lambda_(100))
print(lambda_(100,200))
print('[매개변수에 가변인수(위치 및 키워드) 지정한 람다함수]')
#아래 람다 함수는 가변인수만 취하는 함수
lambda_ = lambda a,*args : args #args는 튜플.최소 인자 1개 전달
print(lambda_(100))#()
print(lambda_(100,200))#(200,)
print(lambda_(100,*[100,200,300]))#(100, 200, 300)
#키워드 인수만 취하는 함수
lambda_ = lambda  a,*args,**kwargs : kwargs
print(lambda_(100,200,300,400,name='가길동',age=20))#{'name': '가길동', 'age': 20}
print('[람다식에 조건식 사용하기]')
#조건부 표현식(식1 if 조건 else 식2)을 람다 표현식에 사용하기
#즉 else문이 빠지면 안되고 elif가 포함되면 에러
#for문 사용할 수 없다
print((lambda  a : a * 2 if a % 2==0 else a)(99))
















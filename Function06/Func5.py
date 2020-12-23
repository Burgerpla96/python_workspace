print('[고정인수를 받는 함수]')
def fixed_args(name,age,addr):
    print('이름:{},나이:{},주소:{}'.format(name,age,addr))
#함수 호출.인수 전달시 인수의 순서와 갯수 를 기억해서 함수를 호출해야 한다
fixed_args('가길동',20,'가산동')
fixed_args(*['가길동',20,'가산동'])
fixed_args(*{'age':40,'addr':'다산동','name':'다길동'})#한번 언패킹이 일어나는데 ,딕션너리에 요소 순서대로 매개변수에 키값이 전달된다
fixed_args(**{'age':40,'addr':'다산동','name':'다길동'})#두번의 언패킹이 일어나서 정확히 매개변수와 키값이 일치하는 값이 매개변수에 전달된다
                                                      #반드시 매개변수명과 딕셔너리의 키값은 일치해야 한다

#매개변수명을 키워드로 사용해서 값을 전달:키워드 인수라고 한다
#키워드는 ' 나 "로 감싸지 않은다
#키워드 인수로 값 전달. 이때 순서는 상관 없다
#키워드명과와 매개변수명은 일치 해야한다
fixed_args(age=20,addr='가산동',name='가길동')

'''
※ *위치 가변인수를 받는 매개변수는 튜플이된다
  **키워드 가변인수를 받은 매개변수는 딕셔너리가 된다
'''

print('[키워드 인수를 받은 가변인수를 사용한 함수 첫번째]')
#키워드 인수를 받는 가변 매개변수는 앞에 **를 붙인다
def variable_args(**kwargs):#인수가 0개이든 여러개이든 키=밸류 형태를 받을 수 있는 함수,kwargs는 딕셔너리가 된다
    print('value:{},type:{}'.format(kwargs,type(kwargs)))
    print('---가변인수의 모든 요소 출력---')
    for key,value in kwargs.items():
        print('Key:%s,Value:%s' % (key,value))
#함수 호출
variable_args()#빈 딕셔너리.value:{},type:<class 'dict'>
#variable_args('코스모')#TypeError: variable_args() takes 0 positional arguments but 1 was given
variable_args(name='코스모')#이때 키워드는 임의의 이름
variable_args(name='코스모',age=20,addr='가산동')
#variable_args({'name':'나길동','addr':'나산동','tel':'010','years':30})#위치인수가 전달됨.TypeError: variable_args() takes 0 positional arguments but 1 was given
#즉 위 처럼 키워드=값의 형태로 전달해야한다
variable_args(**{'name':'나길동','addr':'나산동','tel':'010','years':30})

print('[키워드 인수를 받은 가변인수를 사용한 함수 두번째]')
def variable_args2(**kwargs):
    # in으로 딕셔너리 안에 특정 키가 있는지 확인
    if 'name' in kwargs:
        print('이름:',kwargs['name'])
    if 'addr' in kwargs:
        print('주소:', kwargs['addr'])
variable_args2(name1='가길동',addr1='가산동')#아무것도 출력 안됨
variable_args2(name='가길동',addr='가산동',age=20)
print('[고정인수와 키워드 인수를 받는 가변인수를 함께 사용하기]')#고정인수가 항상 가변인수보다 앞에 와야한다.그렇지 않으면 함수 호출시 에러
def fixed_variable(arg,**kwargs):
    print('고정인수:{},가변인수:{}'.format(arg,kwargs))
    print('---가변인수의 모든 요소 출력---')
    for key, value in kwargs.items():
        print('Key:%s,Value:%s' % (key, value))

#함수 호출
#fixed_variable()#TypeError: fixed_variable() missing 1 required positional argument: 'arg'
fixed_variable(10)#고정인수:10,가변인수:{}
fixed_variable('파이썬',subject='파이썬',location='가산',institue='코스모')
fixed_variable('자바',**{'subject':'JAVA','location':'GASAN'})
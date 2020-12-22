print('[고정인수를 받는 함수]')
def fixed_args(name,age,addr):
    print('이름:{}, 나이:{}, 주소:{}'.format(name,age,addr))
fixed_args('김길동',24,'청담동')
fixed_args(*{'name':'김길동','addr':'청담동','age':24})
fixed_args(**{'name':'김길동','addr':'청담동','age':24})#매개변수명과 키값이 같으면 언패킹후 맵핑해서 value값이 전달된다.
fixed_args(addr='청담',name='길동',age=20)#키워드 인수 사용


#위치 가변인수를 받는 매개변수는 튜플이 되고
#키워드 가변인수를 받은 매개변수는 딕셔너리가 된다.
print('[keyword인수를 받는 함수]')
def variable_args(**kwargs):#kwargs는 딕셔너리가 된다,인수의 갯수제한이 없다.
    print('value:{}, type:{}'.format(kwargs,type(kwargs)))
    print('---가변인수의 모든 요초 출력---')
    for key,value in kwargs.items():
        print('Key:%s, value: %s' % (key,value))
variable_args()#빈 딕셔너리
variable_args(name='코스모')#키워드는 임의의 이름
#딕셔너리로 전달하거나, 키워드 인수로 전달하기
#variable_args({'name':'나길동','주소':'나산동','나이':20})#위치인수 전달이므로 언패킹 필요
variable_args(**{'name':'나길동','주소':'나산동','나이':20})

def variable_args2(**kwargs):
    if 'name' in kwargs:
        print('이름:',kwargs['name'])
    if 'addr' in kwargs:
        print('주소:', kwargs['addr'])
variable_args2(name='가길동')
variable_args2(name='가길동', addr='가짜주소')
variable_args2(name1='가길동', addr1='가짜주소')#출력없다

def fixed_variable(arg,**kwargs):
    print('고정인수:{}, 가변인수:{}'.format(arg, kwargs))
    print('---가변인수의 모든 요초 출력---')
    for key, value in kwargs.items():
        print('Key:%s, value: %s' % (key, value))

fixed_variable(12)#최소 한개의 매개변수를 받아야한다.
fixed_variable(12,name='몰라',name2='바보')
fixed_variable(12,**{'name':'몰라'})
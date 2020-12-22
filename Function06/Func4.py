'''주석'''

print('[고정 인수를 사용]')
def fixed_args(age,tall,weight):
    print('나이: {}, 키: {}, 몸무게: {}'.format(age,tall,weight))
#함수 호출시, 인수의 위치 및 개수를 기억해야한다.
fixed_args(35,184,89)
age,tall,weight= [20,174,76]#언패킹
fixed_args(age,tall,weight)#리스트를 그냥 전달할 수는 없다.*를 붙이면 가변인수가 된다.
fixed_args(*[20,174,76])


def variable_args(*args):#가변 인수이자 위치인수
    print('value:{}, type:{}'.format(args,type(args)))
    sum_ = 0
    for i in args:
        sum_ += i
    print('인수가 {}개인 튜플의 합: {}'.format(len(args), sum_))
variable_args()# 빈 튜플
variable_args(10,20,32)
variable_args(1,2,3,4,5)
#리스트 하나를 가진 튜플이다.
variable_args(*[1,2,3,4,5])

print('[고정인수와 위치인수를 받은 가변인수를 함께 사용하기]')
def fixed_variable(arg,*args):#고정인수가 항상 가변인수보다 앞에 와야한다.
    print('고정인수:{}, 가변인수:{}'.format(arg,args))
    print('[가변인수의 모튼요소 출력]')
    for i in args:
        print(i)
fixed_variable(1)#고정인수로 인하여 최소 하나의 인자 전달
fixed_variable(1,2,3)
fixed_variable(*[1,2,3])

'''
매개변수의 순서:
1.고정인수 > 가변인수
2.위치가변인수(*) >키워드 가변인수(**)
3.고정인수 > 위치 가변인수 > 키워드 가변인수 > 매개변수 초기화
'''
print('[매개변수 초기값 설정하기]')
def args_init(arg1,arg2,arg3='디폴트값1',arg4='디폴트값2'):
    print(arg1,arg2,arg3,arg4)
#함수 호출:최소 2개에서 최대 4개까지 인수 전달
args_init(10,20)#매개변수 갯수만큼 값을 전달해야 되지만 매개변수 초기값 설정으로
                #초기값이 설정 안된 매개변수 수만큼 전달하면 된다
args_init(10,20,30)
#SyntaxError: non-default argument follows default argument
'''
def args_init2(arg1,arg2='디폴트값2',arg3):
    pass
'''
help(print)
#print(value,..., sep=' ', end='\n', file=sys.stdout, flush=False)
print('이름','홍길동',sep='는 ')#'이름','홍길동'는 위치 가변 매개변수인 value 가 받는다
                              # 매개변수 sep에 키워드인수로 "는 "을 전달
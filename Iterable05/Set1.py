#순서가 없기때문에 출력시 순서없이 출력된다.
#단,숫자로만 이루어진 세트는 오름차순으로 출력된다
#단 자리수가 다른 경우
print('[집합 생성 첫번째:빈 집합]')
a={}
print(type(a))#<class 'dict'>
a=set()
print(type(a))#<class 'set'>
print('[집합 생성 두번째:{}]')
a={4,10,282,5,19}
b= {'4','10','282',5,'19'}
print(a)#오름차순으로 출력
print(b)#실행할때마다 순서가 바뀜
print('[집합 생성 세번째:set(반복가능한 객체)]')
#a=set(1,2,3,4,5)#TypeError: set expected at most 1 argument, got 5
a=set([1,2,3,4,5])# 혹은 set((1,2,3,4,5)) 리스트나 튜플을 집합으로 변환
print(a)
print(set(range(1,6)))#range객체를 집합으로 변환
print('[집합 생성 네번째:set(문자열)]')
a = {'HELLO'}
print('value:{},type:{}'.format(a,type(a)))
a=set('HELLO')#{'H','E','L','O'}
print('value:{},type:{}'.format(a,type(a)))
print('[집합 생성 다섯번째:집합안에 집합]')
a={(1,2),(3,4)}#[O]
#a={[1,2],[3,4]}#TypeError: unhashable type: 'list'
#a={{'name':'가길동'}}#TypeError: unhashable type: 'dict'
#a={{1,2},{3,4}}#TypeError: unhashable type: 'set'
print(a)




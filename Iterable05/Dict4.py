#딕션너리 표현식:기존 딕션너리 객체로 새로운 딕션너리 객체를 생성할때 주로 사용한다
'''
{키:값  for 키[, 값 ] 혹은 [키,]값    in 딕션너리.items() }
{키:값  for 키[, 값] 혹은 [키,]값   in 딕션너리.items() if 조건식}

dict({키:값  for 키[, 값 ] 혹은 [키,]값  in 딕션너리.items()})
dict({키:값  for 키[, 값 ] 혹은 [키,]값  in 딕션너리.items() if 조건식})
딕션너리 표현식으로
특정 값을 기준으로 딕션너리를 다시 생성하는 방식으로 삭제 효과를 구현할 수 있다
'''
keys =['A','B','C','D']
print('[딕셔너리 표현식 첫번째- {} : 리스트로 생성]')#리스트의 요소를 키로 사용
print('---dict.fromkeys() 함수---')
a=dict.fromkeys(keys,'PYTHON')#딕셔너리의 정적메소드인 fromkeys()메소드 사용
print(a)
print('---표현식---')
b = {key:'PYTHON' for key in  keys}#표현식으로 fromkeys()함수 와 같은 객체 생성
print(b)

print('[딕셔너리 표현식 두번째- dict({}) : 리스트로 생성]')
c = dict({key:'PYTHON'+key for key in keys})
print(c)
print('[딕셔너리 표현식 세번째- keys() : 기존 딕셔너리로 생성]')
d= {key:len(key) for key in a.keys()}#키의 길이를 value로
print(d)
print('[딕셔너리 표현식 네번째- values() : 기존 딕셔너리로 생성]')
e = {value : value for value in a.values()}
print(e)
print('[딕셔너리 표현식 다섯번째- items() : 기존 딕셔너리로 생성]')
f={'name':'가길동','tel':'010','addr':'가신동'}
#키와 밸류를 바꾸기
g = {value : key for key,value in f.items()}
print(g)
#키가 'name'인 요소는 제외-삭제효과
g = {value : key for key,value in f.items() if key != 'name'}
print(g)
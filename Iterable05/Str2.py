print('[문자열 관련 주요 메소드]')

def pprint(value):
    print('value:{}\ntype:{}'.format(value,type(value)))

print('1.join():리스트를 문자열로 변환')
#단,리스트의 모든 요소는 문자열이어야 한다.리스트 요소중 하나라도 숫자인 경우 에러발생
#이런경우 map함수를 보통 같이 적용한다
a=['한라산','설악산','대둔산','덕유산']
b = '▲'.join(a)
pprint(b)
a.append(2020)
print(a)#['한라산', '설악산', '대둔산', '덕유산', 2020]
#b = '▲'.join(a)#[x]TypeError: sequence item 4: expected str instance, int found
b = '▲'.join(map(str,a))
pprint(b)
#split()는 str객체의 메소드
#list() 는 리스트 생성자
print('2.split()혹은 list():문자열을 리스트로 변환')
'''
list(str객체):문자열의 각 문자를 하나의 요소로 갖는 리스트 생성
split(구분자):구분자를 기준으로 쪼갠 요소를 갖는 리스트 반환
'''
print('----split()함수 사용----')
c=b.split('▲')
pprint(c)
#구분자가 없는 경우 문자열 전체가 리스트의 하나의 요소로 생성된다
d=b.split()#만약 split하려고하는 문자열안에 공백이 있는 경우-공백으로 분리(디폴트 공백)
pprint(d)
print('3.replace():문자열 변경')
e="Hello World"

print(e.replace('World','PYTHON'))
print('원본 문자열:',e)
#변경할 문자열이 없는 경우 원본 문자열 전체 반환
print(e.replace('world','PYTHON'))
print('4.lower():소문자로 변경')
print(e.lower())
print('5.upper():대문자로 변경')
print(e.upper())
print('6.lstrip([문자열]):왼쪽의 공백제거')
f='        Hello World    '
print('{}{}{}'.format('X',f.lstrip(),'Y'))
#인자로 문자열 지정시 왼쪽에서 일치하는 문자열 삭제
#print('{}{}{}'.format('X',f.lstrip('        He'),'Y'))#Xllo World    Y
print('{}{}{}'.format('X',f.lstrip().lstrip('He'),'Y'))
print('7.rstrip([문자열]):오른쪽의 공백제거')
print('{}{}{}'.format('X',f.rstrip(),'Y'))
print('{}{}{}'.format('X',f.rstrip().rstrip('ld'),'Y'))

print('8.strip([문자열]):양쪽의 공백제거')
print('{}{}{}'.format('X',f.lstrip().rstrip(),'Y'))
print('{}{}{}'.format('X',f.strip(),'Y'))
print('9.zfill():0으로 자리수 채우기')
print('9'.zfill(2))
print('3.14'.zfill(6))
print('PYTHON'.zfill(7))
#문자열의 길이보다 지정된 자리 숫자의 길이가 작거나 같으면 아무것도 채우지 않는다
print('PYTHON'.zfill(1))
g = 'Hello! He is a good'
print('10.find()/rfind():문자열 찾기(찾은 문자열의 시작인덱스 반환)')
#찾은 문자열이 없는 경우 -1 반환
print(g.find('He'))#0
print(g.find('he'))#-1
print(g.rfind('He'))#오른쪽 즉 뒤에서 부터 찾는다
print('11.index()/rindex():문자열 찾기(찾은 문자열의 시작인덱스 반환)')
#찾는 문자열이 없는 경우 에러
print(g.index('He'))
print(g.rindex('He'))
#print(g.index('he'))#ValueError: substring not found
print('12.count():찾은 문자열의 갯수 반환')
print(g.count('He'))#2
print(g.count('he'))#0









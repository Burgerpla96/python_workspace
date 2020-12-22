print('[리스트 생성 첫번째:빈 리스트]')#동적으로 요소 추가시 주로 사용
def pprint(obj):
    print('객체:{},타입:{}'.format(obj,type(obj)))
    if not isinstance(obj,int) and not isinstance(obj,float) and not isinstance(obj,bool):
        print('객체의 요소 수:',len(obj))

#방법1-[]
a = []
pprint(a)
#방법2-list():list클래스의 생성자
a=list()
pprint(a)
print('[리스트 생성 두번째:같은 타입의 객체(요소) 저장]')
b = [1,2,3,4,5]#변수 하나에 여러개 데이타 설정:패킹
pprint(b)
print('[리스트 생성 세번째:다른 타입의 객체(요소) 저장]')
c=['가길동',20,3.14,True]
pprint(c)
print('[리스트 Unpacking]')
#리스트의 각 요소를 여러 변수에 나눠 담는 것:언패킹(구조분해)
#단, 변수의 개수가 요소의 개수와 일치해야 한다
c1,c2,c3,c4 = c#언패킹
pprint(c1);pprint(c2);pprint(c3);pprint(c4)
print('[리스트 생성 네번째:문자열로 리스트 만들기')
s='PYTHON'
print(list(s))#문자열의 각 문자를 요소로하는 리스트가 생성됨
print(s.split())#공백이 기본값 ['PYTHON']
print('[리스트 생성 다섯번째:list(range객체) 즉 list(range(숫자))')
r=range(10)
print(list(r))
print('[빈 리스트에 값 할당하기]')
#빈 리스트에 값을 할당할때는 [인덱스]=값 으로 할당하는게 아니라 append()함수를 이용해서 할당한다
#a[0] ='가길동'#IndexError: list assignment index out of range
a.append('가길동')
a.append(20)
a.append('송파구')
pprint(a)
print('[리스트객체[인덱스]=값 : 해당 인덱스의 값 수정]')
#a[3]='코스모'#IndexError: list assignment index out of range
a[1]=40
a[len(a)-1]='금천구'
pprint(a)
print('[리스트객체[인덱스] : 해당 인덱스의 값 읽기]')
print('a[0]:{},a[{}]:{}'.format(a[0],len(a)-1,a[len(a)-1]))
print('[리스트의 요소수 구하기;len()]')
#len()함수:range()함수로 리스트를 만든 경우 전체 요소수 파악하기가 쉬움
print('총 요소수 :',len(list(range(10,100,2))))
print('[리스트 슬라이싱하기]')
#c : ['가길동',20,3.14,True]
print(c[1:3])#[20,3.14]
print(c[1:1])#[]
print(c[1:])
print(c[:3])
print(c[:len(c)])
print(c[:])#위와 동일 즉 전체 요소
print('[for문을 사용해서 리스트의 인덱스 및 요소 가져오기]')
f = ['가','나','다','라']
print('---요소만 출력---')
for element in f:
    print('%-2s' % element,end='')
print('---인덱스 및 요소 동시 출력---')
for index in range(len(f)):
    print('인덱스:{},요소:{}'.format(index,f[index]))
#for 인덱스, 값 in enumerate(순서가 있는 객체):  #인덱스와 값을 동시에 꺼내올 수 있다
print('---enumerate()함수---')
for index,element in enumerate(f):
    print('인덱스:{},요소:{}'.format(index, f[index]))










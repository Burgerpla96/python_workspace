def pprint(obj):
    print('객체:{},타입:{}'.format(obj,type(obj)))
    if not isinstance(obj,int) and not isinstance(obj,float) and not isinstance(obj,bool):
        print('객체의 요소 수:',len(obj))

print('[튜플 생성 첫번째 : 빈 튜플]')
#빈 튜플은 클래스나 함수에서 주로 사용
#방법1-()
a=()
pprint(a)
#방법2-tuple()
a=tuple()
pprint(a)
#※튜플은 () 생략 가능
print('[튜플 생성 두번째 :요소가 하나인 튜플]')
b=(1)#튜플이 아니다.int형이다
pprint(b)
#요소가 하나인 튜플을 만들때는 반드시 뒤에 ,(콤마)를 붙여라
b=(1,)#혹은 1,
pprint(b)
print('[튜플 생성 세번째 :같은 타입의 객체 저장]')
b=(1,2,3,4,5,)#혹은 1,2,3,4,5,
pprint(b)
print('[튜플 생성 네번째 :다른 타입의 객체 저장]')
c='가길동',20,3.14,True,#괄호 생략
pprint(c)
print('[튜플 언패킹]')
#튜플의 각 요소를 여러 변수에 나눠 담는 것:언패킹
#단, 변수의 개수가 요소의 개수와 일치해야 한다

c1,c2,c3,c4 = c#언패킹
pprint(c1);pprint(c2);pprint(c3);pprint(c4)
print('[튜플 생성 네번째:문자열로 튜플 만들기')
s='PYTHON'
print(tuple(s))#('P', 'Y', 'T', 'H', 'O', 'N')
print(tuple(s.split()))#('PYTHON',)
print('[튜플 생성 다섯번째:tuple(range객체) 즉 tuple(range(숫자))')
r=range(10)
print(tuple(r))

print('[튜플객체[인덱스] : 해당 인덱스의 값 읽기]')
a=(True,1,3.14,'가길동')
print('a[0]:{},a[{}]:{}'.format(a[0],len(a)-1,a[len(a)-1]))
#튜플은 읽기 전용이다. 요소값 변경 불가능
#a[1]=10#TypeError: 'tuple' object does not support item assignment
print('[튜플의 요소수 구하기;len()]')
print('총 요소수 :',len(tuple(range(10,100,2))))
print('[튜플 슬라이싱하기]')
print(a[1:3])#(1, 3.14)
print(a[1:1])#()
print(a[1:])
print(a[:3])
print(a[:])
print('[for문을 사용해서 튜플의 인덱스 및 요소 가져오기]')
f = ('가','나','다','라')
print('---요소만 출력---')
for element in f:
    print('%-2s' % element,end='')
print('---인덱스 및 요소 동시 출력---')
for index in range(len(f)):
    print('인덱스:{},요소:{}'.format(index,f[index]))
print('---enumerate()함수---')
e=enumerate(f)
print('객체:{},타입:{}'.format(e,type(e)))
print(dir(e))#__iter__존재 즉 반복가능한 객체
print(list(e))#[(0, '가'), (1, '나'), (2, '다'), (3, '라')] 튜플의 첫번째:인덱스,두번째:요소
for index,element in enumerate(f):
    print('인덱스:{},요소:{}'.format(index,element))


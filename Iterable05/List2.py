print('[리스트의 주요 메소드]')
print('1.append():요소 추가')
a=[1,2,3]
a.append(4)
a.append(1)#중복 저장가능
a.append(['가','나'])#[1, 2, 3, 4, 1,['가','나']]
print(a[len(a):])#[]
#a[len(a):] =[10]#[O] a.append(10)와 같다
#append()함수가 아닌 리스트객체[새로운인덱스]=값로 새로운 요소추가시에는 값은 반드시 반복가능한 객체여야한다
#단,리스트객체[기존인덱스]=값은 업데이트에 해당 즉 새로운 요소 추가가 아니다
#a[len(a):] =10#[X]TypeError: can only assign an iterable
a[0]='GA'#[O] 새로운 요소 추가가 아니고 기존 요소 업데이트
print(a)
print('2.extend():리스트 확장')
b=[1,2,3]
#인자로 반복가능한 객체여야 한다
#b.extend(4)#TypeError: 'int' object is not iterable
b.extend([4])#요소가 하나일때는 b.append(4)와 같다
b.extend([5,6])#[1, 2, 3, 4, 5, 6]요소가 여러개일때는 append()와 다르다 즉 extent는 ㅎ확장,append는 추가
#b.append([5,6])#[1, 2, 3, 4, [5, 6]]
print(b)
print('3.insert(인덱스,객체):기존 인덱스 위치에 요소 삽입')
c=[1,2,3]
c.insert(0,'가길동')
c.insert(100,'나길동')#인덱스 범위를 벗어난 경우 항상 len(리스트객체)인덱스에 삽입된다
                     #c.append('나길동')와 같다
print(c)
print('4.copy():리스트 복사')#원본 리스트가 복사되어 새로운 리스트가 생성되고 그 새로운 리스트의
                           #주소가 저장된다
d= c.copy()
print('---d에 c를 복사---')
print(d)
d[0]=0
print('d는 ',d)
print('c는 ',c)
print('c의 주소:{},d의 주소:{}'.format(id(c),id(d)))
print(c is d)
print('5.remove():리스트의 요소 삭제')#반환값 없다(None)
e=[1,2,3,4,5,2]
e.remove(4)
print(e)#[1, 2, 3, 5, 2]
#동일한 객체를 삭제하는 경우 인덱스가 작은 요소가 삭제됨
print(e.remove(2))#None
print(e)
print('6.pop():리스트의 마지막 요소 삭제')
#pop()는 리스트의 마지막 요소삭제.반환값은 삭제한 요소
#pop(인덱스) : 인덱스에 헤당하는 요소 삭제.
f=[1,2,3,4,5,2]
print(f.pop())#마지막요소인 2 출력
print(f)
print(f.pop(2))#3
print(f)
#f.pop(100)#IndexError: pop index out of range
print('--- del 연산자로 리스트요소 삭제허기---')
#변수삭제시 : del 변수명
#del f #[o] f라 변수를 메모리에서 삭제
#print(f)#NameError: name 'f' is not defined
#del f[:]#전체 요소 삭제. f.clear()와 같다
#print(f)#[]출력 즉 변수는 삭제되지 않는다
# del f[1:3]
# print(f)#[1, 5]
# del f[1]#f.remove(1)과 같다
# print(f)
print('7.index(요소):리스트 요소의 인덱스 반환,count(요소):요소의 빈도수 반환')
g=['가','나','다','라','나','마','나']
print('"나"의 인덱스:',g.index('나'))
print('"나"의 빈도수:',g.count('나'))
print('8.reverse():리스트의 요소를 반대로 정렬')
print(g.reverse())#None #IN-PLACE방식 :새로운 객체가 반환되는 게 아니라 자신이 바뀌는 방식
print(g)
print('9.sort():리스트의 요소 정렬')
g.sort()##디폴트는 오름 차순
print(g)
g.sort(reverse=True)#내림차순
print(g)
print('10.join(반복가능한 객체):리스트를 문자열로 변환')
h=['한라산','백두산','금강산']
print('▲'.join(h))
print(','.join(h))#한라산,백두산,금강산
print(''.join(h))#한라산백두산금강산
print('[리스트의 산술 연산]')#+와 *만 가능
x=[1,2,3]
y=['가','나','다']
print(x+y)#[1, 2, 3, '가', '나', '다'] 즉 x.extend(y)와 같다
print(x*3)#[1, 2, 3, 1, 2, 3, 1, 2, 3].
#리스트에 0이나 음수를 곱하면 빈 리스트[]가 나온다
print(x*-1)#[]
#print(x*3.14)#TypeError: can't multiply sequence by non-int of type 'float'
             #정수만 곱하기 가능
#in (not in)  연산자 : 리스트에 요소의 존재여부를 파악할 수 있다
z=[1,2,3,]
print(4 not in z)
print(1 in z)







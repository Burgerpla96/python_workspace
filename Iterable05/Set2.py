print('[집합의 주요 메소드]')
a={1,2,3,4}
b={3,4,5,6}
#set(클래스명)으로 접근한 메소드는 정적 메소드
print('---1.합집합---')
print(a | b)
print(set.union(a,b))
#a.update(b)
#print('a:',a)#in-place방식의 합집합. a의 요소가 변경됨

print('---2.교집합---')
print(a & b)
print(set.intersection(a,b))
#a.intersection_update(b)#in-place방식의 교집합. a의 요소가 변경됨
print('a:',b)
print('---3.차집합---')
print(a - b)
print(set.difference(a,b))
#a.difference_update(b)#in-place방식의 차집합. a의 요소가 변경됨
print('---4.대칭 차집합---')
print(a ^ b)
print(set.symmetric_difference(a,b))
#a.symmetric_difference_update(b)in-place방식의 대칭차집합. a의 요소가 변경됨
print('---5.add(요소)---')
a.add(5)
print(a)
a.add(1)#중복 저장 안됨
print(a)
print('---6.remove(요소)---')
a.remove(3)
print(a)
#a.remove(3)#KeyError: 3
print('---7.discard(요소)---')
a.discard(3)#요소가 없어도 에러 안남
print(a)
print('---8.clear()---')
a.clear()

print(a)#set()
print('---9.copy()---')
a={1,2,3,4}
c= a.copy()
print( a is c)
print('a의 주소:{},c의 주소:{}'.format(id(a),id(c)))
print('---10.len()---')
print(len(a))

#in (not in)  연산자 : 집합에 적용시 집합에 요소의 존재여부를 파악할 수 있다
print('[집합에 in 및 not in 연산자 적용]')
a={'가','나','파이썬','자바'}
print('다' in a)
print('파이썬' in a)
print(dir(a))#__iter__존재 즉 반복 가능한 객체(Iteratable)다
print(dir.__doc__)
#순서가 없기때문에 출력시 순서없이 출력된다.실행시마다 다르다
#단,숫자로만 이루어진 세트는 오름차순 순서대로 출력된다
a={2,5,94,3,997}
for element in a:
    print(element)



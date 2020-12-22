import sys
#getrefcount()를 호출하면서 2020을 내부적으로 3번 참조
print(sys.getrefcount(2020))
x=2020# 2020 참조 : 참조횟수 한번 추가됨
print(sys.getrefcount(2020))# 레퍼런스 카운트 1 증가하여 4
y=2020# 2020 참조 : 참조횟수 한번 추가됨
print(sys.getrefcount(2020))# 레퍼런스 카운트 1 증가하여 5
# is 연산자 : 객체가 같은 타입인지 판단하는 연산자.
print( x is y)
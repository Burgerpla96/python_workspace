#값을 변경할 수 있는 메소드 즉 append()나 extend() ,pop(),remove() del
#등은 튜플에는 없다
print('[튜플의 주요 메소드]')
print('1.index(요소):튜플 요소의 인덱스 반환,count(요소):요소의 빈도수 반환')
g='가','나','다','라','나','마','나'
print('"나"의 인덱스 : ',g.index('나'))
print('"나"의 빈도수 : ',g.count('나'))
print('2.join(반복가능한 객체):튜플을 문자열로 변환')
h='한라산','백두산','금강산',
print('▲'.join(h))
print(','.join(h))#한라산,백두산,금강산
print(''.join(h))#한라산백두산금강산
print('[튜플의 산술 연산]')#+와 *만 가능
x=1,2,3
y='가','나','다'
print(x+y)#(1, 2, 3, '가', '나', '다')
print(x*3)#(1, 2, 3, 1, 2, 3, 1, 2, 3)
#튜플에 0이나 음수를 곱하면 빈 튜플()가 나온다
print(x*-1)#()
#in (not in)  연산자 : 튜플에 요소의 존재여부를 파악할 수 있다

z=(1,2,3,)
print(4 not in z)
print(1 in z)

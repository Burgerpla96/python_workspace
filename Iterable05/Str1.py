'''
순서가 있는 자료형(시퀀스 객체):str,list,tuple,range
공통 기능
1. (not) in 연산자로 요소(객체) 존재 파악
2. 인덱싱([인덱스]) 및 슬라이싱([시작인덱스 : 끝인덱스])
3. + 나 * 연산자로 시퀀스객체를 연결(+)하거나 같은 시퀀스객체를 배수(*)로 늘릴 수 있다
   단,range객체는 list로 변환후 +,*를 적용하자
   그리고 *연산자 사용시 0이나 음수를 곱하면 빈 객체가 된다
4. len(시퀀스객체)함수는 저장된 요소의 갯수 반환
'''

print('[빈 문자열 만들기]')
a=''#"",'''''',"""""",str()
#len(반복가능한 객체)는 모든 반복 가능한 객체의 요소수를 반환
print('value:{},len:{},type:{}'.format(a,len(a),type(a)))
print('[NOT 빈 문자열 만들기]')
a='PYTHON'
print('value:{},len:{}'.format(a,len(a)))
#순서가 있는 자료형(str,list,tuple,range)들은 각 요소에 인덱스로 접근 가능
print('[인덱스로 요소에 접근하기]')
#시퀀스객체[인덱스]
#인덱스는 양수(인덱스는 0부터 시작하고 왼쪽기준) 혹은 음수(인덱스는 1부터시작하고 오른쪽 기준)
#index = list(map(int,input('추출할 문자의 인덱스를 입력(단,최대값은 {})?'.format(len(a)-1))))[0]
index = int(input('추출할 문자의 인덱스를 입력(단,최대값은 {})?'.format(len(a)-1)))
print(type(index))
print('양수 인덱스(왼쪽부터 인덱싱):',a[index])
print('음수 인덱스(오른쪽부터 인덱싱):',a[-index])
print(a[-1])#맨 끝 문자
#print(a[len(a)])#IndexError: string index out of range
print('문자열에 for문 적용하기]')
'''
index =0
for element in a:
    print('인덱스:{},요소:{}'.format(index,element))
    index+=1
'''
#enumerate(순서가 있는 자료형): 리스트, 튜플, 문자열객체,range객체의 요소의 순서(인덱스)와 요소를
#튜플로 묶어서 enumerate 객체(반복가능한 객체)로 반환
#※ 보통 enumerate 함수는 for문과 함께 자주 사용된다
for index,element in enumerate(a):#튜플인 각 요소를 구조분해(언팩킹)로 각 변수에 저장
    print('인덱스:{},요소:{}'.format(index,element))

print('[시퀀스객체[인덱스]=새로운요소  요소 변경하기]')
#str객체는 요소할당을 할수 없다(불변객체)
#a[0] = 'B'#TypeError: 'str' object does not support item assignment
#※문자열(불변)의 값을 변경하려면 리스트로 변환후 변경해야 한다
#1.먼저 문자열을 리스트로 변환한다
a=list(a)
print('value:{},type:{}'.format(a,type(a)))
#2.특정 인덱스의 문자열을 변경한다
a[0] = 'B'
print(a)
#3.리스트를 다시 str로 변경
##아래처럼 str함수로 문자열로 변환하면 ['B', 'Y', 'T', 'H', 'O', 'N'] 리스트형태가
# 그대로 문자열로 변경된다
#a=str(a)
print('value:{},type:{}'.format(a,type(a)))
#4. join()함수를 사용하거나 아래처럼 리스트의 각 요소를 문자열에 누적하여 변경된 문자열을 만든다
#a=['B', 'Y', 'T', 'H', 'O', 'N']
print('[str객체의 join()함수 사용]')
b = ''.join(a)
print('value:{},type:{}'.format(b,type(b)))
print('[리스트의 각 요소를 누적]')
'''
객체 == 객체:값비교(연산자)
객체 is 객체:주소비교(id(객체) 주소 반환)(연산자)
isinstance(객체,클래스 타입):객체의 타입비교(함수)
'''
b = str()#빈문자열
for temp in a:
    if isinstance(temp,int):
        b+=str(temp)
    else:
        b+=temp
print('value:{},type:{}'.format(b,type(b)))

'''
문] 'desert'이라는 문자열을 'dessert'으로 변경하여라
-힌트
1.문자열을 리스트로 변경:list(문자열)
2.리스트의 함수나 인덱싱 사용
3.스트링 객체의 join함수와 map함수를 이용해서  바꾼 문자열로 변경
  ''.join(리스트)  #리스트 요소중 특정요소를 변경할 필요가 없을때
  ''.join(map(함수,리스트)) #리스트 요소중 특정요소가 변경이 필요할때
'''
a='desert'
b=list(a)
b.insert(2,'s')
b=''.join(b)
print('문자열 변경 : ',b)
#슬라이싱: 인덱스를 사용해서 특정 위치의 요소들을 꺼내올수 있다(시퀀스 객체인 경우)
print('[문자열 Slicing하기]')
d='ABCDEFG'
#인덱스 1부터 2까지 슬라이싱
#[시작인덱스:끝인덱스] - 시작인덱스부터  끝인덱스-1까지
print(d[1:3])
print(d[1:1])#빈 문자열
#[:끝인덱스] -  처음부터 끝인덱스-1까지
print(d[:4])
#[시작인덱스:] -  시작인덱스부터 끝까지
print(d[1:])
#인덱스 1부터 뒤에서 두번째 즉 인덱스 -2(-1-1이니까)까지 슬라이싱
print(d[1:-1])
print(d[:len(d)])#인덱스 0부터 끝까지 슬라이싱
print(d[:])#인덱스 0부터 끝까지 슬라이싱
#in (not in)  연산자 : 모든 시퀀스 객체에 공통으로 적용될수 있는 연산자
#                    객체안의 특정 요소의 존재여부를 파악할 수 있는 연산자
#찾을객체 in 반복가능한 시퀀스객체
e='JAVA'
print('A' in e)
print('A' not in e)
print('AVA' in e)

while True:
    email = input('이메일 주소를 입력하세요?')
    if '@' not in email:
        print('이메일 형식이 아닙니다')
    else:
        break








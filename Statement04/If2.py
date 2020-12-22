num1 =100
print('[if문 형식 첫번째로 짝/홀수 판단]')
#조건식이 두번 실행됨.
if num1 % 2 == 0:
    print('짝수')
if num1 % 2 !=0:
    print('홀수')
print('[if문 형식 두번째로 짝/홀수 판단]')
#조건식 한번만 실행됨.
if num1 % 2 == 0:
    print('짝수')
else:
    print('홀수')
#[조건부 표현식- 다른 언어에서는 삼항연산자라 함]
'''
 if ~else문과 같다.
 코드를 짧게 표현할때 주로 사용(if ~else문  대신에)
 구문]
 변수 = 값 if 조건문 else 값
'''

print('[조건부 표현식(삼항연산자) 짝/홀수 판단]')
result = '짝수' if num1 % 2 == 0 else '홀수'
print(result)
#※else는 항상 if문과 짝을 이루어야 한다. 단독 사용불가
if num1 % 2 == 0:
    print('짝수')
print('num1는 ',num1)#if문과 무관
#[x]아래 else는 짝을 이루는 if문이 없다.
'''
else:
    print('홀수')
'''
#문]한 문자를 입력받아 숫자인지 아닌지
#   if ~else문 과  조건부 표현식를 이용하여 판단하여라.
character = input('한 문자를 입력?')
'''
print('[if~else문으로 구현]')
if '0' <= character <= '9' :
    print('숫자')
else :
    print('숫자가 아님')
print('[조건부 표현식으로 구현]')
print('숫자' if '0' <= character <= '9' else '숫자가 아님' )
'''
'''
문]숫자인지 판단후 2의 배수를 판단하고
   2의 배수면 '2의 배수' 출력,아니면 '2의배수가 아님'출력
   또한 숫자가 아니고
   알파벳이라면 대소문자를 판단한후
   대문자인경우 '대문자' 출력 소문자인 경우 
   '소문자'출력
   가정]숫자나 알파벳만 입력한다고 가정하자.
'''
if '0' <= character <= '9' :
    if (ord(character)-ord('0')) % 2 ==0:
        print('2의 배수')
    else:
        print('2의 배수가 아님')
else :
    if 'a' <= character <= 'z':
        print('소문자')
    else:
        print('대문자')

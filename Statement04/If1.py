#0,0.0,0+0j는 False와 같고 None,''(빈문자열) ,빈 이터레이터 객체([],{},(),set()등)는
#조건식으로 판단시 False로 간주된다
if not 0:
    print('0은 False다')
if not None:
    print('None은 False다')
if not "":
    print('""은 False다')
if not {}:
    print('{}딕셔너리은 False다')
#조건식은 모든 식이 될 수 있다
num1 = 10
if num1:
    print('num1은 %d' % num1)
if num1 % 2 == 0:
    print('%d는 짝수' % num1)
if num1 % 2 != 0:
    print('%d는 홀수' % num1)

if num1 % 2==0 and num1 >=10 :
    print('%d는 짝수고 10보다 크거나 같다' % num1)
if 1 :
    print('항상 실행되는 명령문')
if 0 :
    print('항상 실행 안되는 명령문')
#파이썬에서 조건식을 수학에서 사용하는 방식으로 간편화 할 수도 있다.
if 5 < num1 < 15:#num1 > 5 and num1 < 15와 같다
    print('{}는 5보다 크고 15보다 작다'.format(num1))
#if 조건식:
#조건식 들여쓰기 한 다음줄에 코드가 없으면 에러 즉 pass생략시 에러
if num1 % 2 ==0 :
    pass
print('위의 if문과 관련이 없는 명령문:들여쓰기 수준이 다르다')
'''수행할 명령문이 여러개인  경우, 들여쓰기를 같게 하지않으면
     의도하지 않은 결과를 초래할수 있다.
    고로 조건식이 참일때 수행할 명령문이 여러개인 경우는
    반드시 들여쓰기를 똑같이 해주어라.'''

if num1 % 2 !=0 :
    print('num1은 %d다' % num1)
    print('%d는 홀수다' % num1)

'''
ord(문자) : 문자의 아스키코드나 유니코드값을 반환
chr(숫자) : 숫자(아스키코드값 혹은 유니코드값)에 대응하는 문자를 반환
'''
print('[문자를 아스키(유니)코드로 변환:ord(문자)]',ord('가'),sep='\n')
print('[아스키(유니)코드를 문자로 변환:chr(숫자코드)]',chr(44032),sep='\n')
#2자이상의 문자열 전달시:TypeError: ord() expected a character, but string of length 2 found
#codeValue=ord(input('한 문자를 입력하세요?'))
#print('value:{},type:{}'.format(codeValue,type(codeValue)))
#1]아스키 코드값을 알때
#isNumber = 48 <=codeValue <=57
#2]아스키 코드값을 모를때
#isNumber = ord('0') <=codeValue <=ord('9')#[o]
#isNumber = '0' <=codeValue <='9'#[x]TypeError: '<=' not supported between instances of 'str' and 'int'
#isNumber = '0' <= str(codeValue) <='9'#[o]
'''
if isNumber :
    print('당신이 입력한 문자는 숫자이군요')
if not isNumber:
    print('당신이 입력한 문자는 숫자가 아니군요')
'''
asciiCode = input('한 문자를 입력하세요?')
'''
문]사용자가 입력한 문자가 알파벳이거나 숫자이면
  '알파벳 혹은 숫자'라고 출력하고
  아니면 '기타'라고 출력 하여라.
    (아스키 코드값 모른다고 가정) else문 불가
  참고로 영문 알파벳의 
  아스키 코드값은 대문자 A(65)~Z(90) ,소문자 a(97) ~z(122)
'''
'''
isAlphabet = '0' <= asciiCode and '9' >= asciiCode  or\
             'a' <= asciiCode <='z' or\
             'A' <= asciiCode <='Z'
if isAlphabet :
    print('알파벳 혹은 숫자')
if not isAlphabet:
    print('기타')
'''
'''
문]사용자가 입력한 값이 숫자인지 먼저 판단하고
   숫자라면 2의 배수인지를 판단하여
   2의 배수인 경우만 '2의 배수입니다'라고 출력하여라.
   2의 배수가 아닌 경우 '2의 배수가 아니다'라고 출력
   문자 '0'의 아스키 코드값:48
        '1':49 '2':50......
'''
#방법1]하나의 조건식안에서 논리 연산으로 처리
'''
isMultiple = '0' <= asciiCode and '9' >= asciiCode and (ord(asciiCode)-ord('0')) %2 ==0
if isMultiple :
    print('2의 배수입니다')
if '0' <= asciiCode and '9' >= asciiCode and not isMultiple:
    print('2의 배수가 아니다')
'''
#방법2]if문 안의 if문으로 처리
if '0' <= asciiCode and '9' >= asciiCode :
    isMultiple =  (ord(asciiCode)-ord('0')) %2 ==0
    if isMultiple:
        print('2의 배수입니다')
    if not isMultiple:
        print('2의 배수가 아니다')



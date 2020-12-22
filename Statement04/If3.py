kor=99;eng=80;math=96
avg = (kor+eng+math)/3
if avg >=90 :
    print('A학점')
elif avg >=80:
    print('B학점')
elif avg >= 70:
    print('C학점')
elif avg >= 60:
    print('D학점')
else:
    print('F학점')
'''문]
숫자인지 판단후 2의 배수를 판단하고
2의 배수면 "2의 배수"출력,아니면 "2의 배수가 아님" 출력
또한 숫자가 아니고
알파벳이라면 대소문자를 판단한후
대문자인경우 "대문자" 출력, 소문자인 경우 "소문자"출력
단, if ~elif()~[else]만이용
'''
'''
char_ = input('한 문자를 입력?')
if '0' <= char_ <='9' and (ord(char_)-ord('0')) % 2 == 0 :
    print('2의 배수')
elif '0' <= char_ <='9' and not (ord(char_)-ord('0')) % 2 == 0 :
    print('2의 배수가 아님')
elif 'a' <= char_ <= 'z':
    print('소문자')
elif 'A' <= char_ <= 'Z':
    print('대문자')
else:
    print('기타')
'''
'''
문]  사용자로 부터 한 문자를 입력받아 숫자이면 "숫자"
     알파벳이면 "알파벳"
     숫자도 알파벳도 아니면 "기타"를 출력하여라.
     if ~ elif ~ else 사용 
'''
'''
char_ = input('한 문자를 입력?')
if '0' <= char_ <= '9':
    print('숫자')
elif 'A' <= char_ <= 'Z' or 'a' <= char_ <='z':
    print('알파벳')
else
    print('기타')
'''
#문](종합)세 숫자 중 최대 값을 구하는
#   로직을 작성하자(if문 형식 3가지중 아무거나 사용가능)
num1,num2,num3 = 199,204,19
max = num1
if max < num2 :
    max = num2
if max < num3:
    max = num3
print('최대값 : ',max)

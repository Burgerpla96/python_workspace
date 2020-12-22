#bool형:True,False 두 값만 가진다
#      True는 1, False는 0의 값을 가진다
#0,0.0,0+0j는 False와 같고 None,''(빈문자) ,빈 객체([],(),{},set())는 조건식으로 판단시 False로 간주된다
print('[bool형 연습]')
b1 = True
b2 = False
print('value:',b1,',type:',type(b1),sep="")
#산술연산[O]
print(b1 + b2)# 1+0   => 1
#비교연산[O]
print(b1 > b2)# 1 > 0   => True
#논리 연산[O]
print(b1 and b2)# True and False => False
print('[escaped문자 연습]')
print('Welcome To PYTHON\n',end="")
print('Welcome To PYTHON',end='')
print('\nHi PYTHON',end='')
print('\nLet\'s Do it\nGo Fighting!!')
#2]\r:커서를 해당 줄에서 맨 처음으로(carrige return)
print("My Nick is Superman\rXX")
#3]\t:탭키 만큼 띄어쓰기 기능
print('국어t영어t수학')
print('국어\t영어\t수학')
#4]\':single quotation 표시
#문자열을 '(싱글쿼테이션)으로 감싸도 되는 곳에서는 의미 있다.
print('나의 닉은 \'슈퍼맨\' 입니다')
#5]\":double quotaion표시
print("나의 닉은 \"슈퍼맨\" 입니다")
#6]\\:\은 이스케이프 문자 역할을 하는
# 특수문자가 아니라는 것을
# 인터프리터에게
# 알려주는 기능(중요)
print("E:\nDrive\table")
'''
E:
Drive	able
'''
print("E:\\nDrive\\table")
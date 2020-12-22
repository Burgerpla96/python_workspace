#파이썬에서 문자열은 만드는 방법은 총 4가지로
# ' , " ,''',"""로 감싸면 문자열이 된다.
print('[문자열 만들기 1]')
print('Hello World')
print('[문자열 만들기 2]')
print("Hello World")
print('[문자열 만들기 3]')
print('''
    Hello World
    Hi Python!!!
    Good Luck To You!!!
    ''')
print('[문자열 만들기 4]')
print(
"""
    Hello World
    Hi Python!!!
    Good Luck To You!!!
    """)
print('[문자열안에 \' 넣기]')
print('파이썬 3.9\'버전')
print("[문자열안에 \" 넣기]")
print("파이썬 3.9\"버전")
print("[문자열안에 \" 와 ' 동시에 넣기]")
# '''와 """안에는 ' 와 " 둘다 넣을 수 있다
print('''
    Hello World
    Hi "Python"!!!
    Good Luck To 'You'!!!
    ''')
#문자열 길이 구하기
print('[len()함수로 문자열 길이 구하기]')
print("'Hello'의 길이:"+str(len('Hello')))
print("'안녕하세요'의 길이:"+str(len('안녕하세요')))
'''
※유니코드 문자열을 인코딩없이 그대로 파일에 쓰거나 다른 시스템으로 
  네트워크 전송을 할 수는 없다. 
  왜냐하면 유니코드 문자열은 단순히 문자셋의 규칙이기 때문이다.
  파일에 쓰거나 다른 시스템으로 유니코드 문자열을 전송하기 위해서는 
 바이트로 변환해야만 한다
'''
#encode('문자셋') : 유니코드 문자열을 바이트 문자열로 만드는 함수
#문자셋를 생략하면 디폴트 값인 utf-8로 동작.

print('[encode()함수로 문자열의 바이트길이 구하기]')
print('Hello')
print('Hello'.encode(encoding='utf-8'))#b'Hello'
print(len('Hello'.encode(encoding='utf-8')))
#한글은 유니코드로 파이썬에서는 한글 한자가 3바이트를 차지한다
print('안녕하세요')
enc = '안녕하세요'.encode(encoding='utf-8')
print(enc)#b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'
print(len(enc))#15
#decode():인코딩된 바이트 문자열을 유니코드 문자열로 변환하는 함수
print('[인코딩된 바이트 문자열을 다시 유니코드 문자열로 변환]')
print(enc.decode())# 유니코드 문자열
#문자열 연결하기 : + 사용
print('[+로 문자열 연결하기]')
print('Hello '+'World')
#문자열 반복하기 : * 사용
#0이나 음수를 곱하면 빈 문자열 단, 실수는 곱할 수 없다(에러)
print('[* 로 문자열 반복하기]')
print('파이썬 ' * 3)
mul = '파이썬' * -3
print('value:',mul,',len:',len(mul),sep='')#빈 문자열
#print('문자열 : '+100)#TypeError: can only concatenate str (not "int") to str
#str(): 숫자(정수, 실수)를 문자열로 변환하는 함수
print('문자열 : '+str(100))#[o]


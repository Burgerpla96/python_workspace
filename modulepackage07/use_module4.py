#use_module4.py:from절을 사용해서  module4 사용하기
'''
print('[from 패키지.모듈명 import * 혹은 변수,함수,클래스]')
#아래 처럼 가져올때는 date패키지의 __init__.py의 __all__변수에
#지정한 것과 상관없이 모두 사용할 수 있다
from date.module4 import *
print(dir())
print('년도:',getYear())
print('월:',getMonth())
print('일:',getDate())
'''

print('[from 패키지 import * 혹은 변수,함수,클래스]')
from date import *
print(dir())
#print('년도:',getYear())#[x]초기화 파일 __init__.py설정 전 NameError: name 'getYear' is not defined
print('년도:',getYear())#[O]초기화 파일 __init__.py설정 후
print('일:',getDate())#[O]

#print('월:',getMonth())#[X]NameError: name 'getMonth' is not defined


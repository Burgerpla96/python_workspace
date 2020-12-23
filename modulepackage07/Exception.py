# try:
#     list_ =[]
#     fnum,snum = map(int,input('두 개의 숫자를 입력?(공백)').split())
#     list_.append(fnum)
#     list_.append(snum)
#
#     result = list_[0]/list_[1]
#     print(result)
# except (ValueError, ZeroDivisionError, IndexError) as e:
#     print('예외 발생:',e)
'''
except Exception:#java처럼 오류는 나지않지만 모든 오류를 Exception이 잡는다.
    print('오류발생')
except ValueError:
    print('숫자만 입력')
'''

try:
    fnum,snum=0,0
    result = fnum/snum
    print(result)
except:
    print('오류')

try:
    fnum, snum = 0, 0
    result = fnum / snum
    print(result)
except Exception as e:# as 뒤에 변수를 지정하면 변수에 에러 메시지가 저장됨
    print('오류 message:',e)


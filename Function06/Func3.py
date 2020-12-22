print('[함수형식 3 - 매개변수 YES,반환값 NO]')
#start부터 end까지 누적합 구하는 함수
def getTotal(start,end):
    sum_=0
    for i in range(start,end+1):
        sum_ += i

    print('%d부터 %d까지 누적합:%d' % (start,end,sum_))
# 함수 호출
# 변수에 저장후 변수 전달
start,end = 1,10
getTotal(start,end)
'''문] 국영수 세 과목의 점수를 매개변수로 전달받아
    평균을 구하고 학점을 출력하는 함수를 정의해라
    그리고 함수를 호출하여 결과를 확인해라.'''
def printGrade(kor,eng,math):
    avg =(kor+eng+math) / 3
    if avg >=90:
        print('A학점')
    elif avg >=80:
        print('B학점')
    elif avg >=70:
        print('C학점')
    elif avg >=60:
        print('D학점')
    else:
        print('F학점')
#함수 호출
printGrade(90,89,95)
score = [
    [90,67,89],
    [45,67,88],
    [56,100,99],
    [99,34,88],
    [99,88,99]]
#문]위에 정의한 printGrade()함수를 호출하여
#2차원 리스트 score에 저장된 5명의 학생의
#학점을 출력하여라.
for i in range(len(score)):
    print('[{}번째 학생의 성적]'.format(i+1))
    printGrade(score[i][0],score[i][1],score[i][2])
'''
  문] 숫자 두개를 매개변수로 입력받아서 즉 시작단 과 끝단을 
      매개변수에 입력받아  해당 구구단을 출력하는 함수를 정의하고
      함수를 호출하여라. 
'''
def printGugudan(start,end):
    for k in range(1,end+1):
        for j in range(start,end+1):
            print('%-2d * %-2d = %-4d ' % (j,k,k*j),end='')
        print()#줄바꿈
printGugudan(2,9)
print('=' * 225)
printGugudan(2,16)
print('[함수형식 4 - 매개변수 YES,반환값 YES]')
'''
 인원수를 매개변수로 전달받아
 인원수만큼 나이를 사용자로부터 입력받고
 그 나이를 합을 반환하는 함수 정의 
'''
def getTotalAge(persons):
    total=0
    for i in range(persons):
        total += int(input('{}번째 학생의 나이 입력?'.format(i+1)))

    print(persons,'명의 나이 합:',end='',sep='')
    return total
print(getTotalAge(3))
'''
문]매개변수로 두 숫자와 연산자(+,-,*,/,%)를
전달 받아서 그 결과값을 반환하는 함수를 정의해라
함수를 호출하여 그 결과값을 확인 하여라.
'''
def getCalc(num1,num2,op):
    if op == '+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2
    else:
        return 99999999999999999999999999999999999999999999999999999
num1,num2 = tuple(map(int,input('공백기준 두 개의 숫자 입력?').split()))
op = input('연산자 입력?')
calc = getCalc(num1,num2,op)
if calc == 99999999999999999999999999999999999999999999999999999:
    print('잘못된 연산자 기호')
else:
    print('{} {} {} = {}입니다'.format(num1,op,num2,calc))
'''
* 문]여러개의 숫자를 입력받아서 그 중에 최대값을 구하는 함수를 정의하자
단, 숫자의 개수는 매개변수로 입력받고 숫자의 개수 만큼 사용자로부터 숫자를
입력받아 최대값을 구해 그 최대값을 반환하는 함수이다.
'''
def getMax(count_):
    max_ = 0
    for i in range(count_):
        num = int(input('{}번째 숫자 입력?'.format(i+1)))
        if num > max_:
            max_ = num
    return max_
print('최대값:',getMax(3))









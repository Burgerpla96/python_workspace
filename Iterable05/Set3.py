print('[set 표현식 첫번째 - {}]')
print({i for i in 'HELLO'})#{'H', 'E', 'O', 'L'}
print('[set 표현식 두번째 - set()]')
print(set({i for i in 'HELLO'}))#[O]
print(set(i for i in 'HELLO'))#[O]
print('[set 표현식 세번째 - 딕셔너리]')
a={'kor':90,'eng':80,'math':100}
print({key for key in a})#a.keys()와 같다
print({key for key in a if key != 'math'})#{'eng', 'kor'}


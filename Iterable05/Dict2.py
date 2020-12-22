print('[딕션너리의 주요 메소드]')
print('1.setdefault(키) 혹은 setdefault(키,기본값)')
a={'name':'가길동','age':20,'addr':'천호동'}
a.setdefault('tall')#value는 None.a['tall']=None와 같다
print(a)
a.setdefault('weight',30)#a['weight']=30와 같다
#setdefault는 기존 키값의 value는 수정이 안된다
#a.setdefault('name','가길동2')#수정안됨
#a['name']='가길동2'#수정됨
a.update(name='가길동2')#a['name']='가길동2' 와 같다
print(a)
print('2.update(키=값): 기존 키에 해당하는 값이 수정됨')
a.update(tel='010')#없는 키로 update()하면 해당 키가 요소로 추가된다
print(a)
print('3.pop(키) 혹은 pop(키,기본값)')
#삭제한 키의 밸류값 반환
#pop(키) : 키에 해당하는 요소 삭제
#          만약 키가 없다면 에러발생(KeyError)
#pop(키,기본값):키가 없으면 에러 발생하지 않고 그냥 기본값 반환
print('삭제한 요소의 value:',a.pop('weight'))
#print('삭제한 요소의 value:',a.pop('years'))#KeyError: 'years'
print('삭제한 요소의 value:',a.pop('years',-1))#-1
print(a)
#del 딕셔너리객체[키]#키가 존재하지 않으면 KeyError발샐 .print문에 사용불가
del a['tall']
#del a['tall']#KeyError: 'tall'
print(a)
print('4.popitem() : 마지막요소 삭제.삭제된 요소를 튜플로 반환')
key,value=a.popitem()#('tel', '010')
print('삭제된 요소 key:{},value:{}'.format(key,value))

print('5.clear() :전체 요소 삭제.반환값 없다')
a.clear()
print(a)#{}
#dict()생성자로 딕셔너리 생성
b = dict(institute='KOSMO',loc='가산디지털단지역',course='파이썬을 활용한 자바과정')
print('6.copy()함수')
c= b.copy()
print('b의 주소:{},c의 주소{}'.format(id(b),id(c)))
b.update(loc='강남')
print('b:',b)
print('c:',c)

d= b
print('b의 주소:{},d의 주소{}'.format(id(b),id(d)))
b.update(loc='제주도')
print('b:',b)
print('d:',d)

print('7.get(키)함수 혹은 get(키,기본값)함수')
#키가 없어도 에러 발생 안함
#get(없는 키)는 None반환
#get(없는키,기본값)는 기본값 반환
#print(b['location'])#KeyError: 'location'
print(b.get('location'))
print(b.get('location','강릉'))
print('8.items()/keys()/values()함수')
x=b.items()
print('value:{},type:{}'.format(x,type(x)))#dict_items([('institute', 'KOSMO'), ('loc', '제주도'), ('course', '파이썬을 활용한 자바과정')]),<class 'dict_items'>
print(dir(x))#__iter__
for key,value in x:
    print('키:{},값:{}'.format(key,value))

y = b.keys()
print('value:{},type:{}'.format(y,type(y)))#dict_keys(['institute', 'loc', 'course']),<class 'dict_keys'>
print(dir(y))

for key in y:
    print(key)

z=b.values()
print('value:{},type:{}'.format(z,type(z)))#dict_values(['KOSMO', '제주도', '파이썬을 활용한 자바과정']),<class 'dict_values'>
print(dir(z))
for value in z:
    print(value)

print('9.dict.fromkeys(리스트나 튜플)함수 혹은 dict.fromkeys(리스트나 튜플,값)함수')
#반복가능한 객체의 요소를 키로 사용하고 두번째인자인 값은 각 키의 value로 사용하는
#새로운 딕션너리객체 반환
print(dict.fromkeys([1,2,3,4,5]))#{1: None, 2: None, 3: None, 4: None, 5: None}
print(dict.fromkeys([1,2,3,4,5],100))#{1: 100, 2: 100, 3: 100, 4: 100, 5: 100}








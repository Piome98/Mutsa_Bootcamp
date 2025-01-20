"""p = 'hong', (28,167), '010-2179-7048','Korea'
name, (age,height), phone, address = p

print(name, age, height, phone, address, sep = ' ')

name, (_, he), _, _ = p # _(언더스코어)를 이용한 언패킹 예제 -> 값 무시
print(name, he, end='===============', sep=',')

ps = [('Lee',172),('Jung',182),('Yoon',179)] #리스트에 담긴 튜플
for n,h in ps:
    print(n,h, sep = ', ')
"""
from collections import namedtuple

# 네임드 튜플
"""
Tri = namedtuple('Triangle',['width','height'])

t = Tri(3,7) # 네임드 튜플 객체 생성
print(t[0],t[1]) #일반 튜플과 동일한 방법으로 접근 가능하다.

print(t.width , t.height) #일반 튜플과 달리 이름으로도 접근이 가능하다.

def show(n1,n2):
    print(n1, n2)

t = Tri(3,8)
show(*t)

t = Tri(1,1)"""
# t[0] = 1 # 에러가 나는 이유 -> 튜플의 값을 변경하려고 해서(immutable임)

# 네임드 튜플을 사용하여
"""Circle = namedtuple('Circle', 'radius')
circle = Circle(10)
print(circle[0])
print(circle.radius)"""

# dic의 생성과 zip
"""dic = {'a':1, 'b':2, 'c':3}
print(dic)
print(type({}))
# 주의 {}중괄호로 묶인 두 가지 타입 -> dict, set
dic1 = dict(a=1, b=2, c=3) # 형변환 함수 이용
print(dic1)

dic2 = dict([('a',1), ('b',2), ('c',3)]) # 리스트로 파라미터 받아서 각각 키값과 value값에 저장
print(dic2)

dic3 = dict((('a',1), ('b',2), ('c',3))) # 튜플로 파라미터 받아서 각각 키값과 value값에 저장
print(dic3)

dic4 = dict(zip(['a', 'b', 'c'], [1,2,3])) # zip함수를 이용해 왼쪽 리스트는 키값으로, 오른쪽 리스트는 value값으로 할당
print(dic4)

if dic1 == dic2 == dic3 == dic4:
    print(True)
"""
# zip을 for문으로 구현
"""z = zip(['a', 'b', 'c'], [1,2,3]) # iterable 객체
for i in z:
    print(i)

t = tuple(zip('abc', (1,2,3)))
print(t)

z = zip(['abc', (1,2,3), ('one', 'two', 'three')])
print(list(z))"""

#func(*iterable)     iterable 객체를 전달하면서 *을 붙여서 함수 호출할 때
#func(**dict)        dict 객체를 전달하면서 **을 붙여서 함수 호출할 때
#def func(*args)     함수를 정의하면서 매개변수 args에 *붙일 때
#def func(**args)    함수를 정의하면서 매개변수 args에 **붙일 때

"""def who(a,b,c):
    print(a,b,c, sep=' ')

who(1,2,3)
who(*[1,2,3]) # 언패킹
who(*(1,2,3)) # 언패킹
who(*'abc')   # 언패킹

dic1 = dict(a=1, b=2, c=3)
who(*dic1)  # 딕셔너리의 경우 * 한개짜리는 키 값을 언패킹 해서 넘김
who(**dic1) # 딕셔너리의 경우 **두개짜리는 value값을 언패킹해서 넘김"""

# key 와 value를 한번에 넘기는 방법:
"""for k, v in dic1.items():
    print(k,v)
who(*dic1.items())

def func(*args):
    print(args)

func()    # 빈 튜플이 나옴
func(1)   # 절반이 빈 튜플 나옴(1,)
func(1,2) # 1,2"""

"""def func(**args): # 딕셔너리로 묶음
    print(args)

func(a=1) # {'a':1} 생성되어 args에 전달
func(a=1, b=2) #{'a':1, 'b':2} 생성되어 args에 전달달
func(a=1,b=2, c=3)

def practical_func(*arg, **args):
    print(arg)
    print(args)

practical_func(1,2,3,a=1,b=2) # 1,2,3으로 묶이고, 포지션인자는 딕셔너리로 묶이고"""

"""def sumI(*nums):
    s = 0
    for i in nums:
        s += i
    return s 

print(sumI(1, 2, 3, 4))
print(sum(1,2,3,4,5,6,7,8,9)) 
"""


"""users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'},
         {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'gender': 'F'}]

female = list(filter(lambda user: user['gender'] =="F", users ))
for name in female:
    print(name['name'])

"""

# ordered dictionary:

"""d = {}
d['a'] = 1 # 제일 먼저 저장
d['b'] = 2 # 두 번째로 저장
d['c'] = 3 # 마지막에 저장

print(d)

import sys
print(sys.version)

from collections import OrderedDict # collections 모듈의 OrderedDict
od = OrderedDict() # OrderedDict 객체 생성
od['a'] = 1 # 딕셔너리 사용 방법과 동일
od['b'] = 2
od['c'] = 3
od
OrderedDict([('a',1),('b',2),('c',3)])
for kv in od.items(): # 딕셔너리와 마찬가지로 items 메소드 호출 가능
    print(kv)

('a', 1)
('b', 2)
('c', 3)"""

# Ordered dictionary의 사용 이유:
"""d1 = dict(a = 1, b = 2, c = 3)
d2 = dict(c = 3, a = 1, b = 2)

print(d1)
print(d2)
print(d1 == d2)

od1 = OrderedDict(a = 1, b = 2, c = 3)
od2 = OrderedDict(c = 3, a = 1, b = 2) 

print(od1)
print(od2)
print(od1 == od2) # 순서가 부여되므로 입력 순서가 다르면 False 출력 -> 순서 있는 dictionary는 OrderedDict로 생성"""


# set 과 FrozenSet 차이
# set 예제:
"""A = set(['a', 'b', 'c', 'd', 'f']) # set함수에 iterable 객체 전달해서 set 생성
B = set('fdca') # 문자열도 iterable 객체이미ㅡ로 이를 통해 set 생성 가능

A == B # 저장 순서 상관(x) -> component가 같으면 동일 객체

for c in A and B:
    print(c, end =' ')


# frozenset 사용 예제:
A = frozenset(['a', 'b', 'c', 'd'])
B = frozenset(['a', 'b', 'd', 'e', 'f'])

print(A)
print(B)
print(A-B)
print(A|B)

t = [3,3,3,3,3,'z', 'z'] # 중복 제거
t = list(set(t))
print(t)"""

# frozenset은 immutable 데이터 타입-> 선언 및 초기화 된 후로 값 변경 불가
"""frozen_set = frozenset({1,2,3,5,5}) 
print(frozen_set)
#frozen_set.add(6) #  에러 발생 
frozen_set.discard(7) #  에러 발생"""

# 정렬 -> sort(), sorted, key
"""ns =  [3,1,2,5]
ns.sort()
print(ns)

ns.sort(reverse=True)
print(ns)

def age(t):
    return t[1]

person_info = [('hong', 28), ('go', 27), ('park',29)]
person_info.sort(key=age)
print(person_info)
person_info.sort(key=age,reverse=True) # 키워드 인자로 함수를 집어넣음(콜백 함수) -> key == 정렬 기준
print(person_info)"""



"""names = ['asdasdadasf', 'qwerwqerqwer', 'asdfasdf']
def count(t):
    return len(t)

names.sort(key = count) # 글자 개수 순서대로 정렬
print(names)

names.sort(key = lambda t: len(t))
print(names)

names.sort(key = len)
print(names)"""


"""nums = [(3,1), (2,9), (0,5)]
nums.sort(key= lambda x: x[0] + x[1], reverse=True)
print(nums)

nums_dict = dict(nums)
nums_dict = nums_dict.sort(*nums_dict.items)
print(nums_dict)"""

"""arr = ['abc', 'bac', 'bca']
arr.sort(key = lambda x : x[1])
print(arr)
"""
# resesion
# 1, 2. 네임드 튜플이란: 튜플의 컴포넌트에 이름이 붙어있는 형태로, 일반 튜플과 동일한 기능에 더해 이름으로도 컴포넌트에 접근이 가능하다
"""Tri = namedtuple('Triangle',['width','height'])

t = Tri(10,18) # namedTuple은 camel case를 쓴 것에서 class 임을 짐작할 수 있다 -> 파라미터를 입력해서 t를 namedTuple의 객체로 생성한다

print(t[0],t[1]) #일반 튜플과 동일한 방법으로 접근 가능하다.

print(t.width , t.height) # 이름이 부여돼있으므로 컴포넌트의 이름을 이용해 접근이 가능하다

def show(n1,n2):
    print(n1, n2)

show(*t) # 튜플의 컴포넌트 전체를 불러온다"""

# 3.아래를 완성하시오.
"""
Circle = namedtuple('Circle',['radius'])

circle = Circle(10,)

print(circle[0]) #10
print(circle.radius) #10"""

# 4, 5 딕셔너리 만드는 4가지 케이스를 예를 들어 설명하시오. -> 정확히는 5가지 방법이 있다
"""dic = {'a':1, 'b':2, 'c':3} # 키값과 value값 직접 부여

dic1 = dict(a=1, b=2, c=3) # 형변환 함수 이용
print(dic1)

dic2 = dict([('a',1), ('b',2), ('c',3)]) # 리스트로 파라미터 받아서 각각 키값과 value값에 저장
print(dic2)

dic3 = dict((('a',1), ('b',2), ('c',3))) # 튜플로 파라미터 받아서 각각 키값과 value값에 저장
print(dic3)

dic4 = dict(zip(['a', 'b', 'c'], [1,2,3])) # zip함수를 이용해 왼쪽 리스트는 키값으로, 오른쪽 리스트는 value값으로 할당
print(dic4)"""

# 6.  아래를 zip함수를 이용하여 만드시오.
"""dic = dict((('a', 1), ('b', 2), ('c', 3)))
dic_zip = zip(tuple(dic.keys()), tuple(dic.values()))
print(dic)
print(dict(dic_zip))"""

# 7. 아래를 zip함수를 이용하여 만드시오.
"""zipper = zip(('a','b','c'),(1,2,3),('one','two','three'))
print(list(zipper))"""

# 8. * 와 ** 사용 규칙 4가지로 요약하여 설명하시오.
#func(*iterable)  # iterable 객체 unpacking -> mutable datatype
#func(**dict)     # dictionary unpacking -> key, value 쌍을 함수의 키워드 인자로 unpack하여 전달
#def func(*args)  # 가변 위치 인수    -> 함수가 여러 개의 posional 인자를 받을 수 있도록 정의할 때 사용  
#def func(**args) # 가변 키워드 인수  -> 함수가 여러 개의 keyword 인자를 받을 수 있도록 정의할 때 사용


# 9. 아래의 함수가 있다. 키와 값을 한꺼번에 넘기는 방법을 코딩하시오.

"""def who(a,b,c):
    print(a,b,c ,sep=",")

d = dict(a=1,b=2,c=3)
who(*d.items()) # iterable 객체를 언패킹 -> 키값과 키값에 해당하는 value값을 반환환
who(**d) # 키값을 전달받아 value값 반환"""

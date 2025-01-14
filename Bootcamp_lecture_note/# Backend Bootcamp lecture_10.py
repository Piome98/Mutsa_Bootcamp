"""import random

class Person:
    def __init__(self, name):
        self.name = name  # 참가자의 이름
        self.numbers = []  # 각 참가자의 난수 리스트
    
    def set_numbers(self):
        # 난수를 3개 생성하여 리스트로 저장
        self.numbers = [random.randint(1, 3) for _ in range(3)]
    
    def get_numbers(self):
        # 저장된 난수를 반환
        return self.numbers
    
# 참가자 이름 입력
name1 = input("첫 번째 참가자의 이름을 입력하세요: ")
name2 = input("두 번째 참가자의 이름을 입력하세요: ")

# 참가자 객체 생성
participant1 = Person(name1)
participant2 = Person(name2)

# 게임 진행
print("\n게임을 시작합니다! 각 참가자는 자신의 차례에 <Enter> 키를 누르세요.")

while True:
    for participant in (participant1, participant2):
        input(f"\n{participant.name}의 차례입니다. <Enter> 키를 누르세요.")
        participant.set_numbers()
        numbers = participant.get_numbers()
        print(f"{participant.name}님의 숫자: {numbers}")
        
        # 숫자가 모두 같은 경우 승리
        if len(set(numbers)) == 1:
            print(f"\n축하합니다! {participant.name}님이 승리하셨습니다!")
            exit()"""

# mutable: list, dict, set / immutable: int, float, str, tuple
"""r = [1, 2, 3]
print(id(r)) # 리스트 주소 확인인

r += [4]
print(r)
print(id(r)) # 프로그램이 실행되는 동안 주소값이 변하지 않음

t = (1, 2, 3)
print(id(t)) # 튜플 주소 확인

t += (4,)   # 튜플은 한개의 요소만 넣을 때는 ,를 붙여줘야함
print(t)
print(id(t)) # 튜플은 새로운 객체를 만들어서 주소값이 변함"""

"""def add_last(m,n):
    m += n
    return m

r = [1, 2, 3]
add_last(r, [4])
print(r) # 리스트는 mutable이라 값이 변함

t = (1, 2, 3)
add_last(t, (4,)) # 튜플은 immutable이라 값이 변하지 않음
print(t)"""

"""def add_tuple(t1,t2):
    t1 += t2
    return t1

tp = (1, 2, 3)
tp = add_tuple(tp, (4,)) # 튜플은 immutable이라 값이 변하지 않음
print(tp)"""

"""def min_max(d):
    d.sort()
    print(d[0], d[-1],sep=',')

l = [3,1,5,4]
min_max(l) # 1,5
print(l)

import copy

def min_max(d):
    d = copy.deepcopy(d) # 리스트를 복사하여 새로운 객체를 만듦
    d.sort()
    print(d[0], d[-1],sep=',')

l = [3,1,5,4]
min_max(l) # 1,5
print(l) # 원본 리스트는 변하지 않음
"""

# iterable: list, tuple, dict, set, str -> 반복 가능한 객체
# iterator: iterable 객체를 반복하는 객체(값을 하나씩 꺼내는 객체)
# iter() 함수로 iterator 객체를 생성
# next() 함수로 iterator 객체에서 값을 하나씩 꺼냄

"""sample = [1, 2, 3]
for num in sample:
    print(num)

# sample.next() # 에러 발생
sample = iter(sample)
sample.next() # 1
sample.__iter__() # 이 방법도 됨
sample.__next__() # 2
sample.__next__() # 3
# sample.__next__() # 에러 발생 -> 더 이상 값이 없음"""

"""class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration
counter = Counter(10)

for i in counter:
    print(i,end=' ') # 0 1 2 3 4 5 6 7 8 9

counter = Counter(10).__iter__()
print(counter)"""

"""import copy

john = ['John', ('man','USA'),[175,23]]
chulsu = copy.deepcopy(john)
john[2][1] += 1
print(john)
print(chulsu) # john과 chulsu는 다른 객체이므로 chulsu는 변하지 않음"""

"""[print(x) for x in range(1,101) if x % 2 == 0] # 2부터 100까지 짝수 출력"""

"""import random

class Person:
    def __init__(self, name):
        self.name = name
        self.numbers = []
    
    def set_numbers(self):
        self.numbers = [random.randint(1, 3) for _ in range(3)]
    
    def get_numbers(self):
        return self.numbers

while True:
    try:
        participant1 = Person(input("첫 번째 참가자의 이름을 입력하세요: "))
        participant2 = Person(input("두 번째 참가자의 이름을 입력하세요: "))
        break
    except:
        print("잘못된 입력입니다. 다시 입력하세요.")
        continue


print("\n게임을 시작합니다! 각 참가자는 자신의 차례에 <Enter> 키를 누르세요.")

is_stop = False
while True:
    for participant in (participant1, participant2):
        input(f"\n{participant.name}의 차례입니다. <Enter> 키를 누르세요.")
        participant.set_numbers()
        numbers = participant.get_numbers()
        print(f"{participant.name}님의 숫자: {numbers}")
        
        
        if (numbers[0] == numbers[1] == numbers[2]):
            print(f"\n축하합니다! {participant.name}님이 승리하셨습니다!")
            break
    
    if is_stop:
        break"""

"""from datetime import datetime 

current_time = datetime.now()
print(current_time)

if current_time.hour < 12:
    print("오전입니다.")
elif current_time.hour == 12:
    print("정오입니다.")
elif current_time.hour > 12:
    print("오후입니다.")
elif current_time.hour == 0:
    print("자정입니다.")
else:
    print("잘못된 시간입니다.")

if 4<= current_time.hour < 12:
    print('굿모닝')
elif 12 <= current_time.hour < 18:
    print('굿애프터눈')
elif 18 <= current_time.hour < 22:
    print('굿이브닝')
else:
    print('굿나잇')"""

# 람다의 이해: 이름이 없는 함수
"""def func1(): # 입력이 없는 함수 -> 호출되면 hello 출력
    print('hello')

print(type(func1)) # <class 'function'>

def func2():
    print('bye')

def caller(fct):
    fct() # fct()는 func1()을 호출 -> fct에 func1이 들어가 있기 때문 (콜백 함수-> 함수를 파라미터로 넘김)

caller(func1) # hello
caller(func2) # bye

def fct_fac(n):
    def exp(x):
        return x ** n
    return exp
f10 = fct_fac(10)
print(f10(10)) # <function fct_fac.<locals>.exp at 0x0000020D3D3A3D30>"""


"""ref = lambda x : print(x *2)
ref('안녕')

f1 = lambda x,y: x + y
print(f1(3,4))  # 7

f2 = lambda x : print(len(x))
f2('simple')    # 6

fct = lambda x,n: x**n
print(fct(2,4)) # 16
print(fct(3,4)) # 81

def fct_fac(n):
    return lambda x: x ** n

f2 = fct_fac(2)
f3 = fct_fac(3)
print(f2(4)) # 16
print(f3(4)) # 64"""

# 람다 함수 만들어서 바로 실행
"""print((lambda x: x**2)(3)) # 9
print((lambda x,y: x+y)(3,4)) # 7"""

# 함수 심화 -> 객체의 증거
"""import sys

def add(x,y):
    return x + y

print(id(add))  # 22636656
print(sys.getsizeof(add)) # 객체 사이즈"""

# ressesion: 오늘의 회고록
# 1. 아래의 메모리 그림을 그려서 설명 부탁드리겟습니다.
"""def add_tuple(t1,t2):
    t1 += t2 # 튜플 t1에 t2를 더하고, t1에 저장
    return t1 

tl = (1, 2, 3)
tr = (4, 5, 6)
add_tuple(tl, tr) # (1, 2, 3, 4, 5, 6) -> 새로운 객체를 만들어서 저장
print(add_tuple(tl, tr)) # (1, 2, 3, 4, 5, 6) """

# 2. 아래의 원본이 바뀌지 않도록 코드를 수정하시오.
"""import copy
def min_max(d):
    d = copy.deepcopy(d) # 딥카피로 객체를 새로 생성
    d.sort()
    print(d[0], d[-1], sep = ",")

l = [3, 1, 5, 4]
min_max(l) # 1,5
print(l) # 원본 리스트가 변하지 않도록 수정"""


# 3. iterable 객체 와 interator 객체에 대하여 설명하시오.
"""iterable: list, tuple, dict, set, str -> 반복 가능한 객체
iterator: iterable 객체를 반복하는 객체(값을 하나씩 꺼내는 객체)
iter() 함수로 iterator 객체를 생성
next() 함수로 iterator 객체에서 값을 하나씩 꺼냄"""

# 4. 아래를 코딩하시오.
"""class Counter:
    def __init__(self,stop):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

counter = Counter(3)

for i in counter:
    print(i, end=' ') #0,1,2"""

# 5. 함수도 객체인 증거를 대시오
"""import sys
def add(x,y):
    return x + y

print(id(add))  # 22636656
print(sys.getsizeof(add)) # 객체 사이즈"""

# 6. 아래의 결과를 예측하고 설명하시오.
"""def say1():
    print('hello')

def say2():
    print('hi')

def caller(fct): 
    fct()  

caller(say1) # hello -> 함수를 호출해 파라미터로 넘김 -> say1()이 호출 -> hello 출력
caller(say2) # hi -> 함수를 호출해 파라미터로 넘김 -> say2()가 호출 -> hi 출력
"""

# 7. 일반함수를 람다함수로 바꾸는 방법에 대하여 설명하시오.
"""def add(x,y):
    return x + y

print((lambda x,y: x+y)(3,4)) # 7 -> 일반함수를 람다함수로 바꾸는 방법은 lambda 키워드를 사용하여 함수를 만들고, 함수를 호출할 때 인자를 넣어주면 됨 
                              #   -> def 키워드를 사용하지 않고 함수를 만들 수 있음"""

# 8. 아래를 람다 함수로 바꾸어 보시오.
"""def fct_fac(n):
    def exp(x): # 함수 내에서 정의된, x의 n제곱을 반환하는 함수
        return x ** n
        return exp  # 위에서 정의한 함수 exp를 반환한다.
    
    
f2 = fct_fac(2) # f2는 제곱을 계산해서 반환하는 함수를 참조한다.
f3 = fct_fac(3) # f3는 세제곱을 계산해서 반환하는 함수를 참조한다."""

"""f2 = lambda x,n: x**n
f3 = lambda x,n: x**n

print(f2(4,2)) # 16
print(f3(4,3)) # 64
"""

# 9. 이름(name), 전화번호(tel) 필드와 생성자 등을 가진 Phone 클래스를 작성하고, 실행 예시와 같이 작동하는 PhoneBook클래스를 작성하라.
"""class Phone:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def __str__(self):
        return f'이름: {self.name}, 전화번호: {self.tel}'
    
class PhoneBook:
    def __init__(self):
        self.phone_book = []

    def add_tel(self, name):
        # 전화번호를 입력받고 Phone 객체를 생성하여 추가
        tel = input(f'{name}의 전화번호를 입력하세요: ')
        self.phone_book.append(Phone(name, tel))

    def search_tel(self, name):
        # 이름으로 전화번호를 검색
        for i in self.phone_book:
            if i.name == name:
                return i
        return None
    
    def all_tel(self):
        # 전화번호부에 저장된 모든 연락처 출력
        for i in self.phone_book:
            print(i)

# PhoneBook 인스턴스 생성
phone_book = PhoneBook()

# 이름을 입력받고 전화번호 추가
while True:
    name = input('이름을 입력하세요: (종료: exit) ')
    if name == 'exit':
        break
    phone_book.add_tel(name)

# 전화번호부 출력
print('\n전화번호부:')
phone_book.all_tel()

# 이름으로 전화번호 검색
search_name = input('\n검색할 이름을 입력하세요: ')
contact = phone_book.search_tel(search_name)

if contact:
    print(f'{search_name}의 전화번호는 {contact.tel}입니다.')
else:
    print(f'{search_name}의 전화번호를 찾을 수 없습니다.')
"""

# 10.문자열을 입력받아 한 글자씩 회전시켜 모두 출력하는 프로그램을 작성하라.
"""word = input('문자열을 입력하세요: ')

for i in range(len(word)):
    print(word[i:] + word[:i], end=' ')
print()
"""


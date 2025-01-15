# 키워드인자와 포지셔널인자:
# 키워드인자는 함수 호출시 인자의 이름을 명시하는 것을 말한다.
# 포지셔널인자는 함수 호출시 인자의 위치를 이용하여 인자를 전달하는 것을 말한다.
# 키워드인자와 포지셔널인자를 혼용하여 사용할 수 있다.
# 키워드인자는 반드시 포지셔널인자 뒤에 사용해야 한다.

"""def func(a, b, c):
    print(a, b, c)

func(1, 2, 3) # 1 2 3
func(a=1, b=2, c=3) # 1 2 3
func(1, c=3, b=2) # 1 2 3
func(1, c=3, b=2) # 1 2 3"""
# func(a=1, 2, 3) # SyntaxError: positional argument follows keyword argument
# func(1, 2, c=3) # TypeError: func() got multiple values for argument 'c'
# func(1, b=2, 3) # SyntaxError: positional argument follows keyword argument
# func(1, b=2, c=3) # 1 2 3
# func(1, b=2, c=3, d=4) # TypeError: func() got an unexpected keyword argument 'd'


# 키워드인자의 기본값:
# 함수의 인자에 기본값을 설정할 수 있다.
# 인자의 기본값을 설정하면 함수 호출시 인자를 생략할 수 있다.
# 인자의 기본값을 설정한 인자는 반드시 포지셔널인자 뒤에 사용해야 한다.
"""
def func(a, b, c=3):
    print(a, b, c)

func(1, 2) # 1 2 3  # c의 기본값이 사용된다.
func(1, 2, 3) # 1 2 3  # c의 기본값이 무시된다."""
# func(1) # TypeError: func() missing 1 required positional argument: 'b'
# func(1, c=3) # TypeError: func() missing 1 required positional argument: 'b'
# func(a=1, b=2) # 1 2 3  # c의 기본값이 사용된다.
# func(a=1, b=2, c=3) # 1 2 3  # c의 기본값이 무시된다.
# func(a=1, b=2, 3) # SyntaxError: positional argument follows keyword argument
# func(a=1, b=2, c=3, d=4) # TypeError: func() got an unexpected keyword argument 'd'
"""
def only_positional(a, b, c=3, /):
    print(a, b, c)

only_positional(1, 2) # 1 2 3  # c의 기본값이 사용된다.
only_positional(1, 2, 3) # 1 2 3  # c의 기본값이 무시된다.


def only_keyword(a, b, c=3, *, d):
    print(a, b, c, d)

only_keyword(1, 2, d=4) # 1 2 3 4  # c의 기본값이 사용된다.
only_keyword(1, 2, 3, d=4) # 1 2 3 4  # c의 기본값이 무시된다.
"""
# a,b는 포지션으로만 h,i는 두가지 다 사용 가능, x,y는 키워드로만
"""def two_type_keyword_positional(a, b, / , h, i , *, x, y):
    print(a - b)
    print(h - i)
    print(x * y)
"""

# 딕셔너리 루핑 테크닉:
# 딕셔너리의 키와 값을 동시에 루핑할 수 있다.
# items() 메소드를 사용하면 키와 값을 동시에 루핑할 수 있다.
# items() 메소드는 키와 값을 튜플로 묶어서 반환한다.

"""d = dict(a=1, b=2, c=3)

for k in d:
    print(k, d[k], end=' ') # a 1 b 2 c 3

for k in d.keys():
    print(k, d[k], end=' ') # a 1 b 2 c 3

for k in d.items():
    print(k, end=' ') # ('a', 1) ('b', 2) ('c', 3)

for k, v in d.items(): # 언패킹 -> 튜플을 풀어서 변수에 할당하는 것
    print(k, v, end=' ') # a 1 b 2 c 3  # 키와 값을 동시에 루핑한다.
"""
# 딕셔너리의 키와 값을 뒤집을 수 있다.
# 딕셔너리의 키와 값을 뒤집으려면 딕셔너리의 키와 값을 뒤집어서 새로운 딕셔너리를 생성한다.

# view 객체는 단순히 키와 값을 얻어오는데 사용할 뿐만 아니라 딕셔너리의 상태를 그대로 반영한다는 특징이 있다
# '뷰'라는 이름처럼 딕셔너리의 현재 상태를 바라본다
# 딕셔너리의 상태가 변하면 view 객체도 같이 변한다
"""d = dict(a=1, b=2, c=3)
d2 = {v: k for k, v in d.items()}
print(d2) # {1: 'a', 2: 'b', 3: 'c'}

vo = d.items() # view 객체 생성

for kv in vo:
    print(kv)

d['a'] = d['a'] + 3 # 값 수정
d['c'] += 2

for kv in vo:
    print(kv)"""

# 딕셔너리도 컴프리핸션 사용 가능
"""d = {k: v for k, v in zip('abc', range(1, 4))}
d1 = dict(a=1, b=2, c=3)
d2 = {k: v*2 for k, v in d1.items()} # d1의 값을 두배 늘린 딕셔너리 생성
print(d2) # {'a': 2, 'b': 4, 'c': 6}
d3 = {k: v **2 for k, v in d1.items()} # d1의 값을 제곱한 딕셔너리 생성
print(d3)

# 딕셔너리 컴프리핸션 -> if 문 사용:
d4 = {k: v for k, v in d1.items() if v % 2 == 1} # 값이 홀수인 경우만 딕셔너리 생성

"""
# map 과 filter 함수:
# map 함수는 리스트의 요소를 지정된 함수로 처리해주는 함수이다.
# map(함수, 리스트)
# filter 함수는 리스트의 요소를 지정된 함수로 걸러주는 함수이다.
# filter(함수, 리스트)
"""
def pow(n):
    return n ** 2

str1 = [1,2,3]
str2 = [pow(str1[0]), pow(str1[1]), pow(str1[2])]
print(str2) # [1, 4, 9]

str3 = list(map(pow, str1)) # map 함수 사용 -> 리스트의 요소를 pow 함수로 처리 -> 리스트로 변환 -> str3에 저장
print(str3) # [1, 4, 9]

ir = map(pow, str1) # map 객체 생성 -> map 객체는 iterator 객체이다(연산이 끝나면 iterator 객체로 리턴됨)
for i in ir:
    print(i, end=' ') # 1 4 9

def sum(n1, n2):
    return n1 + n2

str4 = list(map(sum, str1, str3)) # 두 리스트의 요소를 더한 리스트 생성
print(str4) # [2, 6, 12]"""


"""def fct_fac(n):
    return lambda x: x ** n

f2 = fct_fac(2)
f3 = fct_fac(3)
print(f2(4)) # 16
print(f3(4)) # 64

class Counter():
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
    
counter = Counter(3)

for i in counter:
    print(i, end=' ') # 0 1 2"""

# filter 함수 사용
# filter 함수는 리스트의 요소를 지정된 함수로 걸러주는 함수이다.
# filter(함수, 리스트)

"""def rev(s): # 문자열을 뒤집는 함수 : 1234 -> 4321
    return s == s[::-1]

lambda x: x[::-1] # 문자열을 뒤집는 람다함수

s1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ref = list(map(lambda x: x[::-1], s1)) # 문자열이 뒤집어진 리스트 생성
print(ref) # ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin', 'net']"""

"""def is_odd(n):
    return n % 2 == 1 # 홀수인 경우 True 반환

st = [1,2,3,4,5,6,7,8,9,10]
st1 = list(filter(is_odd, st)) # 홀수만 걸러진 리스트 생성
print(st1) # [1, 3, 5, 7, 9]
"""
# map이든 filter든 람다함수를 사용할 수 있으며, 그 외에도 함수의 형태로 필터링 기준이 되는 함수와 파라미터로 걸러지는 변수를 넣어서 사용한다
"""users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'},
         {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'gender': 'F'}]
def is_woman(user):
    return user['gender'] == 'F'
woman = list(filter(is_woman,users))
print(woman)

for user in filter(is_woman, users):
    print(user['name']) # Madison Martinez -> 여성인 경우 이름만 출력"""

# 튜플, 리스트 언팩킹:
# 튜플과 리스트의 요소를 변수에 할당하는 것을 언패킹이라고 한다.
# 튜플과 리스트의 요소를 변수에 할당할 때 개수가 맞지 않으면 에러가 발생한다.
# 튜플과 리스트의 요소를 변수에 할당할 때 *를 사용하면 나머지 요소를 리스트로 할당한다.
"""
t = (1,2,3)
a,b,c = t # 튜플 언패킹
print(a,b,c) # 1 2 3
print(a)

l = [1,2,3]
a,b,c = l # 리스트 언패킹
print(a,b,c) # 1 2 3
print(a)

nums = [1,2,3,4,5]
n1,n2,*n3_others = nums # 나머지 요소를 리스트로 할당
print(n1)
print(n2)
print(n3_others) # [3, 4, 5]

def pack_unpack(*args): # 가변인자 함수
    return args # 튜플로 반환

i_want_to_unpack, i_want_to_unpack_too, *others = pack_unpack(1,2,3,4,5) # 튜플로 받아서 1,2 언패킹하고 나머진 리스트로 반환
print(i_want_to_unpack) # 1
print(i_want_to_unpack_too)
print(others) # [3, 4, 5]"""

# *파라미터의 응용:
"""def sum(*nums): # 가변인자 함수 -> 인자를 튜플로 받음 -> 인자의 개수에 상관없이 인자를 받을 수 있음 -> nums는 튜플 -> 무조건 튜플로 받음
    s = 0
    for i in nums:
        s += i
    return s

print(sum(1,2,3,4,5)) # 15"""

"""def show_man(name, age, heigt):
    print(name, age, heigt)

p = ('hong', 28, 167)
show_man('hong', 28, 167)
show_man(*('hong',28,167)) # ('hong', 28, 167) -> 튜플이 하나의 요소로 들어감"""
# 함수를 호출할 때 튜플을 언패킹해서 전달하려면 *를 사용한다.
# 사용하는 위치에 따라 패킹 또는 언패킹을 한다
# p에 담긴 값을 풀어서 각각의 매개변수로 전달
# 언패킹하는 케이스는 함수의 인자로 전달할 때 많이 사용한다


# resession:
# 1. 키워드인자와 포지셔널 인자에 대해 설명하시오:
# 키워드 인자는 매개변수의 이름을 지정해서 인자를 전달 -> 매개변수의 입력 순서와 관계 업싱 이름과 값만 명시하면 됨
# 포지셔널 인자는 매개변수의 위치를 이용해서 인자를 전달 -> 매개변수의 입력 순서를 지켜야 함

"""def func_keyword(a, b, c):
    print(a, b, c)

def func_positional(a, b, c):
    print(a, b, c)

keyword = func_keyword(a=1, b=2, c=3) # 입력값을 다 전달했으므로 순서와 관계 없이 입력인자가 전달이 됨
keyword2 = func_keyword(c=3, a=1, b=2) 
keyword, keyword2 # (1, 2, 3) (1, 2, 3)

position = func_positional(1,2,3)
position2 = func_positional(1,3,2) # 입력값을 순서대로 전달해야함 따라서 키워드 함수완 달리 b와 c의 값이 바뀜
position, position2 # (1, 2, 3) (1, 3, 2)"""

# 2. 아래가 에러가 나는 이유는?

"""def mul(x,y,/): #포지션 인자만 받겠다.
    print(x * y) 

#mul(x=3,y=4) # 값을 키워드 인자로 전달했기 때문 -> 함수 선언단에서 포지션 인자로만 받겠다고 지정했으므로 포지션 인자만 전달해야됨
mul(3,4) # 12"""

# 3. 아래가 에러가 나는 줄은 몇번째 줄이며 이유는?
"""def only_keyword(*,x,y): # 키워드 인자만 받겠다
    print(x + y) 

only_keyword(x=1,y=2)
# only_keyword(1,2) # 매개변수에 전달되는 값이 포지셔널로 전달됐기 때문에 에러 발생"""

# 4. 아래와 같은 함수가 있다. mix_fun 함수를 호출하여 결과 물이 나오도록 하시오.

"""def mix_fun(a,b,/,h,i,*,x,y): 
    print(a-b) # a,b는 포지션으로만
    print(h-i) # h,i는 두가지 다 사용 가능
    print(x*y) # x,y는 키워드로만

mix_fun(0,0,0,0,x=8,y=3) # 따라서 곱셈 연산을 위해선 키워드 인자로만 전달해야됨"""

# 5. 아래의  출력이 어떻게 나오는지 예측하고, 그이유는?
"""d = dict(a=1,b=2,c=3) # 파라미터로 키워드 인자를 전달 -> 딕셔너리로 생성

vo = d.items()  # view 객체 생성 -> 딕셔너리의 키와 값을 묶어서 반환

for kv in vo: # for kv in d.items()와 같음 -> 딕셔너리 루핑
    print(kv) # 딕셔너리 출력

d['a'] = d['a'] + 3 # 값 수정 -> 딕셔너리의 'a'의 키에 해당하는 value값 수정
d['c'] += 2  # 값 수정 -> 마찬가지로 'c'의 키에 해당하는 value값 수정

for kv in vo:
    print(kv) # 딕셔너리 출력 -> 딕셔너리의 상태가 변하면 view 객체도 같이 변함"""

# 6. 아래의 소스코드를 컴프리헨션으로 줄여 보시오.
"""d1 = dict(a=1,b=2,c=3)

d2 ={} # 딕셔너리 초기화 -> 빈 딕셔너리로 생성성

for k,v in d1.items():
    d2[k] = v*2


#컴프리 헨션으로 채우시오.
d2 = {k: v*2 for k, v in d1.items() } ## d1의 값을 두 배 늘린 딕셔너리 생성 -> 키값은 그대로 두고 value값만 두배로 늘림(람다함수 사용용)
print(d1)
print(d2)"""

# 7.map을 예를 들어 설명해 보시오.
"""def pow(n):
    return n ** 2
mapping = list(map(pow, [1,2,3,4,5])) # map 함수 사용 -> 리스트의 요소를 pow 함수로 처리 -> 리스트로 변환 -> mapping에 저장"""

# 8.filter 함수를 예를 들어 설명하시오.
"""users = [
    {"id": 1, "name": "Alice", "verified": True},
    {"id": 2, "name": "Bob", "verified": False},
    {"id": 3, "name": "Charlie", "verified": True},
    {"id": 4, "name": "Diana", "verified": False},
]

def is_verified(user):
    return user["verified"]

verified_users = list(filter(is_verified, users)) # filter 함수 사용 -> 리스트의 요소를 지정된 함수로 걸러줌 -> 리스트로 변환 -> verified_users에 저장
for person in verified_users:
    print(person['name']) # 딕셔너리로 선언된 users에서 name 키값에 해당하는 value 값만 출력 -> 이름만 출력됨
"""

# 9. 아래가 돌아가도록 sum 함수를 만드시오.
"""st1 = [1,2,3]
st2 = [3,2,1]

def sum(*args): # 가변인자 함수 -> 인자를 튜플로 받음 -> 인자의 개수에 상관없이 인자를 받을 수 있음 -> nums는 튜플 -> 무조건 튜플로 받음
    s = 0
    for i in args:
        s += i # 인자로 받은 값들을 더함
    return s

result = sum(*(st1 + st2)) # 두 리스트를 튜플로 변환하여 합친 후 sum 함수에 전달
print(result)

def sum_different_way(iterable):  # 리스트나 튜플 등 반복 가능한 객체를 처리
    s = 0
    for i in iterable:
        s += i
    return s

result = sum_different_way(tuple(st1) + tuple(st2))  # 튜플을 생성하고 sum 함수에 전달
print(result)"""

# 10. 아래의 함수를 완성하시오.
"""s1 = ['one', 'two','three']
ref = list(map(lambda x:x[::-1],s1)) # 문자열이 뒤집어진 리스트 생성 -> 람다함수 사용 -> lambda x: x[::-1] -> 문자열을 뒤집는 람다함수 -> 입력 인자로 st1의 component 전달
print(ref) 
#['eno', 'owt', 'eerht']"""

# 11, 12 filter 함수를 써서  'gender' 가 M, F 인 사람의 이름만 뽑아내시오.

"""users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'},
         {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'gender': 'F'}]

man = list(filter(lambda user: user['gender'] == 'M', users)) # filter 함수 사용 -> 리스트의 요소를 지정된 함수로 걸러줌 -> 리스트
for name in man:
    print(name['name']) # 딕셔너리로 선언된 users에서 name 키값에 해당하는 value 값만 출력 -> 이름만 출력됨

for name in list(filter(lambda user: user['gender'] == 'F', users)):
    print(name['name']) # 딕셔너리로 선언된 users에서 name 키값에 해당하는 value 값만 출력 -> 이름만 출력됨"""


# 13. 아래 결과를 예측하시오.
"""nums = (1,2,3,4,5)
first, *others, last = nums # 튜플 언패킹 -> *를 사용하면 나머지 요소를 리스트로 할당
print(first) # 1
print(others) # [2, 3, 4]
print(last) # 5
"""

# 14 .함수에서 * 단독으로 쓰일때와 , *변수명 쓰일때의 차이는?
# *단독으로 쓰일때는 가변인자 함수를 만들때 사용
# *변수명으로 쓰일때는 언패킹을 할때 사용

"""def pack_unpack(*args): # 가변인자 함수
    return args # 튜플로 반환

i_want_to_unpack, i_want_to_unpack_too, *others = pack_unpack(1,2,3,4,5) # 튜플로 받아서 1,2 언패킹하고 나머진 리스트로 반환
print(i_want_to_unpack) # 1
print(i_want_to_unpack_too)
print(others) # [3, 4, 5]
"""

# 15. 튜플에서 *이 언패킹 하는 케이스를 예를 들어 설명하시오.
"""t = (1,2,3,4,5) # 쪼개고싶음
a,b,*c = t # a,b는 각각 1,2로 할당되고 나머지는 리스트로 할당됨
print(a) # 1
print(b) # 2
print(c) # [3, 4, 5]
"""
# 16.다음을 프로그래밍 하시오.
"""class Shape:
    def __init__(self,shape):
        self.shape = shape

    def get_area_circle(self,r):
        return 3.14 * r ** 2
    
    def get_area_rectangle(self,w,h):
        return w * h
    
    def get_area_triangle(self,b,h):
        return b * h / 2
    
shape_c = Shape('circle')
shape_rec = Shape('rectangle')

c = shape_c.get_area_circle(10)
print(c)

rec = shape_rec.get_area_rectangle(10,10)
print(rec)
"""


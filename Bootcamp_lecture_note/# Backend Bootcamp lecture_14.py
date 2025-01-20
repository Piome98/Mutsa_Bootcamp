# emumerate 함수
# enumerate(iterable, start=0) -> iterable 객체의 요소를 index와 함께 반환
# start는 index의 시작값을 지정하는 것
# enumerate 객체는 한번 생성되어서 한바퀴 다 돌았으면 다시 enumerate 객체 생성 해야함
# enumerate 객체는 index와 요소를 튜플로 반환
# enumerate 객체는 for문으로 돌릴 수 있음
# enumerate 객체는 딕셔너리로 변환 가능
"""names = ['홍길동','김현주','윤나은','이지선']

eo = enumerate(names)

for i, name in eo: # 한번 생성되어서 한바퀴 다 돌았으면 다시 enumerate(names) 객체 생성 해야함
    print(i, name)

for n in enumerate(names):
    print(n)

dnames = {k:v for k,v in enumerate(sorted(names),1)}    
print(dnames)"""


"""class Simple():
    def seti(self,i):
        self.i = i # 변수 자체를 동적으로 생성한다.
    
    def geti(self):
        return self.i # 에러가 나는 이유
    
s = Simple()
s.i = 100

print(s.geti())

s.hello = lambda s : print(s)

s.hello('hello')

del s.i
del s.hello

s.hello('hello') # 에러가 나는 이유"""



# 상속과 오버로딩
# 상속: 부모 클래스의 모든 속성과 메소드를 자식 클래스가 물려받는 것
# 오버로딩: 같은 이름의 메소드를 여러개 정의하고, 매개변수의 타입과 개수에 따라 다르게 호출하는 것 ->  파이썬은 오버로딩을 지원하지 않음 -> inner method로 구현
# 오버라이딩: 부모 클래스의 메소드를 자식 클래스에서 재정의하는 것
# 다형성: 같은 이름의 메소드가 서로 다른 기능을 하는 것

"""class Account:
    def __init__(self, aid, abl):
        self.aid = aid
        self.abl = abl
    def __add__(self,m):
        self.abl += m
        print('add', m)
    def __sub__(self,m):
        self.abl -= m
        print('sub', m)
    def __call__(self):
        print('call')
        return str(self.aid) + ':' + str(self.abl)
    
def main():
    acnt = Account('kim', 100)
    acnt + 100
    acnt - 50
    print(acnt())

main()"""

# 상속 = 재사용(reuse) = 부모에 있는 함수및 변수를 써먹을수 있다.
# 파이썬 에서는 다중상속 지원 (자바에서는 단일 상속만 지원)
# 다중상속: 여러 부모 클래스로부터 상속을 받는 것
# 다중상속의 문제점: 다이아몬드 문제 -> 다이아몬드 상속 문제는 다중 상속에서 발생하는 문제로, 같은 클래스를 여러 경로로 상속받을 때 발생하는 문제
# 다이아몬드 상속 문제 해결: super() 함수 사용 -> super() 함수는 부모 클래스의 메소드를 호출할 때 사용하는 함수
"""class Father:
    def run(self):
        print("so fast!")

class Mother:
    def dive(self):
        print("so deep!")

class Son(Father,Mother):# 다중 상속
    def __init__(self,num):
        print(num)

    def jump(self):
        print("so high!!")


s = Son(2)
s.jump()
s.run() # 부모 함수 호출 가능
s.dive() # 부모 함수 호출 가능"""

# 상속을 활용한 사각형 삼각형 넓이 구하는 것을 클래스로 ~~
"""
class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self): # 자식이 구현하라.
        pass 

class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__(width,height)

    def area(self):
        return self.width * self.height

rec = Rectangle(10,20)
print(rec.area())

class Triangle(Shape):
    def area(self):
        return self.width * self.height / 2

tri = Triangle(10,20)
print(tri.area())

shape_list = [Rectangle(10,20),Triangle(10,20)]

sum_area = 0
for shape in shape_list:
    sum_area += shape.area()

print(sum_area)"""

# ==============================================================================================================

# 정보 은닉: 객체의 속성을 외부에서 직접 접근하지 못하도록 막는 것 -> 정보 은닉을 위해 private 변수 사용
# 정보 은닉을 위한 방법: private 변수, getter, setter
# private 변수: 변수 이름 앞에 __를 붙이면 private 변수가 됨
# getter: private 변수를 가져오는 메소드
# setter: private 변수를 설정하는 메소드

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self,age):
        if age < 0:
            print('나이는 0보다 작을 수 없습니다.')
        else:
            self.age += age

    def __str__(self):
        return f'이름: {self.name}, 나이: {self.age}' # __str__은 객체를 문자열로 변환할 때 호출되는 메소드 -> 함수 오버라이딩으로 동일 이름의 함수를 재정의
        
    
p = Person('kim', 20)
p.add_age(1)
p.age -= 20
p.age -= 100 # 조건문으로 -값을 받지 않도록 설정했지만 함수에 다이렉트로 접근하면 -값을 받을 수 있음 -> 정보은닉이 필요
print(p)"""

"""""class Person:
    def __init__(self, name, age):
        self.__name = name # 언더바 두개를 붙이면 private 변수가 됨 -> 다이렉트 접근을 차단하고 간접 접근만 허용
        self.__age = age
    # 언더바 하나만 붙이고 사용하는 경우도 있음 이는 protected 변수로 사용 -> 상속받은 클래스에서 사용 가능 -> 다이렉트 접근을 차단하지 않음
    # protected와 private의 차이점은 다이렉트 접근 차단 여부
    # protected 변수엔 함수로 접근 -> 다이렉트 접근을 차단하진 않지만 함수로 접근하게 함으로써 변수의 값을 변경할 때 조건을 걸어줄 수 있음""


    def add_age(self,age):
        if age < 0:
            print('나이는 0보다 작을 수 없습니다.')
        else:
            self.__age += age # private 변수에 접근할 때는 __를 붙여야함
    
    def __str__(self):
        return f'이름: {self.__name}, 나이: {self.__age}'

p = Person('hong', 27)
p.add_age(1)
p.add_age(-30) # 다이렉트 접근 차단
# p.__age -= 100 # 다이렉트 접근 차단
print(p)

# 클래스 인스턴스 내에는 해당 객체의 변수 정보(속성 정보)를 담고 있는 딕셔너리가 존재
p.shool = 'hanyang'
p.address = 'seoul'
print(p.__dict__) # 객체의 속성을 딕셔너리로 반환

# 개발자가 정보 은닉을 위해 __를 사용하면 딕셔너리에 반환될 땐 _클래스명__변수명으로 반환됨"""

# 데코레이터: 함수나 메소드의 앞뒤에 기능을 추가할 때 사용하는 것
# 데코레이터 사용법: @데코레이터 함수 이름
# 데코레이터 함수: 함수를 인자로 받아서 내부에서 다른 함수를 반환하는 함수
# 데코레이터 함수의 구조: def 데코레이터 함수(함수): def wrapper(): return 함수() return wrapper
"""class Emotions: # 클래스 내부에 데코레이터 함수를 정의
    def smile(self):
        print(':-)')
    
    def confused(self):
        print('@_@')


def deco(func):
    def wrapper():
        print('emotion')
        func()  # 함수를 인자로 받아서 내부에서 다른 함수를 반환하는 함수
        print('emotion')
    return wrapper



emotions = Emotions()

smile_deco = deco(emotions.smile)
smile_deco()

confused_deco = deco(emotions.confused)
confused_deco()"""

"""def confused(): # 함수 밖에 데코레이터 함수를 정의
    print('@_@')

def deco(func):
    def wrapper():
        print('emotion')
        func()
        print('emotion')
    return wrapper

confused_deco = deco(confused)
confused_deco()"""

"""def deco(func):
    def wrapper():
        print('emotion')
        func()
        print('emotion')
    return wrapper

@deco # 데코레이터 -> @ + 함수명 == 함수 호출을 의미
def smile2():
    print(':-)')

smile2()"""

# 데코레이터 파라미터가 붙을 때

"""def adder_deco(func):
    def add(*n):  # 튜플 언패킹으로 인자 처리
        print('Result:', func(*n))  # 결과 출력
    return add

@adder_deco
def adder(*nums):  # 입력받은 숫자를 모두 더하는 함수
    return sum(nums)

# 숫자 입력받기
try:
    # 쉼표로 구분된 숫자를 입력받음
    numbers = input("Enter numbers to add (separated by commas): ")

    # 입력된 문자열을 정수 리스트로 변환
    nums = tuple(map(int, numbers.split(',')))  # 문자열을 정수로 변환 후 튜플로 만듦
                                                # map(함수, 리스트) -> 리스트의 모든 요소에 함수를 적용
    adder(*nums)  # 튜플 언패킹을 이용해 adder 호출
except ValueError:
    print("Please enter valid integers separated by commas.")"""


# multiple decorators
"""def deco1(func):
    def wrapper():
        print('deco1')
        func()
        print('deco1')
    return wrapper

def deco2(func):
    def wrapper():
        print('deco--2')
        func()
        print('deco--2')
    return wrapper

@deco1
@deco2
def smile():
    print(':-)')

smile()"""


# 클래스 변수, 클래스 함수, 스태틱 함수
"""class Simple:
    count = 0 # 클래스 변수: 클래스 내에서 공유되는 변수 -> 공용 변수 -> 일반적으로 private으로 선언하진 않음

    def __init__(self, num):
        self.num = num
        Simple.count += 1 # 객체를 생성할 때마다 클래스 변수를 증가시킴

    def get_num(self):
        return self.num
    def set_num(self, num):
        self.num = num

s = Simple(10)
print(s.get_num())
s.set_num(20)
print(s.get_num())

print(Simple.count) # 클래스 변수에 접근할 때는 클래스명.변수명으로 접근
print(s.count) # 물론 클래스의 인스턴스로도 접근 가능

s2 = Simple(20)
print(Simple.count) # 객체의 총 개수를 알 수 있음"""


"""class Circle:
    Pi = 3.14 # 클래스 변수

    def get_area(self,r):
        return Circle.Pi * r * r

c = Circle()
print(c.get_area(10)) 

class Circle2:
    Pi = 3.14 # 클래스 변수
    @classmethod # 클래스 메소드 -> self 대신 cls를 사용 -> 클래스 변수에 접근할 때는 cls.변수명으로 접근
    def get_area(cls,radius):
        return cls.Pi * radius * radius
    
print(Circle2.get_area(10))

result = Circle2.get_area(10)
print(result)

c2 = Circle2()
print(c2.Pi)
result = c2.get_area(10)
print(result)"""



"""
class Card:
    width = 100 # 클래스 변수
    height = 200 # 클래스 변수

    def set_size(self,w,h):
        self.width = w
        self.height = h
    
    def get_size(self):
        return self.width, self.height

    def get_area_of_card(self):
        return self.width * self.height
    
card = Card()
print(card.get_size())
print(card.get_area_of_card())"""

# 클래스 메소드 @classmethod
"""class Calculator:
    def set_num(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self): # 인스턴스 메소드 -> self 를 이용해 인스턴스 변수에 접근
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    
calc = Calculator()
calc.set_num(10,20)
print(calc.add(), calc.sub(), calc.mul(), calc.div())
# print(calc.add(10,20)) # 클래스로 인스턴스 메소드는 접근 불가"""

"""class StaticCalculator:
    @staticmethod
    def add(num1, num2): # 스태틱 메소드 -> self를 사용하지 않음
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2
    
    @staticmethod
    def mul(num1, num2):
        return num1 * num2
    
    @staticmethod
    def div(num1, num2):
        return num1 / num2

static_calc = StaticCalculator()
print(static_calc.add(10,20)) # 스태틱 메소드는 인스턴스로 호출 가능"""

# 프로퍼티의 이해:
"""class Natural:
    def __init__(self, n):
        if n < 0:
            self.__n = 0
        else:
            self.__n = n # 정보 은닉 기능까지 써서 함부로 값을 변경하지 못하게 함

    def getn(self):
        return self.__n
    
    def setn(self, n):
        if n < 0:
            self.__n = 1
        else:
            self.__n = n

    p = property(getn, setn) # 프로퍼티 -> getter, setter를 한번에 정의할 수 있음
    
n1 = Natural(10)
n2 = Natural(-10)

print(n1.getn())
print(n2.p) # 프로퍼티로 인해 n으로 접근 가능 -> getter 함수 호출 -> __p 반환(private 변수)

n1.setn(20)
print(n1.getn())
n1.p = n2.p + n2.p
print(n1.p)"""

# resession

# 1. 정보 은닉이란? 
# 객체의 속성을 외부에서 직접 접근하지 못하도록 막는 것
# 정보 은닉을 위해 private 변수 사용
# private 변수: 변수 이름 앞에 __를 붙이면 private 변수가 됨
# getter: private 변수를 가져오는 메소드
# setter: private 변수를 설정하는 메소드

#2. 아래의 소스코드에서 에러가 나는 이유와 age 50으로 바꾸어 보시오.

"""class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # if 문의 해당 함수에서 0이 들어 가지 않도록 막음
    def add_age(self,age):
        if age < 0:
            print('나이는 0보다 커야 합니다. 나이 정보 오류')
        else:
            self.__age += age

    def __str__(self):
        return f'이름은 {self.__name}, 나이는 {self.__age}'


p = Person('홍길동', 20)
# self.__age -= 20 # 에러가 나는 이유 -> private로 선언돼 있기 때문에 함수로 접근해야 됨
p.add_age(30)
print(p.__str__())"""


# 3. 데코레이터란?
# 함수나 메소드의 앞뒤에 기능을 추가할 때 사용하는 것
# 데코레이터 사용법: @데코레이터 함수 이름
# 데코레이터 함수: 함수를 인자로 받아서 내부에서 다른 함수를 반환하는 함수

# 4. 아래와 같이 출력이 나오도독 데코레이션 함수를 만들어 보시오.
"""def smile():
    print('^_^')

def confused():
    print('@_@')

def deco(fun):

    def wrapper():
        print('emotion!')
        fun()
        print('emotion!')

    return wrapper


smile_deco = deco(smile)
smile_deco()"""


# 5. 아래와 같이 출력이 나오도록  adder_deco 를 만들어 보시오.
"""def adder_deco(func):
    def add(*n): # 튜플 언패킹으로 인자 처리
        result = func(*n)
        print('Result:', func(*n))
        return result
    return add

@adder_deco
def adder1(n1,n2):
    return n1 + n2

@adder_deco
def adder2(n1,n2 ,n3):
    return n1 + n2 + n3

@adder_deco
def adder3(n1,n2 ,n3,n4):
    return n1 + n2 + n3 + n4

adder1(3,5) # 8
adder2(1,2,3) # 6
adder3(1,2,3,4) # 6"""

# 6. 아래를 예를 들어 설명하시오.
# -  클래스 변수 
"""class Simple:
    count = 0 # 클래스 변수

    def __init__(self, num):
        self.num = num
        Simple.count += 1

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num"""



# -  클래스 함수
"""class Circle2:
    Pi = 3.14 # 클래스 변수
    @classmethod # 클래스 메소드 -> self 대신 cls를 사용 -> 클래스 변수에 접근할 때는 cls.변수명으로 접근
    def get_area(cls,radius):
        return cls.Pi * radius * radius
    
print(Circle2.get_area(10))"""


# -  스택틱 함수
"""class StaticCalculator:
    @staticmethod
    def add(num1, num2): # 스태틱 메소드 -> self를 사용하지 않음
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2
    
    @staticmethod
    def mul(num1, num2):
        return num1 * num2
    
    @staticmethod
    def div(num1, num2):
        return num1 / num2
    
static_calc = StaticCalculator()
print(static_calc.add(10,20)) # 스태틱 메소드는 인스턴스로 호출 가능 -> 함수로 접근"""

# 7. 아래가 에러가 나는 이유를 설명하시오.
"""class Calculator:

    @staticmethod # 스태틱 메소드 = 정적 메소드 = 간단한 함수들 = 객체와 상관없는 함수들
    def add(n1, n2):
        return n1 + n2

    def add2(self, n1,n2): #인스턴스 메소드
        return n1 + n2

    @staticmethod
    def mul(n1, n2):
        return n1 * n2
        

cal = Calculator()
# print(Calculator.add2(10,20)) # 에러가 나는 이유 -> 스태틱 메소드는 인스턴스로 호출 불가능
print(cal.add2(10,20)) # 인스턴스로 호출 가능"""

# 8. 아래의 출력 결과를 예측하시오.

"""def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
        print('decorator1')
    return wrapper
 
def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
        print('decorator2')
    return wrapper
 
# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')
 
hello() # 데코레이터 2개로 감싸진 hello 함수가 호출됨됨"""

# 9. 아래가 에러가 나는 이유와 수정을 하시오.
"""class Cirle2:
    PI = 3.12419
    
    @classmethod # 클래스 메소드로 선언이 돼야 클래스 변수에 접근이 가능
    def get_area(cls, radius):
        return cls.PI * radius * radius

print(Cirle2.PI)

result = Cirle2.get_area(5) 
print(result)"""

# 10. 프로퍼티 함수에 대하여 설명하시오.
"""프로퍼티 메서드(Property Method)
@property는 파이썬에서 제공하는 내장 데코레이터로, 클래스 내의 메서드를 마치 인스턴스 변수처럼 사용할 수 있게 만들어줍니다. 
이를 통해 캡슐화를 유지하면서도 속성 값을 읽고 쓸 수 있는 깔끔하고 직관적인 인터페이스를 제공합니다.

주요 특징
1. 인스턴스 변수처럼 접근:
    메서드임에도 불구하고, 호출할 때 괄호 없이 접근할 수 있습니다.

2. 캡슐화(Encapsulation):
    내부적으로 계산되거나 가공된 값을 제공하면서 외부에서는 속성처럼 보이게 만듭니다.
    내부 데이터의 보호 및 무결성을 유지할 수 있습니다.

3. 읽기 전용 속성:
    @property로 선언된 메서드는 기본적으로 읽기 전용입니다.
4. setter와 deleter 지원:
    @property로 선언된 메서드에 대해 @속성.setter 및 @속성.deleter를 사용해 속성을 설정하거나 삭제하는 동작을 정의할 수 있습니다.
"""

"""class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14 * self.__radius ** 2 # 속성처럼 circle.area로 접근할 수 있지만, 값을 바꾸려고 하면 에러 발생(읽기 전용)
    
    
circle = Circle(10)
print(circle.area) # 314.0"""


"""class Circle2:
    def __init__(self, radius):
        self._radius = radius  # protected 변수

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('반지름은 0보다 커야 합니다.')
        self._radius = radius

circle2 = Circle2(10)
print(circle2.radius) # 10

circle2.radius = 5 # setter 함수 호출 -> 값 변경 가능해짐(protected 변수라서 가능)
print(circle2.radius) # 5"""

"""class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # getter
        return self._name

    @name.setter
    def name(self, value):  # setter
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @name.deleter
    def name(self):  # deleter
        print("Deleting name...")
        del self._name

person = Person("Alice")
print(person.name)  # 출력: Alice

person.name = "Bob"  # setter 호출
print(person.name)  # 출력: Bob

del person.name  # deleter 호출
# print(person.name)  # AttributeError 발생"""

    
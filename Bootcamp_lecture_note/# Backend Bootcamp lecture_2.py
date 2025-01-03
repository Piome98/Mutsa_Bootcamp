import math


# 강의 목차:
"""
    1. 지난 시간 학습 정리(메모리)
    2. 함수 및 변수 생성 및 이용
    3. 주석 처리 방법 및 관례
    4. 반복문의 사용법


"""


# 지난 시간 학습정리(메모리 스왑)
"""
a = 10
b = 20

temp = a
a = b
b = temp     # memory swap_1

a, b = b, a  # memory swap_2

print(a, b)
"""

# 함수(function), 메서드(Method):
"""
    input(매개변수)을 받아서 중간 처리 과정(함수)를 통해 output(반환값, 결과)를 출력
    def func():
        변환 내용
        return -> 함수의 결과 출력

    def Method(name):  #name -> 변수 선언 -> 함수에 변수 선언은 파라미터(인자) 라고 표현현
    print('반갑습니다', name)
    print('환영합니다', name)

    Method(3) -> 매개변수의 입력은 자료형에 맞춰서 문자열이면 "" 사용, 숫자형이면 숫자 그대로 입력력


    func()<- 괄호 안에에 매개변수 넣어주면 변환되어 결과값 출력됨

    함수가 생성되지 않은 상태로 함수 안에 함수를 선언하면 무한 루프 발생 -> 에러 발생
    따라서 함수의 생성을 완료하면 꼭 1줄 띄우고 함수 사용 요망



"""
"""
def add(a,b):
    c = a+b
    print(c)

add(1,3)

def adder(num1, num2):
    return num1 + num2 # 결과값을 리턴
    # 때에 따라 return을 단독으로 써서 함수 탈출 가능


result = adder(1,3)
print(result)

print(adder(1,3))

def example():
    print("안녕하세요")
    return # 함수 종결을 의미, break가 더 많이 쓰이지 않나 싶음
    print('블라블라') # 리턴문 뒤의 내용은 실행되지 않음

#파이썬에서만 제공되는 함수 만들기 기능
def say_myself(name, age, man=True): #파라미터(변수)에 값을 집어넣을 수 있음(초기화) -> 초기화: 변수의 시작값을 지정해주는 것것
    print(name, '입니다')
    print('나이:', age)
    print('남자입니까', man) #man이 아닌 다른 값이 입력으로 들어오면 에러 발생
    # 파라미터를 스킵할 수는 있으나, 초기화 된건 스킵이 안되므로 파라미터의 입력 순서에서 초기화 된 파라미터는 꼭 맨 마지막에 넣어야됨됨

say_myself('홍길동', 27)

# 리턴값이 두개 이상일 수 있음
def two_returns():
    return 1,2,3

a,b,c = two_returns()
print(a,b,c)

def calc_result(a,b):
    c = a + b
    d = a - b
    return c,d

x,y = calc_result(5,2)
print(x,y)
"""

# 함수(변수)이름 짓는 법: 
"""
    snake 표기법: 여러 단어로 된 함수 및 변수명을 선언할 때 첫 글자는 무조건 소문자로, 서로 다른 단어를 이을 땐 _(언더바)로 연결
    Camel 표기법: 

"""


# 주석의 생성:
"""
    주석은 작성된 소스코드의 설명을 위한 목적으로 사용됨
    # 함수 및 변수의 선언 일자
    # 함수 및 변수의 작성자
    # 함수 및 변수의 선언 목적
    # 함수에서 사용되는 파라미터(종류):

"""

# 입력 함수-> input() 함수 사용법:
"""
str = input('How old are you: ').format(int)  # "How old are you"를 출력하고 사용자의 입력을 기다림, format()메서드를 이용해 입력되는 값의 자료형을 초기화화
print(str)                                    # 사용자의 입력을 받아서 print() 함수 실행
print(type(str))
print(type(1))                                # 입력받은 파라미터의 타입(자료형) 출력
print(id(1))                                  # 입력받은 파라미터의 인덱스(주소) 출력

year = input('올해는')
print(year)
"""
# eval() 함수 주의
"""
year = int(year) + 1
year = int(year) + 1  
     
print(year)
print(eval("3+5"))                            # eval(): 연산함순데 파라미터(매개변수)로 받은 값을 **강제 연산**해서 결과로 돌려보냄 -> 웬만하면 안쓰는게 좋음
                                              #         사전적 의미론 표현식(문자열로 만들어진 식)을 해석하는 함수

"""

# 반복문 사용법(for):
# 1. 단순 리스트 내 반복 동작 수행:
"""
for i in [0,1,2]:
    print(i)
"""

# 2. 범위, 간격 지정 및 해당 범위 내 반복 동작 수행:
"""
for i in range(1, 101, 1): # 1부터 100까지(마지막 인덱스-1) 인덱스 1 간격으로 반복 동작 수행
    print(i)               # 1부터 100까지 출력
"""
"""
sum = 0
for i in range(1, 11):
    sum = sum + i
    print(sum)             # 반복문 내부에서 print()문 출력하면 i의 인덱스 + 1 되는 단계마다 더해지는 결과값이 출력됨됨
print(sum)                 # 반복문을 탈출한 결과값 -> 최종 1부터 10까지 모두 더한 값 이 출력됨
"""
"""
summation = 0
for i in range(1, 1001, 1):
    summation += i
print(summation)

for i in range(1,101):
    print("Hello world")
"""
"""
for i in range(5):
    print('hello world' + str(i)) # 반복문의 인덱스 시작지점 0, 총 5회 반복이므로 마지막 인덱스는 4
"""
"""
for i in range(1, 10):
    for j in range(1, 10):
        answer = j * i
    print(j,"*", i, "=", answer) # 구구단 2중 for문 이용

def gugudan(dan):
    for i in range(1,10):
        print(dan, "*", i, "=" , dan *i) # 구구단 함수 이용용

gugudan(9) # 입력으로 받은 단수의 구구단만 출력
"""
"""
def whole_gugudan(dan):
    for i in range(1, dan + 1):
        for j in range(1, dan+1):
            answer = j * i
            print(i,"*", j, "=", answer) # 구구단 2중 for문 이용

whole_gugudan(int(input()))

num1 = 1.0000000000000001
num2 = 1.1
print(num1 + num2) # 오차로 0.000000000001 단위 출력 안됨
"""
#같은 숫자라고 해도, 자료형을 어떻게 주느냐에 따라 실제로 연산될 때 취급되는 값이 달라짐
"""
float(1) != int(1)

이를 맞춰주기 위해 실수형을 이진수로 바꾸는 방법이 필요함
+-(1.m) * 2^(e-127)

num3 = 3.14
print(num3)
print(int(num3))
"""



# 추가 문제
"""
def rec_area(width, length):
    area_square = width * length
    return area_square

def tri_area(width, height):
    area_triangle = width * height / 2
    return area_triangle

def circle_area(radius1, radius2):
    area_circle1 = (radius1 **2) * math.pi
    area_circle2 = (radius2 **2) * math.pi
    return area_circle1, area_circle2

print(rec_area(3,4)) # 사각형 넓이 구하는 함수
print(tri_area(2,5)) # 삼각형 넓이 구하는 함수
print(circle_area(2,5)) # 원의 넓이를 구하는 함수

"""

"""
i = 0
while i <= 100:
	
	print(i)
	i += 1
"""



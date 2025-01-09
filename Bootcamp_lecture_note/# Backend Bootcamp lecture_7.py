import pandas as pd
# 객체 지향 프로그래밍(Object Oriented Programming)
"""
객체를 이용한 프로그램으로 객체는 속성과 기능으로 구성된다
객체: 제풐
속성: 이름, 기능, 색깔, 등
객체 지향의 4대 특징: 추상화(클래스), 캡슐화, 상속성, 다형성
"""
"""
class AgeInfo: # 클래스 이름은 camel case로 작성
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age
    def get_birth_day(self):
        return self.birth_day
    
fa = AgeInfo() # 생성자 함수: 객체(인스턴스) 생성, class의 속성(기능, 특징)을 모두 부여받은 '제품'
fa.age = 39    # fa에 저장된 객체의 변수 age에 39를 저장
print('현재 아빠 나이', fa.get_age(), '살') # get_age를 호출할 때 self에 값 전달하지 않음
fa.up_age()
print('1년 뒤 아빠 나이', fa.get_age(), '살')
print(type(fa)) # 객체의 타입을 물어보면 __main__ 네임스페이스에 생성된 .AgeInfo: AgeInfo 클래스의 객체임을 나타냄

mo = AgeInfo() # mo 객체 생성(AgeInfo 클래스의 속성 부여)
mo.age = 36
print('현재 엄마 나이', mo.get_age(),'살')
mo.up_age()
print('1년 뒤 엄마 나이', mo.get_age(), '살')

sis = AgeInfo()
sis.age = 25
print('현재 누나 나이', sis.get_age(), '살')
sis.up_age()
print('1년 뒤 누나 나이', sis.get_age(), '살')


class NameInfo():
    def get_name(self): # 여기서 파라미터로 입력되는 self는 자기자신을 의미하는게 아니라 호출'한' self 즉 객체가 입력되는 것임
        return self.name # 객체가 클래스의 속성을 부여받고, 그걸 쓰기 위해 호출하는 것
name_info = NameInfo()
name_info.name = '홍태준'
print(name_info.get_name())

fa.name = '홍길동' # fa 객체에 name 속성 부여(클래스엔 딕셔너리와 같이 추가 또는 수정할 수 있는 기능이 있음->키가 없으면 추가, 키가 있으면 수정)
AgeInfo.up_age(fa)
print(AgeInfo.get_age(fa)) # 이 방법도 가능 -> 클래스 내부에 다이렉트 접근 방법

AgeInfo.up_age(sis)
print(AgeInfo.get_age(sis))

fa.birth_day = int(input('생일을 입력하세요: '))
print(fa.get_birth_day())
"""

# 복습 + 클래스 활용:
"""
class four_type_calc:
    def add(self,num1, num2):
        return num1 + num2

    def sub(self,num1, num2):
        return num1 - num2

    def mul(self,num1, num2):
        return num1 * num2

    def div(self,num1, num2):
        return num1 / num2

calc = four_type_calc()
adder = calc.add(5,15)
subtracter = calc.sub(5,15)
multiplier = calc.mul(5,15)
divider = calc.div(5,15)

print(adder, subtracter, multiplier, divider)
"""
"""
class four_type_calc():
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

calc = four_type_calc()
calc.num1, calc.num2 = int(input('숫자를 입력하세요: ')), int(input('숫자를 입력하세요: '))  # 변수를 동적으로 생성함 -> 함수는 동적 생성이 안됨
print(calc.add())
"""

# getter() 함수 -> 클래스의 동작 결과 반환
# setter() 함수 -> 클래스의 데이터 값 생성
"""
class AgeInfo: # 클래스 이름은 camel case로 작성
    def get_age(self): 
        return self.age
    def get_birthday(self):
        return self.birthday
    def set_birth_day(self,birthday):
        self.birthday = birthday
    def set_age(self, age): # 생성자 함수
        self.age = age

taejun = AgeInfo() # 클래스 속성 부여 받아서 태준 객체 생성
taejun.set_age(int(input('나이를 입력하시오: '))) # 태준 객체의 age 값 부여
taejun.set_birth_day(int(input('생일을 입력하시오: ')))
print(taejun.get_age())  # 태준 객체의 age 값 호출
print(taejun.get_birthday())
"""


# 생성자 함수의 이해 및 활용:
"""
class Car:
    def __init__(self, brand, color):  # 스페셜 함수: __~~__: 특정 상황에 맞게 사용 가능 -> 생성자 함수, 인스턴스 변수 초기화
        self.brand = brand
        self.color = color
        print(self.brand, self.color, '생성')

    def get_brand(self):
        return self.brand
    
    def set_brand(self, brand):
        self.brand = brand

car1 = Car('BMW', "Black")
car2 = Car('Benz', "White")
car3 = Car('Porche', 'Yellow')
# print(dir(__builtins__))

print(car2.get_brand())
"""

"""
class Grade:
    def __init__(self,kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.math = mat

    # setter의 추가 선언 -> 추후에 수정을 위한 목적적
    
    def set_kor(self, kor):
        self.kor = kor
    def set_eng(self, eng):
        self.eng = eng
    def set_mat(self, mat):
        self.mat = mat
    
    def get_total(self):
        return self.kor + self.eng + self.math  

    def get_avg(self):
        return self.get_total() / 3  

    def get_grade(self):
        avg = self.get_avg()  
        if avg >= 90:
            return "수"
        elif avg >= 80:
            return "우"
        elif avg >= 70:
            return "미"
        elif avg >= 60:
            return "양"
        else:
            return "가"



def main():
    while True:
        kor = int(input('국어점수를 입력하세요: '))
        eng = int(input('영어점수를 입력하세요: '))
        mat = int(input('수학점수를 입력하세요: '))

        grade = Grade(kor, eng, mat)

        print("총점 : ",grade.get_total())
        print("평균 : ",grade.get_avg())
        print("학점 : ",grade.get_grade())

        continue_yn = input('계속하시겠습니까?: (y/n)')
        if continue_yn == 'n' or continue_yn == "N":
            break
    print('프로그램 종료')

main()
"""

# 계산기 프로그램(추상화):
"""
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 # setter 함수
    
    def adder(self):
        return self.num1 + self.num2
    def substracter(self):
        return self.num1 - self.num2
    def multiplier(self):
        return self.num1 * self.num2
    def divider(self):
        return self.num1 / self.num2 # getter 함수
    
def main():
    num1 = int(input())
    num2 = int(input())

    calculator = Calculator(num1, num2)
    print(calculator.adder())
    print(calculator.substracter())
    print(calculator.multiplier())
    print(calculator.divider())
        
    
main()
"""


# 추가 문제:
# 1. 아래 코드를 참고 하여 금일 배운 AgeInfo 에 대한 메모리 그림을 그려보시오.

"""
class AgeInfo: # 클래스 이름은 camel case
    
    def up_age(self):
        self.age += 1

    def get_age(self):
        return self.age

fa = AgeInfo() # AgeInfo : 클래스명 + ()함수 = AgeInfo() = (객체=인스턴스)생성자함수
fa.age = 39

[Class 영역]
AgeInfo
 ├── up_age()    # 메서드 참조
 └── get_age()   # 메서드 참조

[Heap 영역 (Instance)]
fa
 ├── age: 39    # 인스턴스 변수
 ├── up_age()    # 클래스의 메서드 참조
 └── get_age()   # 클래스의 메서드 참조

[Stack 영역]
fa → 객체 (Heap 영역의 fa를 참조)
"""

# 2. self 란?: 
"""
클래스의 인스턴스(객체)를 참조하는 변수, 클래스 내부에서 매서드 정의 시 첫 번째 매개변수로 반드시 포함되며, 이를 통해 클래스의 속성 및 매서드에 접근 가능
"""
# 3. 클래스와 객체에 대하여 설명하시오.
"""
클래스는 객체를 생성하기 위한 틀(설계도) -> 데이터(속성)와 메서드(동작)을 묶어 하나의 단위로 정의
객체는 클래스를 기반으로 생성된 실제 인스턴스(제품) -> 메모리에 실제로 존재하며 동작할 수 있는 실체(메모리 차지)
"""
# 4. instance 변수에 대하여 설명하시오.
"""
인스턴스 변수는 클래스의 각 객체에 독립적으로 존재하는 변수, 객체를 통해 생성되며 self를 사용해 선언됨
각 객체마다 다른 값을 가질 수 있으며, 클래스의 다른 매서드에서 self를 통해 접근 가능능
"""
# 5. 생성자 함수란?
"""
객체가 생성될 때 자동으로 호출되는 클래스의 매서드 __init__()으로 생성 -> 객체가 생성될 때 초기화 작업 수행하며, 인스턴스 변수를 설정함
"""
# 6. dir() 함수에 대하여 설명하시오.
"""
객체가 가진 속성과 매서드의 목록을 반환
객체가 가진 모든 멤버를 확인할 때 사용용
"""
# 7. 스페셜 메소드란?
"""
특정 상황에서 파이썬이 자동으로 호출하는 메서드로, 함수명 앞 뒤로 언더바 2개로 감싸짐 __함수명__()
객체의 동작을 커스터마이징하거나 오버라이딩(부모클래스(큰 틀, 너무 무거움)에서 자식클래스(작은 틀, 딱 필요한 기능만 골라냄)에 기능 상속)할 때 사용
"""
# 8 __init__ 함수의 용도는?
"""
클래스의 생성자 함수로, 객체가 생성될 때 자동으로 호출됨
주요 용도는 객체 초기화(인스턴스 변수 설정), 객체 생성 시 추가 작업 수행행
"""

# 9. 국영수 를 입력 받아, 평균과 총점 ,성적을 출력 프로그램을 작성하시오 -> 객체지향적으로(클래스 활용하여) 프로그램밍 하시오.
"""
class Score:
    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def total(self):
        return self.kor + self.eng + self.mat
    
    def avg(self):
        return self.total() / 3
    
    def grade_marker(self):
        avg_score = self.avg()
        if avg_score >= 90:
            return('A')
        elif avg_score >= 80:
            return('B')
        elif avg_score >= 70:
            return('C')
        elif avg_score >= 60:
            return('D')
        else:
            return('F')

def main():
    while True:
        kor = int(input('국어점수를 입력하세요: '))
        eng = int(input('영어점수를 입력하세요: '))
        mat = int(input('수학점수를 입력하세요: '))
        score = Score(kor, eng, mat)
        print('점수의 총 합은 :', score.total())
        print('점수의 평균은 :', score.avg())
        print('성적은 :', score.grade_marker())  

        check = input('계속하시겠습니까? (yes/no)')
        if check == "no" or check == "No":
            print('프로그램 종료')
            break

main()
"""

# 10.클래스 정의 -> 비어있는 사람 (Human) 클래스를 "정의" 해보세요:
"""
class Human:
    pass # 현재는 빈 클래스 공간(속성x)이지만 후에 속성과 메서드 추가 가능
"""
# 11. 인스턴스 생성 -> 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
"""
class Human:
    pass
areum = Human() # Human클래스의 인스턴스 생성 및 변수 바인딩
"""
# 12. 클래스 생성자- 1.사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
"""
class Human:
    def __init__(self):
        print('응애응애') # 생성자를 이용해 객체가 생성될 때마다 응애응애 출력력
areum = Human()
"""

#13. 인스턴스 속성에 접근 -> 12.에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다
"""
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('응애응애') # 생성자를 이용해 객체가 생성될 때마다 응애응애 출력력
areum = Human(name = '조아름', age = 25, gender ='여성')

# 인스턴스 속성 출력
print("이름: {}".format(areum.name))
print("나이: {}".format(areum.age))
print("성별: {}".format(areum.gender))

"""
# 14 클래스 메소드 - 1. 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
"""
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('응애응애') # 생성자를 이용해 객체가 생성될 때마다 응애응애 출력

    def who(self):
        print('이름:', self.name)
        print('나이:', self.age)
        print('성별:', self.gender)

areum = Human(name = '조아름', age = 25, gender ='여성')

# 인스턴스 속성 출력
areum.who()
"""

# 15. 생성자 ->Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
"""
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_stock_info(self):
        return ('종목:{},종목코드:{}'.format(self.name, self.code))

samsung = Stock('samsung', '005930')
print(samsung.get_stock_info())
"""

# 16. 메서드객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
"""
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_stock_info(self):
        return ('종목:{},종목코드:{}'.format(self.name, self.code))
    
    def set_name(self,name):
        self.name = name

samsung = Stock('samsung', '005930')
print(samsung.get_stock_info())

# set_name 메서드 호출로 종목명 변경
samsung.set_name('Samsung Electronics')

print(samsung.get_stock_info())
"""

# 17 메서드 -> 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.
"""
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_stock_info(self):
        return ('종목:{},종목코드:{}'.format(self.name, self.code))

samsung = Stock('samsung', '005930')
print(samsung.get_stock_info())
"""

# 16. 메서드객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
"""
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_stock_info(self):
        return ('종목:{},종목코드:{}'.format(self.name, self.code))
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
    def set_name(self,name):
        self.name = name

samsung = Stock('samsung', '005930')
print(samsung.get_stock_info())

# set_name 메서드 호출로 종목명 변경
samsung.set_name('Samsung Electronics')

print(samsung.get_stock_info())
print(samsung.get_name())
print(samsung.get_code())
"""

# 18. 객체 생성 -> 17번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요
# Stock 클래스 정의
class Stock:
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name  # 종목명
        self.code = code  # 종목코드
        self.per = per  # PER
        self.pbr = pbr  # PBR
        self.dividend_yield = dividend_yield  # 배당수익률

# 여러 객체 생성
stocks = [
    Stock(name="삼성전자", code="005930", per=15.79, pbr=1.33, dividend_yield=2.83),
    Stock(name="LG전자", code="066570", per=10.25, pbr=0.85, dividend_yield=1.95),
]

# 데이터를 전치하기 위한 준비
data = {
    stock.name: {
        "종목코드": stock.code,
        "PER": stock.per,
        "PBR": stock.pbr,
        "배당수익률 (%)": stock.dividend_yield,
    }
    for stock in stocks
}

df = pd.DataFrame(data)

# 출력
print(df)

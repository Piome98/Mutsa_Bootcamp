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

class Grade:
    def __init__(self,kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.math = mat


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
    kor = int(input('국어점수를 입력하세요: '))
    eng = int(input('영어점수를 입력하세요: '))
    mat = int(input('수학점수를 입력하세요: '))

    grade = Grade(kor, eng, mat)

    print("총점 : ",grade.get_total())
    print("평균 : ",grade.get_avg())
    print("학점 : ",grade.get_grade())


main()
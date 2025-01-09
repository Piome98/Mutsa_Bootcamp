# 객체 지향 프로그래밍(Object Oriented Programming)
"""
객체를 이용한 프로그램으로 객체는 속성과 기능으로 구성된다
객체: 제풐
속성: 이름, 기능, 색깔, 등
객체 지향의 4대 특징: 추상화(클래스), 캡슐화, 상속성, 다형성
"""
class AgeInfo: # 클래스 이름은 camel case로 작성
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age
    
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
    def get_name(self):
        return self.name
name_info = NameInfo()
name_info.name = '홍태준'
print(name_info.get_name())
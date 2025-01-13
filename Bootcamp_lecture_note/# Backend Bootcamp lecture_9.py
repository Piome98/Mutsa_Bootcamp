"""def main():
    while True:
        try:
            age = int(input('나이를 입력하세요: '))
            print('입력하신 나이는 {}살 입니다'.format(age))
            break
        except ValueError:
            print('입력이 잘 못 되었습니(다')
        finally:
            print('프로그램을 종료합니다')
main()"""

# 스페셜 메서드 예제:
"""class Sentence:
    def __init(self,s):
        self.words = s.split()
    def __len__(self):
        return len(self.words)
    
s = Sentence('sometimes bad things happen to good people')
print(len(s))
"""
"""class Car:
    def __init__(self,id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return self.id
    

c = Car('32러5234')
print(len(c)) # c 인스턴스의 문자 개수를 출력함
print(str(c)) # c 인스턴스의 데이터를 문자열 형식으로 출력함
print(dir(c))"""


# 가위 바위 보 게임:
"""import random

class RspGame:
    def __init__(self):
        self.rsp_list = ['가위', '바위', '보']
        self.dic_rsp_result = {
            '가위':('바위', '승'),
            '바위':('보', '승'),
            '보':('가위', '승')
        }
        self.computer = None # null 초기화
        self.user = None # 입력이 들어오기 전에는 null 로 초기값 지정

    def set_rsp(self):
        while True:
            try:
                self.user = input('가위 바위 보를 입력하세요')

                if self.user in self.dic_rsp_result.keys(): #self.rsp_list
                    break
                print('잘못된 입력입니다. 다시 입력하세요')
            except:
                print('잘못된 입력입니다 가위바위보 중 하나를 입력하세요')
                continue

        self.computer = random.choice(list(self.dic_rsp_result.keys()))

    
    def rsp_result(self):
        if self.computer == self.user:
            return '비겼습니다'
        elif self.dic_rsp_result[self.computer][0] == self.user:
            return '유저 당신이 이겼습니다'
        else:
            return '유저 당신이 졌습니다'
        
    def run(self):
        self.set_rsp() # self 에 함수 호출 가능
        print('유저: ', self.user)
        print('컴퓨터: ', self.computer)
        print(self.rsp_result())



rsp = RspGame()
rsp.run()"""


# set 자료형:
"""
집합(set)은 원소의 중복은 허용하지 않으며 순서가 없는 자료형형
{} 딕셔너리와 같이 중괄호를 쓰지만 키값이 없으면 set으로 인식
"""
"""s1 = {1,2,3,4,5,6}
print(s1)
print(type(s1))

s2 = set([1,2,3,4,5])
print(s2)"""

"""# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s3 = s1 & s2 # 교집합, and 연산자는 사용 불가
print(s3)

s3 = s1 | s2
print(s3) # 합집합

s3 = s1 - s2
print(s3) # 차집합

s1 = set([1,2,3])
s1.add(4) # component 추가
print(s1)
s1.update([4,5,6])  # 복수 component 추가
print(s1)

s1.remove(6) # component 제거
print(s1)"""

# set 응용 로또 추첨 프로그램:
"""import random

lotto = set()

while len(lotto) < 6:
    num = random.randint(1,45)
    if num not in lotto:
        lotto.add(num)

print(len(lotto))
print(sorted(lotto)) # sorted()로 숫자 정렬 가능"""


# 다양한 언어에서의 None
"""my_value = 1
print(my_value)
print(type(my_value))

my_value = None
print(my_value)
print(type(my_value))

def my_func():
    pass

print(my_func())"""

# 사전에서 특정 키가 정의 되지 않을때
"""my_dic ={"name":"john"}

if "age" not in my_dic :
    print("None 입니다.")
else:
    print("None이 아닙니다.")

if my_dic.get("age") is None:
    print("None 입니다.")
else:
    print("None이 아닙니다")
    """

# 깊은 복사(deep copy) 와 얕은 복사(shallow copy):
"""a = 100
b = 100

print(a==b)
print(a is b) # 주소가 같은가 확인 -> 주소값 같으면 True, 다르면 False 출력
print(id(a), id(b)) 

r1 = [1,2,3]
r2 = [1,2,3]  # 리스트는 선언 단계부터 주소값이 다르게 지정됨

print(r1==r2)
print(id(r1), id(r2)) 
r2 = r1       # 주소값을 동일하게 만들어줌
print(r1 is r2)

r1.append(1)  # 주소값의 변경 없이 데이터만 추가됨
print(r1)     # 따라서 r1과 r2는 동일한 객체임
print(r2)
print(r1 is r2) # 동일한 객체임을 주소값으로 확인하므로 True 결과값 반환

r1 = ['John',('man','USA'),[175,23]] #John은 미국남자로 175cm 23세
r2 = list(r1) # r1의 내용으로 새로운 리스트를 만듦
print(r1 is r2) # 마찬가지로 r1의 데이터 값을 가진 새로운 r2 리스트를 만듦 -> 리스트는 선언 단계에서 새로운 주소값 부여

s1 = [1,2]
s2 = tuple(s1)
s2 = list(s1) #[1,2] -> 카피 -> 주소는 새롭게 생성하되 데이터 값만 복사(데이터 연동 방지)
"""
import copy
"""r1 = ['John',('man','USA'),[175,23]] #John은 미국남자로 175cm 23세
r2 = list(r1) # r1의 내용으로 새로운 리스트를 만듦 -> 얕은 복사이므로 최상위 수준의 요소만 복사하고, 리스트 안의 가변객체는 동일한 객체를 참조함(주소값 동일)
              # 따라서 두 리스트를 완전히 독립한 객체로 만들기 위해선 deep copy 기능을 써야 함

print(r1 is r2)
r1[2][0] = 180
print(r1)
print(r2)

r3 = copy.deepcopy(r1)
r3[2][0] = 201
print(r1)
print(r2)
print(r3)
print(r1 is r3)
print(id(r1[2][0]))
print(id(r2[2][0]))
print(id(r3[2][0]))"""

"""john = ['John',('man','USA'),[175,23]]
tom = list(john)
sean = copy.copy(john)
jack = copy.deepcopy(john)
john[2][1] += 1

print(john)
print(tom)
print(sean)
print(jack) # 얘만 리스트 안의 컴포넌트가 다른 주소값을 가짐
"""

# 리스트 컴프리핸션(list comprehension)
"""r1 = [1,2,3,4]
r2 = []

for i in r1:
    r2.append(i*2)
print(r2)

#리스트의 생성과 그 리스트의 채울 데이터를 가공 추출하는 일련의 과정들을 하나로 묶는 것이 리스트 컴프리헨션이다.
r2 = [x*2 for x in r1] # 리스트 컴프리헨션 
print(r2)

for i in r1:
    if i % 2 == 0:
        r2.append(i*2)
print(r2)

r2 = [x*2 for x in r1 if x % 2 ==0 ]
print(r2)"""

"""r1 = ['Black', 'White']
r2 = ['Red', 'Blue', 'Green']
r3 = [x+y for x in r1 for y in r2 ] # 리스트 컴프리헨션을 쓰기 위해 최외곽을 리스트형으로 묶음음
print(r3)

r3=[]
for i in r1:
    for j in r2:
        r3.append(i+j)
print(r3)"""

[print(f'{i} * {j} = {i*j}') for i in range(1, 10) for j in range(1, 10)] # 리스트 컴프리핸션으로 구구단 출력력
[print(i,'*', j, '=', i*j)for i in range(1,10) for j in range(1,10)]

result = [x*y for x in range(1,10) for y in range(1,10)]
print(result)
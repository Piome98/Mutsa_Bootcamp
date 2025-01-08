# 딕셔너리의 이해:
"""
튜플, 리스트, 딕셔너리
딕셔너리 -> {키:값}
키의 이름을 호출하면 해당 키와 매칭되는 값이 출력됨
"""

# Read(참조) -> 키에 대한 index로 value값을 가져옴
# 키에 대한 index로 value값을 가져옴 -> 주의할 점: 숫자 인덱스로는 접근 불가능(딕셔너리의 인덱스는 순서가 부여되지 않음)
# 리스트와 튜플은 인덱스 순서 유지(o), 딕셔너리는(x)
"""
value1, value2, value3 = input('값을 입력하세요'),input('값을 입력하세요'),input('값을 입력하세요')
test = {'key1':value1, 'key2': value2, 'key3': value3}
print(test)
print(test['key1'])
val = test['key3']
"""
# 값은 중복돼도 되지만, 키값은 중복되면 안됨 -> 키값이 중복되면 맨 마지막에 입력된 데이터만 출력됨
"""
print(val)
"""

"""
# 딕셔너리 CRUD
dc ={
    '코카콜라': 900,
    '바나나맛우유':750,
    '비타500':600,
    '삼다수':450,
}

print(type(dc))
print(dc)

# 딕셔너리 value값 수정
dc['코카콜라'] = 800
print(dc)

# 딕셔너리 component 추가
dc['카페라떼'] = 1000
print(dc)
dc['사이다'] = 1200
print(dc)

# 딕셔너리 component 삭제
del dc['카페라떼']
print(dc)
"""

# 딕셔너리 조건문:
"""
if '코카콜라' in dc:
    print('코카콜라의 가격은:', dc['코카콜라'], '원 입니다')
    dc['코카콜라'] = 1800
    print('코카콜라의 가격은', dc['코카콜라'], '원으로 인상됐습니다')
"""


# 딕셔너리 for loop -> 키값의 인덱스로 루프 범위 지정되고, 키값 인덱스에 해당하는 value값으로 반복문 수행
"""
for i in dc:
    print(i) # 키값이 리턴됨

for i in dc:
    print(i, dc[i]) # 키값과 value값이 모두 리턴됨
"""

# 딕셔너리 값 for문을 이용해서 일괄 변동
"""
for i in dc:
    dc[i] += 100
    print(i,dc[i])
"""

# 유용한 딕셔너리 함수들들
"""
for key, value in dc.items():
    print(key, value) # items()함수를 이용해 key값과 value값 각각 출력 가능

for key in dc.keys():
    print(key)        # keys()함수를 이용해 key값만 출력 가능

for value in dc.values():
    print(value)      # value()함수를 이용해 value값만 출력 가능능
"""
"""
sum = 0
for value in dc.values():
    sum += value
print(sum)

sum = 0
for i in range(1, 10, 2):
    sum += i
    print(sum)

mul = 1 
for i in range(1,11):
    mul *= i
    print(mul) 

my_list = ['가', '나', '다', '라']
for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])

for i in range(1, len(my_list)):
    print(my_list[i-1], my_list[i])

stock_list = {'시가':[100,200,300], '종가':[80,210,330]}
dic_stock = {
    '시가':[100,200,300],
    '종가':[80,210,330]
}
"""

dic_inventory = {
    '메로나':[300,20],
    '비비빅':[400,3],
    '죠스바':[250,100]}


print(dic_inventory['메로나'][0], '원')
print(dic_inventory['메로나'][1], '개')

def get_sum_and_prices():
    sum = 0
    total =0

    for value in dic_inventory.values(): # 딕셔너리의 인덱스만 가져옴
        sum += value[0]                  # 딕셔너리 value 값의 0번째 자리에 해당하는 데이터만 가져와서 다 더함 
        total = total + (value[0] * value[1]) # 전체 가격 * 개수의 값을 얻기 위해 딕셔너리 value값 부분의 0번째와 1번째 자리의 값을 곱해서 돌려보냄(total에 저장장)

    #for price, count in dic_inventory.values(): # 복수 할당, 구조 분해의 방법법
    #    sum += price
    #    total = total + (price * count)  

    return sum, total

sum, total = get_sum_and_prices()
print(sum, total)


# 클래스와 객체의 이해:
"""
전역 변수 -> global variable -> 로컬변수로 선언했어도 전역취급됨
매개 변수 -> def func(n), n이 인자(매개변수)
로컬 변수 -> 함수 및 반복문 등 특정 범위 내에서만 사용할 수 있는 변수(메모리 절약)
"""
# 객체지향프로그래밍(OOP):
"""
추상화, 캡슐화, 상속성, 다형성
"""

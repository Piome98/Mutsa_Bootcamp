# 지난시간 학습 리뷰:
# 별 찍기:
"""
num = int(input('숫자를 입력하세요: '))

def star_pointer(num):
    for i in range(num):
        for j in range(i + 1):
            print('*', end = "")
        print()

star_pointer(num)

def star_pointer_reduce(num):
    for i in range(num):
        for j in range(num-i):
            print('*', end = "")
        print()

star_pointer_reduce(num)

def right_star_pointer_increase(num):
    for i in range(num+1):
        for j in range(num - i):
            print('*', end ="")
        for j in range(i):
            print(" ", end="")
        print()

right_star_pointer_increase(num)
"""


# 리스트와 문자열
"""
1. 문자열은 리스트와 달리 업데이트가 안됨
2. 리스트와 문자열엔 덧셈과 곱셈 연산자가 지원됨
"""

# 리스트 함수(메서드):
"""
list.append()              
list.insert()
list.remove()
list.pop()
list.extend()
list.clear()
list.index()
list.count()
list.sort()
list.reverse()
list.copy()

"""

st = [1, 3, 5, 7, 9]
num = len(st)       # numbers of index in list
print(num)
print(min(st))      # minimum value of component in the list
print(max(st))      # maximum value of component in the list

st.remove(1)        # remove the component() from the list
print(st)       
st.append(11)       # append the component() at the end of the list
print(st)
st.insert(5,13)     # insert the component(index, inserted_component) in the list
print(st)
st.clear()          # delete every component in the list -> st[:] = []
print(st)

st = [1,3,5,7,9]
st.pop(0)           # delete the componet at the index()
print(st)
print(st.index(3))  # return the first index where the component is firstly come out

string = 'YoonSungWoo'
print(string.count('o'))
print(string.count('oo'))

org = 'Kim'
lcp = org.lower()   # 문자열을 소문자로 출력
ucp = org.upper()   # 문자열을 대문자로 출력
print(lcp)
print(ucp)
# strip() -> 타 언어에선 trim()
cp1 = org.strip()   # 문자열 앞 뒤 공백 제거
cp2 = org.lstrip()  # 문자열 왼쪽 공백 제거
cp3 = org.rstrip()  # 문자열 오른쪽 공백 제거

rps = org.replace('Ki', 'Li')
print(rps)

ret = org.split('i')
print(ret)

tel = '010-1234-5678'
print(tel.split('-'))
tel = tel.split('-') # dash 기준으로 component를 나누고 리스트로 반환
for dash in tel:     # dash 기준으로 나뉜 리스트의 인덱스 순서로 component 반환
    print(dash)

string = "What is important is that you should choose what is best for you"
string.find('is')    # index 값이 리턴됨
string.rfind('is')   # 마지막 is 가 있는 index값이 리턴됨
string.count('is')       # is의 개수 출력

# 이스케이프(탈출문자)
# / 붙이고 문자 한개를 주게 되면 두개가 합쳐져서 하나의 문자를 형성(기능)

print('abcd', end='\n') # 한 줄 띄기
print('abcd', end='\t') # tab키 한 칸 띄기
print('abcd')

# del 명령
string = [1,2,3,4,5]
del string[2:]
print(string)

# 조건문
"""
불린 생략: 조건에 따라 참이면 True, False 반환

num = int(input('숫자를 입력하세요:'))
if num > 0:
    print('양수')
elif num < 0:
    print('음수')
else:
    print('0')
"""
"""
if True and False:
    print()
else:
    print()
num = int(input('숫자를 입력하세요: '))
def minimum_multiplier(num):
    if num % 2 == 0 and num % 3 == 0:
        print(num)
    else:
        print('6의 최소공약수가 아님')

minimum_multiplier(num)

def double_options(num):
    if num % 2 ==0:
        if num % 3 ==0:
            print('2의 배수이자 3의 배수임')
        else:
            print('2의 배수지만 3의 배수는 아님')

double_options(num)
"""
"""
num_kor, num_eng, num_mat = int(input('국어 점수를 입력하세요: ')), int(input('영어 점수를 입력하세요: ')) ,int(input('수학 점수를 입력하세요: '))

def score_avg(num_kor, num_eng, num_mat):
    if (num_kor + num_eng + num_mat) / 3  >= 90:
        print( '총점: ', num_eng + num_kor + num_mat,'평균: ',(num_kor + num_eng + num_mat) / 3, '수')
    elif (num_kor + num_eng + num_mat) / 3 >= 80:
        print('총점: ', num_eng + num_kor + num_mat, '평균: ',(num_kor + num_eng + num_mat) / 3, '우')
    elif (num_kor + num_eng + num_mat) / 3 >= 70:
        print('총점: ', num_eng + num_kor + num_mat, '평균: ',(num_kor + num_eng + num_mat) / 3, '미')
    elif (num_kor + num_eng + num_mat) / 3 >= 60:
        print('총점: ', num_eng + num_kor + num_mat, '평균: ',(num_kor + num_eng + num_mat) / 3, '우')
    else:
        print('총점: ', num_eng + num_kor + num_mat, '평균: ',(num_kor + num_eng + num_mat) / 3, '가')

score_avg(num_kor, num_eng, num_mat)
"""

"""
등호/부등호 연산자, not, or, and 등 연산자는 숫자형 뿐만 아니라 문자열, List 형식에도 쓸 수 있음

isdigit()과 같이 is 로 시작하는 함수는 불린 타입의 결과값을 반환 -> isdigit() 숫자형이냐? True / False

startwith(), endwith()와 같이 입력 인자가 괄호 안의 값으로 시작하는지, 끝나는지 같이 알아볼 수 있도록 함수 이름을 직관적으로 작성하는 것이 좋음

"""
"""
phone_number = input('전화번호를 입력하세요: ')

def phone_number_definer(phone_number):
    if phone_number.isdigit() and phone_number.startswith('010'):
        print('전화번호가 유효합니다')
    else:
        print('전화번호가 유효하지 않습니다')
    
phone_number_definer(phone_number)
"""
"""
s = 'tomato spaghetti'
if 'ghe' in s :
    print('있음')
else:
    print('없음')
"""
"""
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(6):
    for j in range(6-i):
        print('*', end='')
    for j in range(i):
        print(' ', end="")
    print()

for i in range(6):
    for j in range(6-i):
        print(' ', end="")
    for j in range(i):
        print('*', end='')
    print()

for i in range(6):
    for j in range(i):
        print(' ', end="")
    for j in range(6-i):
        print('*', end='')
    print()


for i in range(10):
    print('*' * i)
"""
"""
num = int(input('숫자를 입력하세요:'))

def even_odd_definer(num):
    if num % 2 == 0:
        print('짝수입니다')
    else:
        print('홀수입니다')

even_odd_definer(num)
"""

"""
num = int(input('숫자를 입력하세요: '))

def number_adder(num):
    adder = num + 20
    if adder > 255:
        print('255')
    else:
        print(adder)

number_adder(num)
"""
"""
time = input("시간을 입력하세요: ")

def oclock_definer(time):
    if time.endswith('00'):
        print('정각입니다')
    else:
        print('정각이 아닙니다')

oclock_definer(time)
"""

"""
fruit = ['사과', '홍시', '배', '포도']

fav_fruit = str(input('좋아하는 과일은? : '))
if fav_fruit in fruit:
    print('정답입니다')
else:
    print('오답입니다')
"""

num1, num2, num3 = int(input('숫자를 입력하세요:')), int(input('숫자를 입력하세요:')), int(input('숫자를 입력하세요:'))
list_numbers = [num1, num2, num3]

list_numbers.sort()
print(list_numbers[-1])


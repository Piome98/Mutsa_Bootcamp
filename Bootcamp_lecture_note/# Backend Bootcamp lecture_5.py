import pandas as pd
# while문의 사용:
"""
cnt = 0
sum = 0
while cnt < 11:
    sum += cnt
    cnt += 1
    print(sum)


def option_loop():
    cnt = 0
    while cnt < 100:
        print(cnt)
        cnt += 1
        if cnt == 99:
            print('2%가 부족해!')  # 특정 조건이 성립되면 루프를 중지하고 탈출출
            break

option_loop()

i = 0
sum = 0

while True:
    sum = sum + i

    if sum > 100:
        print(i, "더했을때의 합",sum) #1부터 몇까지 더해야 합이 100을 넘는가?
        break

    i = i + 1
"""

# continue 예제:
"""
for i in range(1,10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1,11):
    if i % 2 != 0 or i == 0 :
        continue                # pass와 같은 개념, return 값을 반환하지 않고 루프 수행
    print(i)
"""

"""
dan = int(input('숫자를 입력하세요: '))
def gugudan(dan):
    for i in range(1,dan+1):
        if i % 3 != 0:
            continue
        for j in range(1,dan+1):
            if i % 3 == 0:
                print(i, '*', j,'=', i * j)

gugudan(dan)

"""
"""
num = int(input('숫자를 입력하세요:'))
def multiplier_definer(num):
    while True:
        if num % 7 ==0 and num % 11 == 0:
            print(num)
            break
        num += 1
multiplier_definer(num)
"""

# 튜플의 이해
"""
벤다이어그램처럼 리스트 안에 튜플() 생성 가능, 튜플은 파라미터의 묶음의 개념이며 튜플을 입력하면 해당 묶음의 매개변수가 전부 입력됨





list_tuple = [
    ('tuple1_component1', 'tuple1_component2', 'tuple1_component3'),
    ('tuple2_component1', 'tuple2_component2', 'tuple2_component3'),
    ('tuple3_component1', 'tuple3_component2', 'tuple3_component3')
]

for i in range(len(list_tuple)):  # 외부 루프: 튜플 인덱스
    t = list_tuple[i]  # 현재 튜플 가져오기
    print(f"ID of tuple {i}: {id(t)}")  # 각 튜플의 ID 출력
    for j in range(len(t)):  # 내부 루프: 튜플 안 요소의 인덱스
        component = t[j]  # 현재 요소 가져오기
        print(f"  ID of component {j} in tuple {i}: {id(component)}")


"""




# 튜플은 mutable이기 때문에 튜플 내부 파라미터의 값을 바꿀 수는 없음:
# 값을 바꾸기 위해 아래와 같이 파라미터 변경:
"""
frns_list = [ ['동수',1],['진우',2],['선영',3]]
frns_tuple = [ ('동수',1),('진우',2),('선영',3)]

frns_tuple[0] = ('철수',1)
print(frns_tuple)

frns_tuple = [ ('동수',1),('진우',2),('선영',3)]
frns_tpl = (['동수',1],['진우',2],['선영',3])
print(frns_tuple.index(('진우',2)))
print(frns_tpl.index(['진우', 2]))
"""

# 지난시간 학습 복습습
"""
score_kor, score_eng, score_mat = int(input('국어점수를 입력하세요: ')), int(input('영어점수를 입력하세요: ')), int(input('수학점수를 입력하세요: '))
def total_avg_score(score_kor,score_eng,score_mat):
    total_score = score_kor + score_eng + score_mat
    avg_score = total_score/3
    if avg_score >= 90:
        print('수')
    elif avg_score >= 80:
        print('우')
    elif avg_score >= 70:
        print('미')
    elif avg_score >= 60:
        print('양')
    else:
        print('가')
    print('total score is: ',total_score)
    print('average score is: ',avg_score)
total_avg_score(score_kor, score_eng, score_mat)
"""

# 3개의 수에 대한 최댓값:
"""
a, b, c = int(input("숫자를 입력하세요: ")), int(input("숫자를 입력하세요: ")), int(input("숫자를 입력하세요: "))

def number_comparer(a,b,c):
    if a > b and b > c:
        print('a is the biggest')
    elif b > a and a > c:
        print('b is biggest')
    else:
        print('c is the biggest')

number_comparer(a,b,c)

number_list = [a,b,c]
max(number_list)
print(max(number_list))
"""

# 리스트 슬라이싱(뒤에서부터 앞으로)
"""
list_kor = ['가', '나', '다', '라']

for string in list_kor[::-1]:
    print(string)
"""

# list() 함수로 range(), 문자열 등을 리스트 파라미터로 변환할 수 있음
# 튜플 리스트 형변환:
    # 튜플 형변환 tuple()
    # 리스트 형변환 list()

# 튜플의 사용법법
"""
print(list('hello'))
print(tuple('hello'))

list_range = list(range(10))
print(list_range)

for i in range(len(list_range)):
    print(i)

print(list(range(10,2,1))) # 범위 벗어나면 빈 리스트 출력
print(list(range(10,0,-1)))# 역순으로 출력
print(list(range(10,3,-2)))# 10부터 3까지 2씩 감소(스탭: -2)
print(list(range(10,3,-3)))

my_tuple = ()
my_tuple = (1)
my_tuple = (1) * 3
print(type(my_tuple))
print(my_tuple)
my_tuple = (1, )
print(my_tuple)
print(type(my_tuple))


"""
"""
t = ('a', 'b', 'c')
T = ('A',)
my_tuple = T + t[1:]
print(my_tuple)

t[0] = 'a' # immutable이라 변경 불가
"""

# 함수의 사용법(파라미터 지정), 디폴트값 부여:
# 파라미터를 지정해서 전달하게 되면 파라미터의 입력 순서와 관계없이 사용 가능
"""
def your_inf(name, age=0):
    print('name: ', name)
    print('age: ', age)

your_inf('Oscar',27)

def func(s):
    s[0] = 0
    s[-1] = 0

st = [1,2,3]
func(st)

"""
# 파라미터 이름 지정해서 값 전달:
"""
print(1,2,3) 
print(1,2,3, sep =',')
print(1,2,3,sep = '_')
"""
# 오늘의 문제:
# 1. 튜플과 리스트의 차이에 대해 설명하시오: 튜플은 immutable, 리스트는 mutable type, 따라서 튜플은 파라미터의 데이터를 바꿀 수 없지만 리스트는 가능
# 2. 아래의 에러가 나는 이유:
"""
t = (1,2,3)
t[0] = 'a'
# 튜플의 첫번째 파라미터 1을 단순 인덱스 슬라이싱 하려고 해서 에러가 발생한 것, 위에 언급한 바와 같이 튜플은 immutable 이라 데이터를 바꿀 수 없음
T = ('a',)
t = T + t[1:]
# 이렇게 바꿔줘야 사용 가능능
"""
# 3. t =1,2,3,4 t의 데이터 타입은
"""
t =1,2,3,4
print(type(t)) # 튜플임
"""

# 4. 리스트 = [3,-20,-3, 44] for문을 이용해서 리스트의 음수 출력:
"""
list_test = [3,-20,-3,44]
for i in list_test:
    if i < 0:
        print(i)
    else:
        continue
"""

# 5. for문을 이용해 3의 배수만 출력해라
"""
list_test = [3,100,23,44]
for i in list_test:
    if i % 3 == 0:
        print(i)
"""

# 6. 리스트에서 20보다 작은 3의 배수를 출력하라
"""
list_test = [13,21,12,14,30,18]
for i in list_test:
    if i % 3 == 0 and i < 20:
        print(i)
"""

# 7.월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라
"""
for years in range(2002,2051,4):
    print(years)
"""

# 8. 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
"""
for num in range(99,-1,-1):
    print(num)
"""
# 9.for문을 사용해서 아래와 같이 출력하라.
"""
for i in range(0,10,1):
    print(i/10)
"""

# 10. 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
"""
sum = 0
for i in range(1,11,2):
    sum += i

print(sum)

sum = 0
for i in range(1,11):
    if i % 2 != 0:
        sum += i
print(sum)
"""

# 11.1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
"""
multiplier = 1
for i in range(1,11):
    multiplier = multiplier * i
    print(multiplier)
"""

# 12. 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])
"""

# 13.리스트를 아래와 같이 출력하라.
"""
my_list = ["가", "나", "다", "라", "마"]
print(my_list[:3])
print(my_list[1:4])
print(my_list[2:])
"""
# 14.리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
# 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 같은 방식으로 나머지 데이터의 평균을 출력한다.
"""
my_list = [100, 200, 400, 800, 1000, 1300]
fisrt_row = my_list[1:4]
second_row = my_list[3:]

for i in my_list:
    avg_first_row = 0
    avg_second_row = 0
    for j in fisrt_row:
        avg_first_row = (avg_first_row + j) / 3
    for j in second_row:
        avg_second_row = (avg_second_row +j) /3

print(avg_first_row)
print(avg_second_row)
"""

# 15. 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
"""
apart = [ ["101호", "102호"], ["201호", "202호"], ["301호", "302호"] ] 
for row in apart:
    print(", ".join(row))  
"""

# 16.아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
"""
price_tag = [[100,200,300], [80,210,330]]
df = pd.DataFrame({'시가': price_tag[0], '종가': price_tag[1]})
print(df) 
"""

# 17. 모듈에 대하여 설명하시오: 
# 위 문제에서 쓴게 모듈이다, 비슷한 동작을 수행하는 기능으로 메서드 및 변수를 선언해 서로 다른 파일에 저장해두고, 이를 불러와 사용하는 방법을 모듈화라 한다
# 위 문제에선 보다 간단히 시가 종가를 나타내기 위해 pandas 라이브러리를 호출해 사용했다.

# 18. 아래의 에러가 발생하는 이유에 대해 설명하라.
"""
hello()
def hello():
    print("Hi")     #함수가 선언 되기 전에 함수를 호출했으므로 순서를 바꿔주면 잘 작동한다

def hello():
    print("Hi")

hello()
"""

# 19.아래 코드의 실행 결과를 예측하라.
"""
def message() :
    print("A")
    print("B")

message()
print("C")
message()

# message()함수는 A 와 B를 순차적으로 출력한다. 그 중간에 C가 한번 print()문으로 강제 출력 됐으므로 ABCAB가 출력 된다(개행 있음)
"""

# 20. 아래가 에러가 나는 이유와 수정을 하시오.
"""
print(sep = ' _ ', 1, 2, 3, , end = ' m^^m ')
print()함수의 파라미터 입력 순서가 틀렸다, 아래와 같이 고쳐주면 정상 작동한다
print( 1, 2, 3, sep = ' _ ', end = ' m^^m ')
"""


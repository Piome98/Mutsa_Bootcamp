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

list_animal = ['dog', 'cat', 'parrot']
for string in list_animal:
    list_animal = list_animal.upper()
    print(list_animal)
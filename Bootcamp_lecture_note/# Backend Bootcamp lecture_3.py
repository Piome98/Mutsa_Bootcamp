# table of content
"""
1. 기본적인 산술 연산자


"""


# 기본적인 산술 연산자:
"""
**     -> 제곱 연산자
/      -> 실수형 나누기 연산자(몫과 나머지 모두 출력)
//     -> 정수형 나누기 연산자(몫을 출력)
%      -> 나머지 연산자(일반적으로 홀/짝 카운트 할 때 많이 사용)
"""

# 형변환 함수:
"""
int(), float(), str(), double()...etc

숫자형을 문자열로, 문자열을 숫자형으로 변환 가능
"""

# 복합 대입 연산자:
"""
num += 1 -> num = num + 1
마찬가지로 뺄셈, 곱셈, 나눗셈에도 적용 가능
-=
#=
/=
결과값은 실수형으로 출력됨됨
"""

# 리스트의 이해(리스트, 튜플, 딕셔너리):
"""
다른 언어의 Array와는 다른 특징이 있음, 파이썬의 리스트는 다른 언어의 배열과는 다르다고 봐야됨
resource = []
def list_usage(resource):
    for i in range(1,11):
        resource.append(i)
    print(resource)

list_usage(resource)

simple_list = [1,2,3]
print(type(simple_list))

different_list_array = [1, 'hello', 3.3]
print(different_list_array) # 리스트 안에는 데이터 타입이 달라도 들어갈 수 있음, 배열은 동일한 자료형으로 component를 구성해야됨

list_in_list = [1,3,[3,4],["AAA", "ZZZ"]]
print(list_in_list)         # 리스트 안에 리스트 생성 가능

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
added_list = list_1 + list_2
multiplied_list = list_1 * 2

print(added_list)
print(multiplied_list)      # 리스트를 이용해 덧셈 곱셈 연산 가능, 이를 이용해 행렬 내적 등 계산 가능
                            # 매트랩을 이용하면 리스트 component의 사칙연산 모두 가능능
"""

# 리스트에서 값 가져오기(인덱싱):
"""
st = [1,2,3,4]
n1 = st[0]
n2 = st[1]
n3 = st[2]
n4 = st[3]

print(n1,n2,n3,n4)  #CRUD(create, read, update, delete) + 함수로 인덱싱 가능


st = [1,2,3,4,5]
print(st[-1], st[-2], st[-3]) # 음수 인덱싱을 이용해 리스트의 맨 뒤부터 인덱싱


st1 = [1,2,3,4,5]
st2 = st1[2:5]
print(st2)                    # 인덱스 슬라이싱, 인덱스(2) 이상, 인덱스(5) 미만의 인덱스에 위치한 데이터를 호출


st1 = [1,2,3,4,5,6,7,8,9]
st2 = st1[2:5]
st1[2:5] = [0,0,0,0,0]
print(st1,st2)

st1 = [1,2,3,4,5,6,7,8,9]
st2 = st1[2:5]
st1[2:5] = [0,0,0,0,0]
print(st1[0:4],st2[0:2])    # 출력할 때도 당연히 인덱스 슬라이싱 가능

st1 = [1,2,3,4,5,6,7,8,9]
st2 = st1[2:5]
st1[2:5] = [0,0,0,0,0]
print(st1[0:4:2],st2[0:2])  # 인덱스 슬라이싱 할 때 스탭(간격) 주고 슬라이싱 가능
                            # 로그 스케일 스탭핑 하려면 반복문 사용해야 되나?(numpy 사용해야됨)


name = '홍태준'
name[2] = '훈'
print(name)                 # 문자형 리스트는 한번 선언 되면(초기화 되면) 수정 불가
                            # 데이터 타입 = 데이터가 수정 가능한 데이터와 수정 불가능한 데이터가 있음
                            # 수정 불가능한 데이터 -> 문자형 데이터/튜플
                            # 안에 있는 데이터 수정 가능   -> mutable   -> list
                            # 안에 있는 데이터 수정 불가능 -> immutable -> str, int, float

"""

#String 형 for문:
"""
for i in "Happy":
    print(i, end = "")
"""

# 문자열의 인덱스를 호출하는 함수 len()
"""
name = '홍태준'
for i in range(len(name)):
    print(i)
"""

# 리스트와 문자열을 인자로 전달하고 반환하기:
"""
def list_string_as_parameter(parameter):
    print(parameter)
    return 'what you want'

test_variable = list_string_as_parameter('this is pretty useful')    # this is pretty useful 출력(함수 파라미터만 출력)
print(test_variable)                                                 # what you want 출력(전달받은 파라미터가 없으므로 return 값 출력력)
"""
"""
for i in range(1,10):
    for j in range(1,10):
        answer = i * j
        print(i, '*', j, '=', answer)
"""
"""
def gugudan(dan):
    for i in range(1,10):
        print(i * dan)

gugudan(5)
"""
# for 문을 이용해 별 찍기
"""
# 왼쪽 정렬 증가
n =5
for i in range(n):
    for j in range(i+1):
        print('*', end="")
    print()

# 왼쪽 정렬 감소
for i in range(n):
    for j in range(n-i):
        print('*', end="")
    print()

# 오른쪽 정렬 증가
for i in range(n+1): #1,2,3,4,5
    for j in range(n-i): #2,3,4,5,6
        print(' ', end="")
    for j in range(i):
        print('*', end="")
    print()

# 오른쪽 정렬 감소
for i in range(n+1):
    for j in range(i):
        print(' ', end='')
    for j in range(n-i):
        print('*',end='')
    print()

# 마름모 꼴
for i in range(n):
    for j in range(n-i): #줄 번호에 따라 공백 개수를 줄이는 공식
        print(' ', end="")
    for j in range(2 * i -1): # 현재 줄의 별 개수를 홀수로 증가시키는 공식
        print('*', end='')
    print()
for i in range(n-1, 0, -1): #범위를 윗 삼각형과 아랫 삼각형이 다르게 주는 이유는 윗 삼각형의 맨 마지막 행이 아랫 삼각형의 첫번째 행과 중복되기 때문
    for j in range(n-i): 
        print(' ', end='')
    for j in range(2 * i -1):
        print('*', end="")
    print()

num = input('석탑의 높이를 입력하시오:')
for i in range(int(num)):
    for j in range(int(num)-i): #줄 번호에 따라 공백 개수를 줄이는 공식
        print(' ', end="")
    for j in range(2 * i -1): # 현재 줄의 별 개수를 홀수로 증가시키는 공식
        print('*', end='')
    print()

"""

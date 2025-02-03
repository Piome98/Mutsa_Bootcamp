# 빅데이터의 이해
# 데이터 분석의 기초 개념
# 넘파이(numpy)의 이해

import numpy as np

arr = np.array([1,2,3])
print(type(arr)) # type -> ndarray 
type(arr)
print(arr)

# numpy를 이용한 2차원 행렬 배열 -> 2중 리스트로 감싸야됨됨
arr = np.array([[1,2,3], [4,5,6]])
print(arr)
type(arr)

# 기본값이 있는 배열 만들기:
arr = np.zeros(10, dtype=np.int32) # 최소값 -21억 ~ 최대값 +21억
arr = np.zeros((2,5)) # 기본형을 실 수로 해서 행과 열의 크기를 정함 -> 첫번쨰 파람은 행, 두번째 파람은 열
print(arr)

arr = np.ones(10, dtype=np.int32) 
print(arr)

# 연속된 값이 있는 행렬 생성
arr = np.arange(1,10,2) # 1부터 10-1까지 2 간격으로 생성
print(arr)

# linspace의 사용
arr = np.linspace(1,101,3, dtype=np.int32) # 1~ 101-1 을 3등분
print(arr)

# 배열의 차원과 크기 알아내기
arr = np.linspace(1,101,3, dtype=np.int32)
print(arr.ndim)
print(arr.shape) 


a1 = np.array( [ 1, 2, 3, 4, 5 ])
a2 = np.array( [ [ 1, 2, 3, 4 ] , [ 1, 2, 3, 4 ] ] ) #1 * 2 matrix
a3 = np.array( [ [ [ 1, 2, 3 ] , [ 1, 2, 3 ] ] ,
                     [ [ 1, 2, 3 ] , [ 1, 2, 3 ] ] ,
                     [ [ 1, 2, 3 ] , [ 1, 2, 3 ] ] ] ) #2 * 3 matrix

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)


print(a1.shape) #(5,) -> 1행 5열
print(a2.shape) #(2, 4) -> 2행 4열
print(a3.shape) #(3, 2, 3) -> 3행 2열 


a = np.array( [ [ 0, 1, 2 ],
                    [ 3, 4, 5 ],
                    [ 6, 7, 8 ] ] ) # 3행 3열 
print(a.shape)
print(a[2,2]) # 행렬 인덱싱 0,1,2(행) 0-1-2(행), 즉 인덱스 기준 2행 2열(실제론 3행 3열)의 component 출력
print(a[-1,-1])
print(a[-2,-2])

# 슬라이싱 -> 인덱스 슬라이싱과 같은 개념
arr = np.array( [ [ 1, 2, 3, 4, 5 ],
                   [ 6, 7, 8, 9, 10 ],
                   [ 11, 12, 13, 14, 15] ] )
print(arr.shape)
print(arr[1,1:3]) #1행의 1번 인덱스부터 3-1번 인덱스까지 출력
print(arr[1:2, 1]) # 인덱스 기준 1행 ~ 2-1행까지 슬라이싱 -> 1행만 슬라이싱 됨 -> 1행의 1번 인덱스를 가진 component 출력

# 불린 어레이
arr = np.array([0,1,2,3,4,5])
bool_arr = np.array([True, False, True, False, True, False])
print(arr[bool_arr]) # True인 component들만 출력
# 불린 인덱싱을 사용할 때 주의할 점은 불린 배열과 인덱싱 배열의 크기가 같아야 됨
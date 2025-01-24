# 파이썬에서 쓰레딩과 멀티쓰레딩의 이유:
# 1. 쓰레딩의 개념: 프로세스 내에서 실행되는 여러 흐름의 단위
# 2. 프로세스의 개념: 실행중인 프로그램
# 3. 멀티쓰레딩의 이유: 프로세스를 생성하고 관리하는데 드는 비용이 크기 때문에 쓰레드를 사용하여 프로세스를 생성하고 관리하는데 드는 비용을 줄이기 위해 사용
# 4. 쓰레드의 장점: 프로세스 내의 데이터를 공유하여 사용할 수 있다.
# 5. 쓰레드의 단점: 프로세스 내의 데이터를 공유하여 사용할 수 있기 때문에 데이터의 무결성을 보장하기 위해 동기화 처리를 해야한다.


# 쓰레드 생성하기:
"""import threading
import time

def task(name):
    print(f'{name} task start')
    time.sleep(3)
    print(f'{name} task end')

# 쓰레드 생성
thread1 = threading.Thread(target=task, args=('first',))
thread2 = threading.Thread(target=task, args=('second',))

# 쓰레드 실행
thread1.start()
thread2.start()

# 메인 쓰레드가 종료되면 쓰레드도 종료된다.
thread1.join()
thread2.join()

print('main thread end') # 메인 쓰레드 종료 -> 모든 쓰레드 종료"""

# 쓰레드 클래스 상속:
"""class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'{self.name} task start')
        time.sleep(3)
        print(f'{self.name} task end')

# 쓰레드 생성 및 실행:
thread1 = MyThread('first')
thread2 = MyThread('second')

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('main thread end')"""

# 멀티 쓰레딩의 한계: GIL(Global Interpreter Lock) 때문에 멀티 쓰레딩이 병렬처리로 동작하지 않는다.
# GIL(Global Interpreter Lock): 파이썬의 쓰레드가 병렬처리로 동작하지 않는 이유 -> CPython에서 GIL이라는 것이 존재하여 파이썬의 쓰레드가 병렬처리로 동작하지 않는다.
# CPU 바운드 작업 -> 멀티 프로세싱 사용
# I/O 바운드 작업 -> 멀티 쓰레딩 사용
# 쓰레드 간 자원 공유로 인해 데드락(Deadlock) 또는 경쟁 상태(race condition)가 발생할 수 있다.

# 쓰레드 동기화:
# 여러 쓰레드가 공유 자원을 사용하는 경우 동기화가 필요함 -> threading.Lock() 사용해 동기화 처리

"""import threading

lock = threading.Lock()
shared_resource = 0 # 공유 자원

def increment():
    global shared_resource
    with lock:  # Lock을 사용하여 동기화
        local_copy = shared_resource
        local_copy += 1
        shared_resource = local_copy

threads = [threading.Thread(target=increment) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"최종 결과: {shared_resource}")

"""

# 쓰레드 함수 호출하기
"""import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

#함수 두개를 순차적으로 호출
#print_numbers()
#print_letters()

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
 """
#파라미터가 있는 함수
"""def first_thread(num,num2):
    for i in range(num +num2):
        print("음성나오기") #음성

def second_thread(num,num2):
    for i in range(num + num2):
        print("비디오나오기") #비디오


thread_first = threading.Thread(target=first_thread, args=(1,100))
thread_second = threading.Thread(target=second_thread, args=(1,100))
"""
"""#import threading
import time
#클래스기반으로 쓰레드 만들기
threading.Thread #클래스를 상속받아서 새로운 클래스를 만든다.
class Worker(threading.Thread):
    def init(self, name):
        super().init()
        self.name = name
        
print("sub thread start! ", threading.current_thread().name)
time.sleep(3)
print("sub thread end! ", threading.current_thread().name)

import threading
import time

# threading.Thread 클래스를 상속받아 Worker 클래스를 정의
class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()  # 부모 클래스의 __init__ 호출
        self.name = name

    # run() 메소드는 쓰레드가 실행할 코드를 포함
    def run(self):  # main 함수 역할
        print("Sub-thread start! ", threading.current_thread().name)
        time.sleep(3)
        print("Sub-thread end! ", threading.current_thread().name)

# 여러 스레드 생성 및 실행
for i in range(5):
    name = f"Thread Number: {i}"
    t = Worker(name)
    t.start()  # 스레드 실행 (run 메소드를 실행)


"""


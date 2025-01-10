import random
# 클래스 사용법 복습:
"""
class Abc:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def set_age(self,age):
        self.age = age
    def get_age(self):
        return self.age
    def get_info(self):
        return ('이름:{},나이:{}'.format(self.name, self.age))

abc = Abc('홍태준', 28)
abc.name = '홍태준'
abc.age = 28
abc.set_age(28)
print(abc.get_age())
print(abc.get_info())
Abc.set_age(abc, 27)
print(abc.get_info())
"""

# 예외처리(Exception Handling):
# try -> except -> fianl 순서로 작성
"""
lst = [1,2,3]
lst[3] #IndexError: list index out of range
"""
# 파이썬의 기본적인 예외 사항 처리법 -> 예외가 발생하는 지점에서 죽는다(에러객체 발생)
# 예외처리의 목적 -> 프로그램의 강제 종료(의도되지 않은)를 막기 위해
"""
while True:
    try:
        age = int(input('나이를 입력하세요: '))
        print(age)
        break # 정상적인 입력이면 break
    except ValueError:
        print('입력이 잘못되었습니다')

print('프로그램을 종료합니다')
"""

"""
def bread_divider():
    bread = 10
    i = 1
    while True:
        try:
            people = int(input('사람 수를 입력하세요:'))
            print('1인당 빵의 수:', bread/people)
            print('von apetite')
            break
        except ValueError as msg:
            print('입력이 잘못되었습니다')
            print(msg) # error message 출력
        except ZeroDivisionError:
            print('0으로는 나눌 수 없습니다')
        
        finally:
            print('{}번째 동작 수행중입니다'.format(i))
        i += 1

bread_divider()
"""
"""
class Grade:
    def __init__(self, kor, eng, math):  # 수정: init → __init__
        self.kor = kor
        self.eng = eng
        self.math = math

    def set_eng(self, eng):
        self.eng = eng

    def get_total(self):
        return self.kor + self.eng + self.math

    def get_avg(self):
        return self.get_total() / 3

    def get_grade(self):
        avg = self.get_avg()
        grade = "가"

        if avg >= 90:
            grade = '수'
        elif avg >= 80:
            grade = '우'
        elif avg >= 70:
            grade = '미'
        elif avg >= 60:
            grade = '양'
        else:
            grade = '가'

        return grade


def main():
    i = 1
    while True:
        try:
            kor = int(input("국어 점수 입력 : "))
            eng = int(input("영어 점수 입력 : "))
            math = int(input("수학 점수 입력 : "))
        except ValueError:
            print('입력이 잘못되었습니다. 처음부터 다시 입력하세요')
            continue

        grade = Grade(kor, eng, math)

        print("총점 : ", grade.get_total())
        print("평균 : ", grade.get_avg())
        print("학점 : ", grade.get_grade())

        try:
            continue_yn = input("계속 하시겠습니까? (y/n) : ")
            # 'y', 'yes', 'Yes', 'Y', 'YES' 처리
            if continue_yn.upper() not in ('Y', 'YES'):
                break
        except ValueError:
            print('입력이 잘못되었습니다')
            continue  # 잘못된 입력 시 다시 루프

        finally:
            print('{}번째 입력 중입니다'.format(i))
            i += 1

    print("프로그램 종료")


main()
"""

# 로또 번호 뽑기:
"""
class Lottery:
    def __init__(self,total_numbers=6, number_range=45):

        self.total_numbers = total_numbers
        self.number_range = number_range
    
    def get_number_list(self):
        numbers = []
        for i in range(self.total_numbers):
            while True:
                num = random.randint(1,self.number_range)
                if num not in numbers:
                    numbers.append(num)
                    break
        return sorted(numbers)

lottery = Lottery()
print(lottery.get_number_list())
"""
"""
lotto_nums = []
# 방법1
while len(lotto_nums) < 6:
    num = random.randint(1,45)

    if num not in lotto_nums:
        lotto_nums.append(num)

print(sorted(lotto_nums))


# 방법2
class Lottonum:
    def __init__(self):
        self.lotto_nums = []
    def get_lotto_nums(self):
        self.lotto_nums = []

        while len(self.lotto_nums) < 6:
            num = random.randint(1,45)
            if num not in lotto_nums:
                self.lotto_nums.append(num)
        return self.lotto_nums

lotto = Lottonum()
print(lotto.get_lotto_nums())
"""

# 주사위게임:
"""class DiceGame:
    def __init__(self):
        self.participant = {}
    
    def add_participant(self,name):
        dice_num = random.randint(1,6)
        self.participant[name] = dice_num

    def get_info(self):
        for name, number in self.participant.items():
            print('{}의 주사위 숫자는 {}입니다'.format(name, number))

    def get_winner(self):
        winner = max(self.participant, key=self.participant.get)
        maximum = self.participant[winner]
        print('승자는 {}입니다'.format(winner))

game = DiceGame()
game.add_participant('철수')
game.add_participant('훈이')
game.add_participant('짱구')    

game.get_info()
game.get_winner()
"""

"""
class DiceGame():
    #def init(self,player1,player2):
    #    self.players = ([player1,0],[player2,0]) #user 2명으로 한정

    def input_players(self):

        while True:
            try:
                player1 =  input("첫 번째 참가자의 이름을 입력하세요: ")
                player2 =  input("두 번째 참가자의 이름을 입력하세요: ")
                break;
            except ValueError:
                print("입력이 잘못되었습니다. 처음부터 다시 입력하세요.")
                continue

        self.players = ([player1,0],[player2,0]) #user 2명으로 한정
        #print(self.players)

    def dice_result(self):

        for i in range(2):
            self.players[i][1] = random.randint(1,6)
            print(self.players[i][0],"주사위 숫자는 : ",self.players[i][1])

        if self.players[0][1] > self.players[1][1]:
            print(self.players[0][0],"가 이겼습니다.")
        elif self.players[0][1] < self.players[1][1]:
            print(self.players[1][0],"가 이겼습니다.")
        else:
            print("비겼습니다.")

    def run(self):
        self.input_players()
        self.dice_result()

dice_game = DiceGame()
dice_game.run()
"""
    
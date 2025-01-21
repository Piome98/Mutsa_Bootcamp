# 데코레이터와 클로저의 차이점:
# 클로저는 함수를 반환하고 데코레이터는 함수를 인자로 받는다.

#클래스 메소드의 사용:
#클래스 메소드는 클래스 변수를 사용할 수 있다.

"""class Simple:
    count = 0  # Private class variable -> 클래스 변수수

    def init(self):
        self.count2 = 0

    @classmethod
    def increment(cls):
        cls.count += 1 # 클래스 변수 증감
        return cls.count

    @classmethod
    def get_count(cls):
        return cls.count # 클래스 변수 반환

Simple._Simplecount = 42

s = Simple()
s.dict['_Simple__count'] = 100

print(s.increment())
print(s.increment())
print(s.increment())
print(s.get_count())


print(Simple.increment())
print(Simple.increment())
print(Simple.increment())
print(Simple.get_count())"""

# 프로퍼티(property) 함수:
"""class Natural:
    def __init__(self, n):
        self.setn(n)

    def getn(self):
        return self.__n
    
    def setn(self, n):
        if n < 1:
            self.__n = 1
        else:
            self.__n = n
        
    p = property(getn, setn) # 프로퍼티 객체


def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    # n1.setn(n2.getn() + n3.getn())
    n1.p = n2.p + n3.p
    print(n1.p)

main()"""

# 프로퍼티 함수를 사용하면 get, set 함수를 사용하지 않고도 변수에 접근할 수 있다.
"""class Citizen:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter # 프로퍼티 함수의 setter -> age가 프로퍼티 객체가 되어 Citizen 객체의 age 변수에 접근할 수 있다. 
                # -> setter 함수를 호출
    def age(self, age):
        print('나이를 업데이트 합니다')
        self._age = age

citizen = Citizen(20)
citizen.age = 30
print(citizen.age)
"""

"""class CharacterInfo:
    def __init__(self, power, speed):
        self.power = power
        self.speed = speed

    def __get__(self, obj, objtype):
        print('(GET)정보 조회됨')
        #<main.CharacterInfo object at 0x000001BCB2AD7D30> 
        # <main.Guardian object at 0x000001BCB2AD7BB0> 
        # <class 'main.Guardian'>
        print(self, obj, objtype)
        return ("공격력 : "+str(self.power) + " / 스피드 : " + self.speed)

    def __set__(self, obj, val):
        print('(UPDATE)정보 갱신 시작')
        self.power = val.power
        self.speed = val.speed

    def __delete__(self, obj):
        print("(DELETE)정보 삭제하기")
        self.power =""
        self.speed = ""

class Guardian:
    info = CharacterInfo(10, "50km/h")


g1 = Guardian()   # g1 이라는 수호천사 인스턴스 하나 생성
print(g1.info)   # 인스턴스 g1의 초기 정보 출력 
info_after_upgrade = CharacterInfo(15, "70km/h")   # 업그레이드 아이템 적용 후 캐릭터 정보
g1.info = info_after_upgrade   # 새 캐릭터 정보를 인스턴스 g1 에 설정
print(g1.info)   # 인스턴스 g1의 정보 출력
del g1.info   # 인스턴스 g1의 정보 삭제
print(g1.info)   # 인스턴스 g1의 정보 출력
"""

"""class Car:
    def __init__(self, initial_speed):
        self._speed = initial_speed

    @property
    def speed(self):
        print('현재 속도 구하기')
        return self._speed

    @speed.setter
    def speed(self, value):
        print('현재 속도 설정하기')
        self._speed = value

    @speed.deleter
    def speed(self):
        print('현재 속도 정보 삭제하기')
        del self._speed


car = Car(50)

print(car.speed)
car.speed = 100
print(car.speed)
del car.speed"""

# 타입 어노테이션: 
# 함수의 매개변수와 반환값에 대한 타입을 지정하는 것 -> 런타임에는 영향을 미치지 않음(생략 가능)
"""def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2)) # 3(정수 출력)"""

# 크롤링 예제 -> 네이버 증권 거래량 탑 10 종목 출력:
"""from bs4 import BeautifulSoup
import requests

# URL 설정 및 User-Agent 헤더
url = "https://finance.naver.com/sise/sise_quant.naver"  # 거래량 상위 페이지
headers = {'User-Agent': 'Mozilla/5.0'}

# HTTP 요청
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Failed to fetch data. HTTP Status: {response.status_code}")
    exit()

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 거래량 상위 종목 테이블 선택
table = soup.find('table', class_='type_2')
rows = table.find_all('tr')  # 테이블의 행 추출

# 거래량 상위 10개 종목 추출
top_10_stocks = []
for row in rows:
    cols = row.find_all('td')  # 각 열 추출
    if len(cols) < 10:  # 데이터가 없는 행 스킵
        continue

    # 종목명, 현재가, 거래량 추출
    stock_name = cols[1].get_text(strip=True)  # 종목명
    current_price = cols[2].get_text(strip=True)  # 현재가
    volume = cols[6].get_text(strip=True)  # 거래량

    top_10_stocks.append((stock_name, current_price, volume))
    if len(top_10_stocks) == 10:  # 상위 10개만 추출
        break

# 결과 출력
print("네이버 증권 거래량 상위 10종목:")
for idx, (name, price, vol) in enumerate(top_10_stocks, 1):
    print(f"{idx}위: {name}, 현재가: {price}, 거래량: {vol}")"""



# OpenWeatherMap API를 이용한 날씨 정보 출력:
# API(Application Programming Interface) 키 발급 및 호출 예제:
#https://home.openweathermap.org/api_keys
"""import requests
import json

city = "Seoul"  # 조회할 도시
apikey = "708973b23ed06b68f853128552163cc9"  # OpenWeatherMap API 키
lang = "kr"  # 언어 설정

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

# API 호출
result = requests.get(api)

# 응답 상태 코드 확인
if result.status_code != 200:
    print(f"Failed to fetch data. HTTP Status: {result.status_code}")
    print(result.text)  # 에러 응답 내용 출력
    exit()

# JSON 데이터 파싱
data = json.loads(result.text)

# 필요한 키가 존재하는지 확인
if "name" not in data or "weather" not in data or "main" not in data:
    print("Incomplete data received. Check API response structure.")
    print(data)
    exit()

# 날씨 정보 출력
print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.")
print("현재 온도는 ", data["main"]["temp"], "입니다.")
print("체감 온도는 ", data["main"]["feels_like"], "입니다.")
print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
print("습도는 ", data["main"]["humidity"], "입니다.")
print("기압은 ", data["main"]["pressure"], "입니다.")
print("풍향은 ", data["wind"]["deg"], "입니다.")
print("풍속은 ", data["wind"]["speed"], "입니다.")
"""


# 번역기 예제:
"""from googletrans import Translator

# 번역기 객체 생성
translator = Translator()

print("실시간 번역기 (한국어 → 영어)")
print("종료하려면 'exit'를 입력하세요.\n")

while True:
    # 사용자 입력
    sentence = input("번역할 문장을 입력하세요: ")

    # 종료 조건
    if sentence.lower() == 'exit':
        print("프로그램을 종료합니다.")
        break

    # 번역 처리
    try:
        translated = translator.translate(sentence, src='ko', dest='en')
        print(f"번역된 문장: {translated.text}\n")
    except Exception as e:
        print(f"번역 중 오류가 발생했습니다: {e}\n")"""



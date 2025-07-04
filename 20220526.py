# 예제 05
class 차:

    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

car = 차(2, 1000)

print(car.바퀴) 
print(car.가격)


# 예제 06

class 자전거(차):
    def __init__(self, value1, value2):
        self.바퀴 = value1
        self.가격 = value2

bicycle = 자전거(2, 100)
print(bicycle.바퀴)
print(bicycle.가격)


class 자전거(차):
    pass

bicycle = 자전거(2, 100)
print(bicycle.바퀴)
print(bicycle.가격)


# 예제 07

class 자동차(차):

    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

    def 정보(self):
        print("바퀴수 :  %d"%(self.바퀴))
        print("가격: %d"%(self.가격))


car = 자동차(4, 1000)
car.정보()        # 바퀴수 : 4 다음줄 가격 : 1000


# 예제 08

import random

a = random.randint(1, 6)
print(a)

#class DIce():    
#    def roll(self):
#        a = random.randint(1,6)
#
#        return a


class DIce():    # 클래스 만드세여 일때
    def roll(self):
        return random.randint(1,6)

# print("주사위 값: " + str(Dice().roll()))


def roll():          #함수 만들어보세여 일때
    return random.randint(1,6)

print(roll())


# 과제 01 하는법 설명

# 함수만
# pass 지우고 그 부분 코딩하기
# 한두줄이면 될 것
# 함수 만드는


# 과제 02 방법

# 함수
# 대한민국 하면 서울, 덴마크는 코펜하겐 하고 프린트 되야함
# 일본을 썻을 때 해당 사항이 없습니다 라고 프린트 해줘야함
# pass 지우거 거기에 쓰기


# 과제 03 방법

# 텍스트파일 자동으로 생성되고 거기에 그 숫자들이 적혀있어야함
# randint값 사이값 


# 과제 04 방법

# 03에서 만든 4가지 파일을 읽어드리는 거
# 영상 설명 다시 보면서 하기... 복잡해ㅠㅠ
# 구글링해서라도 하래
# 1등 점수를 반환하는 함수 "center"...
# 1등 점수가 출력되게 끔
# 파일을 read해서 


# 과제 05 방법

# pass 지우고 거기다 쓰기(?)
# 이미 써있는거 마지막 줄에 print가 없는데 print 되어야함
# 이는 introduce 메소드 안에 print가 있어야함
# 예전 앞에꺼 잘 보셔서 해보래. 

# 전체 5개 해도 그렇게 코딩 양이 많진 않음



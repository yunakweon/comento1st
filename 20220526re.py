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
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

bicycle = 자전거(2, 100)
print(bicycle.바퀴)
print(bicycle.가격)


# 예제 07

class 자동차(차):

    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

    def 정보(self):
        print("바퀴수: %d"%(self.바퀴))
        print("가격: %d"%(self.가격))

car = 자동차(4, 1000)
car.정보()


# 예제 08

import random
print(random.randint(1, 6))
#print(a)

#class Dice():
#    def roll(self):
#        a = random.randint(1, 6)

#        return a


#print("주사위 값: " + str(Dice().roll()))


def roll():
    return random.randint(1, 6)

print(roll())
from re import S
from tkinter import N
from turtle import speed
from unicodedata import name


class introduce:
    name =""
    age = 0

person = introduce()
person.name = "k"
person.age = 24


class introduce:
    name = ""
    age = 0
    mbti = ""

    def show(self):
        print("안녕")

person = introduce()
person.name = "k"
person.age = 24
person.mbti = "estj"
person.show()        

print("person의 mbti = %s입니다"%(person.mbti))


class Car:
    color = ""
    speed = 0

    def upspeed(self, value):
        self.speed += value

    def downspeed(self, value):
        self.speed -= value

car1 = Car()
car2 = Car()

car1.color = "red"
car2.speed = 0

car2.color = "yellow"
car2.speed = 10

car1.upspeed(40)
print("car1의 속도는 %d입니다."%car1.speed)


class Fruitseller:
    numofapple = 100
    mymoney = 0

    apple_price = 1000

    def saleapple(self, money):
        number = money / self.apple_price
        self.numofapple = 100 -number
        self.mymoney += 1000*number

        return number

    def showSaleResult(self):
        print('남은 사과: ',)


# 예제 01

class Human:
    name = ""
    age = 0
    gender = ""

areum = Human()
areum.name = "아름"
areum.age = 25
areum.gender = "여자"

print(areum.name)
print(areum.age)
print(areum.gender)


class Human:
    name = ""
    age = 0
    gender = ""

    def __init__(self, value1, value2, value3):
        self.name = value1
        self.age = value2
        self.gender = value3

areum = Human("아름", 25, "여자")

print(areum.name)


# 예제 02

class Human:
    name = ""
    age = 0
    gender = ""

    def __init__(self, value1, value2, value3):
        self.name = value1
        self.age = value2
        self.gender = value3

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.gender))

    def __del__(self):
        print("나의 죽음을 알리지말라")

areum = Human("아름", 25, "여자")
areum.who()


# 예제 03

class Stock:
    name = ""
    code = ""

    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")

print(삼성.name)
print(삼성.code)


# 예제 04

class Stock:
    name = ""
    code = ""

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, value1):
        self.name = value1

    def set_code(self, value2):
        self.code = value2

a = Stock(None, None)
a.set_name("삼성전자")
a.set_code("005930")

삼성 = Stock("삼성전자", "005930")

print(a.name)
print(a.code)
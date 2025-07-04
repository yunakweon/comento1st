# 문제 01

from itertools import count
from selectors import EpollSelector
from unittest import result


sum = 0

for i in str(3**79):
    sum += int(i)
print(sum)


# 문제 02

i = 0
while i < 7:
    print('*'*i)
    i += 1


# 문제 03

sentence = input("영문자열을 입력하세요: ")
result = sentence[0] + sentence[-1]

# 문제 04

year = int(input("연도를 입력: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("윤년")
        else:
            print("윤년이 아닙니다")
    else:
        print("윤년")
else:
    print("윤년이 아닙니다")


# 예제 05

capital = {"대한민국": "서울"}

for i in capital.keys():
    if len(i) == 3:
        print("%s의 수도는 %s입니다."%(i, capital[i]))


# 예제 06

scores = [80, 75, 91]

average = sum(scores) / len(scores)
print(average)


# 예제 07

phone_number = input("휴대폰 번호를 입력: ")

modified_number = phone_number.replace('-','')


# 예제 08

scores = [856, 917, 705]
pass_num = 0

for i in scores:
    if i >= 550 and i < 730:
        pass_num += 1

print(pass_num)


# 예제 09

quantity_water = int(input("사용하신 물의 양 입력: "))
price = 0

if quantity_water > 30:
    price = 20*430 + 10*570 + (quantity_water - 30)*840
elif quantity_water > 20:
    price = 20*430 + (quantity_water -20)*570
else:
    price = quantity_water*430

print(price)


# 예제 10

number = int(input("게임 최대 숫자 입력: "))
count = 0

for i in range(1, number + 1):
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            count += 1


from ast import arg
import re
from unittest import result


def calculate_plus(a, b):
    c = a+b
    return c 

print (calculate_plus(100, 200))   # 300

hap = calculate_plus(100, 200)
hap2 = calculate_plus(500, 350)

print(hap)
print(hap2)


x3 = 100
y3 = 200
sum = calculate_plus(x3, y3)

print(x3, y3, sum)



#def hap(name):
#    print(name, "님", "두 숫자를 입력해주세여")
#    num1 = int(input("숫자1을 입력해주세요: "))
#    num2 = int(input("숫자2를 입력ㅎ해주세여: "))
    
#    result = num1 + num2
#    print("결과:", result)

#name = input("누구세요")

#hap (name)


def calculate_sum(x1, x2, x3, x4 = 0):
    result = x1 + x2 + x3 + x4

    return result

y = calculate_sum(3, 4, 6, 7)
y2 = calculate_sum(3, 5, 6)

print(y)     # 20
print(y2)     # 14


def calculate_mul(x1, x2, x3, x4 = 1):
    result = x1 * x2 * x3 * x4

    return result

y = calculate_mul(3, 4, 6, 7)

print(y)       # 504


def hap(*yyyy):
    for i in yyyy:
        print(i)

x = hap(1,2,3,4,5,6,7)


def hap (*param):
    sum = 0
    for i in param:
        sum += i

    return sum

a = hap(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a)        # 55


c = 100

def calculate_plus(a, b):
    c = a + b
    return c

c = calculate_plus(3,5)
print(c)         # 8


# 예제 04

def make_url(string):
    print('www.'+string+'.com')

make_url("naver")      #www.naver.com
make_url("facebook")   #www.facebook.com


def make_url(string):
    if string[0] == 0:
        print('www.'+ string + '.com')
    else:
        print('www.' + string + '.co.kr')

make_url("naver")
make_url("facebook")


# 예제 05

def make_list(string):
    print(list(string))

make_list("naver")
make_list("facebook")


def make_list(string):

    result = []
    for i in string:
        result.append(i)

    print(result)

make_list("naver")
make_list("facebook")


# 예제 06

def pickup_even(items):
    result = []
    for i in items:
        if i % 2 == 0:
            result.append(i)

    print(result)

pickup_even([3, 4, 5, 6, 7, 8, 9, 10])   # [4, 6, 7, 10]


# 예제 07

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False

        return True

print(is_prime_num(8))        # False
print(is_prime_num(11))      # True


# 예제 08

food = {"떡볶이":"김밥", "자장면":"단무지","라면":"파김치","치킨":"맥주","삼겹살":"소주"}

def match_food(string):
    print(food[string])


match_food("떡볶이")        #김밥
match_food("자장면")       #단무지
match_food("라면")        #파김치


# 예제 09

def calc(*args):
    if len(args) == 1:
        print(args[0]**2)
    elif len(args) == 2:
        print(args[0]*args[1])
    else:
        print("숫자 한개 또는 두개를 입력해주세요")

calc(3, 2)   # 6
calc(5)     # 25


# 예제 10

def average(list):
    return (sum(list) / len(list))

scores = [6,7,8,0,1,2,3]

print(average(scores))



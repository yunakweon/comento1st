#def calculate_plus(a, b):
#    c= a+b
#    return c

#print(calculate_plus(100,200))

#hap = calculate_plus(100,200)
#hap2 = calculate_plus(500,350)

#print(hap)
#print(hap2)

#x3, y3 = calculate_plus(100,200)

#print(x3,y3,sum)


#name = input("누구세요")

#hap(name)

def hap(name):
    print(name, "님", "두 숫자를 입력해주세요")
    num1 = int(input("숫자 1 입력해주세요: "))
    num2 = int(input("숫자2를 입력해주세여: "))

    result = num1 + num2
    print("결과: ", result)

name = input("누구세요")
hap(name)


def calculate_sum(x1, x2, x3, x4 = 0):
    result = x1 + x2 + x3 + x4

    return result

y = calculate_sum(3, 4, 6, 7)
y2 = calculate_sum(3, 5, 6)

print(y2)


def calculate_mul(x1, x2, x3, x4 =1):
    result = x1 * x2 * x3 * x4


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
print(a)


c = 100

def calculate_plus(a,b):
    c = a + b
    return c

c = calculate_plus(3,5)
print(c)


# 예제04

def make_url(string):
    print('www.'+ string + '.com')

make_url("naver")
make_url("facebook")


def make_url(string):
    if string[0] == 0:
        print('www.'+ string + '.com')
    else:
        print('www.' + string + '.co.kr')

make_url("naver")
make_url("facebook")


# 예제05

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


# 예제06

def pickup_even(items):
    result = []
    for i in items:
        if i % 2 == 0:
            result.append(i)
    
    print(result)

pickup_even([3,4,5,6,7,8,9,10])


# 예제07

def is_prime_num(n):
    for i in range(2, n):   # i = 2,3,4,5,6,7
        if n % i == 0:     # 8/2 8/3 8/4 8/5...8/7
            return False

        return True

print(is_prime_num(8))
print(is_prime_num(11))


# 예제08

food = {"떡볶이":"김밥", "자장면":"단무지", "라면":"파김치", "치킨":"맥주", "삼겹살":"소주"}

def match_food(string):
    print(food[string])

match_food("떡볶이")
match_food("자장면")
match_food("라면")


# 예제09

def calc(*args):
    if len(args) == 1:
        print(args[0]**2)
    elif len(args) == 2:
        print(args[0] * args[1])
    else: print("숫자 한 개 또는 두 개를 입력해주세요...")


calc(3, 2)   #6
calc(5)   #25


# 예제10

def average(list):
    return (sum(list) / len(list)) 

scores = [6,7,8,0,1,2,3]

print(average(scores))
# 예제 01-1

x = 'abcdrfg'

#print(x[1:3])
# print(x[1:] + 'a')
#y = x[1:]
y = x[1:] + x[0]
print(y)

# 또다른방법
y = x.strip('a') + x[0]


# 예제 01-2

y = x[::2]

print(y)


# 예제 02

sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)


sum = 0

for i in range(1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

print(sum)


# 예제 03

n = int(input("수를 입력해주세요: "))
a = 0
b = 1

print(a, end = ' ')

while b < n :
    print(b, end =' ')
    a, b = b, a + b


# 예제 04

second_sum = 0

for hour in range(24):
    for min in range(60):
        if '3' in str(hour) or '3' in str(min):
            second_sum += 60


# 예제 05

sum = {x:0 for x in range(0, 10)}


sum = [0 for i in range(10)]
for i in range(1,1001):
    for x in str(i):
        sum[int(x)] += 1    #985예시: sum[10] += 1, sum[9] += 1, sum[6]+=1
print(sum)      


# 예제 06

a = 0
b = "na"
print("a = %d, 이름 = %s"%(a,b))


print("a = {}, 이름 = {}".format(a,b))

x = 39027523
print(format(x,","))
#print(format(x,",f"))


while True:  
    number = int(input("슛자를 입력하세요: "))

    if len(number) > 20:
        print("다시 입력하세요")
    else: 
        print(format(number, ","))   #format 자동으로 찍어줌 네자리수에
        break


# 예제 07 

time = int(input("초 단위의 시간을 입력해주세요: "))

day = time // 86400
hour = (time % 86400) // 3600
min = (time % 3600) // 60
second = time % 60

print(str(time) + "초 = ", end = "")

if day != 0 : 
    print(str(day) + "일", end = ' ')
if hour != 0:
    print(str(hour) + "시간", end = ' ')
if min != 0:
    print(str(min) + "분", end = " ")
if second != 0:
    print(str(second) + "초", end = " ")


# 예제 08

number = list(input("숫자를 입력해 주세요 (공백)").split())
print(number)
#['11','22','33','44']
#[2,4,6,8]  #각자리더한거

sum = []

for i in number:
    value_sum = 0
    for j in i:
        value_sum += int(j)
    sum.append(value_sum)

#print(sum)

max_num = sum.index(max(sum))
#print(max_num)
print(number[max_num])


# 예제 09

number = int(input("숫자를 입력해 주세여: "))

square = [2**i for i in range(31)]
#print(square)

if number in square:
    print("1")
else:
    print("0")


# 예제 10

import random

print(random.randint(1, 107893434))

a= random.random()

print(a)


# 10 - 2
def make_lotto():
    result = []

    for i in range(6):
        num = random.randit(1, 45)
        result.append(num)

    return result
print(make_lotto())

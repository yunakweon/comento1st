for i in range(0,5,1):
    print(i)         #세로로 0 1 2 3 4


res = 1
for i in range(1, 6, 1):
    res = res * i
    print(res)       #세로로 1 2 6 24 120


for i in range(0, 5, 2):
    print("%d번 반복중입니다." %i)  #세로로 0번 반복중입니다. 2번 반복중입니다. 4번 반복중입니다.


for i in range(0, 11, 1):
    print(i, end = ' ')


res = 0

for i in range(1001, 2000, 2):
    res += i
    print(res)


i = 0
res = 0
num = 0


num = 10

for i in range(1, num+1, 1):
    res = res + i
    print("1부터 %d까지의 합은 %d 입니다.\n" %(num, res))


i, dan = 0, 0
dan = 10
for i in range(1, 10, 1):
    print("%d x %d = %d" %(dan, i, dan*i))


for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print("%d x %d = %d" %(i, j, i*j))
    print("%d단 끝났습니다." %i)
print("끝")


i = 0
while i < 7:
    print("ㅎ")
    i = i + 1


# 예제 01

for i in range(0,5,1):
    print("**********")


# 예제 02

i = 0

while i < 5:
    print("**********")
    i = i + 1


# 예제 03

for i in range(0, 6, 1):
    if i == 0 or i == 5:
        print("********")
    else:
        print("*      *")


i = 0
while i < 6:
    if i == 0 or i == 5:
        print("********")
    else: 
        print("*      *")
    i = i + 1


# 예제 04

for i in range(1, 31, 1):
    if i % 3 == 0:
        print(i)


for i in range(3, 31, 3):
    print(i)


# 예제 05

sum = 0

for i in range (1, 101, 1):
    sum = sum + i
    print(sum)


i = 1
sum = 0

while i < 101:
    sum = sum + i
    i = i + 1
    print(sum)


# 예제 06

for i in range(1, 100000, 1):
    if i % 9 == 0 and i % 10 == 6:
        print(i)
        break


i = 0
while True:
    if i % 9 == 0 and i % 10 == 6:
        print(i)
        break
    else:
        i += 1


# 예제 07

i = 999

while i > 99:
    if i % 24 == 0:
        print(i)
        break
    i = i - 1


# 예제 08

i = 1
gcm = 1

while i < 30:
    if 30 % i == 0 and 75 % i == 0:
       if gcm < 1:
           gcm = i
    i += 1
print(gcm)       #안된다ㅠㅠㅠㅠ


# 예제 09

year = 0
money = 1000

while money<2000:
    money = money * 1.07
    year += 1

print(year)
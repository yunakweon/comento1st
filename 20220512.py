name = "1234.txt"

f = open(name, 'w')

f.close()


name = "1234.txt"

file = open(name, "r")

data = file.read()
print(data)

file.close()


name = "tony.txt"

f1 = open(name, "w")
f1.write("히.\n")
f1.close()            #r w a 기억해주기


import os 

filename = "dfjshdf.txt"

if os.path.exists(filename):       #exists = isfile
    f = open(filename, 'r')
    
    f.close
else:
    print("파일이 옶네여")


directory_name = "midterm"
filename = "fdfd.txt"

if os.path.isdir(directory_name):
    print("디렉토리 있어요")
else:
    os.makedirs(directory_name)


f = open("aaa.txt", 'r')

print(f.readline())    # readline은 첫줄만 읽음

f.close()


f = open("aaa.txt", 'r')

while True:          #while문은 몇번 반복할지 모를때
    line = f.readline()
    if not line:
        break
    print(line.strip())   #원래는 한줄 띄고 빈줄 띄고 한줄인데 스트립쓰면 빈곳 빼고 한줄 디에 바로 한줄
f.close()


f = open("aaa.txt", 'r')

lines = f.readlines()
print(lines)            #['hello\n, 'ddd] 이렇게 리스트로 나옴

f.close()


f = open("aaa.txt", 'r')

lines = f.readlines()

for i in lines:
    print(i.strip())         #hello 다음줄에 ddd일캐 나옴

f.close()


f1 = open("midterm.txt", 'r')
f2 = open("final.txt", 'r')

lines = f1.readlines()
lines2 = f2.readlines()

midterm = []
finalterm = []

for line in lines:
    midterm.append(line.strip())

for line2 in lines2:
    midterm.append(line.strip())

print(midterm)

f1.close()
f2.close()


# 예제 01

f = open("1.txt", 'w')

f.write("oo5930\n")
f.write("005380")

f.close()


# 예제 03

f = open('1.txt', 'r')

result = []

while True:
    line = f.readline()
    if not line:
        break
    result.append(line.strip())

print(result)
f.close()


# 예제 04

f = open("2,.txt", 'r')

lines = f.readlines()
result = {}

for line in lines:

    k, v = line.strip().split(' ')
    result[k] = v    #result[data[0]] = data[1]
 
print(result)


# 예제 05

f = open('even_number.txt', 'w')

for i in range(1, 31):
    if i % 2 ==0:
        f.write(str(i)+ '\n')

f.close()


# 예쩨 06

f = open('star.txt')
i = 0

while i < 7:
    #print('*' * i)
    f.write('*' * i + '\n')     #원래 와일문은 자동으로 띄어지는데 얘는 그게 안되서 붙여야됨 \n이거
    i += 1

f.close()


# 예제 08

f1 = open("test.txt", 'w')
f1.write("Life i too short")
f1.close()  # 정답, 이유:원래는 close 안해도 오류가 안날 수 있는데 여기서는 f1클로즈 안한 상태로 또 새파일을 열었기때문에 오류가 남

f2 = open("test.txt", 'r')
print(f2.read())


# 예제 09

user_input = input("저장할 내용을 입력하세요: ")

f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")

f.close()


# 예제 07

import random

f = open("score.txt", 'w')

for i in range(50):
    score = random.randint(1,100)
    f.write(str(score) + '\n')

f.close()


f = open('score.txt', 'r')

result = []

lines = f.readlines()

for line in lines:
    #print(line.strip())
    result.append(int(line.strip()))

average = sum(result) / len(result)

print(average)

f.close()
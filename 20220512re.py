name = "1234.txt"

f = open(name, 'w')
f.close()


name = "1234.txt"

file = open(name, "r")

data = file.read()
print(data)

file.close()


#name = "tony.txt"

#f1 = open(name, 'w')
#f1.write("히.\n")
#f1.close()

#import os
#from selectors import EpollSelector
#from unittest import result

#filename = "dvfsfs.txt"

#if os.path.exists(filename):
#    f = open(filename, 'r')

 #   f.close
#else:
  #  print("파일이 없네요")


#directory_name = "midterm"
#filename = "fdfd.txt"


f = open("1.txt", 'w')

f.write("oo5930\n")
f.write("005380")

f.close()


# 예제 03 

f = open('1.txt','r')

result = []

while True:
    line = f.readline()
    if not line:
        break
    result.append(line.strip())

print(result)
f.close()


# 예제 04

f = open("2.txt", 'r')

lines = f.readlines()
result = {}

for line in lines:
    k, v = line.strip().split(' ')
    result[k] = v

print(result)


# 예제 05

f = open('even_number.txt', 'w')

for i in range(1, 31):
    if i % 2 == 0:
        f.write(str(i) + '\n')

f.close()


# 예제 06

f = open("star.txt", 'w')
i = 0

while i < 7:
    f.write("*" * i + '\n')
    i += 1

f.close()


# 예제 08

f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

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

f = open("score.txt", 'r')
#sum = 0
average = 0.0

for i in range(50):
    score = random.randint(1,100)
    f.write(str(score) + '\n')

f.close()
print(average)


f = open("score.txt", 'r')
#sum = 0
#average = 0.0

result = []

for line in lines:
    result.append(int(line.strip()))

average = sum(result) / len(result)

print(average)
f.close()
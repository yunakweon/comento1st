f = open('xx.txt', 'r')

lines = f.readlines()

for line in lines:
    print(line.strip())

f.close()



f = open('xx.txt', 'r')

lines = f.readlines()

res = []

for line in lines:
    res.append(line.strip())    # 리스트에 넣을려는거 

print(res)
f.close()



f = open('homework.txt', 'r')

while True:
    line = f.readline()
    if not line: break            # if line == "":
    print(line.strip())

f.close()



f = open('yyy.txt', 'w')

f.write("20221234 김태완")

f.close()

with open('homework.txt', 'r') as f:
    lines = f.readlines

    for line in lines:
        print(line.strip())



f = open("name.txt", "w")

name = ['Alex','Emma','Smith','Jane','Ava','Charlotte','Evelyn']

for i in name:
    if len(i) == 4:
        f.write(i + '\n')

f.close()



f = open("homework.txt", 'r')

lines = f.readlines()
names = []

for line in lines:
    data = line.strip()
    name = data.split(':')[0]
    score = data.split(':')[1]
    names.append(name)
    sum += int(score)

average = sum / len(names)
print(average)

f.close()



# 바로 위에 것을 count를 이용해서 하는 방법
f = open("homework.txt", 'r')

lines = f.readlines()
count = 0
#sum = 0

for line in lines:
    data = line.strip()
    name = data.split(':')[0]
    score = data.split(':')[1]
    count += 1
    sum += int(score)

average = sum / count
print(average)

f.close()



f = open("homework.txt", 'r')

lines = f.readlines()
count = 0
average = 0.0

for line in lines:
    data = line.strip()
    name = data.split(':')[0]
    score = data.split(':')[1]
    count += 1
    sum += int(score)

average = sum / count
print("%.2f"%average)

f.close()



f = open("homework.txt", 'r')
fw = open('len5.txt', 'w')

lines = f.readlines()
num = 1

for line in lines:
    data = line.strip()
    name = data.split(':')[0]
    score = data.split(':')[1]

    if len(name) > 5:
        result = str(num) + ':' + name + '\n'
        fw.write(result)
        num += 1
    

average = sum / count
print(average)

f.close()
fw.close()



# 얘는 위에 num이 1이었던게 0이 됬을 경우 num += 1 위치가 바뀜
f = open("homework.txt", 'r')
fw = open('len5.txt', 'w')

lines = f.readlines()
num = 0

for line in lines:
    data = line.strip()
    name = data.split(':')[0]
    score = data.split(':')[1]

    if len(name) > 5:
        num += 1
        result = str(num) + ':' + name + '\n'
        fw.write(result)
        
    

average = sum / count
print(average)

f.close()
fw.close()



f = open("homework.txt", 'r')

lines = f.readlines()
names = []
scores = []

for line in lines:
    data = line.strip()
    name = data.split(':')[0]
    score = data.split(':')[1]

    names.append(name)
    scores.append(score)

for i in score: 
    sum += int(i)

average = sum / len(scores)
print(average)

f.close()
fw.close()



# 2번 문제 안에 부분, 또 다른 방법
num = 1
for i in names:
    if len(i) > 5:
        fw.write(str(num) + ':' + i + '\n')
        num += 1



import json

x = [
    {'name':'Alex', 'English':90, 'Math':80},
    {'name':'Jane', 'English':77, 'Math':24},
    {'name':'Tom', 'English':86, 'Math':54}
]

print(x)



import json

x = [
    {'name':'Alex', 'English':90, 'Math':80},
    {'name':'Jane', 'English':77, 'Math':24},
    {'name':'Tom', 'English':86, 'Math':54}
]

print(x)

f = open('a.json', 'w')

json.dump(x , f)

f.close()



x = dict()
x['id'] = 0
x['name'] = 'tony'
x['mbti'] = 'istj'
x['like'] = ['drive', 'cook']
x['check'] = True

print(x)

f = open('b.json', 'w')

json.dump(x , f)

f.close()



with open('b.json', 'w') as f:
    json.dump(x, f, indent=4)    # 깔끔하게 들여쓰기가 된다 indent = 4 사용 시 



with open('b.json', 'r') as f:
    data = json.load(f)

    for i in data:
        print(i)

    for i in data:
        print(data[i])

    for k,v in data.items():
        print(k,v)



import numpy as np
import pandas as pd

a = np.array([1,2,3])



import math

a = math.cos(math.pi/3)
print(a)          #0.5000000000000001



import random

a = random.randint(1,10)
print(a)        



#import f20230921 as xx

#xx.star(9)



#import f20230921 

#f20230921.star(9)



#from f20230921 import star, alphabet,
#import f20230921 ff

#star(4)
#print(alphabet)



#import func1 as f1
#from func2 import find_next
# 이 페이지 잘 모르겠음 어려움 

#f1.check_number("010-1234-5678")
#print(find_next(4))



import option.func3

print(option.func3.find_prev(2))



import matplotlib












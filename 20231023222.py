# from turtle import right


# number = int(input("0보다 큰 숫자를 하나 입력: "))

# if number < 0:
#     print("양의 정수를 입력하세여")
# elif number % 2 == 0: print("짝수입니다")



# score = int(input("점수 입력: "))

# if score >= 90: print("A")
# elif score >= 80: print("B")
# else: print("F")

# print("학점입니다")



# a = int(input("a값: "))
# b = int(input("b: "))

# if a > b: print(">")
# elif a < b: print("<")



# def Quadrant(x=0, y=0):
#     if x > 0 and y > 0: print("1")
#     elif x < 0 and y > 0: print("2")
#     elif x < 0 and y < 0: print("3")
#     elif x > 0 and y < 0: print("4")
#     else: print("-1")



# sum = 0

# a = str(3**79)

# for i in a:
#     sum += int(i)

# print(sum)



# for i in range(2, 10):
#     for j in range(1, 10):
#         print("%d X %d = %d"%(i, j, i*j))



# number = int(input("게임 최대 숫자를 입력해 주세요: "))
# count = 0

# for i in (1, number + 1):
#     for j in str(i):
#          if j == '3' or j == '6' or j == '9':
#             count += 1



from ctypes import resize
import re


for i in range(5):
    print("*"*10)



i = 0

while i < 5:
    print("*"*10)
    i += 1



for i in range(6, 0, -1):
    print(("%d"%(i))*i)



for i in range(6, 0, -1):
    print((str(i)+' ')*i)



while i > 0:
    print((str(i)+' ')*i)
    i -= 1



answer = int(input("숫자를 입력: "))
number = 25

while number != answer:
    if answer > number: print("DOWN!")
    elif answer < number: print("UP!")
    answer = int(input("숫자를 입력: "))
print("정답!")



answer = int(input("숫자를 입력: "))
number = 25

while number != answer:
    if answer > number: print("d")
    elif answer < number: print("U")
    answer = int(input("숫자를 입력: "))
print('a')



i = 1

while i <= 30:
    if i % 2 == 0 or i % 3 == 0:
        i += 1
        continue
    else:
        print(i)
        i += 1



a = [1, 11, 80, 24, 67, 32, 19, 24, 88]
res = 0

for i in a:
    if i % 2 == 0:
        res += 1
print(res)



for i in a:
    if i % 2== 0:
        res += 1
print(res)



score = [71, 55, 24, 73, 68, 90]
n = 0

for i in score:
    n += 1
    if i > 70:
        print("%d번 학생 합격"%(n))

for i in score:
    n += 1
    


value = [80, 75, 91, 47, 100, 5, 26]
sum =  0

for i in value:
    sum += i

average = sum / len(value)
print(average)
    


a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school' 'hotel', 'india']

for i in a:
    if len(i) == 5:
        print(i, end = ' ')



answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = ['hello', 62, 'umbrella', 145]
B = ['September', 512.3, 'coffee', 39, 'keyboard', 'notebook', 0.5, 'f12']
C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

x = input("리스트를 입력: ")

if x == 'A':
    for i in A:
        if i in answer: print("O", end ='')
        else: print("X", end='')
else: print("리")



visit = ['영국', '일본', '미국', '프랑스', '폴란드', '칠레', '캐나다', '이탈리아']
wish = ['브라질', '독일', '캐나다', '호주', '영국']
result = []

for i in wish:
    if i in visit:
        result.append(i)

print(result)



def how_many(a,b):
    result = 0
    for i in a:
        if i == b:
            result += 1
    return(result)

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]
print(how_many(x,3))        #5
print(how_many(x,5)) 



def bigger_than(a, b):
    res = 0
    for i in a:
        if i > b:
            res += 1
    print(res)

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]
print(bigger_than(x,4))        #8
print(bigger_than(x,5))   



student = [12,18,3,20,14,5,1,9,10,11,6,2,17,16,4,15,8]

for i in range(1, 21):
    if i not in student:
        print(i, end = ' ')



capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이", "덴마크":"코펜하겐"}

for i in capital:
    if len(i) == 3:
        print("%s의 수도는 %s입니다"%(i, capital[i]))

    

score = {'국어': 90, '영어':95, '수학':77, '미술':68, '과학': 82}

sum = 0
average = 0.0

for i in score:
    sum += score[i]

average = sum/len()



a = {'a':1, "b":2, "c":3}

for i in a.keys():
    print(i, a[i])

for k, v in a.items():
    print(k,v)



sum = 0

for i in str(3**79):
    sum += int(i)



string = "apple"
alphabet = []

for i in string:
    if i not in alphabet:
        alphabet.append(i)



word ='나는 공부가 너무 재미있어서 공부도 공부만 하고 싶어요'

print(word.strip())  

print(word.replace("공부", "운동"))

print(word.split())


word = '하나:둘:셋'

print(word.split(":"))




sentence = input("영문자열을 입력하세요: ")

res = sentence[0] + sentence[-1]



phone_number = input("당신의 휴대폰 번호를 입력해 주세요.")

modified_number = phone_number.replace("-",'')



def calculate_average(list):
    average = sum(list) / len(list)
    return average



def hap(a,b,c=0):
    result = a+b+c
    return result



def cal(a,b):
    sum = 0
    mul = 0

    sum = a+b
    mul = a*b

    return sum, mul

x, y = cal(1,2)
print(x,y)



def plus(*param):
    result = 0
    for num in param:
        result += num
    return result



def star(number): 
    for i in range(number):
       print("*"*number)

def star(number):
    for i in range(number):
        print("*"*number)

num = int(input("0보다 큰 숫자 입력: "))
star(num)


def star(number):
    i = 0
    while i < number:
        print("*"*number)
        i += 1



import numpy as np

a = np.array(1)


print(a, a.shape, a.ndim)

a.size



arr3 = np.array([[0, 1, 2], [3, 4, 5]])

print(arr3.shape)    #(2,3) 
print(arr3.ndim)       #2
print(len(arr3))        #2
print(len(arr3[0]))      #3

print(arr3[0][0:2])



b = np.zeros(5, dtype  = int)
print(b)


c = np.ones((4,3,5), dtype=int)
print(c)


d = np.full((4,3), 8.1)


a = np.empty([2,2], dtype = int)


c = np.arrange(1,8)


d = np.linspace(0,100, num = 11)


a = np.random.randint(0, 10, (3,3))

a = np.random.randn(1,2)

a = np.random.normal(0,1)



a = np.array([[1,2,3],[4,5,6]])
print(a)

print(a.reshape(6,1))


b = a.flatten()

b = a.flatten()

c = a.reshape(-1,)




a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.concatenate([a,b])

c = np.concatenate([a,b])



v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(np.hstack((v1, v2)))
print(np.vstack((v1,v2)))



x = np.array([1, 2, 3, 4])
y = [1,2,3,4]

print(np.sum(x))
print(x.sum())

print(x.max())

print(x.argmin())
print(x.argmax())

print(x.mean)

print(np.var(x))
print(np.std(x))



import numpy as np

a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])

for func in (a.min, a.max):
    print(func.__name__, "=", func())



a = [2,5,1,17,21]

result = np.array(a) + 1

print(result)



import numpy as np

a = np.array([[2,5,1,17,21]])

result = a + 1



import numpy as np

a = np.array([1,3,5,7,8,11])

b = a.reshape(2,3)

print(b)



import numpy as np

a = np.array([1,3,5,7,8,11])

import numpy as np

res1 = np.add(10,30)
res2 = np.subtract(40, 93)
res3 = np.multiply(55,71)   
res4 = np.divide(250,25)

print(res1, res2, res3, res4)



import numpy as np

a = np.random.random((10, 10))

min_a = a.min()
                     


values = np.linspace(0, np.pi, num = 11)
x = np.sin(values)



Python = np.array([90,92,37])
R = np.array([85, 88, 91])
Math = np.array([94,91,84])

s_python = np.sum(Python)
s_r = np.sum(R)
s_math = np.sum(Math)

m_python = np.mean(Python)
m_r = np.mean(R)
m_math = np.mean(Math)


print(s_python, s_r, s_math)
print(m_python, m_r, m_math)


x = np.argmax([m_python, m_r, m_math])

if x == 0: print(m_python)
elif x == 1: print(m_r)



import numpy as np
import random

sales = [86623, 33030, 38117]

n_sales = np.array(sales) 
filter = np.where(n_sales < 40000)

bad_sales = n_sales[filter]



import numpy as np
data = np.loadtxt('data.txt', delimiter=',')

print(data.mean())



data = np.loadtxt('data2.txt')
average = np.mean(data)
print(average)




from pandas import Series, DataFrame

a = Series()
b = DataFrame()

import pandas as pd

a = pd.Series()
b = pd.DataFrame()



f = open('aaasfsdf.txt', 'r')

while True:
    line = f.readline()

    if not line:
        break
    print(line)

f.close()


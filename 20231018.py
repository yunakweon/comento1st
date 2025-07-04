import numpy as np
import pandas as pd

a = [1, 2, 3]
b = np.array([1, 2, 3])

print(a)          #[1, 2, 3]
print(a[0])       #1

print(b)          #[1 2 3]
 

a = np.array(a)
print(a)     #[1 2 3]



a = np.array(1)

print(a, a.shape, a.ndim)          #1 () 0



a = np.array([1])

print(a, a.shape, a.ndim)          #[1] (1,) 1



a = np.array([1,2])

print(a, a.shape, a.ndim)          #[1 2] (2,) 1



a = np.array([[4,19,8],[16,3,5]])

print(a, a.shape, a.ndim)
#[[ 4 19  8]
# [16  3  5]] (2, 3) 2



a = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

print(a, a.shape, a.ndim)
#[[[1 2 3]
#  [4 5 6]
#  [7 8 9]]
#
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
#
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]] (3, 3, 3) 3



a = np.array([1, 2, 3, 4])

print(a.size)        #4
print(a.dtype)       #int32
print(a[3])          #4



a = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

print(a.shape)      #(2, 4)
print(a[1][2])      #7


b = [1,2,3]

print(type(a), type(b))
#<class 'numpy.ndarray'> <class 'list'>

c = np.array(b)

print(c.shape)       #(3,)



a = np.array([[[2,3,4],[6,7,8],[2,3,4],[6,7,8]],[[2,3,4],[6,7,8],[2,3,4],[6,7,8]]])
 
print(a.shape)   #(2, 4, 3) 겹치는거 먼저 써지고 행열 9페이지 마지막 그림 그린것 


print(a.dtype)   #int32


a = np.array([[[2.0,3,4],[6,7,8],[2,3,4],[6,7,8]],[[2,3,4],[6,7,8],[2,3,4],[6,7,8]]])
print(a.dtype)   #float64


a = np.array([[[2.0,3,4],[6,7,8],[2,3,4],[6,7,8]],[[2,3,4],[6,7,8],[2,3,4],[6,7,8]]], dtype = int)
print(a.dtype)   #int32   #뒤에 dtype = int 작성해서 안에 소수있지만 버려짐



a = [1, 2, 3]
b = [6, 7, 8]

print(b+a)        #[6, 7, 8, 1, 2, 3]


a_n = np.array(a)
b_n = np.array(b)

print(a_n + b_n)      #[ 7  9 11]

print(a * 4)          #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
#print(a + 4)         #는 에러, 안됨

print(a_n * 4)        #[ 4  8 12]
print(a_n + 4)        #[5 6 7]


print(a == 2)       #False
print(a_n == 2)     #[False  True False]



arr3 = np.array([[0, 1, 2], [3, 4, 5]])

print(arr3)
#[[0 1 2]
# [3 4 5]]

print(arr3.shape)   #(2, 3)
print(arr3.ndim)    #2 (차원)
print(len(arr3))    #행의 개수(2차원에선)   #2
print(len(arr3[0])) #열의 개수             #3


print(arr3[0][0:2])        #[0 1]    #slicing



arr = np.array([0, 1, 2, 3, 4])

print(arr[1] * arr[3])       #3



arr = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

print(arr[0, :]) # [0 1 2 3]
print(arr[:, 1]) # [1 5]
print(arr[1, 1:]) # [5 6 7]
print(arr[:2, :2]) 
#[[0 1]
# [4 5]]



b = np.zeros(5)
print(b)       #[0. 0. 0. 0. 0.]
 

b = np.zeros(5, dtype=int)
print(b)       #[0 0 0 0 0]


b = np.zeros((2,4), dtype=float)
c = np.ones((4,3,5), dtype=int)

print(b)
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]]

print(c)
#[[[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]
#
# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]
#
# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]
#
# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]]



d = np.full((3,4), 8.1)
print(d)
#[[8.1 8.1 8.1 8.1]
# [8.1 8.1 8.1 8.1]
# [8.1 8.1 8.1 8.1]]
 
d = np.full((3), 8)
print(d)   #[8 8 8]



a = np.empty(2)     #임의의 값으로 채워짐
b = np.empty([2,2], dtype=int)
print(a)
print(b)



c = np.arange(5)
print(c)              #[0 1 2 3 4]

c = np.arange(1, 8)   
print(c)              #[1 2 3 4 5 6 7]

c = np.arange(1, 12, 2)
print(c)                   #[ 1  3  5  7  9 11]



d = np.linspace(0,100, num=11) 
print(d)       #값은 11개 나오는데 10등분, 첨이 0이라 그런듯?



import random

a = random.randint(1,10)
print(a)

a = np.random.randint(1,10)    #정수
print(a)

a = np.random.randn(5)    #소숫점
print(a)


array = np.random.randint(0, 10, (3,3))
print(array)
#[[5 2 2]
# [3 9 2]
# [6 5 9]]



a = np.random.randint(0, 9, (3,2))
print(a)



a = np.array([[1,2,3],[4,5,6]])
print(a)
#[[1 2 3]
# [4 5 6]]

print(a.reshape(6,1))
#[[1]
# [2]
# [3]
# [4]
# [5]
# [6]]


b = a.flatten()
c = a.reshape(-1,)   #위아래 기능 같음

print(b)     #[1 2 3 4 5 6]
print(c)     #[1 2 3 4 5 6]



a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate([a,b]))      #[1 2 3 4 5 6]

c = np.concatenate([a,b])
print(c)                          #[1 2 3 4 5 6]



v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(np.hstack((v1, v2)))       #[1 2 3 4 5 6]
print(np.vstack((v1, v2)))       
#[[1 2 3]
# [4 5 6]]



x = np.array([1, 2, 3, 4])
y = [1,2,3,4]

print(np.sum(x))    #10
print(x.sum())      #10

print(sum(y))       #10

print(x.max())      #4

print(x.argmin())   #0   #0번째가 가장 작다
print(x.argmax())   #3   #최대가 나타내는 위치

print(x.mean())     #2.5
print(np.mean(x))   #2.5
 
print(np.var(x))    #1.25                #분산
print(np.std(x))    #1.118033988749895   #표준편차 



import numpy as np

a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])

for func in (a.min, a.max, a.sum, a.prod, a.std, a.var):
    print(func.__name__, "=", func())



# 예제 01

a = [2,5,1,17,21]
result = np.array(a) + 1

print(result)       #[ 3  6  2 18 22]



import numpy as np

a = np.array([2,5,1,17,21])
result = a + 1

print(result)     #[ 3  6  2 18 22]



# 예제 02

import numpy as np

a = np.array([1,3,5,7,8,11])

b = a.reshape(2,3)

print(b)



# 예제 04

import numpy as np
a = np.array([1,3,5,7,8,11])
## coding here
import numpy as np
res1 = np.add(10,30)
res2 = np.subtract(40,93)
res3 = np.multiply(55,71)
res4 = np.divide(250,25)
print(res1, res2, res3, res4)



# 예제 05

import numpy as np
a = np.random.random((10, 10))
min_a = a.min()
max_a = a.max()
print(a)
print(min_a, max_a)



# 예제 06

values = np.linspace(0, np.pi, num = 11)
x = np.sin(values)
print(x)



# 예제 07

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
#print(x)

if x == 0: print(m_python)
elif x == 1: print(m_r)
else: print(m_math)
#89.66666666666667
 


# 예제 08

import numpy as np
import random

sales = [86623, 33030, 38117]

n_sales = np.array(sales)

filter = np.where(n_sales<40000) # 매출을 달성하지 못한 날
#filter = n_sales < 4000   ##간단하게 이거해도 됨

bad_sales = n_sales[filter] # 매출을 달성하지 못한 날의 매출액

print(filter)
print(bad_sales)



# 예제 09

import numpy as np

data = np.loadtxt('data.txt', delimiter=',')

print(data.mean())



# 예제 10

data = np.loadtxt('data2.txt')
average = np.mean(data)
print(average)




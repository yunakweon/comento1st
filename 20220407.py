#시험 7문제는 빈칸, 뒤에 3문제는 코딩!!
#빈칸은 05. 예제 4번 같은 느낌.



# 챕터 4 예제 7

# i = 999

# while i > 99 :
   # if i % 24 == 0 :
      #  print(i)
      #  break
    #i = i - 1
    # (i -= 1) 위에랑 같은 식


# 챕터4 예제8

#i = 1
#gcm = 1

#while i < 30 :
    #if 30 % i == 0 and 75 % i == 0 :
        #if gcm < i :
           # gcm = i 
    #i += 1
#print(gcm)

# 최대공약수 gcm (원래 res 자리에)

    
# 쳅터 4 예제 9

#year = 0
#money = 1000

#while money < 2000:
    #money = money *1.07
    #year += 1

#print(year) 



from stringprep import c6_set


x1 = 3
x2 = "hello"
x3 = "phyton"
x4 = 1.54

# print(x1)

x_list = [3, "hello", "phyton", 1.54]
x_list[0] = 4055

#print(x_list[4])

print(x_list) #이러면 전체가 나옴

print(x_list[0])



a = []
a.append(3)  
a.append(2)
a.append(5)
a.append(1)

a.insert(2, "hello") #[3, 2, 'hello', 5, 1] 이라고 출력됨.
# 위에 식에서 2라고 쓰는게 칸 수를 0 1 2 순으로 세기 때문에 3번째에 들어가서 출력됨.

print(a) #[3, 2, 5, 1] 이라고 순서대로 출력됨.



data = [6, 3.14, "hello", 10]

#for i in range(0,4):
    #print(data[i])
    # 같은 값 나옴.

print(data[0])
print(data[1])
print(data[2])
print(data[3])




a=[]

for i in range(0,4) :
    a.append(i)



aa = []
bb = []

for i in range(0,100):
    aa.append(2*i)

print(aa)


for i in range(0,100):
    bb.append(aa[99-i])

print(bb)



# 예제1
# 방법1 - 추천!
greetings = ['안녕', '니하오']

for i in greetings:
   print(i)


# 방법2 - 비추
print(len(greetings))

for i in range(0,len(greetings)):
    print(greetings[i])


#for i in greetings :
    #print(i, end=' ')
#안녕 니하오 하이 이런식으로 옆으로 쭉 나옴.


#봉쥬르싸와디캅올라 처럼 거꾸로 쭉
for i in range(0,len(greetings)):
    print(greetings[len(greetings)-i-1], end='')
   # 위에 len(greetings)-i-1 은 6 - 1 랑 같은 뜻.


# 각각 안쪽 곱
a = [1, 2, 3, 4]
b = [5, 2, 4, 6]

for i in range(0, len(a)):
    for j in range(0, len(b)):
        print(a[i]*b[j])



A = [1, 5, 11, 5, 5,5,5,5,5, 5, -3]
A.remove(5) #맨 앞에 5만 지워짐.

print(A)

# pop은 시험문제로도 안나옴 (학교??)
A.pop()
print(A, len(A))


A = [-5, 1, 0, 34, 2, 7]
A.sort()

print(A.sort())



A = [-5, 1, 0, 34, 2, 7]
A.sort(reverse=True)

print(A.sort())

# A.sort() 랑 A.sort(reverse=False)는 같은 것.


greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']
greetings.reverse()

for i in greetings:
    print(i, end='')


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(A[0])
#print(A[1][0])


for i in range(0,3):
    for j in range(0,3): 
        print (A[i][j], end ='')
        # i = 0, j = 0   -> i=0, j=2 -> i=0 j=



#예제3
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']
b = []

for i in a:
    if len(i) == 5:
        b.append(i)

print(b)




# 과제 5번 힌트
a = ['alpha', '권유나', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']

if '권유나' in a :
    print("tttt")


if 'alpha' in a :
    print("o")


# 튜플
A = (1, 2, 3)
print(A)
B = list(A)
print(B)
c = tuple(B)
print(c)
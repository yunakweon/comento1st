from operator import iadd
from re import L


for i in range(0, 5, 1):
    print("안녕하세요")
    print("hi")


for i in range(0, 5, 1):
    print(i)
print("끝")


for i in range(0, 5, 2):
    print("%d번 반복중입니다." %i)


for _ in range(0, 5, 1):
    print("안녕하세요")
# 헷갈리니까 _ 보다는 그냥 i로 통일해서 쓰는편 추천



for i in range(0, 30, 1):
    print(i)


#가로로 쭉 나열하고 싶을때
for i in range(0, 11, 1):
    print(i, end=' ')


for i in range(0, 11, 1):
    print(i, end='hi')



res = 0

for i in range(1001, 2000, 2):
    res += i
# 0 + 1001 + 1003 + 1005 + ... + 1999
print(res)



res = 0
for i in range(1000, 2000, 1):
    if i % 2 == 1:
        res += i
print(res)

# if문에 홀수만 걸리기 때문에 짝수는 안걸리고 넘어감




res = 0
for i in range(1000, 2000, 1):
    if i % 2 == 1:
        res += i
print(res)



# 구구단
dan = int(input("구구단 몇단? "))
for i in range(1, 10 ,1):
    print("%d x %d = %d" %(dan, i, dan*i))




#중첩 할때
for i in range(0, 3, 1):
    for j in range(0, 5, 1):
        for k in range(0, 10 ,3):
            print("i=%d, j=%d, k=%d" %(i, j, k))
# 안쪽포문돌고 바깥포문 돌고




# 전체 구구단
for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print("%d x %d = %d" % (i, j, i*j))
    print("%d단 끝났습니다." %i)
print("끝")


  


i = 0
while i < 7:
    print(i)
    i += 1
# 참일때까지 계속 돈다


i = 0
while i < 7:
    print(i)
    i += 1
    if res > 40 : break #(?)
 # break 문을 걸면 바로 빠져나온다 멈춤



while True :
    print("hello")
    break




res = 0

for i in range(1, 11, 1):
    res += i

    if res > 30 :
        print("처음으로 합이 30이 넘는 숫자는 = %d\n", i )
        break
print(res)



#for j in range(1, 11, 0):
    #for i in range(1, 11, 1):
        #if i % 2 == 0 :
           #continue
    #res += i

# continue 가장 가까운 위에 for문으로 올라감.
# 그 밑에 뭐가 있던 상관없음. 131번으로 돌아감
print(res)


 

# 예제1

for i in range (0, 5, 1):
    print("***********")


# 예제2
while i < 5 :
    print("***********")
    i += 1



# 예제3

for i in range (0, 7, 1):
    if i == 0 or i == 6:
       print("********")
    else :
        print("*      *")



# 예제4
#방법1
for i in range (3, 31, 3):
    print("%d" % i)

#방법2 -> 이쪽 추천
for i in range(1 ,31, 1):
    if i % 3 == 0:
        print(i)



# 예제5
# for문으로 했을 때
sum = 0
for i in range(1, 101, 1):
    sum += i

print(sum)

# while문으로 했을 때
i=1
sum = 0

while i <= 100:
    sum += i
    i += 1

print(sum)


# 예제6

i = 0

while True:
    if i % 9 == 0 and i % 10 ==6 :
        print(i)
        break
    else : 
        i += 1


for i in range(1, 100000, 1):
    if i % 9 == 0 and i % 10 == 6:
        print(i)
        break


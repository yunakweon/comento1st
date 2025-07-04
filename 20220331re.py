#for i in range(0, 5, 1):
 #   print("안녕하세요")
  #  print("hi")
    # 안녕하세요 다음줄 hi 다음줄 안녕하세요 반복

#for i in range(3):
 #   print("안녕하세요")

#for i in range(0, 5, 1):
 #   print(i)          #세로로 1 2 3 4
#print("끝")          # 세로로 1 2 3 4 끝

#res = 1
#for i in range(1, 6, 1):
 #   res = res * i
  #  print(res)

#for i in range(0, 5, 2):
 #   print("%d번 반복중입니다." %i)   # 세로 0번 반복중입니다. 2번 반복중입니다. 4번 반복중입니다.

#for i in range(0, 30, 1):
 #   print(i)   # 세로 0 1 2 ... 29

#for i in range(0, 11, 1):
 #   print(i, end=' ')   # 0 1 2 3 4 ... 9 10

#for i in range(0, 11, 1):
 #   print(i, end='hi')   #0hi1hi2hi...10hi

#res = 0

#for i in range(1001, 2000, 2):
 #   res += i
#print(res)
# 0 + 1001 + 1003 ... + 1999



#res = 0
#for i in range(1000, 2000, 1):
 #   if i % 2 == 1:
  #      res = res + i
#print(res)


# 1부터 키보드로 입력한 수까지의 합계 구하기
#i = 0
#res = 0
#num = 0

#num = int(input("숫자를 입력해주세요. : "))

#for i in range(1, num + 1, 1):
 #   res = res + i
#print("1부터 %d 까지의 합은 %d 입니다.\n" %(num, res))


#구구단

#i, dan = 0, 0
#dan = int(input("구구단 몇단? "))
#for i in range(1, 10, 1):
 #   print("%d x %d = %d" %(dan, i, dan*i))


# 전체 구구단
#for i in range(2, 10, 1):
 #   for j in range(1, 10, 1):
  #      print("%d x %d = %d" % (i, j, i*j))
   # print("%d단 끝났습니다." %i)
#print("끝")


#i = 0
#while i < 7:
 #   print(i)
  #  i = i + 1     # 세로로 0 1 2 3 4 5 6


#res= 0
#i = 0
#while i < 7:
 #   print(i)
  #  i += 1
   # if res > 40 : break   # 세로로 0 1 2 3 4 5 6


#while True :
 #   print("hello")
  #  break


#res = 0

#for i in range(1, 11, 1):
 #   res += i

  #  if res > 30 :
   #     print("처음으로 합이 30이 넘는 숫자는 = %d\n", i)
    #    break

#print(res)



# 예제 01

#for i in range(0, 5, 1):
 #   print("**********")


# 예제2

#i = 0
#while i < 5:
 #   print("*********")
  #  i += 1
  


# 예제 03

#for i in range(0, 6, 1):
 # if i == 0 or i == 5:
  #  print("********")
  #else:
   # print("*      *")


# 예제 04

#for i in range(0, 31, 1):
 # if i % 3 == 0:
  #  print(i)

#for i in range(3, 31, 3):
 # print(i)

# 예제 05

sum = 0
for i in range(1, 101, 1):
  sum += i  #sum = sum + i
print(sum)


i = 1
sum = 0

while i <= 100:
  sum += i
  i += 1

print(sum) 


# 예제 06

i = 0

while True:
  if i % 9 == 0 and i % 10 == 6:
    print(i)
    break
  else:
    i += 1


for i in range(1, 100000, 1):
  if i % 9 == 0 and i % 10 == 6:
    print(i)
    break









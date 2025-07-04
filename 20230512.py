# 1번

#n = int(input("자연수를 입력하시오: "))
#x = 0

##def solution(n):
 #   if n**(0.5): #답 다 못씀 
  ## else: 
    #    return 2


# 2번
#num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#numbers = list(map(int, input().split()))
#a = num.remove(numbers)

#result = sum(a)

#print(result)


# 3번

#def factorial(n):
#    output = 1
#    for i in range(1, n+1):
#        output* = i 

#print("5!: ", factorial(5))


# 4번

#i = 0 
#n = int(input("정수를 입력: "))

###  for i in range(0, n+1):
#        sum(i)

#print ("0 to ", n, ": ", hap(n))


# 5번 
#i = 0
#list = []
#x= 0 


#def solution(x, n):
   # global x
##           x += x
  ##3            break
     #       print(list)

#print(solution(2, 5))



# 6번 

S = [1,3,4,8,13,17,20]
x = 0
d = []
a = []
b = []

def solution(S):
     d = []
     a = []
     b = []
for i in range (0, len(S), 1):
    for k in range(i+1, len(x), 1):
     d.append(abs(x[i]**2-x[k]**2))
     a.append(x[i])
     b.append(x[k])

    
res = min(d)
print()


x = int(input("숫자를 입력해주세요: "))           

if x < 0 : print("0보다 큰 숫자를 입력해주세요: ")
else:
    if x % 2 == 0: 
        print("짝수 입니다")
    else: 
        print("홀수 입니다")



score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



age = int(input("고객님의 나이를 입력해 주세요: "))

if age >= 60:
    print("고객님의 연령대는 60대 이상 입니다.")
elif age >= 50:
    print("고객님의 연령대는 50대 입니다.")
elif age >= 40:
    print("고객님의 연령대는 40대 입니다.")
elif age >= 30:
    print("고객님의 연령대는 30대 입니다.")
elif age >= 20:
    print("고객님의 연령대는 20대 입니다.")
elif age >= 10:
    print("고객님의 연령대는 10대 입니다.")
else: 
    print("고객님의 연령대는 10대 이하 입니다.")



a = int(input("숫자 a를 입력하세요: "))
b = int(input("숫자 b를 입력하세요: "))

if a > b: print(">")
elif a < b: print("<")
else: print("=")



def Quadrant(x=0,y=0):          # 함수 def로 만들기  # (x,y)해도 되는데 초기값을 설정한것, y자리가 비어있을 때 그때를 생각해 초기값을 써준것
    
    if x > 0 and y > 0 : print("1")
    elif x < 0 and y > 0 : print("2")
    elif x < 0 and y < 0 : print("3")
    elif x > 0 and y < 0 : print("4")
    else : print("-1")

Quadrant(12,-5)   #4
Quadrant(30)      #-1

#x = int(input("x 값을 입력하세요: "))  # 위에 def함수 x, y입력 어떻게 받지???ㅠㅠ
#y = int(input("y 값을 입력하세요: "))



sum = 0   #더하기의 초기값은 0

for i in range(11):
    sum += i

print(sum)    #55



mul = 1    #곱하기의 초기값은 1

for i in range(1,11):
    mul *= i

print(mul)   #3628800



sum = 0

a = str(3**79)

for i in str(3**79):              # 각 자리 합을 구하는 코드라 3의 79승을 문자열로 바꿔주고 더해지게
    sum += int(i)       #더할땐 다시 숫자로 더해지게

print(sum)    #189



for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d"%(i, j, i*j))



#number = int(input("게임 최대 숫자를 입력해 주세요: "))

number = 33    #그냥 이 문제 33로 고정했을 뿐
count = 0

for i in range(1, number + 1):
    for j in str(i):                       #33 -> 3 / 3     3이 2개   그래서 문자열로
        if j == "3" or j =="6" or j =="9": 
            count += 1

print(count)         #14



sum = 0
i = 1

while i < 11:
    sum += i
    i += 1



# p.13

i = 0

while i < 5:
    print("*" * 10)
    i += 1



for i in range(5):
    print("*" * 10)



i = 6

while i > 0:
    print((str(i) + " ") * i)
    i -= 1



for i in range(6, 0, -1):
    print((str(i) + " ") * i)



#p.14

number = 25

answer = int(input("숫자를 입력하세요: "))

while number != answer:
    if answer < number : print("up")
    elif answer > number : print("down")
    
# answer == number: print("정답")  여기 정답 while문 나와서 출력하는 방법 모르겠음 여기 코드 전체



#p.16



#p.18 
# 짝수 개수 출력 












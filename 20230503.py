# 1번 

apart = [ [101, 102], [201, 202], [301, 302] ]

for floor in apart:
    for room in floor:
        print(str(room) + "호")


# 2번

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
print("학점입니다.")


# 3번

N = int(input("입력: "))

for i in range(1, 2*N):
    if i <= N:
        print(("*" * (2*i-1)).center(2*N-1))
    else:
        print(("*" * (2*(2*N-i)-1)).center(2*N-1))

    
# 4번 

count = 0

for i in range(10000):
    if '8' not in str(i):
        count += 1

print(count)


# 5번

count = 0

for i in range(1, 101):
    count += str(i).count('8')

print(count)


# 6번

n = int(input("정수를 입력하세요: "))
result = ""

while n > 0:
    remainder = n % 2
    result = str(remainder) + result
    n = n // 2

print("2진수 변환 결과: ", result)
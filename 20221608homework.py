## 1. 교과목 정보 출력 ##
#### coding here ####


from ast import Num
from cgi import print_exception


subjectnum = input("학수번호를 입력하세요: ")
if subjectnum == "데사B0001":
    print("입력하신 과목은 데이터사이언스를위한수학 이며, 강의실은 숭의관 1호 입니다.")
elif subjectnum == "문화A0019":
    print("입력하신 과목은 파이썬프로그래밍 이며, 강의실은 인문관 15호 입니다.") 
elif subjectnum == "문화A0007":
    print("입력하신 과목은 데이터사이언스입문 이며, 강의실은 대학원 4호 입니다.")
else:
    print("입력하신 과목은 정보에 없습니다.")
    

## 2. 숫자 맞추기 게임 ##
#answer = 25
#### coding here ####


while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 25 :
        print("정답!")
        break
    elif num < 25 :
        print("UP!")
    elif num > 25 :
       print("DOWN!")


## 3. 물건 값 계산하기 ##
#### coding here ####


a = int(input("물품A를 몇 개 구매 하시겠습니까?"))
b = int(input("물품B를 몇 개 구매 하시겠습니까?"))
c = int(input("물품C를 몇 개 구매 하시겠습니까?"))
d = int(input("물품D를 몇 개 구매 하시겠습니까?"))
e = int(input("물품E를 몇 개 구매 하시겠습니까?"))

print("총 구매하신 항목은 A %d개 B %d개 C %d개 D %d개 E %d개 입니다." %(a, b, c, d, e))

coupon = input("할인 쿠폰을 입력해주세요 : ")

price = 3000 * a + 25000 * b + 1600 * c + 18000 * d + 2600 * e 

if coupon == "A37B2QD":
    pay = price * 0.90
elif coupon == "D8TY41M":
    pay = price * 0.95
elif coupon == "9PBX8UY":
    pay = price * 0.85
else:
    pay = price

print("주문하신 총 금액은 %d원 입니다." %(pay))


## 4. 소수 여부 판단하기 ##
#### coding here ####


num = int(input("숫자를 입력하세요 : "))

if num <= 0:
        print("자연수를 입력하세요.")

if num == 1:
    print("소수가 아닙니다.")

if num == 2:
    print("소수입니다.")
    print("종료합니다.")
      
for i in range (2, num):
    if num % i == 0 :
        print("소수가 아닙니다.")
        break
    else:
        print("소수입니다.")
        print("종료합니다.")
        break    
    

## 5. 리스트 데이터 확인 ##
# answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

#### coding here ####


answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = ['hello', 62, 'umbrella', 145]
B = ['September', 512.3, 'coffee', 39, 'keyboard', 'notebook', 0.5, 'f12']
C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']


a = input("리스트를 입력하세요: ")

if a != A and a != B and a != C:
    print('리스트에 없습니다.')

for i in range(0, len(a)) :
    if a[i] == 'apple' or 39 or 'music' or 568.2 or 'Dongduk' or 145 or 'hello':
        a[i] = 'O'
    else:
        a[i] = 'X'
        
print(range(0, len(a)), end = '')
a = input("리스트를 입력하세요: ")



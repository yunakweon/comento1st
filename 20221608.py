## 1. 약수 구하는 함수 ##
n = int(input("자연수를 입력해주세요: "))

def divisor(n):
    divisor = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i) 
    return divisor
    
print(divisor(n))

#print(divisor(10))
#print(divisor(7))


## 2. 수도 출력 ##
capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}
country = capital.values()

n = str(input("나라를 입력하세요: "))
    
def find_capitalcity(capital, country):
    capital = capital.keys()
    country = capital.values()

    if n in capital:
        print(capital.values(n))
    else:
        print("해당사항이 없습니다.")

#print(find_capitalcity(capital, "대한민국"))
#print(find_capitalcity(capital, "덴마크"))
#print(find_capitalcity(capital, "일본"))


## 3. 파일쓰기 ##
#### coding here ####

import random

name1 = "mid_test.txt"

f1 = open(name1, 'w')

for i in range(50):
    score = random.randint(0, 100)
    f1.write(str(score) + '\n')
  
f1.close()


name2 = "final_test.txt"

f2 = open(name2, 'w')

for i in range(50):
    score = random.randint(0, 100)
    f2.write(str(score) + '\n')
  
f2.close()


name3 = "homework.txt"

f3 = open(name3, 'w')

for i in range(50):
    score = random.randint(0, 20)
    f3.write(str(score) + '\n')
  
f3.close()


name4 = "attendance.txt"

f4 = open(name4, 'w')

for i in range(50):
    score = random.randint(0, 10)
    f4.write(str(score) + '\n')
  
f4.close()


## 4. 파일 읽기 ##
def center(list):
    ## coding here ##
    pass


score = []

#### coding here ####

print(center(score)) # 1등 점수


## 5. 클래스 만들기 ##

class Student_DD:
   name = ""
   major = ""
   grade = 0
   phonenumber = ""

   def __init__(self, value1, value2, value3, value4):
       self.name = value1
       self.major = value2
       self.grade = value3
       self.phonenumber = value4

   def introduce(self):
        print("안녕하세요. 저의 이름은 {}, {} 전공, {}학년이며, 연락처는 {}입니다".format(self.name, self.major, self.grade, self.phonenumber))

student1 = Student_DD("정영희", "데사", "1", "010-1234-5678")
student1.introduce()
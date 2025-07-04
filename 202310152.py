### 2주차 ###

number = int(input("0보다 큰 숫자를 하나 입력하세요: "))

if number < 0:
    print("0보다 큰 숫자를 입력하세요.")
elif number % 2 == 0:
    print("짝수 입니다")
else:
    print("홀수 입니다")


score = int(input("점수를 입력하세요: "))

if score >= 90: print("A")
elif score >= 80: print("B")
elif score >= 70: print("C")
elif score >= 60: print("D")
else: print("F")

print("학점입니다.")



age = int(input("고객님의 나이를 입력해 주세요: "))

if age >= 60: print("고객님의 연령대는 60대 이상 입니다.")
elif age >= 50: print("고객님의 연령대는 50대 입니다.")
elif age >= 40: print("고객님의 연령대는 40대 입니다.")
elif age >= 30: print("고객님의 연령대는 30대 입니다.")
elif age >= 20: print("고객님의 연령대는 20대 입니다.")
elif age >= 10: print("고객님의 연령대는 10대 입니다.")
else: print("고객님의 연령대는 10대 미만입니다.")



a = int(input("정수 a를 입력: "))
b = int(input("정수 b를 입력: "))

if a > b: print(">")
elif a < b: print("<")
else: print("=")



# 이건 내가 푼거...
x = int(input("실수 x를 입력: "))
y = int(input("실수 y를 입력: "))

if x > 0 and y > 0: print("1")
elif x < 0 and y > 0: print("2")
elif x < 0 and y < 0: print("3")
elif x > 0 and y < 0: print("4")
else: print("-1")



def Quadarant(x, y):

    if x > 0 and y > 0: print("1")
    elif x < 0 and y > 0: print("2")
    elif x < 0 and y < 0: print("3")
    elif x > 0 and y < 0: print("4")
    else: print("-1")


Quadarant(12, 3)
# Quadarant(30)           # 여기선 초기값을 설정안했기 때문에 30만 입력하면 오류가 남


def Quadarant(x=0, y=0):

    if x > 0 and y > 0: print("1")
    elif x < 0 and y > 0: print("2")
    elif x < 0 and y < 0: print("3")
    elif x > 0 and y < 0: print("4")
    else: print("-1")


Quadarant(12, 3)
Quadarant(30)          # -1, 초기값을 줬기때문에 숫자를 하나만 넣었지만 x = 30으로 y는 초기값인 0으로 들어감



sum = 0       # 더하기는 초기값이 0

for i in range(11):
    sum += i

print(sum)        # 55



mul = 1       # 곱하기는 초기값이 1

for i in range(1, 11):
    mul *= i

print(mul)



sum = 0

a = "김태완"

for i in a:
    print(i)

print(sum)      # 김 태 완 한줄씩 총 3줄로 나옴



sum = 0

a = str(3**79)         # 문자열로 만들어서 시작

for i in a:
    sum += int(i)       # 이때만 잠시 숫자로 만들어서 더함, 더할 떄는 문자열로 못 더하니까

print(sum)              # 189



for i in range(2, 10):
    for j in range(1, 10):
        print("%d X %d = %d"%(i, j, i*j))



number = int(input("게임 최대 숫자를 입력해 주세요: "))
count = 0       # 박수 수
                # 33 -> 3 / 3

for i in range(1, number+1):
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            count += 1

print(count)



sum = 0
i = 1

while i < 11:
    sum += i
    i += 1

print(sum)    # 55



for i in range(5):
    print("*"*10)


i = 0

while i < 5:
    print("*"*10)
    i += 1



# 내가 푼 방법
for i in range(6, 0, -1):
    print("%d "%(i)*i)


i = 6

while i > 0:
    print(("%d "%(i))*i)
    i -= 1


# 교수님이 푼거 print 안의 식이 다름 
 
for i in range(6, 0, -1):
    print((str(i) + " ")*i)



for i in range(7):
    print((str(6-i) + " ") * (6-i))



answer = int(input("숫자를 입력하세요: "))
number = 25

while number != answer:
    if answer > number: print("DOWN!")
    elif answer < number: print("UP!")
    answer = int(input("숫자를 입력하세요: "))
print("정답!")



i = 1

while i <= 30:
    if i % 2 == 0 or i % 3 == 0:
        i += 1
        continue
    else:
        print(i)
        i += 1


a = [1, 5, 10, 7, 0]
count = 0

for i in a:
    if i % 2 == 0:
        count += 1

print(count)





### 3주차 ###


a = [1, 11, 80, 24, 67, 32, 19, 24, 88]
res = 0

for i in a:
    if i % 2 == 0:
        res += 1

print(res)       # a 리스트 안에 있는 짝수 개수 구하기 



score = [71, 55, 24, 73, 68, 90]
n = 0

for i in score:
    n += 1
    if i >= 70:
        print("%d번 학생 %d점 합격"%(n, i))



value = [90, 70, 22, 78]
sum = 0

for i in value:
    sum += i

average = sum/ len(value)

print(average)



a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']

for i in a:
    if len(i) == 5:
        print(i, end = ' ')             #alpha bravo delta hotel india
 


a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']
b = ''

for i in a:
    if len(i) == 5:
        b += i + ' '         

print(b)                    #alpha bravo delta hotel india



a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']
b = ['alpha', 'bravo']

for i in a:
    if i in b:
        print("yes")    # 그냥 얜 설명하기 위한거 한단어 한줄에 앞에 두개는 단어 대신 yes 출력됨
    else : print(i)



answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = ['hello', 62, 'umbrella', 145]
B = ['September', 512.3, 'coffee', 39, 'keyboard', 'notebook', 0.5, 'f12']
C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

x = input("리스트를 입력하세요: ")

if x == 'A':
    for i in A:
        if i in answer: print('O', end = '')
        else: print('X', end = '')
elif x == 'B':
    for i in B:
        if i in answer: print('O', end = '')
        else: print('X', end = '')
elif x == 'C':
    for i in C:
        if i in answer: print('O', end = '')
        else: print('X', end = '')    
else: print("리스트에 없습니다.")
    


for i in A:
    if i not in answer: print('X', end = '')
    else: print('O', end = '')          # 위에 것을 반대로 not in을 이용해서도 만들 수 있음



visit = ['영국', '일본', '미국', '프랑스', '폴란드', '칠레', '캐나다', '이탈리아']
wish = ['브라질', '독일', '캐나다', '호주', '영국']
result = []

for i in wish:
    if i in visit:
        result.append(i)

print(result)



def how_many(a, b):
    count = 0
    for i in a:
        if i == b:
            count += 1
    
    return count

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]
print(how_many(x,3))        #5
print(how_many(x,5))        #2



def bigger_than(a, b):
    count = 0
    for i in a:
        if i > b:
            count += 1
    return(count)


x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]
print(bigger_than(x,4))        #8
print(bigger_than(x,5))        #6



student = [12,18,3,20,14,5,1,9,10,11,6,2,17,16,4,15,8]

for i in range(1, 21):
    if i not in student: print(i, end = ' ')      #7 13 19



# 나라 이름이 3글자인 국가의 수도 같이 출력
capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이", "덴마크":"코펜하겐"}

for i in capital:
    if len(i) == 3:      
        print("%s의 수도는 %s입니다."%(i, capital[i]))



score = {'국어': 90, '영어':95, '수학':77, '미술':68, '과학': 82}

sum = 0
average = 0.0

for i in score:
    sum += score[i]

average = sum / len(score)

print("전체 평균은 %f 입니다."%average)      # %d하면 소숫점이 안나오니까 %f 해야함, 피피티는 오류임

#  현제 %f 일때는 82.400000 이고, %.1f 하면 82.4로 소숫점 첫째자리까지만 나오고, %d 를 하면 84 까지만 나온다



a = {'a':1, "b":2, "c":3}

for i in a:
    print(i, a[i])    #a 1 다음줄에 b 1 다음줄에 c 1 출력


for i in a.keys():
    print(i, a[i])    # 위에랑 출력값 같음, 위에꺼가 더 편함


for k, v in a.items():
    print(k, v)       # 얘도 똑같이 출력값 같음 



sum = 0 

for i in str(3**79):
    sum += int(i)

print(sum)



string = "apple"
alphabet = []

for i in string:
    if i not in alphabet:
        alphabet.append(i)

print(alphabet)     #['a', 'p', 'l', 'e']



a = '김태완/ 40/ datascience'

name = []
print(a.split('/'))     #['김태완', ' 40', ' datascience']



a = '김태완/40/datascience'

name = []
age = []

name.append(a.split('/')[0])
age.append(a.split('/')[1])

if a.split('/')[1] == '': print("")    # 나이가 공백일 경우 대비

print(name)   #['김태완']
print(age)    #['40']



# 여기 사이 강의안 내용 보기



word ='나는 공부가 너무 재미있어서 공부도 공부만 하고 싶어요'
print(word.split())      #['나는', '공부가', '너무', '재미있어서', '공부도', '공부 만', '하고', '싶어요']



word = '하나:둘:셋'
print(word.split(':'))   #['하나', '둘', '셋']



f = open("aaa.txt", 'w')
data = ['김태완', '40', 'datascience']

data_join = '/'.join(data)
f.write(data_join + '\n')
f.close()          # aaa.txt 메모장에 김태완/40/datascience라고 입력됨



data = ['A', 'B', 'C', 'D', 'E']
data_join = '-'.join(data)
print(data_join)               #A-B-C-D-E



#sentence = input("영문자열을 입력하세요: ")
sentence = 'school'

res = sentence[0] + sentence[-1]

print(res)       #sl



phone_number = '010-1234-5678'

modified_number = phone_number.replace('-','')

print(modified_number)           #01012345678



## 여기서부턴 함수 파트 (3주차 강의자료) ##

def plus(*param):
    sum = 0
    for i in param:
        sum += i
    return sum

hap = 0
hap = plus(100, 200, 300, 400)
print(hap)



def taewan():
    a = 1
    b = 2
    c = 0
    return a, b, c

x, y, z = taewan()    # 입력 값도 없고 반환 값도 없는 함수



def start():
    print("hello")

start()       #hello   # 입력 값은 없고 반환 값은 있는 경우



def star(number):
    for i in range(number):
        print('*'*number)

num = int(input("0보다 큰 숫자 입력: "))
star(num)



def star(number):
    i = 0
    while i < number:
        print('*'*number)
        i += 1

num = int(input("0보다 큰 숫자 입력: "))
star(num)
##### 2023-2학기 데이터마이닝이해와실습 (데사B0002 중간고사) #####

# ----------------------------------------------------------------------------------------------------------
# 다음과 같은 행위를 부정행위로 간주하며, 온라인 시험 부정행위에 대해서는 관련자 모두를 0점(F)처리하고 학칙에 따라 징계처분 될 수 있으니 유념하시기 바랍니다.
# (1) 대리시험을 치르는 행위
# (2) 시험 중 문제나 답안을 전화, SNS, 단톡방, 문제풀이 사이트 등을 통해 공유하는 행위
# (3) 시험도중 시험화면을 이탈하거나 특수키(Ctrl, Alt, Window key 등) 사용, 다른 프로그램을 사용하는 행위
# (4) 동일 장소 내에서 동일한 IP Address를 사용하는 행위
# (5) 중복 로그인(하나의 ID로 두 개 이상의 컴퓨터에서 동시접속)하는 행위
# (6) 마우스 커서가 시험 응시화면에서 이탈되는 경우
# (7) 오픈북 시험이 아닌데 교재나 시험관련 자료를 펴놓고 시험을 보는 행위
# ----------------------------------------------------------------------------------------------------------

# 본인은 온라인 시험 관련 모든 유의사항을 확인하였고 부정행위를 하지 않을 것이며, 부정행위를 하였을 경우에는 0점(F학점)을 감수하며 학칙에 따른 징계절차에 따르겠습니다.
# 위의 사항에 동의할 경우 아래 대답에 "동의합니다" 라고 작성해 주십시오.

##### 대답 : 동의합니다
##### 학번 : 20221608
##### 이름 : 권유나




##### 1번 문제 #####
# num = int(input("*의 개수를 입력 :"))

## for문으로 구현 ##
## coding here ##

num = int(input("*의 개수를 입력 : "))

for i in range(num, 0, -1):
    print("*"*i)


## while문으로 구현 ##
## coding here ##

num = int(input("*의 개수를 입력 : "))

while num > 0:
    print("*"*num)
    num -= 1




##### 2번 문제 #####

fw.open("foods.txt", 'w')

foods = {"떡볶이":"김밥", "자장면":"단무지","라면":"파김치","치킨":"맥주","삼겹살":"소주"}

## coding here ##

for i in foods:
    a = "%s+%s"%(foods.keys(i), foods.values(i))
    fw.write(a.split())

fw.close()




##### 3번 문제 #####
import numpy as np
 
def find_number(array, i, j, k):
    ## coding here ##

    q = np.array[i:j]
    w = sort(q) 
    e = q[k]

a = np.array([1, 5, 2, 6, 3, 7, 4])
print(find_number(a, 2, 5, 3))



##### 4번 문제 #####

n1 = int(input('첫 번째 숫자를 입력하세요.'))
n2 = int(input('두 번째 숫자를 입력하세요.'))

## coding here ##

sum = 0

for i in range(n1, n2+1, 1):
    sum += i

print(sum)



##### 5번 문제 #####

def count_space(k):
    ## coding here ##

    count = 0

    a = k.split()

    for i in a:
        if i == ' ':
            count += 1

    return count

sentence = 'Python is powerful and interesting for me.'
num = count_space(sentence)
print('빈칸의 개수 : ', num)



##### 6번 문제 #####
from pandas import DataFrame

## coding here ##

def DataFrame(a, b):
    Andy = {"age":23, "grade":"A+, "major":"Art"}
    Jane = {"Age":21, "grade":"B-", "major":"Datascience"}
    Chris = {"age":24, "grade":"A", "major":"Music"}
    Som = {"age":22, "grade":"B", "major":"History"}


    DataFrame([Andy, Jane, Chris, Som])

    print(DataFrame.iloc([[0,3],[0,2]]))





df = DataFrame(a,b)

## coding here ##

print(df())




##### 7번 문제 #####

## coding here ##

DataFrame.iloc[0] = "나이"
DataFrame.iloc[1] = "학점"
DataFrame.iloc[2] = "전공"


df2 = DataFrame.iloc([[0,1,3],[:]])

print(df2)

## coding here ##

DataFrame[1,2] = "데이터사이언스"

df3 = DataFrame.iloc([[0,1,3],[0,2]])

print(df3)
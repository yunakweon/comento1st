#p.18
a = [1, 11, 80, 24, 67, 32, 19, 24, 88]
res = 0

for i in a:
    if i % 2 == 0:
        res += 1
        print(res)



#p.19

score = [71, 55, 24, 73, 68, 90]
n = 0

for i in score:
    n += 1
    if i > 70:
        print("%d번 학생 %d점 합격"%(n, i))
        


#p.20

value = [80, 75, 91, 47, 100, 5, 26]
sum = 0

for i in value:
    sum += i 

average = sum / len(value)
print(average)



#p.21

#a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 
#'foxtrot', 'golf', 'cat', 'school' 'hotel', 'india']
#b = []

#for i in a:
#    if len(i) == 5:
        # 여기 줄 못씀 
        
#print(b)



#p.22

answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = ['hello', 62, 'umbrella', 145]
B = ['September', 512.3, 'coffee', 39, 'keyboard', 'notebook', 0.5, 'f12']
C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

for i in A:
    if i in answer:
        print("O", end ='')
    elif i not in answer:
        print("X", end = '')


# 이 코드 맞나 확인해보기
x = input("리스트를 입력: ")

if x == 'A':
    for i in A:
        if i in answer: print("O", end ='')
        elif i not in answer: print("X", end = '')
if x == 'B':
    for i in B:
        if i in answer: print("O", end ='')
        elif i not in answer: print("X", end = '')
if x == 'C':
    for i in C:
        if i in answer: print("O", end ='')
        elif i not in answer: print("X", end = '')
else: print("리스트에 없습니다")



# 바꿔서 not in O X 프린트하는 설명쓰기



#p.23

visit = ['영국','일본','미국','프랑스','폴란드','칠레','캐나다','이탈리아']
wish = ['브라질', '독일', '캐나다', '호주', '영국']
result = []

for i in wish:
    if i in visit:
        result.append(i)

print(result)



#p.24

def how_many(a,b):
    cnt = 0               #cnt는 count 대신 간단히 작성하신듯 
    for i in a:
        if i == b:
            cnt += 1
    return cnt     # 리턴 위치 맞나? 띄어쓰기


x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]

print(how_many(x,3))
print(how_many(x,5))



def bigger_than(a,b):
    count = 0
    for i in a:
        if i > b:
            count +=1
    return count

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]

print(bigger_than(x,4))
print(bigger_than(x,5))



#p.26

student = [12,18,3,20,14,5,1,9,10,11,6,2,17,16,4,15,8]

for i in range(1, 21):
    if i not in student: print(i, end = ' ')

#7 13 19



#p.27

capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", 
"영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}

for i in capital:
    if len(i) == 3:
        print('%s의 수도는 %s 입니다.'%(i, capital[i]))

#프랑스의 수도는 파리 입니다.
#스위스의 수도는 베른 입니다.
#베트남의 수도는 하노이 입니다.
#덴마크의 수도는 코펜하겐 입니다.



#p.28

score = {'국어': 90, '영어':95,'수학':77, '미술':68, '과학': 82}

sum = 0
average = 0.0

for i in score:
    sum += score[i]

print("%s 과목의 점수는 %d 입니다."%(i, score[i]))

average = sum/len(score)

print("전체 평균은 %d 입니다."%average)   # 여기 코드 맞나 영상 확인하기



#p.29

Professor = {'학번': '20231234' , '이름':'김태완', '부서':'데이터사이언스전공'}

for key in Professor.keys():
    print(key, Professor[key])

for k,v in Professor.items():
    print(k,v)

# for문 두개 출력 같음 



#p.31

string = "apple"
alphabet = []

for i in string:
    if i not in alphabet:
        alphabet.append(i) 

print(alphabet)



word = ' 나는 공부가 너무 재미있어서 공부도 공부만 하고 싶어요 '
print(word.strip())


word = '나는 공부가 너무 재미있어서 공부도 공부만 하고 싶어요'
print(word.replace('공부','운동'))
#나는 운동가 너무 재미있어서 운동도 운동만 하고 싶어요


word = '나는 공부가 너무 재미있어서 공부도 공부만 하고 싶어요'
print(word.split())
#['나는', '공부가', '너무', '재미있어서', '공부도', '공부만', '하고', '싶어요']


word = '하나:둘:셋'
print(word.split(':'))
#['하나', '둘', '셋']


data = ['A', 'B', 'C', 'D', 'E']
data_join = '-'.join(data)
print(data_join)
#A-B-C-D-E



#p.34

sentence = input("영문자열을 입력하세요: ")
res = sentence[0] + sentence[-1]
print(res)



#p.35

phone_number = input("당신의 휴대폰 번호를 입력해 주세요.")
modified_number = phone_number.replace('-','')
print(modified_number)



#p.15

def star(number):
    for i in range number:







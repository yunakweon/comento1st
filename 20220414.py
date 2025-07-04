from cgi import print_environ


A = {'학번': '20221234', '이름': '권유나', '부서': '데사'}

#print(A)  # {'학번': '20221234, '이름': '권유나' ... }
 
print(A['이름'])     #권유나

A['나이'] = 39
A['전화번호'] = '010-1234-1234'  #추가는 되는데 순서가 입력한 순서대로 나오진 않는다. 하지만 짝은 맞춰서 나온다.

print(A)


list_A = ['apple', 347, 'kim', 1391]
list_A[3] = 'banana'     ###맞나??????????

print(list_A)


A = {'학번': '20221234', '이름': '권유나', '부서': '데사'}

del(A['부서'])       #두 세트 짝 같이 없어짐

print(A.key())   #dict_keys(['학번', '이름', '부서'])
print(A.get('부서'))   # 데사


for i in list(A.values()):
    print(i)


print('학수번호' in A)   #False

for i in A.keys():
    print(i, A[i])    



# 예제 02

ICECREAM = {'메로나': [1000, 32], '비비빅': [900, 25], '죠스바': [1100, 8]}

print(ICECREAM['메로나'][0])        #앞에꺼 출력하라는 의미, 900원이 출력됨, 가격이 출력


foods = {"떡볶이":"김밥", "짜장면": "단무지", "라면": "파김치", "치킨": "맥주", "삼겹살": "소주"}

food_name = input(str(list(foods.keys()))) + '중 좋아하는 음식은?'       #["떡볶이", "짜장면", "라면", "치킨", "삼겹살"]중 좋아하는 음식은?

print(food_name + "궁합 음식은" + foods[food_name] + "입니다.")


# 예제 04

dans = (2, 3, 4, 5, 6, 7, 8, 9)
print('구구단표')
print('-'*30)

for dan in dans :
    for i in range(1,10):
        print('%d x %d = %d' %(dan, i, dans*i))
#답: 1) dan 2)dans 3)i

# 예제 05

admin_info = ['admin', '12345', 'kimtwan21@dongduk.ac.kr']     #메일은 페이크, 사용되지 않았다.

id = input("관리자 아이디를 입력하세요 : ")
password = input("관리자 비밀번호를 입력하세요 : ")

if id ==  admin_info[0] and password == admin_info[1]:
    print("관리자입니다.")
else :
    print("아이디 또는 비밀번호가 잘못 입력되었습니다.")


# 예제 06  

scores = {'김예진': 90, '박영진': 95, '김소희': 84}
sum = 0

for key in scores:
    sum += scores[key]
    print('%s : %d' % (key ,scores[key]))

avg = sum/len(scores)

print('합계: %d, 평균 : %d.2f' % (sum, avg))


# 문제 07

words = {'사과': 'apple', '컴퓨터': 'computer', '학교': 'school', '책상': 'desk', '의자': 'chair'}

for key in words.keys():
    answer = input(key + "에 해당되는 영어 단어를 입력해주세요 : ")
    if answer == words[i]: 
        print("정답입니다 !")
    else :
        print("틀렸습니다 !")




word = 'python'
print(word[3])   #h
for i in word:
    print(i, end=' ')


a = 'hello eVryOne'
b = '12345'

#print(a.islower())
#print(b,isdigit())


word = '공부가 너무 재미있어서 공부도 공부만 하고 싶어요'
print(word.count('공부'))
print(word.find('너무'))   #전체에서 찾는다
print(word.find('너무',3))   #3에서(3번째거부터랬나?????????) 부터 찾는다
print(word.find('너무',3,9))       #3에서 9까지 찾는다
print(word.rfind('공부'))       #오른쪽부터 찾기
print(word.index('권유나'))       #에러가 난다. 없기 때문에.
word2 = word.replace('공부', '먹는거')
print(word2)


a = ['apple', 'banana']

print(a.index('banana'))


word = '하나:둘:셋'
word2 = word.split() #다못씀......


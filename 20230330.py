# 예제 01

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

a = [1, 2, 3]
b = [4, 5, 6, 7]
c = [8,9]

a.extend(b)
a.extend(c)

for i in a:
    print(i)


# 예제 02

str_input = input("태어난 해를 입력해주세요: ")

birth_year = int(str_input)

if birth_year % 12 == 0:
    print("원숭이 띠입니다.")
elif birth_year % 12 == 1:
    print("닭 띠입니다.")
elif birth_year % 12 == 2:
    print("개 띠입니다.")
elif birth_year % 12 == 3:
    print("돼지 띠입니다.")
elif birth_year % 12 == 4:
    print("쥐 띠입니다.")
elif birth_year % 12 == 5:
    print("소 띠입니다.")
elif birth_year % 12 == 6:
    print("호랑이 띠입니다.")
elif birth_year % 12 == 7:
    print("토끼 띠입니다.")
elif birth_year % 12 == 8:
    print("용 띠입니다.")
elif birth_year % 12 == 9:
    print("뱀 띠입니다.")
elif birth_year % 12 == 10:
    print("말 띠입니다.")
elif birth_year % 12 == 11:
    print("양 띠입니다.")


# 예제 03

startnum = input("시작값을 입력하시오: ")
endnum = input("끝값을 입력하시오: ")
plusnum = input("증가값을 입력하시오: ")

if startnum + endnum * i > plusnum:
    print()

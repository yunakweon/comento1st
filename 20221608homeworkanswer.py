# 4

number = int(input("숫자를 입력하세요: "))
check = 0

while check == 0 :
    check = 1
    number = int(input("숫자를 입력하세요: "))

    if number <= 0 :
        print("자연수를 입력하세요")
        check = 0
        continue
    elif number == 1:
        print("소수가 아닙니다")
        check = 0
        continue
    else :
        for i in range(2, number):
            if number % i == 0:
                print("소수가 아닙니다.")
                check = 0
                break

    if check == 1 :
        print("소수입니다.")
        print("종료합니다.")
        break
print("종료")



# 5

answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = ['hello', 62, 'umbrella', 145]
B = ['September', 512.3, 'coffee', 39, 'keyboard', 'notebook', 0.5, 'f12']
C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']


list_name = input("리스트를 입력하세요 : ")

if list_name == 'A' :
    for i in A : 
        if i in answer :
            print("O", end='')
        else : print("X", end='')

elif list_name == 'B' :
    for i in B : 
        if i in answer :
            print("O", end='')
        else : print("X", end='')

elif list_name == 'C' : 
    for i in C : 
        if i in answer :
            print("O", end='')
        else : print("X", end='')

else : 
    print("리스트에 없습니다.")
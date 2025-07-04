#문제 01

str_input = input("원의 반지름 입력>")
num_input = float(str_input)
print()
print("반지름:", num_input)
print("둘레:", 2*3.14*num_input)
print("넓이:", 3.14*num_input**2)


#문제 02 

A = int(input("정수 A를 입력하시오 => "))
B = int(input("정수 B를 입력하시오 => "))

result = A + B
print(result)


#문제 03

for _ in range(int(input())):
    s = input()
    print(s[0] + s[-1])


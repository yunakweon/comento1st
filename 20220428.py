def calculate_plus(a, b):
    c = a + b
    return c

hap = calculate_plus(100, 150)
hap2 = calculate_plus(500, 350)

print(hap)
print(hap2)


def hap(name):
    print(name, "님, 두 숫자를 입력하세요")
    num1 = int(input("숫자 1 입력해주세요"))
    num2 = int(input("숫자 2 입력해주세요"))

    result = num1 + num2
    print("결과 : ", result)


def calculate_sum(x1, x2, x3, x4 = 0):
    result = x1 + x2 + x3 + x4

    return result

y = calculate_sum(3, 5, 6, 7)
y2 = calculate_sum(3, 5, 6)

print(y2)             # 14


# 예제 05

def make_list(string):
    print(list(string))

    result = []
    for i in string:
        result.append(i)

    print(result)

make_list()  # 43, 44 다 제대로 못씀
make_list()
   

# 예제 06


# 예제 07


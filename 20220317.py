# ctrl + c -> 주석처리
# ctrl + u -> 주석처리 지워짐



a = 10
b = 2

#print(a/b)
print(a/b)
print(type(a/b))



# TERMINAL 아래 부분에  python 본인파일  을 쓰면 아래 파일이 뜸.



x = 100
y = 20

z1 = x + y   # = z_sum = x + y
z2 = x * y   # = z_mul = x * y
z3 = x ** y  # = z_square

print(z1,z2,z3)



x = 10
y = 2
z = 3

a = (x + y) + z   #당연한 부분 같아 보여도 보기 쉽게 암묵적으로 가로를 친다.



x = int(input("숫자를 입력하세요: "))
# x = int(input("숫자를 입력하세요: "))
# x = int(x)

y = x * 10
print(x, type(x))
print(y)


x = str(3)   # 숫자 3이 아니게 됨.
y = float(x * 2)

print(y)



##### coding here ####


weight = int(input("나의 체중은: "))   # weight = float(input("나의 체중은:"))
height = float(input("키는: "))   # m 단위!!
bmi = weight/ (height**2)

print("나의 체중은 ", weight, "kg, 키는 ", height, "m입니다.")
print("계산한 BMI 지수는 ", bmi)


a = 3
print(a)
a = a + 5
print(a)
a += 2
print(a)
a *= 5
print(a)



a = 10
a += 5; print(a)
a -= 5; print(a)
a *= 5; print(a)
a /= 5; print(a)
a //= 5; print(a)
a %= 5; print(a)
a **= 5; print(a)



#나눠지는 수 ==> 25
#나누는 수 ==> 10
#25을(를) 10으로 나눈 몫은 2 입니다.
#25을(를) 10으로 나눈 나머지는 5 입니다.

a = int(input("나눠지는 수: "))   # a = num1   
b = int(input("나누는 수: "))     # b = num2

c = a // b   # c = x
d = a % b    # d = y

print(a, "을(를) ", b, "으로 나눈 몫은 ", c, "입니다.")
print(a, "을(를)", b, "으로 나눈 나머지는 ", d, "입니다.")
#print(str(num1), "을(를)", str(num2), "으로 나눈 몫은", str(x) ...) 식으로 str붙여서 쓰는게 더 좋음.




a = 1
b = 2
c = a*b

print(a != b)
print(a > b)


name = "권유나"

if (name == "권유나"):
    print("권유나")

print("끝")    


a = 10
b = 20

if (a<b):
    print("b가 a보다 큽니다.")



if(10==100):
    print("맞습니다.")

if(10!=100):
    print("맞습니다.")

if(10<100):
    print("맞습니다.")

if(10>100): 
    print("맞습니다.")

if(10<=100):
    print("맞습니다.")



a = 1
b = 1

c = (a==b) and (a > 0)
d = (a==b) or (a > 10)

print(c)
print(d)




num = 99
a = (num > 100) and (num < 200)
b = (num == 99) or (num == 100)
c = not(num == 100)

print(a)
print(b)
print(c)



a = 10
if(type(a) != float):
    print("...")




a = 1
b = 1

if(1):
    print("a와 b가 같습니다.")



a = 10
b = 99

# true and true

print("1. true and true")
if (a==10) and (b==99):
    print("a==10 and b==99 : true")
else:
    print("a==10 and b==99 : false")


# true and false
print("2. true and false")
if (a==10) and (b != 99):
    print("a==10 and b!=10 : true")
else:
    print("a==10 and b!=10 : false")

    

a = 10
b = 5

res = a + b
print(res)    #15

res = a*b
print(res)   #50

res = a / b
print(res)     #2.0

res = a**b
print(res)   #100000


a = 10
b = 2

print(a/b)   # 5.0
print(type(a/b))  #<class 'float'>


x = 100
y = 20

z1 = x + y # z_sum
z2 = x*y  # z_mul
z3 = x**y # z_square

print(z1,z2,z3)   #120 2000 100000000...


x = 10
y = 2 
z = 3

a = (x + y) + z #보기편하게


#x = int(input("숫자를 입력하세요: ")) #10 입력
#y = x*10
#print(x, type(x))   #10 <class 'int'>
#print(y)   #100


x = str(3)
y = float(x*2)
print(y)   #33.0  #문자형으로 바뀌고 곱하기 2 니깐 33이 연속으로 나란히 나온다.


s1, s2, s3 = "100", "100.123", "999"
print(int(s1)+1, float(s2)+1, int(s3) + 1)
# 101 101.123 1000 출력


#weight = int(input("나의 체중은: "))  #int 대신 float도 가능
#height = float(input("키는: "))  # m 단위
#bmi = weight/(height**2)

#print("나의 체중은 ", weight, "kg, 키는 ", height, "m 입니다.")
#print("계산한 BMI 지수는 ", bmi)


#num = int("100") + int("200")
#print(num)   #300


a = 3
a += 2 
a *= 5
print(a)  #25


#num1 = int(input("나눠지는 수: "))
#num2 = int(input("나누는 수: "))

#x = num1//num2
#y = num1 % num2

#print(str(num1), "을(를)", str(num2), "으로 나눈 몫은 ", x, "입니다.")
#print(str(num1), "을(를)", str(num2), "으로 나눈 나머지는 ", y, "입니다.")


print("가방" < "하마")  #True
print("가방" > "하마")  #False


a = 10
b = 20

if (a<b):
    print("b가 a보다 큽니다.")


if(10!=100):
    print("맞습니다.")


a = 1
b = 1

c = (a==b) and (a>0)
d = (a==b) or (a>10)

print(c)   #True
print(d)   #True


num = 99
a = (num>100) and (num<200)
b = (num == 99) or (num == 100)
c = not(num == 100)

print(a)   #False
print(b)   #True
print(c)   #True


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
    print("a==10 and b == 99 : true")
else:
    print("a==10 and b==99 : false")


# true and false
print("2. true and false")
if (a==10) and (b != 99):
    print("a==10 and b!= 99 : true")
else:
    print("a==10 and b != 99 : false")
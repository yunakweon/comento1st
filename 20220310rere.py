var1 = 100
print(type(var1))   #<clsaa 'int'>


print(1+1)     #2
print('1'+'1')   #11


var1 = 200
var2 = 100
res = var1/var2    #2
print(type(res))  #<class 'float'>


# \n 는 enter , 새로운 줄로 이동
# \t 는 tap, 다음 탭으로 이동
# \b 는 backspace, 뒤로 한 칸 이동


var1 = (100>10)
print(var1)        #True


name = input("받는 사람 : ")
adress = input("주소 : ")
weight = input("무게(g) : ")

price = float(weight)*0.3 + 181

print("받는 사람 ==> ", name)
print("주소 ==> ", adress) 
print("배송비 ==> ", price, "원") 
#print("배송비 ==> ", str(price), "원")  


math = 90
korean = 95
science = 88

average = (math + korean + science)/3
print(average)     #90.1


x,y,z = 1,2,3


x=y=z=1
print(x)       #1
print(x, y, z)   #1 1 1


PI = 3.1415   #상수 = 변하지 않는 수는 암묵적으로 대문자로 쓴다.


# 연습문제 01

a = 200
b = 300
c = a + b
print(a, '+', b, '=', c)   #200 + 300 = 500


#연습문제 02

number1 = 200
number2 = 300
result = number1 + 200   # 400


#연습문제 03

#틀린답은 3번, 왼쪽에 변수 1개만 올 수 있어서


#연습문제 04

number1 = 10
number2 = 2
result1 = number1*number2    #20
result2 = number1/number2    #5.0   #정수 나누기 정수는 실수!


#연습문제 05

string1 = '안녕'
string2 = '2'
print(string1 + string2)    #안녕2


#연습문제 06

number1 = input("숫자1 ==> ")      #200
number2 = input("숫자2 ==> ")      #300
print(number1 + number2)           #200300
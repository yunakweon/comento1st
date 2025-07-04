var1 = 100
print(type(var1))



print(1+1)     #2

print('1'+'1')   #11

var1 = 100
var2 = 200
res = var1 + var2
print(res)         #300
print(type(res))       #<class 'int'>


#var1 = 100
#var2 = 200.0
#res = var1 + var2
#print(res)       #300.0
#print(type(res))        #<class 'float'>


#a=10
#print(a)


#var1 = 100
#var2 = 200
#res = var1 / var2
#print(res)          #0.5
#print(type(res))    #<class 'float'>


#var1 = "큰 따옴표 모양은 \" 이고,"
#var2 = "작은 따옴표 모양은 \' 이다."
#print(var1, var2)
# 큰 따옴표 모양은 " 이고, 작은 따옴표 모양은 ' 이다.


#var1 = '대학 \n데이터사이언스'
#print(var1)
# 대학
# 데이터사이언스


#var1 = "데이터" + "사이언스"
#print(var1)     #데이터사이언스


#var1 = "데이터" * 2
#print(var1)      #데이터데이터


#var1 = "동덕"
#var1 = var1 + "여대"
#var1 += var1 + " "
#var1 = var1 + "데이터 "
#var1 += var1 + "사이언스"

#print(var1)


x = 10
y = 3.1
z = x*y
print(z)  #31


var1 = (100 <= 20)
print(var1)   #False


print(10000*0.3)   #3000


print(100 + 300)   #400


a = 100
b = 200
c = a + b
print(c)     #300


num1 = 100
num2 = 50
result = num1 + num2
print(result)          #150


#num1 = input()       #사용자 입력: 100
#num2 = input("숫자 ==> ")       #사용자 입력: 200
#result1 = num1 + num2   
#print(result1)    #100200   #왜냐하면 input()으로 입력받는 데이터는 모두 문자열(str)로 인식하기 때문에


#num1 = int(input("숫자1 ==> "))      #입력: 100       #문자열 데이터를 정수형으로 변환해서 가능
#num2 = int(input("숫자2 ==> "))      #입력: 200
#result = num1 + num2
#print(result)    #300


#name = input("이름? : ")
#univ_id = input("학번? : ")
#print("제 이름은", name, "이고, 제 학번은", univ_id, "입니다.")
# ????????입력한게 왜 다 띄어쓰기 되지?????????
#print("제 이름은 " + name + "이고, 제 학번은 " + univ_id + "입니다")
# + 이용하면 제대로 나옴!


x = 10
y = 3

z = x/y
z1 = x//y  #몫
z2 = x%y    #나머지
print(z2)


x = "kwon yu\" na"    #kwon yu" na
y= "na"
print(x)
print(x+y)            #kwon yu" nana


x = 3

y ='x='
print(y+str(x))    # x=3

print('x=' + str(x))   # x=3

print(type(x))    # <class 'int'>

x = str(x)
print(type(x))     # <class 'str'>


x = 'kwon yu \tna'
print(x)


print("a"+"b"+"c")   # abc
print("a"+"2")          #a2


a = 10
print(a)     # 10
a = a+1
print(a)     # 11


a -= 1
print(a)     # 10


a = "kwon"
print(a)    # kwon

a = a+ "yu"
print(a)    #kwonyu


a = "kwon"
print(a*3)      #kwonkwonkwon


a = 100 > 10
print(a)          #True


hakbun = 20221608 
x = (hakbun % 2 == 0)
print(x)               #True
print(type(x))           #<class 'bool'>


x = 1000000
y = x*(1-0.3)
print(y)           #700000.0


math = 90
korean = 95
science = 88

average = (math + korean + science)/3
print(average)    #91.0


x,y,z = 1,2,3
print(x)   #1
print(y)   #2
print(z)   #3


x=y=z=1
print(x)  #1
print(y)   #1
print(z)   #1
print(x,y,z)   #1 1 1


PI = 3.1415   # 상수 = 변하지 않는 수는 암묵적으로 대문자로 씀.


#print("수학 점수를 입력해주세요.")
#score_math = input("수학 점수를 입력해주세요")

#result = int(score_math) + 5    #수학점수에 5점 추가
#print(result)


a = 1
b = float(a)
a = float(a)
float_a = float(a)
print(a)       #1.0
print(float_a)    #1.0


a = 1
print(a)   #1

x = 1
y = x + 3
print(y)


#print('## 택배를 보내기 위한 정보를 입력하세요. ##')

#name = input("이름 :")
#adress = input("주소 :")
#weight = input("무게(g) :")

#price = float(weight) * 0.3 + 181

#print("받는 사람 ==> " + name )
#print("주소 ==> " + adress )
#print("배송비 ==> " + str(price) + "원")


#연습문제 01

a = 200
b = 300
c = a + b
print(a,'+',b,'=',c)   #200 + 300 = 500


#연습문제 02

number1 = 200
number2 = 300
result = number1 + 200
print(result)  #400


#연습문제 03

# 3번이 틀렸다. 왼쪽에 변수 1개만 올 수 있어서?


#연습문제 04

number1 = 10
number2 = 2
result1 = number1 * number2     #20
result2 = number1 / number2     #5.0
print(result1)
print(result2)


#연습문제 05

string1 = "안녕"
string2 = "2"
print(string1 + string2)   #안녕2


#연습문제 06

number1 = input("숫자1 ==> ")  #200 입력
number2 = input("숫자2 ==> ")  #300 입력
print(number1 + number2)      #200300 출력, input()으로 안에 숫자 str이 되어서.


# 05 변형
number1 = int(input("숫자1 ==> "))  #200 입력
number2 = int(input("숫자2 ==> "))  #300 입력
print(number1 + number2)      #500 출력
#이러면 int 때문에 정수형 되어서 500으로 나온다.
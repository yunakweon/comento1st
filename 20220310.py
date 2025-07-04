from dataclasses import KW_ONLY
from operator import truediv
from re import A


print(1+1)

print('1'+'1')

print("1"+"1")

print(1+3)

a=1   #주석    #integer (int)
b=1.32423874     #floating point      

c=a+b


print(a)
a=10
print(a)


a=True  #boolean  (bool)
b=False  #boolean  (bool)
c=1    #integer  (int)
d="권유나"    #string  (str)
e= 3.141592    #floating point  (float)

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))



print(3.141592 * 4357)
print((90+95+58+32)/4)


x=10
y=3.14

print(x*2)
print(x*y)

print(type(x))

print(x*y)



x=10       # x: int
y=3.14       # y: float

z=x*y
print(z)


a="여러분 안녕하세요"
print(a)

x=10
y=3

z= x/y    #몫3 나머지1
z1= x//y  #몫
z2= x%y   #나머지
print(z)



hakbun=20221234



x="kwon yu na"
y='datascience'
print(x)
print(type(x))
print(y)
print(type(y))


x="kwon yu\" na"  #맞나??
y="na"

print(x)
print(y)
print(x+y)


x=3   #integer
#x=3    #string

y='x= '
print(y+str(x))

print('x= ' + str(x))

print(type(x))

x=str(x)
print(type(x))



x='kwon yu  \tna'
print(x)



print("a"+"b"+"c")
print("a       "+"b"+"c")
print("a"+"     "+"b"+"c")


print("a"+"2")


a=10
print(a)  #10
a=a+1     
print(a)  #11

a += 1
print(a)  

a -= 1  # a= a-1
print(a)




a="kwon"
print(a)   #kwon
a = a+ "yu"

print(a)   #kwonyu




a="kwon"
print(a*100)  




a= 100> 10
print(a)

a= 100< 10
print(a)




hakbun =20221234

x = (hakbun % 2 == 0)   #???모르겠다 #false 나와야하는데 안나옴.

print(x)
print(type(x))




x= 1000000

y= x*(1-0.3)

print(y)

    

org_price=1000000

discount_rate= 30

final_price = org_price*(100-discount_rate)





math= 90
korean= 95
science= 88

average= (math+korean+science)/3
print(average)





a=1
A=5
print(a)
print(A)



science=5
Science=7
sCience=8

print(science)
print(Science)
print(sCience)


x,y,z= 1,2,3

print(x)
print(y)
print(z)



x=y=z=1
print(x)
print(y)
print(z)
print(x,y,z)



score_math = 90
score_korean = 100
num_class = 5

a1 = 3
a2 = 5

year = 2022  #년 정보
month = 5   #월 정보
day = 10    #일 정보


PI = 3.1415   # 상수 변하지 않는 수는 암묵적으로 대문자로 씀

max_hakjum = 18
MAX_HAKJUM = 18


#print("아무 값.\ n")
#input()

#print("아무 값.\n")
#print(input())




#print("수학 점수를 입력해주세요.")
#score_math = input("수학 점수를 입력해주세요")

#result = int(score_math) + 5

#result= "당신의 수학덤수는" + score_math + "점 입니다."

#print(result)

#score_modified = int(score_math) * 0.9
#print(score_modified)
#print(type(score_modified))



a = 1  #int
b = float(a)
a = float(a)
float_a = float(a)
print(a)
print(float_a)

#x = int(input("숫자를 입력해주세요..."))

y = x + 3
print(y)





name = input("이름? :")
univ_id = input("학번? :")
print("제 이름은 " + name + "이고, 제 학번은 " + univ_id + "입니다")




print("## 택배를 보내기 위한 정보를 입력하세요. ##")

name = input("이름 :")
adress = input("주소 :")
weight = input("무게(g) :")

price = float(weight) * 0.3 + 181

print("받는 사람 ==> " + name )
print("주소 ==> " + adress )
print("배송비 ==> " + str(price) + "원")



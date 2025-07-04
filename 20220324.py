weather = 1

if (weather > 0) :
    print("긴팔을 입으세요")
    print("두꺼운 외투를 입으세요")
print("더워요")



a = 1
b = 1

if a == 2 :
    pass



x = 3
if ( x > 3 ) :
    print("3보다 큽니다")



name = "권유나"
if  name == "권유나" :
    print("본인입니다.")



a = 3
if (type(a) == int ) :
    print("정수형 입니다.")



a = input("비밀번호는 무엇입니까? ")

if  a == "0610":
    print("문이 열렸습니다.")


a = int(input("아이가 태어난 지 몇 개월입니까? "))
if (a == 5):
    print ("파상풍 예방접종 대상자입니다.")
    print ("폐렴구균 예방접종 대상자입니다.")

if (0<= a <= 1):
    print("결핵 예방접종 대상자입니다.")
    print("B형간염 예방접종 대상자입니다.")

if ( a== 2):
    print("B형간염 예방접종 대상자입니다.")
    print("파상풍 예방접종 대상자입니다.")
    print("폐렴구균 예방접종 대상자입니다.")

if (a == 15):
    print("폐렴구균 예방접종 대상자입니다.")



a = int(input("아이가 태어난 지 몇 개월입니까? "))

if (0<= a <= 1):
    print("결핵 예방접종 대상자입니다.")

if (0<= a <=2):
    print("B형간염 예방접종 대상자입니다.")

if (2<= a <=6):
    print("파상풍 예방접종 대상자입니다.")

if(2<=a<=15):
     print("폐렴구균 예방접종 대상자입니다.")



x =  10 

if x % 2 == 0 :
    print("짝수 입니다.")
else :
    print("홀수 입니다.")


name = input("이름: ")
if name == "권유나":
    print("확인되었습니다.")
else :
    print("다시 입력하여 주십시오.")




a = float(input("100m 기록(초): "))
b = float(input("1000m 기록(초): "))
c = float(input("윗몸일으키기 기록(회): "))
d = float(input("좌우 악력 기록(kg): "))
e = float(input("팔굽혀펴기 기록(회): "))

if 13.9 < a and 237 < b and 51 < c and 54 < d and 49 < e:
    print("합격 가능성이 매우 높습니다.")

    


x = 110

if x > 100:
    if x > 1000:
        print("x는 1000보다 큽니다.")
    else :
        print("x는 100보다크고 1000보다 작습니다.")
else: 
    print("x는 100보다 작습니다.")

print("끝")




score = 65
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")
print("학점입니다.")


a = input("고객님께서 사용 중이신 통신사를 입력해 주세요 : ")
if a == 'skt' :
    print("고객님께서 사용 중이신 통신사는 SKT 입니다.")
elif a == 'kt' :
    print("고객님꼐서 시용 중이신 통신사는 KT 입니다.")
elif a == 'lg' :
    print ("고객님께서 사용 중이신 통신사는 LG U+ 입니다.")



age  = int(input ("고객님의 나이를 입력해 주세요 : "))
if age >= 10 :
    print("고객님의 연령대는 10대 입니다.")
elif age >= 20 :
    print("고객님의 연령대는 20대 입니다.")
elif age >= 30 :
    print("고객님의 연령대는 30대 입니다.")
elif age >= 40 :
    print("고객님의 연령대는 40대 입니다.")
elif age >= 50 :
    print("고객님의 연령대는 50대 입니다.")
elif age >= 60 :
    print("고객님의 연령대는 60대 이상 입니다.")
else :
    print("고객님의 연령대는 10대 이하 입니다.")



#예제 10

age = int(input("나이를 입력하세요 : "))
if age <=10 :
    print("입장료는 1000원 입니다.")
elif age >= 65 :
    print("입장료는 0원 입니다.")
else :
    print("입장료는 2000원 입니다.")




# 예제 9

english = int(input("영어시험 점수를 입력하세요 : "))
math = int(input("수학시험 점수를 입력하세요 : "))

if english >= 80 and math >= 80:
    print("합격")
elif english >= 80 or math >= 80:
    print("재시험 기회제공")
else:
    print("불합격")



# 예제 8

id = input("아이디를 입력하세요 : ")

if id == "admin" :
    print("모든 콘텐츠 이용 가능")
elif id != "admin" :
    level = int(input("회원 레벨을 입력하세요 : "))
    if 2 <= level <= 7 :
        print("일부 컨텐츠 이용 가능")
    else: print("콘텐츠 이용 불가")



# 예제 5

level = input("회원 등급은 : ")
pay = int(input("구매 금액은 : "))

if level == "S" :
    price = pay*0.95 
elif level == "G" :
    price = pay*0.90
elif level == "V" :
    price = pay*0.85

print("회원님께서 지불하실 총 금액은", price, "입니다.")




#예제 1

kor = float(input("국어 점수 입력하세요: "))
eng = float(input("영어 점수 입력하세요: "))
his = float(input("한국사 점수를 입력: "))

choice1 = float(input("선택 첫 번쨰 과목 점수를 입력하세요: "))
choice2 = float(input("선택 두 번째 과목 점수를 입력하세요: "))

if kor < 40 or eng < 40 or his < 40 or choice1 < 40 or choice2 < 40:
    print("과락")
else :
    print("과락 아님")




#예제2

number = int(input("자연수를 입력하여 주십시오: "))

if number > 0 and number % 2 == 0:
    print("짝수 입니다.")
elif number > 0 and number % 2 == 1:
    print("홀수 입니다.")
else:
    print("자연수가 아닙니다.")



#예제3

number = int(input("수를 입력하여 주십시오: "))

if number >= 1000:
    print("세 자릿수 초과")
elif number >= 100:
    print("세 자릿수")
elif number >= 10:
    print("두 자릿수")
elif number >= 1:
    print("한 자릿수")
else: print("자연수가 아닙니다.")



#예제4

print("사이다-700원 콜라-800원 물-1200원")
money = int(input("얼마를 입력하겠습니까: "))
choice = int(input("선택) 1- 사이다 2-콜라 3- 물: "))

if money >= 700 and choice == 1:
    print("사이다가 나왔습니다.  덜컹")
    print("잔돈 %d 원 반환합니다" %(money - 700))
elif money >= 800 and choice == 2:
    print("콜라가 나왔습니다. 덜컹")
    print("잔돈 %d 원 반환합니다" %(money-800))
elif money >= 1200 and choice == 3:
    print("물이 나왔습니다. 덜컹")
    print("잔돈 %d 원 반환합니다" % (money - 1200))
else: 
    print("음료수를 뽑을 수 없습니다.") 
    print("잔돈 %d 원 반환합니다" % (money))


# int 일때 퍼센트머니 들어가게 %d 로 써야한다(?)
#print("1 + 1 = 2")
#print("%s + %d = %d" %(hi, 1, 2))
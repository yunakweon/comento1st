weather = 1

if weather > 0:
    print("긴팔을 입으세요")


a = input("비밀번호는 무엇입니까? ")
if a == "0610":
    print("문이 열렸습니다.")


a = int(input("아이가 태어난 지 몇 개월입니까? "))

if (0 <= a <= 1):
    print("결핵 예방접종 대상입니다.")


x = 10
if x % 2 == 0:
    print("짝수 입니다.")
else: 
    print("홀수 입니다.")
  

a = float(input("100ㅡ 기록(초): "))


x = 110

if x > 100:
    if x < 1000:
        print("100보다 크고 1000보다 작군요")
    else: 
        print("와 1000보다 크군요.")
else: print("100보다 작다")

score = 65

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
print("학점입니다.")

a = input("고객님께서 사용 중이신 통신사를 입력해 주세요: ")
if a == 'skt':
    print("고객님께서...")


age = int(input("고객님의 나이를 입력해주세요: "))
if age >= 10:
    print("고객님의 연령대는 10대 입니다.")
elif age >= 20:
    print("고객님의 연령대는 20대 입니다.")


# 에제 01

kor = float(input("국어 점수 입력: "))
eng = float(input("영어 점수 입력: "))
his = float(input("한국사 점수 입력: "))
choice1 = float(input("선택 첫 번째 과목 점수: "))
choice2 = float(input("선택 두 번째 과목 입력:"))

if kor < 40 or eng < 40 or his < 40 or choice1 < 40 or choice2 < 40:
    print("과락")
else:
    print("과락 아님")


# 예제 02

number = int(input("자연수를 입력하여 주십시오:"))

if number > 0 and number % 2 == 0:
    print("짝수 입니다")
elif number > 0 and number % 2 == 1:
    print("홀수 입니다.")
else:
    print("자연수가 아닙니다.")


# 예제 03

number = int(input("자연수 입력: "))

if number >= 1000: 
    print("세 자릿수 이상")
elif number >= 100:
    print("세 자릿수")
elif number >= 10:
    print("두 자릿수")
elif number >= 1:
    print("한 자릿수")


# 예제 0


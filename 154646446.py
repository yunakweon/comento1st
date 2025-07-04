# 함수 선언 부분
def find_and_insert_data(person, ticket_number):
    arr.append(None)
    kLen = len(arr)
    arr[kLen-1] = (person, ticket_number)

    for i in range(0, kLen):
        if int(arr[i][1]) > int(ticket_number):
            insert_data(i,(person, ticket_number))
            arr.pop()
            break
        
    
    
    
def insert_data(position, information):
    if ((position < 0) or (position > len(arr))):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    arr.append(None)
    kLen = len(arr)
    
    for j in range(kLen - 1, position, -1):
        arr[j] = arr[j-1]
        arr[j-1] = None
        
    arr[position] = information
    
# 전역 변수 선언 부분
arr = [("다현", "1"), ("정연", "3"), ("쯔위", "9")]
select = 0

# 메인 함수 부분
if __name__ == "__main__":
    print(arr)
    while (select != 2):
        # select 변수의 의미 (1: 데이터 추가, 2: 프로그램 종료)        
        select = int(input("값을 입력하세요 (1: 데이터 추가, 2: 프로그램 종료) : "))
        
        if select == 1:
            data = input("추가할 사람 >> ")
            count = input("대기 번호 >> ")
            find_and_insert_data(data, count)
        elif select == 2:
            print("프로그램을 종료합니다.")
        else:
            print("잘못 입력하셨습니다!")
            continue
            
        print(arr)















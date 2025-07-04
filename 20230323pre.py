# or 연산자

a = 100
b = 200

if a>100 or b>100:
    print('참')
else:
    print('거짓')  #참

# and 연산자

a= 100
b = 200
if a >100 and b>100:
    print('참')
else:
    print('거짓')  #거짓


# elif


massage = 'success' if a >= 60 else 'failure'
print(massage)    #success


# continue문

a = 0
while a<0:
    a += 1
    if a % 2 == 0: continue  #while문을 빠져나가지 않고 while문의 맨 첨으로 돌아감 그래서 print(a)값 안나오는듯
    print(a)


# 무한루프

#while True:    #무한히 수행
#    print('Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다')


# for문

test_list = ['one', 'two', 'three']
for i in test_list:   #순서대로 대입
    print(i)

#one
#two
#three  


# range 함수

a = range(1,11)
print(a)   #???1,2,3,4,5,6,7,8,9,10 원래 이렇게 나와야하는데 나는 range(1,11)이라고 나온다???


# 예제: 구구단을 2단부터 9단까지 차례대로 출력해보자

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print('')


#리스트 내포

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)   #[3, 6, 9, 12]


#리스트
#리스트명 = [요소1, 요소2, 요소1, ...]

a = []
b = [1,2,3]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']
e = [1, 2, ['life', 'is']]


# 리스트 인덱싱

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])  #1
print(a[-1])  #['a', 'b', 'c']   #리스트의 마지막 요소 
print(a[3])   #['a', 'b', 'c']
print(a[3][0])   #a   #리스트에 내포된 리스트에서 값 도출, 리스트[i][j]


#리스트 슬라이싱

a = [1,2,3,4,5]
print(a[0:2])   #[1, 2]
print(a[:2])    #[1, 2]
print(a[2:])   #[3, 4, 5]


#리스트연산

a = [1,2,3]
b = [4,5,6]

print(a+b)  #[1, 2, 3, 4, 5, 6]    #리스트 더하기, 2개의 리스트를 합치는 기능
print(a*3)   #[1, 2, 3, 1, 2, 3, 1, 2, 3]   #리스트n번 반복
print(len(a))   #3    #리스트 길이 구하기


#리스트 수정과 삭제

a = [1,2,3]
a[2] = 4   #[1, 2, 4]  # 리스트[x] = 새로운 값
#print(a)   
del a[1]   #[1, 4]  #리스트 삭제 1번자리 그니까 0부터 시작해서 두번째 자리인 2가 사라진것
#print(a)

a = [1,2,3]
del a[2:]    #[1, 2]   #2번째 자리 이상 삭제, 0부터니까 세번째 자리 이상부터 삭제
print(a)


# append

a = [1,2,3]
a.append(4)
print(a)   #[1, 2, 3, 4]   # append(x)는 리스트 맨 마지막에 x를 추가하는 함수


# sort

a = [1,4,3,2]
a.sort()
print(a)    #[1, 2, 3, 4]
# 리스트 요소를 순서대로 정렬해준다
#숫자는 오름차순, 문자는 알파벳 순서로 정렬 


# reverse

a = [1, 4, 3, 2]
a.reverse()
print(a)    #[2, 3, 4, 1]
#리스트를 역순으로 뒤집어준다 


# index

a = [1,2,3]
print(a.index(3))    #2   
a.index(1)     #0
# 리스트에 x값이 있으면 위치 값을 돌려준다 


# insert

a = [1,2,3]
a.insert(0,4)    #print(a)       #[4, 1, 2, 3]
# insert(a,b)는 리스트의 a번째 자리에 b를 삽입하는 함수 


# remove

a = [1,2,3,1,2,3]
a.remove(3)
print(a)    #[1, 2, 1, 2, 3]
# 리스트에서 첫번째로 나오는 x값을 삭제하는 함수
# x값이 2개 이상 있을 경우 첫번째 하나만 제거 


# pop

a = [1,2,3]
a.pop()   #3    # pop()는 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
print(a)   #[1, 2]

a = [1,2,3]
a.pop(1)    #2
print(a)    #[1, 3]   
# pop(x) 리스트의 x번째 요소를 돌려주고 그 요소는 삭제 


# count

a = [1,2,3,1]
a.count(1)    #2
#리스트 안에 x가 몇개 있는지 그 개수를 


# extend

a = [1,2,3]
a.extend([4,5])
print(a)         #[1, 2, 3, 4, 5]
# extend(x)에서 x에는 리스트만 올 수 있으며, 원래의 a리스트에 x리스트를 더함

a = [1,2,3]
a += [4,5]
print(a)    #[1, 2, 3, 4, 5]


# 튜플다루기 

t1 = (1, 2, 'a', 'b')
print(t1[0])   #1    #인덱싱
print(t1[1:])  #(2, 'a', 'b')   #슬라이싱
t2 = (3,4)     
print(t1 + t2) #(1, 2, 'a', 'b', 3, 4)   #튜플 더하기
print(t2 * 3)  #(3, 4, 3, 4, 3, 4)     #튜플 곱하기
print(len(t1)) #4   #튜플 길이 구하기


# 딕셔너리 

#{key1:value1, key2:value2, key3:values}


# 딕셔너리 요소 추가, 삭제

a = {1:'a'}
a[2] = 'b'    # a[key] = 새 요소   #딕셔너리 요소 추가
print(a)    #{1: 'a', 2: 'b'}

del a[1]    # del a[key]  # 저장된 key 값에 해당하는 {key: value} 쌍 삭제
print(a)    #{2: 'b'}


# 딕셔너리 호출

a = {1:'a', 2:'b'}
print(a[1])   #a   
print(a[2])   #b
# key를 이용하여 value 얻기
# '딕셔너리 변수 이름[key]' 사용 


# keys(), values()

a = {1:'a', 2:'b', 3:'c'}
print(a.keys())    #dict_keys([1, 2, 3])
a.values()         #dict_values(['a', 'b', 'c'])


# 딕셔너리 쌍 얻기, 지우기 

a = {1:'a', 2:'b', 3:'c'}
print(a.items())  #dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
 # item 함수  # key와 value값의 쌍을 튜플로 묶은 값을 dict_items객체로 돌려준다
a.clear()  #{}  #clear 함수  # 딕셔너리 안의 모든 요소를 삭제 
print(a)


# 딕셔너리 get()

a = {1:'a', 2:'b', 3:'c'}
print(a.get(1))   #a    #get(x) 함수: x라는 key에 대응되는 value를 돌려준다
print(a.get(4))   #None  #존재하지 않는 키 값을 가져오려 할 경우 'None'을 돌려준다


# 딕셔너리 in

a = {1:'a', 2:'b', 3:'c'}
print(2 in a)   #True  #딕셔너리 안에 존재
print(5 in a)   #False #딕셔너리 안에 존재하지 않음 
# 'key' in a 를 호출하면 참 또는 거짓으로 돌려준다
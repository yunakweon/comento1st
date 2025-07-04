# 챕터 04 예제 07

#i = 999

#while i > 99:
 #   if i % 24 == 0:
  #      print(i)
   #     break
    #i = i - 1


# 챕터 04 예제 08 

#i = 1
#gcm = 1

#while i < 30:
 #   if 30 % i == 0 and 75 % i == 0:
  #      if gcm < 1:
   #         gcm = i
    # i += 1
#print(gcm)


# 챕터 04 예제 09

#year = 0
#money = 1000

#while money < 2000:
 #   money = money * 1.07
  #  year += 1

#print(year)



#a = []
#a.append(3)
#a.append(2)
#a.append(5)
#a.append(1)

#a.insert(2, "hello")   #[3, 2, 'hello', 5, 1]

#print(a)  #[3, 2, 5, 1]



#data = [6, 3.14, "hello", 10]


a =[]

for i in range(0, 4):
    a.append(i)


aa = []
bb = []

for i in range(0, 100):
    aa.append(2*i)
print(aa)

for i in range(0,100):
    bb.append(aa[99-i])
print(bb)



# 예제 01

#방법1

greetings = ['안녕', '니하오', '하이']

for i in greetings:
    print(i)

#방법2

print(len(greetings))

for i in range(0, len(greetings)):
    print(greetings[i])


a = [1, 2, 3, 4]
b = [5, 2, 4, 6]

for i in range(0, len(a)):
    for j in range(0, len(b)):
        print(a[i]*b[j])


# 예제 03

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']
b = []

for i in a:
    if len(i) == 5:
        b.append(i)
print(b)




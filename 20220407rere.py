a = []
a.append(3)
a.append(2)
a.append(5)
a.insert(2, "hello")
print(a)


a = []
for i in range(0, 4):
    a.append(i)
print(a)


aa = []
bb = []

for i in range(0, 100):
    aa.append(2*i)
    print(aa)

for i in range(0, 100):
    bb.append(aa[99-i])
    print(bb)


# 예제 01

# 방법1

greetings = ['안녕', '니하오', '하이']

for i in greetings:
    print(i)

# 방법2

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

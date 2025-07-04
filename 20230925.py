f = open('xx.txt','r')

lines = f.readlines()

res = []

for line in lines:
    res.append(line.strip())



f = open('homework.txt','r')

while True:
    line = f.readline()
    if not line: break
    print(line.strip())

f.close()



f = open('yyy.txt', 'w')

f.write('권유나')

f.close()

with open('homework.txt','r') as f:
    lines = f.readlines()

    for line in lines:
        print(line.strip())



#p.10

f = open("name.txt","w")

name = ['Alex','Emma','Smith','Jane','Ava','Charlotte','Evelyn']

for i in name:
    if len(i) == 4:
        f.write(i + '\n')

f.close()



f = open('homework.txt', 'r')

lines = f.readlines()
names = []

for line in lines:
    data = line.strip()
    name = data.split(':')[0]
    score = data.split(':')[1]
    sum += int(score)

print(sum)













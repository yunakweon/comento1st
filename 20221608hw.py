# (1)

with open("midterm.txt", 'r') as f:
    lines = f.readlines()[1:]

all_average = []

for line in lines:
    data = line.strip()
    Korean = data.split(',')[0]
    Mathmatics = data.split(',')[1]
    English = data.split(',')[2]
    Art = data.split(',')[3]
    
    sum = int(Korean) + int(Mathmatics) + int(English) + int(Art)
    average = sum / 4
    average = float(average)

    all_average.append(average)


max_average = max(all_average)

number = all_average.index(max_average) 


with open("name.txt", 'r') as f:
    lines = f.readlines()

count = 0

for line in lines:
    if count == number:
        if number < 9: print(line[2:])
        else: print(line[3:])
        break
    else: count += 1




# (2)


with open("midterm.txt", 'r') as f1:
    lines = f1.readlines()[1:]

    all_Korean = []
    all_Mathmatics = []
    all_English = []
    all_Art = []

for line in lines:
    data = line.strip()
    Korean = data.split(',')[0]
    Mathmatics = data.split(',')[1]
    English = data.split(',')[2]
    Art = data.split(',')[3]

    all_Korean.append(int(Korean))
    all_Mathmatics.append(int(Mathmatics))
    all_English.append(int(English))
    all_Art.append(int(Art))


max_Korean = max(all_Korean)
max_Mathmatics = max(all_Mathmatics)
max_English = max(all_English)
max_Art = max(all_Art)



number_Korean = []
number_Mathmatics = []
number_English = []
number_Art = []

for i in range(len(all_Korean)):
    if all_Korean[i] == max_Korean:
        number_Korean.append(i)
    
for i in range(len(all_Mathmatics)):
    if all_Mathmatics[i] == max_Mathmatics:
        number_Mathmatics.append(i)
    
for i in range(len(all_English)):
    if all_English[i] == max_English:
        number_English.append(i)
    
for i in range(len(all_Art)):
    if all_Art[i] == max_Art:
        number_Art.append(i)
    



with open("name.txt", 'r') as f2:
    lines = f2.readlines()

name_Korean =[]
name_Mathmatics =[]
name_English =[]
name_Art =[]




for i in number_Korean: 
    count = 0
    for line in lines: 
        if count == int(i):
            k = line.strip()
            if int(i) < 9: name_Korean.append(k[2:])
            else: name_Korean.append(k[3:])
            break
        else: count += 1
        
        
for i in number_Mathmatics: 
    count = 0
    for line in lines: 
        if count == int(i):
            k = line.strip()
            if int(i) < 9: name_Mathmatics.append(k[2:])
            else: name_Mathmatics.append(k[3:])
            break
        else: count += 1
        
for i in number_English:
    count = 0
    for line in lines: 
        if count == int(i):
            k = line.strip()
            if int(i) < 9: name_English.append(k[2:])
            else: name_English.append(k[3:])
            break
        else: count += 1
        
for i in number_Art: 
    count = 0
    for line in lines: 
        if count == int(i):
            k = line.strip()
            if int(i) < 9: name_Art.append(k[2:])
            else: name_Art.append(k[3:])
            break
        else: count += 1


        
        
        
with open("top.txt", 'w') as fw:
  
    fw.write("Korean : ")
    fw.write("%s"%(name_Korean[0]))
    
    for i in name_Korean[1:]:
        fw.write(", %s"%(i))
    
    fw.write("\n")
    
    
    fw.write("Mathmatics : ")
    fw.write("%s"%(name_Mathmatics[0]))
    
    for i in name_Mathmatics[1:]:
        fw.write(", %s"%(i))
    
    fw.write("\n")
    
    
    fw.write("English : ")
    fw.write("%s"%(name_English[0]))
    
    for i in name_English[1:]:
        fw.write(", %s"%(i))
    
    fw.write("\n")
    
    
    fw.write("Art : ")
    fw.write("%s"%(name_Art[0]))
    
    for i in name_Art[1:]:
        fw.write(", %s"%(i))
    
    fw.write("\n")
        




## 공동 1등 각각 새로운줄로 출력할거면
    # for i in name_Korean:
    #     fw.write("Korean : %s \n"%(i))
        
        
    # for i in name_Mathmatics:
    #     fw.write("Mathmatics : %s \n"%(i))
        
    # for i in name_English:
    #     fw.write("English : %s \n"%(i))
        
    # for i in name_Art:
    #     fw.write("Art : %s \n"%(i))
    








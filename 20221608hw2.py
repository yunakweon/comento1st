# 1번 문제

# 1-1번

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:/Users/yunac/Downloads/homework2.csv')
#print(df)

# df = pd.DataFrame({
#     'Name':['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#     'Age':[26,39,34,30,27],
#     'Gender':['Female','Male','Male','Male','Female'],
#     'Country':['USA','Canada','UK','USA','Canada'],
#     'Salary':[94732,61284,56265,66850,87194]
# })

pd.pivot_table(data=df, index='Country', values='Salary', aggfunc='mean').plot(kind='bar')


# 1-2번

df.plot(kind='scatter', x='Age', y='Salary')
plt.show()




# 2번 문제

from PIL import Image

with open('list.txt', 'r') as f:

    lines = f.readlines()
    directory_name = 'images/'

    j = len(lines) 

    for i in range(0, j, 1):
        filename = directory_name + lines[i].strip()

        if i % 2 == 1:
            img = Image.open(filename)
            img = img.rotate(30, expand=True)
            img.save(filename.replace('dog', 'rot30_dog'))



with open('list.txt', 'r') as f:

    lines = f.readlines()
    directory_name = 'images/'

    j = len(lines) 

    for i in range(0, j, 1):
        filename = directory_name + lines[i].strip()

        if i % 2 == 0:
            img = Image.open(filename)
            x = int(img.size[0])
            y = int(img.size[1])
            img = img.crop((x*0.1, y*0.2, x*0.3, y*0.5))
            img.save(filename.replace('dog', 'crop_dog'))


    









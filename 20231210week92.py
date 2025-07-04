import pandas as pd

df = pd.read_cvs('')

print(df)

df.head()
df.tail()

df.info()
df.shape()
print(df.shape)

df.dtypes

df.columns

len(df)

df.describe()

df['출고수량'].describe()

df['카테고리'].unique()








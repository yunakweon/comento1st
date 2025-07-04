# 시험문제 7문제에서 +-1, 35점, 과제 2주 기한
# 인터넷에 연결되어있지 않은채로 보기, 오늘꺼 까지, 수업시간에 배운거 위주로
# 시험범위는 46페이지까지

import numpy as np   # 잉 왜 하얗지
import pandas as pd

#df = pd.read_csv



import numpy as np
from pandas import Series, DataFrame  #5번째 또는 10번째 줄로 쓰면됨

a = [10, 20, 30]
b = Series(a)

print(b)
print(type(b))



a = [1, 2, 3]
c = ['국어', '영어', '수학']
b = Series(a , c)
b = Series(data=a , index=c)      # 위에랑 같은거 

print(b)

#국어    1
#영어    2
#수학    3



a = {'국어':100, '영어':90}
b = Series(a)

print(b)       
#국어    100
#영어     90

print(b.index)
print(b.values)
print(b.array)



index = ['국어', '수학', '영어']
values = [100, 90, 85]

a = Series(values, index)

print(a)
print(type(a))
print(a[1])         #90


# a = Series(values)만 있을때는 print(a[-1])이 오류 나옴

print(a.iloc[1])   #a[1]    #90
print(a.iloc[-1])  #a[-1]   #85

print(a.loc['수학'])    #90
print(a.loc['영어'])    #85

print(a.iloc[  [1,2]  ])
#수학    90
#영어    85

print(a.loc[  ['국어','영어']  ])
#국어    100
#영어     85

print(a.iloc[0:2])   # 얘는 0부터 1까지만 인데
#국어    100
#수학     90

print(a.loc[ '국어':'수학'  ])   # loc는 '수학'까지 포함시켜서 출력, 위에랑 같은거 출력됨
#국어    100
#수학     90

a.loc['미술'] = 70   # 미술 추가
print(a)
#국어    100
#수학     90
#영어     85
#미술     70

a.loc['수학'] = 100     # 수학 점수 변경함
print(a)
#print(a.drop('수학'))  # 얘는 눈요기로만 지워주는거지 실제 데이터에는 변동 없음

a.drop('수학', inplace=True)   # False 일 경우 값이 안바뀌고 그대로 출력됨, True 여야지 삭제됨
print(a)



from pandas import Series

s = Series([10, 20, 30])

print(s+10)
#0    20
#1    30
#2    40



from pandas import Series

a = Series([10, 20, 30])
b = Series([0, 40, 100])
c = a - b

print(c)



from pandas import Series

s = Series([1,2,3,4,5])
cond = s > 3

print(cond)
#0    False
#1    False
#2    False
#3     True
#4     True

print(type(cond))
#dtype: bool
#<class 'pandas.core.series.Series'>

print(s[cond])          
#3    4
#4    5       



from pandas import Series

a = Series([30, 14, 24, 50, 12])
b = Series([0, 9, 22, 46, 13])

cond = abs(a-b)
print(b[  cond>4  ])



c = Series([1, 2, np.nan, 4])
k = c.isna()

print(k) #여기부분 모르겠음, 영상 다시 보기
print(sum(k))   #1



from pandas import Series

data = ['라일락','코스모스','코스모스','장미','코스모스','장미']
series_data = Series(data)

print(series_data.unique())   #['라일락' '코스모스' '장미']

print(series_data.value_counts())
#코스모스    3
#장미      2
#라일락     1

print(series_data.isin(['코스모스']))
#0    False
#1     True
#2     True
#3    False
#4     True
#5    False

print(sum(series_data.isin(['코스모스'])))    #3



from pandas import DataFrame

data = {
    '나이': [20,21,24],
    '성별' : ['여','남','여'],
    '학교':['A','B','C']
}

index = ['김지연','이태형','전지희']

c = DataFrame(data, index)
print(c)



from pandas import DataFrame

data = [
    [20,'여', 'A'],
    [21,'남', 'B'],
    [24,'여', 'C']
]
index = ['김지연','이태형','전지희']
columns = ['나이','성별','학교']

df = DataFrame(data, index, columns)
print(df)



from pandas import DataFrame

data =[
    {'나이':20,'성별':'여','학교':'A'},
    {'나이':21,'성별':'남','학교':'B'},
    {'나이':24,'성별':'여','학교':'C'}
]
index = ['김지연','이태형','전지희']
df = DataFrame(data=data, index=index)

print(df)


print(df['나이'])
print(df[['나이','학교']])

print(df.iloc[1,2])       #B

print(df.iloc[0:2])  #여기 관련된 페이지들 이해 안감, 따로 더 보기


print(df.iloc[[0,1], [0,1]])
#     나이 성별
#김지연  20  여
#이태형  21  남

print(df.iloc[[0,2], [0,2]])   
#     나이 학교
#김지연  20  A
#전지희  24  C

print(df.loc[['김지연','이태형'],['나이','성별']])
#     나이 성별
#김지연  20  여
#이태형  21  남



# 시험범위는 46페이지까지



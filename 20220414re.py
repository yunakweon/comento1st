A = {'학번':'2022', '이름':'권'}

print(A['이름'])

A['나이'] = 39

print(A)

A = {'학번': '20221234', '이름': '권유나', '부서': '데사'}

del(A['부서'])
print(A.get('부서'))


for i in list(A.values()):
    print(i)

print('학수번호' in A)

for i in A.keys():
    print(i,A[i])
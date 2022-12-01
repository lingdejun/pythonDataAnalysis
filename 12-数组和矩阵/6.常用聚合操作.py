import numpy as np
'''
常用聚合操作
sum
max
min
mean
'''
arr1 = np.random.randint(1, 100, size=(5, 6))
print(arr1)
print('----')
print(arr1.sum())
print(arr1.sum(axis=0))
print(arr1.sum(axis=1))

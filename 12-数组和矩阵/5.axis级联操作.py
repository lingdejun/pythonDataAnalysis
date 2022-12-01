import numpy as np
'''
axis级联操作:将numpy数组进行横向或者纵向拼接（同一纬度,必须行列数相同）
axis 轴向理解：
    -0:列
    -1:行
'''
arr = np.random.randint(1, 100, size=(2, 3))
print(arr)
arr1 = np.random.randint(1, 100, size=(5, 6))
print(arr1)
print('----------')
# arr2 = np.concatenate((arr1,arr1),axis=0)
# print(arr2)
print('----------')
arr3 = np.concatenate((arr1,arr1),axis=1)
print(arr3)
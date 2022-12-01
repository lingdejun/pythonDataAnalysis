import numpy as np
'''
变形reshape
'''
# 二维数组
arr1 = np.random.randint(1, 100, size=(5, 6))
print(arr1)
#将二维变形为 一维数组
arr2 =arr1.reshape((30,))
print(arr2)
print('--------')
#将一维变为 多维
print(arr2.reshape(6,5))




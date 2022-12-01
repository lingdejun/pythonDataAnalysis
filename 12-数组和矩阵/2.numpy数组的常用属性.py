import numpy as np

'''
shape 返回的是数组的形状
ndim  返回的是数组的维度
size  返回数组元素的个数
dtype 返回数组元素的类型
'''
arr = np.random.randint(0, 100, size=(2, 5))
print(f'数组形状{arr.shape},数组维度{arr.ndim},元素个数{arr.size},元素类型{arr.dtype}')

'''
创建指定元素类型的数组 dtpye,会将其他类型元素尝试转换为目标类型
np.array([1,2,3,],dtpye='int32')
'''
arr1 = np.array(['1', 2.9, 3], dtype='int32')
print(arr1)
print(arr1.dtype)
print(type(arr1))

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3 = arr2*3
print(arr2*arr3)
print(np.dot(arr2,arr3))
# print(arr3)

# 矩阵相乘结果为：
#  [[ 90 108 126]
#  [198 243 288]
#  [306 378 450]]
# 矩阵对应元素相乘结果为：
#  [[  3  12  27]
#  [ 48  75 108]
#  [147 192 243]]




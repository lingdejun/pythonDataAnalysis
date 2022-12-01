import numpy as np

# 数组中存储的数据元素类型必须统一类型
# 优先级：
#     字符串>浮点型>整型
'''
数组创建1
np.array()
'''
# array = np.array([1, 2, 3])
# print(array)
# array2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(array2)
# array3 = np.array([1,'2','three'])
# print(array3)
# array4 = np.array([1,2.2,3])
# print(array4)
# list1 = [1,2,3]
# print(list1)

'''
创建数组2
import matplotlib.pyplot as plt
plt.imread() #读取图片载入方式创建array
'''

'''
创建数组3
np.zero()
np.ones(shape=(3,4)) #返回几行几列的数组
np.linespace(0,100,num=20) #返回一维的等差数列数组
np.arange(10,50,step=2) #返回一维等差数列
np.random()
arr5= np.random.randint(0,100,size=(5,3)) 返回5行3列的0-100的随机数组
'''
arr1 = np.zeros(shape=(2, 5))  # 二维 [[0. 0. 0. 0. 0.][0. 0. 0. 0. 0.]]
# print(arr1)
arr2 = np.zeros(3)  # [0. 0. 0.] 一维
# print(arr2)
arr3 = np.ones(shape=(3, 4))  # 二维 [[1. 1. 1. 1.][1. 1. 1. 1.][1. 1. 1. 1.]]
# print(arr3)
arr4 = np.ones(3)  # 一维 [1. 1. 1.]
arr5 = np.random.randint(0, 100, size=(5, 3))  # 返回5行3列的0-100的随机数组
arr6 = np.random.random(size=(2, 4))  # 返回 2行4列的0.0-1.0的随机一维数组
print(arr6)



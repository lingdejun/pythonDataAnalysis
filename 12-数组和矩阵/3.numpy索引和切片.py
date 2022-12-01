import numpy as np

'''
索引操作和列表同理
'''
arr1 = np.random.randint(1, 100, size=(5, 6))
print(arr1)
print('--------')
# print(arr1[1])
# print('--------')
# print(arr1[[1, 3, 4]])  # 取多行

print(arr1[0:2])  # arr[行切片] 行切片 切前两行
print(arr1[:, 0:2])  # arr[行切片，列切片]  切前两列
print(arr1[0:2, 0:2])  # 切前两行的抢两列数据

print(arr1[::-1])  # 行翻转倒置
print(arr1[:, ::-1])  # 列倒置
print(arr1[::-1, ::-1])  # 所有元素倒置

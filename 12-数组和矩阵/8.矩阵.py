import numpy as np

''''
一个矩阵是由行row列column元素排列组成的矩形阵列
1.矩阵创建 :
-可以使用mat、matrix以及bmat函数来创建矩阵。使用mat函数创建矩阵时，若输入matrix或ndarray对象，
    则不会为它们创建副本。因此，调用mat函数和调用matrix(data, copy=False)等价。
-很多时候会根据小的矩阵创建大的矩阵，即将小矩阵组合成大矩阵。在NumPy中，可以使用bmat分块矩阵（block matrix）函数实现。
-numpy.identity()函数返回给定大小的单位矩阵。单位矩阵是个方阵，从左上角到右下角对角线（称为主对角线）
上的元素均为1，除此之外全部为0,返回其实是个数组，需要使用mat将其转换为矩阵
-eye()直接创建对角矩阵
'''
# 使用分号隔开数据
matr1 = np.mat("1 2 3;4 5 6;7 8 9")
print('------mat创建矩阵------')
print('matr1:',type(matr1))
print(matr1)
# 使用列表创建矩阵
matr2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('matr2')
print(matr2)

print('----identity创建矩阵----')
id1 = np.identity(3)
A = np.mat(id1)
print(id1)
print(A)
print('----eye创建,bmat分块矩阵----')
arr1 = np.eye(3)  # arr1 = np.eye(3, k=2)
arr2 = 3 * arr1
print(arr1)
print(arr2)
print(np.bmat("arr1 arr2"))

'''
矩阵计算
'''
print('-------矩阵计算-------')
matr3 = matr1 * 3  # 矩阵与数相乘
print('矩阵为：\r\n', matr1)
print('创建的矩阵为：\r\n', matr3)
print(f'矩阵相加结果为：\r\n {matr1 + matr3}')  # 矩阵相加
print('矩阵相减结果为：\r\n', matr1 - matr3)  # 矩阵相减
print('矩阵相乘结果为：\r\n', matr1 * matr3)  # 矩阵相乘
print('矩阵对应元素相乘结果为：\r\n', np.multiply(matr1, matr3))

'''
矩阵属性
'''
print('-------矩阵属性-------')
print('矩阵转置结果为：\r\n', matr1.T)  # 转置
print('矩阵共轭转置结果为：\r\n', matr1.H)  # 共轭转置（实数的共轭就是其本身）
print('矩阵的二维数组结果为：\r\n', matr1.A)  # 返回二维数组的视图
# print('矩阵的逆矩阵结果为：\r\n', matr1.I)  # 逆矩阵

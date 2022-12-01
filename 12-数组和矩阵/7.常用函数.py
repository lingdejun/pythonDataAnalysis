import numpy as np
'''
常用数学函数:
    -三角函数：sin() cos() tan()
    -返回指定数字的四舍五入：np.around(a,decimals)
        a:数组
        decimals:舍入小数位数，默认0,如果为负，整数将四舍五入到小数点左侧位置

常用统计函数:
       -amin() amax()，用于计算数组中元素沿指定轴的最小，最大值
       -ptp()：计算元素中最大值与最小值的差（最大值-最小值）
       -median()：计算数组a中元素的中位数（中值）
       -std()：标准差，是一组数据平均值分散程度的之中度量     
            std=sqrt(mean((x-x.mean())**2))
       -var():方差
    

'''
# arr1 = np.random.randint(1, 100, size=(5, 6))
# # print(np.sin(arr1))
# # print(np.around(15.15, 1))
# print(arr1)
# print('----------')
# print(arr1[1])
# print('----------')
# print(arr1[1].std())
# print('----------')
# print(arr1[1].var())

matr1 = np.matrix([[1,2],[3,4]])  #创建矩阵
print(type(matr1))
# print('创建的矩阵为：\r\n',matr1)
# print('inv\r\n',np.linalg.inv(matr1))
# print('矩阵的逆矩阵结果为：\r\n',matr1.I)

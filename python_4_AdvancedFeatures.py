# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 高级特性
'''
    切片
    迭代
    列表生成式
    生成器
    迭代器
'''
# ========= 切片 Slice ==============
# L[1:3]; L[:3]
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L2 = [1,2,3,4,5,6,7,8,9,10]
print(L[1:3])
# 每两个取一个, 第一个：是复制前一个L 后一个：2是说隔2个取第一个
print(L[::2])
print(L2[3:10:2])
# 切片函数是List Tuple Sring对着三个类型



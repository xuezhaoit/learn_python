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
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# L2 = [1,2,3,4,5,6,7,8,9,10]
# print(L[1:3])
# # 每两个取一个, 第一个：是复制前一个L 后一个：2是说隔2个取第一个
# print(L[::2])
# print(L2[3:10:2])
# 切片函数是List Tuple Sring对着三个类型

# ===========迭代 Iteration ===================
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# dict 也是迭代对象
# 字符串也是可迭代对象
# dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in dict.values()，如果要同时迭代key和value，可以用for k, v in dict.items()。
# dict1 = {'a':1,'b':2,'c':3}
# for key in dict1:
#     print (key)
# for key, value in dict1.items():
#     print (key, value) 
# for ch in 'ABC':
#     print(ch)

# 判断对象是否是迭代对象
# # 方法是通过collections.abc模块的Iterable类型判断
# from collections.abc import Iterable
# print(isinstance('abc', Iterable))

# # Python内置的enumerate函数可以把一个list变成索引-元素对
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
    
# ===========列表生成器================
# [变脸 for item1 in d 条件1]
# [m + n for m in 'ABC' for n in 'XYZ']
# 等效于
L = []
for chr1 in "ABC":
    for chr2 in "XYZ":
        L.append(chr1+chr2)
print(L)   
print([chr1+chr2 for chr1 in "ABC" for chr2 in "XYZ" ]) 
# if 语句
print( [x for x in range(10) if x % 2 == 0] )
# if else 语句
print( [ x if x % 2 == 0 else 0 for x in range(10) ] )

# ===========列表生成器================
# 这种一边循环一边计算的机制，称为生成器：generator
# 创建generator
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g = (x*x for x in range(10))
# 打印 generator
# 方法1
# print(next(g))
# print(next(g))
# print(next(g))
# 方法2
for item in g:
    print(item)
    


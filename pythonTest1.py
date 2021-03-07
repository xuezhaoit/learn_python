# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#Python 基础

#注释
#多行注释
'''
    print("多行注释")
'''
"""
    print("多行注释")
"""


#整数
# print(2**2)
#浮点数
#字符串多行换行
# print('''line1
# line2
# line3''')
#中文
# print('\u4e2d\u6587')
# ord()函数获取字符的整数表
# chr()函数把编码转换为对应的字符
# len()函数计算的是str的字符数
# print( ord("A") )
# print( chr(65)  )
# print( len("A") )
'''print( 'AF'.encode('ascii'))
print( '中国'.encode('UTF-8'))
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
'''

#布尔 True 和 False
# print(True)
#空字符串

print("123"[1:])



#变量

#list 和tuple
'''L = ['a','b','c']
print(L)
T = (1,2,3)
# T[0]=12
print(T[0])'''

# print("中国")
# if语句
# age=18
# if age>=18:
#     print('ault');
# elif 14<=age<18:
#     print('teen')
# else:
#     print("childs")

'''    
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
'''
# 自定义函数
'''
def test1(x):
    if x>0:
        print(222)
        return x;
    else:
        print(123)
        return -x;

print(test1(-19))
'''
# 递归函数
'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))        
'''        

#切片
'''
print(L[0:2])
print(L[-2:])
print(L[-2:-1])
'''

#迭代
'''from collections.abc import Iterable
print(isinstance('abc', Iterable))      # str是否可迭代
print(isinstance([1,2,3], Iterable))     # list是否可迭代
print(isinstance(123, Iterable))         # 整数是否可迭代'''

'''for item in L:
    print(item)
for i, item in enumerate(L):
    print(i, item)'''

#列表生成
'''print( list(range(1,11)) )
print( [ x for x in range(1,11) ] )
print( [ x*x  for x in range(1,11) if x % 2 == 0 ] )
print( [ x+y  for x in "AB" for y in "XYZ" ] )

d = {'x': 'A', 'y': '15', 'z': 'C' }
print([k + '=' + v.lower() for k, v in d.items()])
print([ k + '=' + v if v == "A" else "B" for k, v in d.items()])'''
##判断类型是不是字符串
'''d = {'x': 'A', 'y': 15 , 'z': 'C' }
for k,v in d.items():
    if isinstance(v, str) :
        print(k,v)'''

#生成器和迭代器

#高阶函数
##map和reduce
'''##绝对值
print(abs(-1))
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])#r是一个对象
print(list(r))
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))'''

#filter
'''def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))'''
#sorted
'''print(sorted([-2,4,-1,0,18,7]))
print(sorted([-2,4,-1,0,18,7], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))'''

#匿名函数lambda
print(list(map(lambda x: x*x, [1,2,3])))


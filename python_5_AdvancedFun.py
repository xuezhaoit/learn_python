# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


'''
    高阶函数：map/reduce、filter、sorted
    返回函数
    匿名函数
    装饰器
    偏函数
'''

# ---------高阶函数-------------
# -----------map--------------
# def fun1(args):
#     return args * args
# r = map(fun1, range(3))
# print (list(r))

# # ---------reduce-----------------
# def fun2(x,y):
#     return  x + y 
# from functools import reduce
# print (reduce(fun2,[1,2,3,4,5]))

# ---------filter----------------
def fun3(x):
    return x % 2 ==1

print(list(filter(fun3,[1,2,3,4,5,6])))

# ----------sorted--------------------
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))

# ---------返回函数-------------

# ---------匿名函数-------------
# lambda表示匿名函数
# lambda x: x * x 等效
# def f(x):
#     return x * x

# ---------装饰器-------------
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# ---------偏函数-------------
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
import functools
int2 = functools.partial(int, base=2)
print(int2('1010101'))






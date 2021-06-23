# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


'''
    调用函数
    定义函数
    函数参数
    递归函数
'''
# ======调用函数========
# print(abs(-20))
# print(max(1, 2))
# print(int(12.34))
# print(str(100))
# print(bool(1))

# =====定义函数=======  
# def
# def test(x):
#     if x > 0:
#         return x
#     else:
#         return -x    
# print ( test(-9) )
# # 空函数
# def test_pass():
#     pass
# # 参数检查
# print( isinstance("0.22",(int,float)) )

# 开根号
# import math
# print(math.sqrt(2))

# # 练习
# def quadratic(a, b, c):
#     x1 = (-b + math.sqrt(b*b-4*a*c))/2*a
#     x2 = (-b - math.sqrt(b*b-4*a*c))/2*a
#     return x1, x2

# # print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# ===========函数参数===============


# ============递归函数=============
# 注意防止栈溢出 fact(1000)
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# print (fact(1000))

# 尾递归优化,只是做了优化，但还是会导致栈溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, products):
    if num == 1:
        return products;
    return fact_iter(num-1, num*products)

# print(fact_iter(10, 1))
print(fact_iter(1000, 1))
        
        
    
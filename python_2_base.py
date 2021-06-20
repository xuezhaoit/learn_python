# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


'''
    数据类型和变量

    整数、浮点数
    字符串
    布尔值
    空值
    变量
'''
# ==============整数================
# 整数 十进制 -1 0 1 ； 十六制 0x
# 数字的分隔符
#print( 1_000_000 )
# 浮点数 科学计数法 1.2e3 1.2e-3
# print( 1.23333e3 )
# print( 1.2e-3 )


# ==============字符串================
# 转义 \' ; \n 换行； \t 制表； \\ 斜杠
# print (' Im \' OK  ')
# # 多行内容 
# print ('''
# line1 
# line2 
# ''')
# print(r'''
# hello
# world''')


# ==============布尔================
# True 和 False
# and、or和not运算
# print(True)
# print(not True)

# ===========空值=============
# 空值 None

# ===========变量=============
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# ============动态语言================ 
# 等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
# a = 123 # a是整数
# print(a)
# a = 'ABC' # a变为字符串
# print(a)
# ============静态语言================  
# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错
# int a = 123; // a是整数类型变量
# a = "ABC"; // 错误：不能把字符串赋给整型变量

#=========常量=========
# 常量就是不能变的变量

#=========除法===========
# # / 除法，结果为浮点数
# print(10 / 3)
# # //地板除取整，结果为整数
# print(10 // 3)
# # % 除法取余，结果为整数
# print(10 % 3)



'''
    字符串和编码
'''
# =======格式化===========
'''
常见的占位符有：
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数

用%%来表示一个%
'''
# print('Age: %s. Gender: %s' % (25, True))
#========f-string=========
# r = 2.5
# s = 3.14 * r ** 2
# print(f'The area of a circle with radius {r} is {s:.2f}')

'''
    list 和 tuple

'''
# ========list============
# list是一种有序的集合
classmates = ['Michael', 'Bob', 'Tracy']
# len()函数可以获得list元素的个数
print( len(classmates) )
# 索引是 0 开始
print( classmates[1] )
# insert 添加
classmates.insert(1,'123')
# 追加末尾

classmates.append('Adam')
print( classmates )
# pop 删除 classmates.pop(2)
classmates.pop()
print(classmates)

# ========tuple============
classmates1 = ('Michael', 'Bob', 'Tracy')

'''
    条件和循环
'''

'''
    dict 和 set
'''



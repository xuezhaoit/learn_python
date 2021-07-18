# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')



'''
    
文件读写
StringIO和BytesIO
操作文件和目录
序列化

'''

# ---------文件读写------------
# f = open('./iotest.txt', 'r')
# str = f.read()
# print(str)
# f.close()
# 测试IOError关闭文件
# with open('/path/to/file', 'r') as f:
#     print(f.read())
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
# f = open('./iotest.txt', 'r')
# str = f.readlines()
# for item in str:
#     print(item.strip())
#     print("---------")
# f.close()
# 二进制文件
#  f = open('/Users/michael/test.jpg', 'rb')
# 字符编码
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# 写入文件
# f = open('Writetest.txt', 'w')
# f.write('Hello, world!')
# f.close()

# ---------StringIO和BytesIO------------
# StringIO顾名思义就是在内存中读写str
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())
# BytesIO顾名思义就是在内存中读写字节
# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())



# ---------操作文件和目录------------
# Python内置的os模块也可以直接调用操作系统提供的接口函数。
# import os
# print (os.name) # posix操作系统类型Linux、Unix或Mac OS X，如果是nt，就是Windows
# print(os.uname()) #uname()系统详细信息 window没有
# print(os.environ)
# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))
# 然后创建一个目录:
# os.mkdir('./testdir')
# 对文件重命名:
# os.rename('test.txt', 'test.py')
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
# ---------序列化------------
# 变量从内存中变成可存储或传输的过程称之为序列化
import pickle
# d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d)
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()
# 反序列化
# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# print(d)
# f.close()

# JSON
import json
d = dict(name="Bob", age=20, score=88)
print(d)
print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json_str)
print(json.loads(json_str))
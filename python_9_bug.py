# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')



'''
    
错误处理
调试
单元测试
文档测试


'''
# --------错误处理----------
# try...except...finally...

# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# logging
# import logging
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)   
# main()
# print('END')
# --------调试----------
# loggin
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# pdb
# pdb.set_trace()
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
# --------单元测试----------
# --------文档测试----------


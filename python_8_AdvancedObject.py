# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')



'''
    
    使用__slots__
    使用@property
    多重继承
    定制类
    使用枚举类
    使用元类

'''
#--------- 使用__slots__-------------
# # __slots__-限制对象属性的定义
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

#--------- 使用@property-------------
# class Student(object):
    
#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.score = 60
# print(s.score)
# s.score = 9000

#--------- 多重继承-------------

#--------- 定制类-------------
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
# stu = Student('name1')
# print(stu)        

# __iter__
        
        

#--------- 使用枚举类-------------

#--------- 使用元类-------------
# type
from hello1 import Hello
h = Hello()
print(h.hello())
print( type(h) )
print( type(Hello) )





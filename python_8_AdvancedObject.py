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
# __slots__-限制对象属性的定义
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

#--------- 使用@property-------------

#--------- 多重继承-------------

#--------- 定制类-------------

#--------- 使用枚举类-------------

#--------- 使用元类-------------


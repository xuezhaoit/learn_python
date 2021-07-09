# # -*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')



'''
    类和实例
    访问限制
    继承和多态
    获取对象信息
    实例属性和类属性
'''

# --------类和实例---------------
# （Class）和实例（Instance）


# class Student(object):
#     def __init__(self, *args):
#         self.name = args[0]
#         self.score = args[1]
#     def print_score(self):
#         print("name: %s, score: %s" % (self.name, self.score))
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# s1 = Student('name23',90)
# print(s1)
# print(Student)
# print(s1.name)
# print(s1.print_score())
        
# ----------继承和多肽--------------
class Animal(object):
    def __init__(self, *args):
        pass
    def run(slef):
        print(' Animal is running ...')

class Cat(Animal):
    pass

cat = Cat()
cat.run()

# ------------获取对象信息-------------------
print(type(123))
print(type('str'))
print(type(object))
        





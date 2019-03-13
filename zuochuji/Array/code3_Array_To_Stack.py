# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_Array_To_Stack.py
@Time : 2019/3/13 15:03
'''

class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def size(self):
        return len(self.array)

    def pop(self):
        if self.size():
            return self.pop()
        return False

    def peek(self):
        if self.size():
            return self.array[-1]
        return False

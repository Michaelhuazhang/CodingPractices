# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_Array_toQueue.py
@Time : 2019/3/13 14:58
'''

class ArrayQueue():
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if len(self.array) == 0:
            print("The Queue is Empty!")
            return
        return self.array.pop(0)

    def peek(self):
        if len(self.array) == 0:
            print("The Queue is Empty!")
            return
        return self.array[0]

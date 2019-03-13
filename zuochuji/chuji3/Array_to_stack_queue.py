# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : Array_to_stack_queue.py
@Time : 2019/3/9 15:47
'''

# 用一个数组实现栈和队列

class Stack:
    def __int__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def push(self, item):
        self.array.append(item)

    def isEmpty(self):
        return self.array.size() == 0

    def pop(self):
        if self.isEmpty():
            return False

        return self.array.pop()

    def peek(self):
        if self.isEmpty():
            return False
        return self.array[-1]

class Queue:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def isEmpty(self):
        return len(self.array) == 0

    def pop(self):
        if self.isEmpty():
            return False

        return self.array.pop(0)

# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : getMinstack.py
@Time : 2019/3/9 15:54
'''

# 最小栈只需要另外申请一个空间，最小栈，
# 进栈的时候判断是否比当前栈顶小，若小，进栈，否则还是上次最小的数进栈

class minStack():
    def __init__(self):
        self.array = []
        self.minarray = []

    def push(self, item):
        self.array.append(item)
        if self.isEmpty(self.minarray):
            self.minarray.append(item)
        elif self.minarray[-1] > item:
            self.minarray.append(item)
        else:
            self.minarray.append(self.minarray[-1])

    def isEmpty(self, array):
        return  len(array) == 0

    def getmin(self):
        if self.isEmpty(self.minarray):
            return False
        return self.minarray[-1]

    def pop(self):
        if self.isEmpty(self.array):
            return False

        return  self.minarray.pop(), self.array.pop()



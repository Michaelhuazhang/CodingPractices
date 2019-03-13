# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_GetMinStack.py
@Time : 2019/3/13 15:54
'''

'''
实现一个特殊的栈，能够获得当前栈中最小元素

需要一个辅助栈：该辅助栈中存放当前最小元素
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, item):
        self.stack.append(item)
        # 最小栈，如果为空，进栈，不为空，比较当前元素和栈顶元素的大小
        if len(self.minstack) == 0:
            self.minstack.append(item)
        else:
            self.minstack.append(item if self.minstack[-1] > item else self.minstack[-1])

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("The Stack is Empty")
        self.minstack.pop()
        return self.stack.pop()

    def getMin(self):
        if len(self.stack) == 0:
            raise IndexError("The Stack is Empty")
        return self.minstack[-1]



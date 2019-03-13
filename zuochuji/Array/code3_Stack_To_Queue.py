# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_Stack_To_Queue.py
@Time : 2019/3/13 16:34
'''

'''
两个栈实现一个队列
进队，直接进
出队，第二个辅助栈不为空，弹出
      第二个辅助栈为空，将第一个栈中元素出栈，进第二个辅助栈，然后弹出
'''
class Stack_to_Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.push(item)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            raise IndexError("The Queue is Empty")
        if len(self.stack2):
            return self.stack2.pop()
        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            raise IndexError("The Queue is Empty")
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
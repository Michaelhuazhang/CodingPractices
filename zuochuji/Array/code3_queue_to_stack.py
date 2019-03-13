# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_queue_to_stack
@Time : 2019/3/13 16:02
'''

'''
两个队列实现一个栈

进栈，直接进队
出栈，将一个队的元素进入另一个队，只剩一个，将其弹出
取出栈顶元素，则将进队的所有元素出队到队2中，剩下一个为栈顶元素
# 加入队2中，然后再次进行交换两个队

'''
class Queue_to_stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if len(self.queue1) == 0:
            raise IndexError("The stack is Empty")
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))

        res = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def peek(self):
        if len(self.queue1) == 0:
            return
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        res = self.queue1.pop()
        self.queue2.append(res)
        self.queue2, self.queue1 = self.queue1, self.queue2
        return res


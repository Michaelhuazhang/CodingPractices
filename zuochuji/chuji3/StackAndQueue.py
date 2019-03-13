# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : StackAndQueue.py
@Time : 2019/3/9 16:07
'''

# 队列实现栈结构

# 两个队列，进队直接进，出队的时候将第一个队出队，只剩最后一个，返回
# 然后交换两个队


# 栈实现队列

# 进队的时候进一个栈
# 出队，第二个栈只要有数据直接弹出
# 没数据，将第一个栈中的元素加入到第二个栈中
# 出队的时候，弹出第二个队列的元素
# 若没有，将第一个栈的元素弹到第二个栈中

#

class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if len(self.queue1) < 0:
            return False
        for i in range(0, len(self.queue1)-1):
            self.queue2.append(self.queue1.pop(0))
        a = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return a

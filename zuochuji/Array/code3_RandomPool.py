# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_RandomPool.py
@Time : 2019/3/13 16:20
'''
'''
设计随机池
不重复插入，删除，等概论随机返回
'''
import random
class RandomPool:
    def __init__(self):
        self.keyIndex = dict()
        self.IndexKey = dict()
        self.size = 0

    def insert(self, key):
        '''
        不重复插入
        :param key:
        :return:
        '''
        if key not in self.keyIndex:
            self.size += 1
            self.keyIndex[key] = self.size
            self.IndexKey[self.size] = key

    def delete(self, key):
        '''
        将删除的元素和最后的元素交换，进行删除，否则再随机取出元素，将存在大量的空洞
        这样的操作保证了size 是连续的
        :param key:
        :return:
        '''
        if key in self.keyIndex:
            # 找到删除元素的值
            deleteindex = self.keyIndex[key]
            # 找到最后的键
            lastKey = self.IndexKey[self.size]
            self.keyIndex[lastKey] = deleteindex
            self.keyIndex.pop(key)

            self.IndexKey[deleteindex] = lastKey
            self.IndexKey.pop(self.size)
            self.size -= 1

    def getRandom(self):
        if self.size == 0:
            raise  IndexError("The Structure is Empty")
        randNum = random.randint(1, self.size)
        return self.IndexKey[random]

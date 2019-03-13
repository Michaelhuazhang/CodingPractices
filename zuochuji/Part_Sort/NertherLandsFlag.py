# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : NertherLandsFlag.py
@Time : 2019/3/13 10:40
'''

# 一个数组中，大于num放右边，小于num放左边
# 进阶，一堆数组中，小于num放左边，大于num放右边，等于num放中间

class Solution:
    def partition(self, array, num):
        '''
        less指针，cur指针遍历
        小于num，less+1，cur和less+1数组交换，cur+1
        否则，cur+1
        :param array:
        :param num:
        :return:
        '''
        if not array or len(array) < 2:
            return array
        less = -1
        for cur in range(len(array)):
            if array[cur] < num:
                less += 1
                array[less], array[cur] = array[cur], array[less]
        return array

    def partitionequalnum(self, array, num):
        '''
        less ， more， cur
        若cur小于num，进行交换，cur继续+1
        若cur大于num，more交换，cur 不动
        若相等，cur+1
        :param array:
        :param num:
        :return:
        '''
        if not array or len(array) < 2:
            return array
        less = -1
        more = len(array)
        cur = 0
        while cur < more:
            if array[cur] < num:
                less += 1
                array[less], array[cur] = array[cur], array[less]
                cur += 1
            elif array[cur] > num:
                more -= 1
                array[more], array[cur] = array[cur], array[more]
            else:
                cur += 1
        return array, less, more

    def generateRandom(self, length):
        import random
        a = []
        for i in range(length):
            a.append(random.randint(1, 100))
        return a

solu = Solution()
array = [20, 41, 12, 23, 20, 45, 20, 11, 45, 3]

print("排序前：", array)
print("小于num：", solu.partition(array, 20))
print("等于num：", solu.partitionequalnum(array, 20))
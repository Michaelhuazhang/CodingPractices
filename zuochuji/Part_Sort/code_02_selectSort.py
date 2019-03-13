# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_02_selectSort
@Time : 2019/3/13 9:24
'''
# 快速排序，选择一个最大的放到最终位置
# 时间复杂度为n^2
import random
class Solution:
    def selectSort(self, array):
        if not array or len(array) < 2:
            return array
        for i in range(len(array)-1, 0, -1):
            max_index = i
            for j in range(i):
                if array[max_index] < array[j]:
                    max_index = j
            array[max_index], array[i] = array[i], array[max_index]
        return array

    def generateRandom(self, length):
        array = []
        for i in range(length):
            array.append(random.randint(1, 100))
        return array
array = Solution().generateRandom(10)
print("排序前：", array)
print("排序后：", Solution().selectSort(array))
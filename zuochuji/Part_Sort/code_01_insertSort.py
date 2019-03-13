# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_01_insertSort.py
@Time : 2019/3/12 8:59
'''

# 插入排序，每次将一个元素，插入数组前面合适的位置上
# 稳定的排序
# 和数据初始状态有关
# 最好情况：O（N），平均和最差时间复杂度为O（N^2）
import random
class Solution:
    def insertSort(self, array):
        if not array or len(array) < 2:
            return array
        for i in range(1, len(array)):
            for j in range(i-1, -1, -1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                else:
                    break
        return array

    def generateRandomArray(self, length):
        array = []
        for i in range(length):
            array.append(random.randint(1, 100))
        return array

array = Solution().generateRandomArray(10)
print("排序前：", array)
print("排序后：", Solution().insertSort(array))

# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_00_bubbleSort.py
@Time : 2019/3/12 8:48
'''

# 冒泡排序
# 每一次将一个最大的元素放在数组后面
# 冒泡排序是和数据状况有关的，时间复杂度，最好：O（N），最差：O(N^2)
# 冒泡排序是稳定的排序方法
import random
class Solution:
    def bubbleSort(self, array):
        if not array or len(array) < 2:
            return array
        for i in range(len(array)-1, 0, -1):
            flag = False
            for j in range(i):
                if array[j] > array[j+1]:
                    flag = True
                    array[j], array[j+1] = array[j+1], array[j]
            if not flag:
                break
        return array

    def generateRandomArray(self, length):
        arr = []
        for i in range(length):
            arr.append(int(random.randint(1, 100)))# [1~100]
        return arr

array = Solution().generateRandomArray(10)
print("排序前：", array)
print("排序后：", Solution().bubbleSort(array))


# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : heapSort.py
@Time : 2019/3/12 9:11
'''

# 堆排序
# 建堆
# 调堆
# 排序
import random
class Solution:
    def insertHeap(self, array, index):
        '''
        # 将元素插入堆(大根堆)
        :param array: 数组(存放堆)
        :param index: 插入的索引
        :return:
        '''
        parent = (index - 1) >> 1
        while parent >= 0 and array[parent] < array[index]:
            array[parent], array[index] = array[index], array[parent]
            index = parent
            parent = (index - 1) >> 1

    def heapify(self, array, index, length):
        '''
        调整堆
        :param array: 数组存放堆
        :param length: 有效堆的长度
        :return:
        '''
        left = 2 * index + 1
        while left < length:
            # 记录左右子树哪一个最大
            largets = left + 1 if array[left+1] > array[left] and left + 1 < length else left
            largets = index if array[largets] < array[index] else largets
            if largets == index:
                break
            array[index], array[largets] = array[largets], array[index]
            index = largets
            left = 2 * index + 1

    def getMinkNums(self, array, k):
        '''
        返回一个数组中最小的K个元素，利用一个大小为k大根堆维护，小于堆顶，交换进行进堆，然后调整
        大根堆中存放的是最小的K个元素，因为比堆顶中最大的元素以及在剩余元素中不会出现
        :param array:
        :param k:
        :return:
        '''
        if not array or k <= 0 or len(array) <= k:
            return array
        res = [array[0]]
        for i in range(1, k):
            res.append(array[i])
            self.insertHeap(res, i)
        for i in range(k, len(array)):
            if res[0] > array[i]:
                res[0] = array[i]
                self.heapify(res, 0, k)
        return res

    def heapSort(self, array):
        if not array or len(array) < 2:
            return array
        for i in range(len(array)):
            self.insertHeap(array, i)
        size = len(array)-1
        array[0], array[size] = array[size], array[0]
        while size>0:
            self.heapify(array, 0, size)
            size -= 1
            array[0], array[size] = array[size], array[0]
        return array

    def generateRandomArray(self, length):
        array = []
        for i in range(length):
            array.append(random.randint(1, 100))
        return array


array = Solution().generateRandomArray(10)
print("排序前：", array)
print("排序后最小的三个元素：", Solution().getMinkNums(array, 3))
print("排序后：", Solution().heapSort(array))
#

# def josephus(n, k, m):
#     people = list(range(1,n+1))
#     i = k-1
#     for num in range(n, 0, -1):
#          i = (i+m-1) % num
#          print (people.pop(i))
#     return
# n, s, m = [i for i in  map(int, input().split())]
# josephus(n,s,m)

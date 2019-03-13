# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_04_QuickSort
@Time : 2019/3/13 9:35
'''

# 快排基于分治的思想，每次确定基准元素，小于放左边，大于放右边，然后递归处理左边和右边
#时间复杂度，最差情况就是有序用快排，是N^2,平均时间复杂度为O（N）

# 非递归的思路就是将继续需要排序的首尾进栈，不断弹栈，实现快排

class Solution:
    def quickSort_simple(self, array):
        if not array or len(array) == 0:
            return []
        else:
            pivot = array[0]
            left = self.quickSort_simple([i for i in array[1:] if i < pivot])
            right = self.quickSort_simple([i for i in array[1:] if i > pivot])
            return left + [pivot] + right

    def quickSort_stack(self, array):
        '''
        非递归需要借助栈，来进行压入待排序的收尾元素
        :param array:
        :return:
        '''
        if not array or len(array) == 0:
            return []
        if len(array) < 2:
            return array
        stack = []
        stack.append(len(array)-1)
        stack.append(0)
        while len(stack) != 0:
            l = stack.pop()
            r = stack.pop()
            index = self.partition_lr(array, l, r)
            if l < index-1:
                stack.append(index - 1)
                stack.append(l)
            if r > index + 1:
                stack.append(r)
                stack.append(index + 1)
        return array

    def partition_lr(self, array, start, end):

        pivot = array[start]

        while start < end:
            while start < end and array[end] > pivot:
                end -= 1
            array[start] = array[end]
            while start < end and array[start] < pivot:
                start += 1
            array[end] = array[start]
        array[start] = pivot
        return start

    def quickSort(self, array):
        if not array or len(array) < 2:
            return array
        p = self.partition_lr(array, 0, len(array) - 1)
        left = self.quickSort(array[:p])
        right = self.quickSort(array[p+1:])
        return left + [array[p]] + right

    def generateRandomArray(self, length):
        import random
        array = []
        for i in range(length):
            array.append(random.randint(1, 100))
        return array

a = Solution()
array = a.generateRandomArray(10)
print("排序前：", array)
print("Simple Version Quick Sort:", a.quickSort_simple(array))
print("Stack Version Quick Sort:", a.quickSort_stack(array))
print("Quick Sort:", a.quickSort(array))
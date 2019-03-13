# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_05_MergeSort.py
@Time : 2019/3/13 10:06
'''

# 归并排序时间复杂度NlogN
# 空间复杂度为O（N）
# 稳定

class Solution:
    def mergeSort(self, array):
        if not array or len(array) < 2:
            return array
        middle = int(len(array) / 2)
        left = self.mergeSort(array[:middle])
        right = self.mergeSort(array[middle:])
        return self.merge(left, right)

    def merge(self, left, right):
        c = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                c.append(left[i])
                i += 1
            else:
                c.append(right[j])
                j += 1
        if i == len(left):
            for x in right[j:]:
                c.append(x)
        if j == len(right):
            for x in left[i:]:
                c.append(x)
        return c

    def generateRandom(self, length):
        import random
        a = []
        for i in range(length):
            a.append(random.randint(1, 100))
        return a

solu = Solution()
array = solu.generateRandom(10)

print("排序前：", array)
print("排序后：", solu.mergeSort(array))
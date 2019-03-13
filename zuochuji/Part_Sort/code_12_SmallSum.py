# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_12_SmallSum
@Time : 2019/3/13 11:59
'''
'''
小和问题，就是一个数字比后面的小，产生小和
利用归并排序加速计算小和
逆序对的问题，同样如粗
'''
class Solution:
    def smallSum(self, array):
        if not array or len(array) < 2:
            return 0
        return self.mergeSort(array, 0 , len(array) - 1)

    def mergeSort(self, array, left, right):
        if left == right:
            return 0
        mid = left + ((right - left) >> 1 )
        return self.mergeSort(array, left, mid) + self.merge(array, left, mid, right) + self.mergeSort(array, mid+1, right)

    def merge(self, array, left, mid, right):
        help = [0 for i in range(right-left+1)]
        res = 0
        p1 = left
        p2 = mid + 1
        index = 0
        while p1 <= mid and p2 <= right:
            res += array[p1] * (right - p2 + 1) if array[p1] < array[p2] else 0
            if array[p1] < array[p2]:
                help[index] = array[p1]
                p1 += 1
                index += 1
            else:
                help[index] = array[p2]
                p2 += 1
                index += 1
        while p1 <= mid:
            help[index] = array[p1]
            index += 1
            p1 += 1
        while p2 <= right:
            help[index] = array[p2]
            index += 1
            p2 += 1
        for i in range(len(help)):
            array[left + i ] = help[i]
        return res

    def generateRandom(self, length):
        import random
        a = []
        for i in range(length):
            a.append(random.randint(1, 100))
        return a

solu = Solution()
# array = solu.generateRandom(10)
array = [ 1, 2, 3, 4]
print("排序前：", array)
print("排序后：", solu.smallSum(array))
# 1*3 + 2 *2+ 3=10
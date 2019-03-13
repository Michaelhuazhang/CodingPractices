# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_FindNumInSortedMatrix.py
@Time : 2019/3/13 15:34
'''

'''
一个特殊数组，从左到右递增
从上到下递增
目标从中查找到一个数

利用其特质，从左上方或者右下方进行查找

这里我们从右下方开始查找:如果当前元素小于num，向右查找
                        如果当前元素大于num，向上查找
                        

'''
class Solution:
    def isContains(self, array, k):
        if not array or len(array) == 0:
            return -1
        curleft = len(array) - 1
        curright = 0
        while curleft >= 0 and curright <= len(array[0]) - 1:
            if array[curleft][curright] > k:
                curleft -= 1
            elif array[curleft][curright] < k:
                curright += 1
            else:
                return curleft, curright

matrix = [
	[0, 1, 2, 3, 4, 5, 6],
	[10, 12, 13, 15, 16, 17, 18],
	[23, 24, 25, 26, 27, 28, 29],
	[44, 45, 46, 47, 48, 49, 50],
	[65, 66, 67, 68, 69, 70, 71],
	[96, 97, 98, 99, 100, 111, 122],
	[166, 176, 186, 187, 190, 195, 200],
	[233, 243, 321, 341, 356, 370, 380]
	]
k =  200
print(Solution().isContains(matrix, k))

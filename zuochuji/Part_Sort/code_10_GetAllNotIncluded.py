# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_10_GetAllNotIncluded
@Time : 2019/3/13 11:24
'''

class Solution:
    def getallnotIncluded(self, array1, array2):
        res = []
        for i in range(len(array2)):
            l = 0
            r = len(array1) - 1
            contains = False
            while l < r:
                mid = l + ((r - l) >> 1)
                if array1[mid] == array2[i]:
                    contains = True
                    break
                if array1[mid] > array2[i]:
                    r = mid - 1
                else:
                    l = mid + 1
            if not contains:
                res.append(array2[i])
        return res


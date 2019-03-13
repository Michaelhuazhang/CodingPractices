# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : pingduoduo.py
@Time : 2019/3/10 15:51
'''
import sys

# n = int(sys.stdin.readline().strip())
# line = sys.stdin.readline().strip()
# array1 = list(map(int, line.split()))
# line = sys.stdin.readline().strip()
# array2 = list(map(int, line.split()))
# a = sorted(array1, reverse=False)
# b = sorted(array2, reverse=True)
# sums = 0
# for i in range(len(a)):
#     sums += a[i] * b [i]
# print(sums)

import collections
# line = sys.stdin.readline().strip()
# class Solution:
#     # Time complexity(O(N^2))
#
#     def delete_nth_naive(self, array, n):
#         ans = []
#         for i in array:
#             if ans.count(i) < n:
#                 ans.append(i)
#         return ans
#
#     # Time Completity O(N)
#     def delete_nth(self, array, n):
#         result = []
#         counts = collections.defaultdict(int)
#         for i in array:
#             if counts[i] < n:
#                 result.append(i)
#                 # print(counts)
#                 counts[i] += 1
#                 # print(counts)
#         return result
# array = list(line.lower())
# s = Solution()
# array  = s.delete_nth_naive(array, 1)
# array = sorted(array)
# print(array[0])
#
#
class Solution_3():
    def getmaxsum(self, array, d):
        maps = {}
        # 金额， 位置
        for i in range(len(array)):
            maps[array[i][1]] = array[i][0]
        temp = -sys.maxsize
        for i in range(len(array)):
            temp = max(temp, array[i][1])
        index = maps[temp]

        sums = -sys.maxsize
        for i in range(len(array)):
            if array[i][0] == index:
                continue
            if abs(index - array[i][0]) >= d:
                sums = max(sums, temp + array[i][1])
        return sums








line = sys.stdin.readline().strip()
n, d = list(map(int, line.split()))[0], list(map(int, line.split()))[1]
array = []
for i in range(n):
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    array.append(a)
sums = Solution_3().getmaxsum(array, d)
print(sums)
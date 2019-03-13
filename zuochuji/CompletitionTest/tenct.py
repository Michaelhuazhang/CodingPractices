# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : tenct
@Time : 2019/3/10 19:12
'''
import sys

class Solution:
    def getmin(self, array):

        res = []
        for i in range(1, len(array)):
            mins = sys.maxsize
            temp = sys.maxsize
            for j in range(0, i):

                if abs(array[i] - array[j]) < mins:
                    mins = abs(array[i] - array[j])
                    temp = min(temp, j+1)

            res.append([mins, temp])

        return res

    def gettime(self, array):
        f = [[0 for i in range(len(array) + 1)] for j in range(2)]
        a = [i for i in array]
        for i in range(1, len(array) +1):
            f[0][i] = min(f[1][i-1], f[0][i-1]) + a[i-1]
            f[1][i] = min(f[0][i-1], f[0][i-2])
        return min(f[0][len(array)], f[1][len(array)])

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
array = list(map(int, line.split()))

res = Solution().getmin(array)
for i in range(n-1):
    print(str(res[i][0]) + "  " + str(res[i][1]))






# n = int(sys.stdin.readline().strip())
# array = []
# for i in range(n):
#     array.append(int(sys.stdin.readline().strip()))
# res = Solution().gettime(array)
# print(res)




# line = sys.stdin.readline().strip()
# n, a = list(map(int, line.split()))[0], list(map(int, line.split()))[1]
#
# line = sys.stdin.readline().strip()
# array = list(map(int, line.split()))



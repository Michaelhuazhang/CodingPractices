# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : cutMoney.py
@Time : 2019/3/11 22:01
'''

# 两个数组，一个代表代价数组，花费多少钱
# 另一个代表数组，代表利润
# 启动资金，利用启动资金做项目

# 花费组成一个小根堆，只要花费小于启动资金，弹出，弹出的放入，按照收益排成大根堆
# 大根堆弹出，作为投资

import heapq
class Node:
    def __init__(self,  profit, cost):
        self.cost = cost
        self.profits = profit



class Solution:
    def lessMoney(self, array):
        if not array:
            return None
        heapq.heapify(array)
        sums = 0
        cur = 0
        while (len(array) > 1):
            cur = heapq.heappop(array) + heapq.heappop(array)
            print(array, cur)
            sums += cur
            print(sums)
            heapq.heappush(array, cur)
        return sums

    def findMaxmizedCapital(self, k, w, profits, costs):
        '''

        :param k: k projects
        :param w: Money we have begin
        :param profits: the project can make
        :param costs:  the project need to cost
        :return: the max money we do k projects
        '''
        nodes = []
        for i in range(len(profits)):
            nodes.append(Node(profits[i], costs[i]))
        heapq.heapify()

array = [5, 3, 1, 2, 4]
print(Solution().lessMoney(array))



# heapq.heapify(array)
# print(array)
# print(len(array))
# print(heapq.heappop(array))
# print(heapq.heappop(array))
# print(heapq.nlargest(1, array, key=lambda x:x[1]))

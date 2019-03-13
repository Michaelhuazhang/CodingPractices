# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : print_matrix.py
@Time : 2019/3/9 19:22
'''
# 打印每一条边
# 左上右下，各自调整

# 正方形，顺时针旋转90C

# 之子字形打印
# A点往右，然后往下
# B点往下，然后向右


# def solution(n, s, m):
#     people = [i+1 for i in range(n)]
#     num = n
#     for i in range(num-1):
#         if s == 0:
#             s = (s+m)%num
#         else:
#             s = (s+m-1)%num
#         print(people[s-1])
#         for j in range(s, num):
#             if j < 0:
#                 break
#
#             people[j-1] = people[j]
#         num -= 1
#     print(people[0])
# n, s, m = [i for i in  list(map(int, input().split()))]
# solution(n,s,m)



def josephus(n, k, m):
    people = list(range(1,n+1))
    i = k-1
    for num in range(n, 0, -1):
         i = (i+m-1)%num
         print (people.pop(i))
    return
n, s, m = [i for i in  list(map(int, input().split()))]
josephus(n,s,m)
from collections import deque
def maxsum(array, m):
    maps = {}
    for i, v in enumerate(array):
        maps[v] = array.delete(i+1)
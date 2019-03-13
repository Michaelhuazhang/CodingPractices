# -*- encoding:utf-8 -*-

'''
@Author:ZJH
@concat:jianhua-zhang@qq.com
@SoftWare:Pycharm
@file:chuji3.py
@Time:2019/3/9 15:23
'''

#  判断一个数组排序后，相邻两数的最大差值

# n个数，准备n+1一个桶
# 遍历数组，找到最小值和最大值，若最大等于最小->0
# 最小值放在第一个桶，最大数放最后面的桶
# 必然存在一个空桶
# 否定最大差值来自同一个桶

# 每个桶要含有是否有数，最大值，有最小值


# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code2_KMP.py
@Time : 2019/3/13 14:44
'''

'''
给定两个字符串，返回第二个字符串在第一个字符串中的位置

'''
class Solution:
    def getNextArray(self, match):
        '''
        基于match 生成next数组
        :param match: 匹配串
        :return: 返回next数组
        '''
        if len(match) == 1:
            return [-1]
        nextArray = [-1, 0]
        cn = 0 # 表示前一个字符最长匹配前缀的长度
        while len(nextArray) < len(match):
            if match[len(nextArray) - 1] == match[cn]:# 当前next数组最后一个核前一个是否相等
                cn += 1
                nextArray.append(cn)
            elif cn > 0:
                cn = nextArray[cn]
            else:
                nextArray.append(0)
# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : treestr.py
@Time : 2019/3/11 21:25
'''

# 将一个字符串构造出一颗树
# 计算每次字符串结尾的数据 ->找到多少个以该字符结尾的数据项
# 有多少个字符串开头的 ->  到一次，累计一次

# 字符串树，那么每个节点有26个


# 拼接后的字符串最小的拼接结果是什么？

#
# import operator as op
#
# print(op.gt("zjhl", "zjhk"))
# print(op.eq("ac" + "acv", "ac" + "acz"))
a, b = map(str, input().split())
print(a, b)
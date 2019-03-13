# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : tree_isBalance.py
@Time : 2019/3/11 16:27
'''
# 判断一颗二叉树是否是平滑二叉树
# 任意一个结点左子树和右子树的高度差不超过1个结点
# 递归思想很重要
# 考查每一个结点的整棵子树是否满足平衡
# 判断左树是否平衡，右树是否平衡，左右子树的高度


#
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class ReturnData():
    def __init__(self, isB, h):
        self.isB = isB
        self.h = h

class Solution:
    def process(self, head):
        if not head:
            return ReturnData(True, 0)

        leftData = self.process(head.left)
        if not leftData.isB:
            return ReturnData(False, 0)
        rightData = self.process(head.right)
        if not rightData.isB:
            return ReturnData(False, 0)
        if abs(leftData.h - rightData.h) > 1:
            return ReturnData(False, 0)
        return ReturnData(True, max(leftData.h, rightData.h) + 1)
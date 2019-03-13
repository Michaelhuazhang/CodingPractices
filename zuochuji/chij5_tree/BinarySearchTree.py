# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : BinarySearchTree.py
@Time : 2019/3/11 16:40
'''

# 判断一颗二叉树是否是二叉排序树

# 中序遍历是升序的，判断一颗二叉树的中序遍历为升序


# 判断一颗树是否是完全二叉树
# 遍历的过程中，发现一棵二叉树如果出现有右没左，那么False
# 任意一个结点发现左右不是都有，那么接下来所有结点都是叶子节点


# 求一棵完全二叉树的结点的个数

# 首先：遍历整棵树的左边界，判断二叉树的高度
# 遍历右子树的左边界是否到达最后一层，到达最后一层，左子树是满的
# 没到，右子树是满的
# 复杂度：每一层只遍历一个结点
# logN的平方



import sys
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

# 树的中序遍历：将树入栈，栈中不为空或者当前节点不为空，进栈
# 如果左子树存在，进栈，如果左子树不存在，弹出，转为右子树
# 打印的时机进行判断一下
class Solution:
    def isBST(self, head):
        pre = -sys.maxsize
        if head != None:
            stack = []
            while len(stack) != 0 or head:
                if head:
                    stack.append(head)
                    head = head.left
                else:
                    head = stack.pop()
                    if pre > head.val:
                        return False
                    pre = head.val
                    head = head.right
        return True

    def isCBT(self, root):
        if not root:
            return True
        queue = []
        leaf = False
        queue.append(root)
        while len(queue) != 0:
            head = queue.pop(0)
            leftc = head.left
            rightc = head.right
            # 如果是叶子节点，不能存在左子树和右子树/出现右子树但是没有左子树   -> 这两种情况都会返回False
            if (leaf and (not leftc or not rightc)) or (rightc and not leftc):
                return False
            if leftc:
                queue.append(leftc)
            if rightc:
                queue.append(rightc)
            else:
                leaf = True
        return True

    def nodeNum(self, root):
        if not root:
            return 0
        return self.bs(root, 1, self.mostleftLevel(root, 1))

    def bs(self, node, level, height):
        '''

        :param node: 当前节点
        :param level: 当前节点所在的层数
        :param height: # 当前节点的深度
        :return: 返回该节点下的结点个数
        '''
        if level == height:
            return 1
        if self.mostleftLevel(node.right, level+1) == height:
            # 左子树是满的 + 当前节点
            return 1 << (height - level) + self.bs(node.right, level+1, height)
        else:
            # 右子树是满的 + 当前节点
            return 1 << (height - level - 1) + self.bs(node.left, level+1, height)

    def mostleftLevel(self, root, level):
        while root:
            level += 1
            root = root.left
        return level - 1
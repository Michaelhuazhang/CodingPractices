# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code_11_MaxGap
@Time : 2019/3/13 11:29
'''

'''
分成n+1个桶，首先找出最小和最大值分别放在第一个桶和最后一个桶，
剩下的n-1个桶按照数组的最大和最小值平均分。
当数组元素大于2时，排序之后的相邻元素的最大差值肯定不是存在于同一个桶内，
因此只需存储每个桶内的最大和最小值，以及该桶内是否有元素（1表示有，0表示没有），
从而遍历多个桶，求后一个桶最小值与前一个桶最大值之间的差值，返回最大的那个，即为最终所求的结果。
此时时间复杂度为O(n)，且不是基于比较的排序。

分桶只是为了否定最大差值来自同一个桶内部

会导致存在多个空桶
遍历上一个桶的最大值和下一个非空桶最小值
'''
import sys
class Solution:
    def maxgap(self, nums):
        if not nums or len(nums) < 2:
            return nums
        maxs = -sys.maxsize
        mins =  sys.maxsize
        for i in nums:
            maxs = max(maxs, i)
            mins = min(mins, i)
        if maxs == mins:
            return 0
        # 记录该桶是否有元素
        hasNum = [False for i in range(len(nums) + 1)]
        # 记录该桶的最大元素
        maxsall = [0 for i in range(len(nums) + 1)]
        # 记录该桶的最小元素
        minsall = [0 for i in range(len(nums) + 1)]
        bid = 0
        lens = len(nums)
        for i in range(lens):
            # 划分到哪个桶
            bid = self.bucket(nums[i], lens, mins, maxs)
            #进行更新该桶的最大和最小值
            minsall[bid] = nums[i] if not hasNum[bid] else min(nums[i], minsall[bid])
            maxsall[bid] = nums[i] if not hasNum[bid] else max(nums[i], maxsall[bid])
            hasNum[bid] = True
        # 记录最大差值
        res = 0
        lastMaxs = maxsall[0]
        for i in range(1, len(nums) + 1):
            if hasNum[i]:
                res = max(res, minsall[i] - lastMaxs)
                lastMaxs = maxsall[i]
        return res




    def bucket(self, num, len, mins, maxs):
        return int(len * (num - mins) / (maxs - mins))


print(Solution().maxgap([1, 2, 4, 7, 9, 5, 50, 12, 56, 42]))
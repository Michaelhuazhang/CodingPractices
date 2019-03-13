# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : wangyi.py
@Time : 2019/3/9 21:47
'''

# -*- encoding:utf-8 -*-

'''
@Author:ZJH
@concat:jianhua-zhang@qq.com
@SoftWare:Pycharm
@file:wangyi1.py
@Time:2019/3/9 14:39
'''
import sys

class Solution:
    def mat_inter(self, box1, box2):
        x01, y01, x02, y02 = box1
        x11, y11, x12, y12 = box2
        lx = abs((x01 + x02) / 2 - (x11 + x12) / 2)
        ly = abs((y01 + y02) / 2 - (y11 + y12) / 2)
        sax = abs(x01 - x02)
        sbx = abs(x11 - x12)
        say = abs(y01 - y02)
        sby = abs(y11 - y12)
        if lx <= (sax + sbx) / 2 and ly <= (say + sby) / 2:
            return True
        else:
            return False

    def solve_coincide(self, box1, box2):
        if self.mat_inter(box1, box2) == True:
            x01, y01, x02, y02 = box1
            x11, y11, x12, y12 = box2
            col = min(x02, x12) - max(x01, x11)
            row = min(y02, y12) - max(y01, y11)
            intersection = col * row
            area1 = (x02 - x01) * (y02 - y01)
            area2 = (x12 - x11) * (y12 - y11)
            coincide = area1 + area2 - intersection
            return coincide
        else:
            return 0

n = int(sys.stdin.readline().strip())
res = []
answer = Solution()
for i in range(n):
    # 读取每一行
    b = int(sys.stdin.readline().strip())
    all_mat = []
    for j in range(b):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        all_mat.append(values)
    ans = 0
    for k in range(b):
        for m in range(k+1, b):
            if answer.mat_inter(all_mat[k], all_mat[m]) == True:
                ans += answer.solve_coincide(all_mat[k], all_mat[m])
                break
    res.append(res)
    print(ans)

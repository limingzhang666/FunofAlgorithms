# -*- coding: utf-8 -*-
"""
@Time : 2020/6/12 14:16
@Author : liming
@Email : laimingcham@163.com
@File : handoutCandy.py
@Project : FunofAlgorithms
@Desc: 
"""

"""
题目：已知一些孩子和一些糖果，每个孩子有需求因子g，每个糖果有大小s，
 当某个糖果的大小s>=某个孩子的需求因子g时，代表该糖果可以满足该孩子， 求使用这些糖果，最多能满足多少孩子（注意，某个孩子最多只能用1个糖果满足）
"""


class Solution:
    def findContentChild(self, g, s):
        """

        :param g:  需求因子
        :param s:  糖果的大小
        :return:
        """
        g = sorted(g)
        s = sorted(s)
        childIndex = 0
        cookieIndex = 0
        while childIndex < len(g) and cookieIndex < len(s):
            # 如果 当前需求因子<= 糖果大小，说明可以孩子被满足，则 孩子加1，糖果+1
            if g[childIndex] <= s[cookieIndex]:
                childIndex += 1
            cookieIndex += 1
        return childIndex


if __name__ == '__main__':
    g = [5, 10, 2, 9, 15, 9]
    s = [6, 1, 20, 3, 8]
    S = Solution()
    result = S.findContentChild(g, s)
    print("最多能满足 个小孩", result)

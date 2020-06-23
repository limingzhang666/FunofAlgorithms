# -*- coding: utf-8 -*-
"""
@Time : 2020/6/23 15:09
@Author : liming
@Email : laimingcham@163.com
@File : climbstairs.py
@Project : FunofAlgorithms
@Desc:  动态规划-爬楼梯问题
"""

"""

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
分析:
      假定n=10,首先考虑最后一步的情况,要么从第九级台阶再走一级到第十级,要么从第八级台阶走两级到第十级,因而,要想到达第十级台阶,最后一步一定是从第八级或者第九级台阶开始.也就是说已知从地面到第八级台阶一共有X种走法,从地面到第九级台阶一共有Y种走法,那么从地面到第十级台阶一共有X+Y种走法.
即F(10)=F(9)+F(8)
     分析到这里,动态规划的三要素出来了.
        边界:F(1)=1,F(2)=2
        最优子结构:F(10)的最优子结构即F(9)和F(8)
        状态转移函数:F(n)=F(n-1)+F(n-2)

原文链接：https://blog.csdn.net/htbeker/article/details/102566986

"""

import numpy as np
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        # 斐波那契公式
        # sqrt5 = math.sqrt(5)
        # fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        # return int(fibn // sqrt5)

        '''
        暴力法
        # 超时
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''

        # 动态规划
        # 52 ms	13.6 MB
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1] + [2] + [False] * (n - 2)
        # print(dp)
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    '''
        Binets 方法
        # 120 ms	28.8 MB
        q = np.mat([[1, 1], [1, 0]])
        res = self.matPow(q, n)
        return res.tolist()[0][0]

    def matPow(self, q, n):
        ret = np.mat([[1, 0], [0, 1]])
        while n:
            if n & 1 == 1:
                ret = np.dot(ret, q)
            n >>= 1
            q = np.dot(q, q)

        return ret
    '''


# 链接：https: // leetcode - cn.com / problems / climbing - stairs / solution / guan - fang - ti - jie - pythonshi - xian - by - hialiens /

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))

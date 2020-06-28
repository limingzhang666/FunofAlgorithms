# -*- coding: utf-8 -*-
"""
@Time : 2020/6/23 18:43
@Author : liming
@Email : laimingcham@163.com
@File : miniEditDistance.py
@Project : FunofAlgorithms
@Desc: 
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        print('n:', n)
        m = len(word2)
        print('m:', m)
        # 有一个字符串为空串
        if n * m == 0:
            return n + m

            # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]
        print('D:', D)

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                # min_sum= min(left, down, left_down)
                D[i][j] = min(left, down, left_down)
                print(i, j, D[i][j])

        return D[n][m]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('zhang', "zhou"))

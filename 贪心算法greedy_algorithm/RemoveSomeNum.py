# -*- coding: utf-8 -*-
"""
@Time : 2020/6/12 17:39
@Author : liming
@Email : laimingcham@163.com
@File : RemoveSomeNum.py
@Project : FunofAlgorithms
@Desc: 
"""

"""
题目：已知一个使用字符串表示非负整数num，将num中的k个数字移除，求移除k个数字后，可以获得的最小的可能的新数字(num不会以0开头，num长度小于10002)

例如：输入：num = “1432219”,k=3 
在去掉3个数字后得到的很多可能里，如1432，4322，2219，1219。。。。；去掉数字4、3、2、得到的1219最小

思考与分析： 

一个长度为n的数字，去掉k个数字，可以有多少种可能？C(k,n)=n!/(n−k)!∗k!C(k,n)=n!/(n−k)!∗k!种可能 
所以用枚举法肯定是不可能的。 
若去掉某一位数字，为了使得到的新数字最小，需要尽可能让得到的新数字优先最高位最小，其次次位最小，再其次第三位最小。。。。

例如：一个四位数 “1。。。”，一定比任何“9.。。。”小。 
一个四位数若最高位确定，如“51。。”一定比任何“59。。”、“57。。”小。

贪心规律：
 
从高位向地位遍历，如果对应的数字大于下一位数字，则把该位数字去掉，得到的数字最小。
"""


class Solution:
    def removeKNums(self, nums, k):
        s = []
        # 将nums的string转换成为  list
        nums = list(map(int, nums))
        print(nums)
        # 循环遍历每个 数字
        for i in range(len(nums)):
            number = int(nums[i])
            print(number)
            # 从高位往地位遍历，如果当前数字大于下一位数字，则应该被去掉
            # 先判断出是否需要 pop，再去 push
            while len(s) != 0 and s[len(s) - 1] > number and k > 0:
                s.pop(-1)
                k -= 1

            if number != 0 or len(s) != 0:
                s.append(number)
        print(s)
        # while len(s) != 0 and k > 0:
        #     s.pop(-1)
        #     k -= 1
        # result = ""
        result = ''.join(str(i) for i in s)
        return result


if __name__ == '__main__' :
    s = Solution()
    print(s.removeKNums("1432219", 2))

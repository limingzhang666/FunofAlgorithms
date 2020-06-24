# -*- coding: utf-8 -*-
"""
@Time : 2020/6/24 10:46
@Author : liming
@Email : laimingcham@163.com
@File : googleEquation.py
@Project : FunofAlgorithms
@Desc: 穷举搜索Google方程式

"""
"""
# 问题：有一个由字符组成的等式。WWWDOT-GOOGLE=DOTCOM，每个字符代表一个0~9之间的数字，
# WWWDOT、GOOGLE和DOTCOM都是合法的数字，不能以0开头。
# 请找出一组字符和数字的对应关系，使它们互相替换，并且替换后的数字能够满足等式。
# 解答：
# 777589-188103=589486
"""

import time


class Solution:
    USE_MY_ISVALUE = 1


    def OnCharListReady(self, char_items):
        """
        判断结果是否满足，如果满足则 print
        :param char_items:  各个字母所代表值 的二元数组
        :return:
        """
        minuend = "WWWDOT"
        subtrahead = "GOOGLE"
        diff = "DOTCOM"

        m = self.MakeIntegerValue(char_items, minuend)
        s = self.MakeIntegerValue(char_items, subtrahead)
        d = self.MakeIntegerValue(char_items, diff)
        if (m - s) == d:
            print(str(m) + "-" + str(s) + "=" + str(d))


    def MakeIntegerValue(self, char_items, caluStr):
        """
         将 字符串变成 int数值，用于后面计算验证
        :param char_items:  各个字母所代表值 的二元数组
        :param string:  需要转换为int数值的 字符串，例：WWWDOT
        :return:
        """
        strLen = caluStr.__len__()
        result_list = []
        # 垃圾方法看着难受死了，都不知道怎么计算的
        # for i in range(0, strLen):
        #     for item in char_item:
        #         # ['W', 3, True],这个就是 item， item[0]代表字母，item[1]代表其对应的值 ，例如3
        #         if caluStr[i] == item[0]:
        #             int_value *= 10
        #             int_value += item[1]

        """先将 字母的字符串转换成 其代表数字的字符串，然后将str-> int强转换就好了 """
        for i in range(0, strLen):
            for item in char_items:
                if caluStr[i] == item[0]:
                    result_list.append(item[1])
        result_str = ''.join(str(i) for i in result_list)
        # print('resultStr', result_str)
        return int(result_str)

    def IsValueVaild(self, char_Item, value_Item):
        """
        剪枝评估函数
        其实就是校验
        :param char_Item: 如[W,-1,False]
        :param value_Item: 如[0，False]，[1,False]
        :return:
        """
        #
        if value_Item[0] == 0:
            # if self.USE_MY_ISVALUE:
                # 开始位置的数字不能是0，也就是W、G和D这三个字母不能是0，
            if char_Item[0] == 'W' or char_Item[0] == 'D' or char_Item[0] == 'G':
                    return False
            else:
                # 如果当前位置是0，且当前字母不是wdg，  返回 （！leading），
                return not char_Item[2]
        # 如果当前位置不是0，则判断当前值是否被使用过
        return not value_Item[1]


    def SearchResult(self, char_items, char_values, index, callback):
        """
        :param char_items:  二维数组，包含每个 字母代表的值
        :param char_values:  0~9 以及使用情况 的数组
        :param index:  鸡肋
        :param callback: 每次循环迭代完后的  一个 校验结果是否满足的 方法
        :return:
        """
        max_char_count = char_items.__len__()
        # 0~9 长度是10
        max_number_count = char_values.__len__()

        # 如果
        if index == max_char_count:
            callback(char_items)
            return
        for i in range(max_number_count):
            if self.IsValueVaild(char_items[index], char_values[i]):
                char_values[i][1] = True  # 设置使用标志
                char_items[index][1] = char_values[i][0]
                self.SearchResult(char_items, char_values, index + 1, callback)
                char_values[i][1] = False  # 清除使用标志


if __name__ == '__main__':
    s = Solution()
    # 字符元素列表
    char_item = [
        ['W', -1, True], ['D', -1, True], ['O', -1, False],
        ['T', -1, False], ['G', -1, True], ['L', -1, False],
        ['E', -1, False], ['C', -1, False], ['M', -1, False],
    ]
    # # 字符元素列表
    char_value = []
    for i in range(10):
        char_value.append([i, False])
    print(char_value)

    start = time.perf_counter()
    s.SearchResult(char_item, char_value, 0, s.OnCharListReady)
    end = time.perf_counter()
    print("使用了: %f s" % (end - start))

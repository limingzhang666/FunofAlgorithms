#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: yinshi
@contact:laimingcham@163.com
@version: 1.0.0
@license: Apache Licence
@file: transChinese2Num.py
@time: 2020/6/28 18:11
@desc:
https://www.jianshu.com/p/033d7aadba30
"""

"""
中文数字转换成阿拉伯数字的算法实现， 首先要做两件事情， 
一件是将中文数字转换成阿拉伯数字，
另一件事情就是将中文权位转换成10的倍数。 中文数字转换成阿拉伯数字可以通过反查chnNumChar表实现
"""


class Solution:
    chn_value_pair = [["十", 10, False], ["百", 100, False], ["千", 1000, False], ["万", 10000, True],
                      ["亿", 100000000, True]]
    '''中文数字表'''
    chnNumChar = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']

    # chnNumChar_map = []
    # for index, value in enumerate(chnNumChar):
    #     chnNumChar_map.append([value, index])
    # print(chnNumChar_map)

    def ChineseToValue(self, chn_str):
        """
        返回中文数字汉字所对应的阿拉伯数字，若str不为中文数字，则 返回-1

        :param chn_str:
        :return:
        """
        for index, value in enumerate(self.chnNumChar):
            if chn_str == value:
                return index
        return -1

    def ChnUnitToValue(self, chn_str):
        """
        返回中文汉字权位在chnNameValue数组中所对应的索引号，若不为中文汉字权位，则返回-1

        :param chn_str:
        :return:
        """
        # for index, (x, y, z) in enumerate(self.chn_value_pair):
        for index, value in enumerate(self.chn_value_pair):
            # print('value', value)
            if chn_str == value[0]:
                return index
        return -1

    def ChineseToNum(self, chineseStr):
        """
        返回中文数字字符串所对应的int类型的阿拉伯数字
        :param chineseStr:
        :return:
        """
        rtn = 0
        section = 0
        number = 0
        secUnit = False
        pos = 0
        while pos < len(chineseStr):
            # 1.当 当前中文字符对应的是：   中文的 0~9的数字时候，处理方式 是：
            alabo_num = self.ChineseToValue(chineseStr[pos:pos + 1])
            if alabo_num >= 0:
                '''1. 若num>=0，代表该位置（pos），所对应的是数字不是权位。若小于0，则表示为权位'''
                number = alabo_num
                pos += 1
                # pos是最hou一位，直接结束
                if pos >= len(chineseStr):
                    section += number
                    rtn += section
                    break
            else:
                '''2 当前中文 文字对应的是：十 百 千 万 亿'''
                chnNameValueIndex = self.ChnUnitToValue(chineseStr[pos:pos + 1])

                secUnit = self.chn_value_pair[chnNameValueIndex][2]
                unit = self.chn_value_pair[chnNameValueIndex][1]
                if secUnit:
                    '''2.1  当前中文对应的 是节权位(万，亿)，说明一个节 已经结束'''

                    '''chnNameValue[chnNameValueIndex].secUnit==true，表示该位置所对应的权位是节权位，'''
                    section = (section + number) * unit
                    rtn += section
                    section = 0
                else:
                    '''2.2 当前中文 对应的是 十 百  千'''
                    section += number * unit
                number = 0
                pos += 1
                if pos >= len(chineseStr):
                    rtn += section
                    break
        return rtn


if __name__ == '__main__':
    s = Solution()
    num = s.ChineseToNum("一百亿一千零三万一千二百三十四")
    print(num)
    # print(s.ChnUnitToValue("亿"))

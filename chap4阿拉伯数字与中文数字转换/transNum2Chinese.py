#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: yinshi
@contact:laimingcham@163.com
@version: 1.0.0
@license: Apache Licence
@file: transNum2Chinese.py
@time: 2020/6/28 13:30
@desc:
"""


class Solution:
    '''中文数字表'''
    chnNumChar = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    '''节与 权位'''
    chnUnitSection = ['', '万', '亿', '万亿']
    '''每个节内 对应的权位'''
    chnUnitChar = ['', '十', '百', '千']

    def SectionToChinese(self, section, chnStr):
        """
        将一个节 的数字转换为中文数字， 利用中文数字表chnNumChar，利用 chnUnitChar得到数字权位，unitpos变量 用作权位索引
         关键部分是对于 0的处理，
        :param section:  3456
        :param chnStr:
        :return:
        """
        #  节点 结尾的0不需要 转换成 零，但是2个数字之间的0 需要转换成零， 如果2个数字之间有多个0，也只转换一个零
        isZero = True
        unitPos = 0
        list_chn_str = list(chnStr)
        while section > 0:
            v = section % 10  # 取模，得到最后一位的值
            if v == 0:
                if section == 0 or (not isZero):
                    isZero = True  # 需要补 零，zero的作用是确保 对连续多个，只会补一个中文零
                    list_chn_str.insert(0, self.chnNumChar[0])

            else:
                isZero = False
                # 该位置对应的中文数字
                strIns = self.chnNumChar[v]
                strIns += self.chnUnitChar[unitPos]
                list_chn_str.insert(0, strIns)

            unitPos += 1
            section = int(section / 10);
        chnStr = ''.join(list_chn_str)
        print('SectionToChinese chnStr', chnStr)
        return chnStr

    def numberToChinese(self, inputNum):
        """
         num == 0需要特殊处理， 直接返回"零

        :param inputNum:
        :return:
        """
        list_chn_str = []
        unitPos = 0

        needZero = False
        while inputNum > 0:
            section = inputNum % 10000
            if needZero:
                list_chn_str.insert(0, self.chnNumChar[0])
            tempIns = self.SectionToChinese(section, '')

            '''是否需要 节权位'''
            tempIns += self.chnUnitSection[unitPos] if (section != 0) else self.chnUnitSection[0]
            list_chn_str.insert(0, tempIns)
            '''如果 千位是0，需要 在下一个section 补零 '''
            needZero = 1000 > section > 0
            inputNum = int(inputNum / 10000)
            unitPos += 1
        chnStr = ''.join(list_chn_str)
        print('numberToChinese chnStr', chnStr)
        return chnStr


if __name__ == '__main__':
    s = Solution()
    print(s.numberToChinese(10010031234))

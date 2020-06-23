# -*- coding: utf-8 -*-
"""
@Time : 2020/6/17 16:01
@Author : liming
@Email : laimingcham@163.com
@File : SantaClausHandoutCandy.py
@Project : FunofAlgorithms
@Desc: 
"""
from pip._vendor.distlib.compat import raw_input

"""
 圣诞节来临了，在城市A中，圣诞老人准备分发糖果。现在有多箱不同的糖果，每一种糖果都有自己的价值和重量。每箱糖果都可以拆分成任意散装组合带走。圣诞老人的驯鹿最多只能承受一定重量的糖果。请问圣诞老人最多能带走多大价值的糖果。
输入数据： 输入的第一行由两个部分组成，分别为糖果箱数正整数n(1<=n<=100)，驯鹿能承受的最大重量正整数w(0<w<10000)；其余n行每行对应一箱糖果，由两部分正整数v和w组成，分别为一箱糖果的价值和重量。
输出要求： 输出圣诞老人能带走的糖果的最大总价值，保留一位小数，输出为一行。
输出样例：
　　4     15
　　100  4
　　412  8
　　266  7
　　591  2
输出样例:
　　1193.0
注：此处并没有按照这样的格式进行输入
原文链接：https://blog.csdn.net/sweetseven_/article/details/95197131
"""

# encoding:utf-8
from __future__ import division

input_a = raw_input(u'箱数:')
input_b = raw_input(u'最大承受重量:')

list_c = []
list_z = []

for i in range(1, int(input_a) + 1):
    input_c = raw_input('第' + str(i) + '箱的总价值:')
    input_d = raw_input('第' + str(i) + '箱的重量:')
    avg = round(int(input_c) / int(input_d), 1)  # 每一箱，重量为1的价值
    list_c.append(avg)  # 添加到列表，用于之后做比较
    list_z.append([int(input_d), avg, 0])  # 此处列表中添加列表，中间的列表一个存放总重量，第二个存放单位价值，第三个存放是否该物品已被取走

list_c.sort(reverse=True)  # 降序排序
sum = [0, 0]  # 用于存放取走的总重量，第一个参数是取走的重量，第二个是超出前的备份
num = 0
ji = 0

for i in range(len(list_c)):
    for k in range(len(list_z)):
        if ji == 0:  # 做是否超出马车最大承受量的标记，未超出为0
            if (list_c[i] == list_z[k][1]) and (list_z[k][2] == 0):
                sum[1] = sum[0]  # 备份
                sum[0] = sum[0] + list_z[k][0]  # 取走的重量
                v = list_z[k][0]  # 取走的重量
                if sum[0] > int(input_b):  # 如果所有取走的重量超出马车的重量，就依次减少一单元的重量
                    ji = 1  # 超出为1
                    t = list_z[k][0]
                    while True:  # 依次减去单位1的重量
                        z = sum[1] + t  # 使用备份进行判断，此时取走的数量已经大于最大承受量了
                        if z <= int(input_b):
                            break
                        t = t - 1
                    v = t  # 等于最大承受量时，价值较大的一件物品应取走的数量
                    sum[0] = sum[1]  # 从备份恢复
                    sum[0] = sum[0] + t  # 此时为真正的取走数量
                num = list_c[i] * v + num  # 总价值
                list_z[k][2] = 1  # 取走的标记
print
u'能带走的糖果的最大价值为:', num

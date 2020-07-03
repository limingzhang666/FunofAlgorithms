# -*- coding: utf-8 -*-
"""
@Time : 2020/6/30 17:40
@Author : liming
@Email : laimingcham@163.com
@File : pourWater.py
@Project : FunofAlgorithms
@Desc:  三个水桶等分8升水问题python实现--穷举、简单状态转移与递归
"""
from collections import deque

"""
https://www.jianshu.com/p/46f6aa196e1ex
"""


# class Solution:
    # # 水桶的初始状态
    # initial_bucket_state = [0, 0, 8]
    # # 每个水桶对应的容积
    # bucket_volume = [3, 5, 8]
    # # 利用python的deque队列记录状态转移情况，
    # # 初始化时加入水桶初始状态。deque是可以从头尾插入和删除的队列，在不指定大小时，为一个无边界的队列
    # record = deque()
    # record.append(initial_bucket_state)
    #
    # def IsBucketFull(self, bucketNo, current_state):
    #     """
    #     判断当前桶是否满了
    #     true： 满
    #     false： 不满
    #     :param bucketNo:  桶编号
    #     :param current_state:
    #     :return:
    #     """
    #     return self.bucket_volume[bucketNo - 1] == current_state[bucketNo - 1]
    #
    # def IsBucketEmpty(self, bucketNo, current_state):
    #     """
    #     判断当前桶是否空了
    #     true： 空
    #     false： 非空
    #     :param bucketNo:  桶编号
    #     :param current_state:
    #     :return:
    #     """
    #     return current_state[bucketNo - 1] == 0
    #
    # def CanTakeDumpAction(self, fromBucket, toBucket, current_state):
    #     """
    #
    #     :param fromBucket:
    #     :param toBucket:
    #     :return:
    #     """
    #     if fromBucket != toBucket \
    #     and not self.IsBucketEmpty(fromBucket, current_state) \
    #     and not self.IsBucketFull(toBucket, current_state) :
    #         return True
    #     else:
    #         return False
    #
    # def  SearchState(self,states):
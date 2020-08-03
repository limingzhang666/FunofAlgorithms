# -*- coding: utf-8 -*-
"""
@Time : 2020/8/3 10:41
@Author : liming
@Email : laimingcham@163.com
@File : dance_partner.py
@Project : FunofAlgorithms

https://blog.csdn.net/sunny1235435/article/details/95939432
@Desc:   稳定匹配和舞伴问题
"""

from collections import deque

## 初始化
boys = ['Albert', 'Brad', 'Chuck']
girls = ['Laura', 'Marcy', 'Nancy']

# 偏爱列表
sort_boy_to_girl = [[1, 3, 2], [3, 1, 2], [1, 2, 3]]
sort_girl_to_boy = [[2, 3, 1], [1, 3, 2], [2, 1, 3]]


def find_free_partner(boys, girls, sort_boy_to_girl, sort_girl_to_boy):
    # 当前选择的舞伴
    current_boys = {boys[0]: None, boys[1]: None, boys[2]: None}
    current_girls = {girls[0]: None, girls[1]: None, girls[2]: None}
    count = len(boys)
    # 建立队列，男孩下一次选择的女孩
    next_select = {}
    for i in range(count):
        next_select[boys[i]] = deque()
        argsort_p = sorted(range(count), key=lambda k: sort_boy_to_girl[i][k])
        for j in range(count):
            next_select[boys[i]].append(girls[argsort_p[j]])

    # 女孩选择男孩字典
    sort_girl = {}
    for i in range(count):
        sort_girl[girls[i]] = {}
        for j in range(count):
            sort_girl[girls[i]][boys[j]] = sort_girl_to_boy[i][j]

    while None in current_boys.values():
        for i in range(count):
            bid = boys[i]
            if current_boys[bid]:
                # 男孩有对象，跳过
                continue
            else:
                # 优先 选择的女孩
                select = next_select[bid][0]
                if current_girls[select] == None:
                    # 女孩没有对象，两者结合
                    current_boys[bid] = select
                    current_girls[select] = bid
                    next_select[bid].popleft()
                else:
                    # 和女孩的对象的好感度进行对比
                    if sort_girl[select][current_girls[select]] < sort_girl[select][bid]:
                        next_select[bid].popleft()
                    else:
                        current_boys[current_girls[select]] = None
                        current_boys[bid] = select
                        current_girls[select] = bid
                        next_select[bid].popleft()
    return current_boys

print(find_free_partner(boys, girls, sort_boy_to_girl, sort_girl_to_boy))

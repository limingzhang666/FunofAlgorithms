# -*- coding: utf-8 -*-
"""
@Time : 2020/8/3 14:09
@Author : liming
@Email : laimingcham@163.com
@File : perfect_match.py
@Project : FunofAlgorithms
@Desc: 
"""

### 去除不稳定因素
# 男孩选择女孩字典

## 初始化
boys = ['Albert', 'Brad', 'Chuck']
girls = ['Laura', 'Marcy', 'Nancy']

# 偏爱列表
sort_boy_to_girl = [[1, 3, 2], [3, 1, 2], [1, 2, 3]]
sort_girl_to_boy = [[2, 3, 1], [1, 3, 2], [2, 1, 3]]


count=len(boys)
sort_boy={}
for i in range(count):
    sort_boy[boys[i]]={}
    for j in range(count):
        sort_boy[boys[i]][girls[j]]=sort_boy_to_girl[i][j]

# 女孩选择男孩字典
sort_girl={}
for i in range(count):
    sort_girl[girls[i]]={}
    for j in range(count):
        sort_girl[girls[i]][boys[j]]=sort_girl_to_boy[i][j]

def remove_unstable_factors(all_select):
    global sort_boy,sort_girl
    a=0
    stable=[]
    for select in all_select:
        judge_girl=[]
        for boy,girl in select.items():
            if sort_boy[boy][girl]==1:
                judge_girl.append(girl)
                a+=1
            else:
                for i in range(sort_boy[boy][girl] - 1):
                    ju_girl = list(sort_boy[boy].keys())[list(sort_boy[boy].values()).index(i + 1)]
                    if ju_girl in judge_girl:
                        ju_boy = list(select.keys())[list(select.values()).index(ju_girl)]
                        if sort_girl[ju_girl][ju_boy] > sort_girl[ju_girl][boy]:
                            a = -1000000
                        else:
                            a += 1

        if a>0:
            stable.append(select)
        a=0
    return stable


print(remove_unstable_factors(all_select))
# -*- coding: utf-8 -*-
"""
@Time : 2020/7/3 15:32
@Author : liming
@Email : laimingcham@163.com
@File : monsterAndMonkAcrossRiver.py
@Project : FunofAlgorithms
@Desc:  和尚和妖怪过河问题
"""


class Solution:
    local = True
    remote = False

    # local_monster,local_monk,remote_monster,remote_monk,boat_location
    init_state = [3, 3, 0, 0, local]
    final_state = [0, 0, 3, 3, remote]

    # actionname,boat_to,move_monster,move_monk
    action_effection = [
        ['ONE_MONSTER_GO', remote, -1, 0],
        ['TWO_MONSTER_GO', remote, -2, 0],
        ['ONE_MONK_GO', remote, 0, -1],
        ['TWO_MONK_GO', remote, 0, -2],
        ['ONE_MONK_ONE_MONSTER_GO', remote, -1, -1],
        ['ONE_MONSTER_BACK', local, 1, 0],
        ['TWO_MONSTER_BACK', local, 2, 0],
        ['ONE_MONK_BACK', local, 0, 1],
        ['TWO_MONK_BACK', local, 0, 2],
        ['ONE_MONK_ONE_MONSTER_BACK', local, 1, 1]
    ]




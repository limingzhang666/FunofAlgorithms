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

    def CanTakeAction(self, current_state, curr_action):
        # 如果当前boat的位置==CanTakeAction 动作boat将要去的位置，不可以
        if current_state[4] == curr_action[1]:
            return False
        # 如果岸边 妖怪+ boat上妖怪 (如果要去对面就是 负数做减法)<0
        # 如果岸边 妖怪+ boat上妖怪 (如果要去对面就是 负数做减法)<0
        if (current_state[0] + curr_action[2] < 0) \
                or (current_state[0] + curr_action[2] > self.init_state[0]):
            return False
        # 如果岸边 和尚+ boat上 和尚 (如果要去对面就是 负数做减法)<0
        # 如果岸边 和尚+ boat上 和尚 (如果要去对面就是 负数做减法)<0
        if (current_state[1] + curr_action[3] < 0) \
                or (current_state[1] + curr_action[3] > self.init_state[0]):
            return False
        return True

    def ProcessStateOnNewAction(self, states, current, action_effection):
        '''

        :param states:
        :param current:
        :param action_effection:
        :return:
        '''
        print(11)

    def SearchState(self, statesDeque, curr_state, curr_action):
        '''

        :param statesDeque:
        :param curr_state:
        :param curr_action:
        :return:
        '''
        # 使用action，创建一个新 state

        # 如果新的state 是 有效的valid，且 新的state 之前从未出现过
        # 则 把新的 state加入到 statesDeque中，然后接续 递归SearchState

    def MakeActionNewState(self, curr_state, curr_action, new_state):
        if self.CanTakeAction(curr_state, curr_action):
            newState = curr_state;
            # newState.local_monster += ae.move_monster;
            # newState.local_monk += ae.move_monk;
            # newState.remote_monster -= ae.move_monster;
            # newState.remote_monk -= ae.move_monk;
            # newState.boat = ae.boat_to;
            # newState.curr_action = ae.act;
            return True
        else:
            return False

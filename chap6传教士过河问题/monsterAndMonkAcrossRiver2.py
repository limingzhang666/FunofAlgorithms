# -*- coding: utf-8 -*-
"""
@Time : 2020/7/3 15:32
@Author : liming
@Email : laimingcham@163.com
@File : monsterAndMonkAcrossRiver.py
@Project : FunofAlgorithms
@Desc:  和尚和妖怪过河问题
"""
from collections import deque

local = True
remote = False
# # local_monster,local_monk,remote_monster,remote_monk,boat_location
initial_state = [3, 3, 0, 0, True]
final_state = [0, 0, 3, 3, False]
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

record = deque()
record.append(initial_state)

def CanTakeAction(current_state, curr_action):
    '''
    初步判断当前的动作是否合法
    :param current_state:
    :param curr_action:
    :param init_state:
    :return:
    '''
    # 如果当前boat的位置==CanTakeAction 动作boat将要去的位置，不可以
    if current_state[4] == curr_action[1]:
        return False
    # 如果岸边 妖怪+ boat上妖怪 (如果要去对面就是 负数做减法)<0
    # 如果岸边 妖怪+ boat上妖怪 (如果要去对面就是 负数做减法)<0
    if (current_state[0] + curr_action[2] < 0) \
            or (current_state[0] + curr_action[2] > initial_state[0]):
        return False
    # 如果岸边 和尚+ boat上 和尚 (如果要去对面就是 负数做减法)<0
    # 如果岸边 和尚+ boat上 和尚 (如果要去对面就是 负数做减法)<0
    if (current_state[1] + curr_action[3] < 0) \
            or (current_state[1] + curr_action[3] > initial_state[0]):
        return False
    return True


def judgeSafeState(local_monk, local_monster, remote_monk, remote_monster):
    '''
    判断当前的状态是否安全
    :param local_monk:
    :param local_monster:
    :param remote_monk:
    :param remote_monster:
    :return:
    '''
    # 如果本地有和尚 and 本地妖怪> 本地和尚，则危险
    if local_monk > 0 and local_monster > local_monk:
        return False
    # 同理，对岸
    if remote_monk > 0 and remote_monster > remote_monk:
        return False
    return True


def next_state_lawful(current_state):
    # 下一个动作的 判定
    next_legal_action = []
    for action in action_effection:
        if CanTakeAction(current_state, action):
            # print('action:', action)
            next_legal_action.append(action)

    # 迭代每一个 合法的action，得到next_state
    for legal_action in next_legal_action:
        # state的结构： # local_monster,local_monk,remote_monster,remote_monk,boat_location
        # action的结构：actionname,boat_to,move_monster,move_monk
        # print('actionName:', legal_action[0])
        local_monster = current_state[0] + legal_action[2]
        local_monk = current_state[1] + legal_action[3]
        remote_monster = current_state[2] - legal_action[2]
        remote_monk = current_state[3] + legal_action[3]
        boat_location = legal_action[1]
        # 为什么要转换为list
        next_state=list(current_state)
        if judgeSafeState(local_monk, local_monster, remote_monk, remote_monster):
            # 这才是安全的 两岸 状态
            next_state[0] = local_monster
            next_state[1] = local_monk
            next_state[2] = remote_monster
            next_state[3] = remote_monk
            next_state[4] = boat_location
            yield next_state

num = 0
record_list = []
def searchResult(record):
    global num, record_list
    # 由record的末尾元素得到当前状态
    current_state = record[-1]
    # 得到关于当前状态的下一状态的可迭代生成器，供下一步循环使用
    next_state = next_state_lawful(current_state)

    # 遍历所有可能的下一状态
    for state in next_state:
        if state not in record:
            # 保证当前状态之前没有出现过，如果状态已经出现还进行搜索就会形成环路，陷入死循环
            record.append(state)
            if state == final_state:
                print('record ', record)
                record_list.append(deque(record))
            else:
                # 递归搜索
                searchResult(record)
            # 去除当前循环中添加的状态，进入下一个循环，关键步骤,保证每次都是新的开始
            record.pop()


searchResult(record)
print("实现方式的最少步骤为：%d 步" % (min([len(i) for i in record_list])-1))


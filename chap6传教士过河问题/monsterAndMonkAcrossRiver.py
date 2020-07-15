from collections import deque

initial_state = [3, 3, 0, 0, 0]  # 初始状态
final_state = [0, 0, 3, 3, 1]  # 最终状态

action = [[0, -1, 0], [0, -2, 0], [-1, 0, 0], [-2, 0, 0], [-1, -1, 0], [0, 1, 1], [0, 2, 1], [1, 0, 1], [2, 0, 1],
          [1, 1, 1]]

# 利用python的deque队列记录状态转移情况，初始化时加入初始状态。deque是可以从头尾插入和删除的队列，在不指定大小时，为一个无边界的队列
record = deque()
record.append(initial_state)


def next_state_lawful(current_state):
    # 下一个动作判定
    next_action = []
    for state in action:
        if current_state[4] == state[2] and (current_state[1] + state[1]) >= 0 and (current_state[1] + state[1]) <= 3 \
                and (current_state[0] + state[0]) >= 0 and (current_state[0] + state[0]) <= 3:
            next_action.append(state)

    # 下一个状态
    for state in next_action:
        left_monk = current_state[0] + state[0]
        left_monster = current_state[1] + state[1]
        right_monk = current_state[2] - state[0]
        right_monster = current_state[3] - state[1]
        next_state = list(current_state)

        if (left_monk == 0 or (left_monk > 0 and left_monk >= left_monster)) and \
                (right_monk == 0 or (right_monk > 0 and right_monk >= right_monster)):
            next_state[0] = left_monk
            next_state[1] = left_monster
            next_state[2] = right_monk
            next_state[3] = right_monster
            next_state[4] = int(not (current_state[4]))
            yield next_state

        # 记录调试的变量：num表示总共实现方法数，record_list记录所有实现路径


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
            # 保证当前状态没在以前出现过。如果状态已经出现还进行搜索就会形成状态环路，陷入死循环。
            record.append(state)
            # 添加新的状态到列表中
            if state == final_state:
                print(record)
                # 打印出可行方案
                # record_list.append(record)这样使用错误，导致加入列表的是record的引用，应该使用下面的式子来进行深复制，得到一个新的队列再加入列表。
                record_list.append(deque(record))
                num += 1
            else:
                # 递归搜索
                searchResult(record)
            # 去除当前循环中添加的状态，进入下一个循环，关键步，第一次实现的时候遗漏了
            record.pop()

searchResult(record)
print("总共实现方式的种类数目：", num)
print("实现方式的最少步骤为：%d 步" % (min([len(i) for i in record_list])-1))

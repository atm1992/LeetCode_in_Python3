# -*- coding: UTF-8 -*-
"""
title: 生命游戏1 (二维细胞自动机)。可参考LeetCode题289
"""
import time

import matplotlib.pyplot as plt
import numpy as np

# 设置初始状态，随机生成0或1
state = np.random.randint(0, 2, (50, 50))


# 定义更新函数，根据规则更新每个细胞的状态
def update(state):
    new_state = state.copy()
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            # 计算邻居细胞的数量
            neighbors = state[(i - 1) % state.shape[0], (j - 1) % state.shape[1]] + \
                        state[(i - 1) % state.shape[0], j] + \
                        state[(i - 1) % state.shape[0], (j + 1) % state.shape[1]] + \
                        state[i, (j - 1) % state.shape[1]] + \
                        state[i, (j + 1) % state.shape[1]] + \
                        state[(i + 1) % state.shape[0], (j - 1) % state.shape[1]] + \
                        state[(i + 1) % state.shape[0], j] + \
                        state[(i + 1) % state.shape[0], (j + 1) % state.shape[1]]
            # 根据规则更新细胞状态
            if state[i, j] == 0 and neighbors == 3:
                new_state[i, j] = 1  # 死细胞复活
            elif state[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_state[i, j] = 0  # 活细胞死亡
    return new_state


# 可视化函数，用颜色表示细胞状态
def visualize(state):
    plt.imshow(state, cmap='Blues')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    while True:
        visualize(state)
        state = update(state)
        time.sleep(5)

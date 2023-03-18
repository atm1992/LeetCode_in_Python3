# -*- coding: UTF-8 -*-
"""
title: 生命游戏2 (三维细胞自动机)
"""
import time

import matplotlib.pyplot as plt
import numpy as np

# 设置初始状态，随机生成0或1
state = np.random.randint(0, 2, (50, 50, 50))


# 定义更新函数，根据规则更新每个细胞的状态
def update(state):
    new_state = state.copy()
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            for k in range(state.shape[2]):
                # 计算邻居细胞的数量
                neighbors = state[(i - 1) % state.shape[0], j, k] + \
                            state[(i + 1) % state.shape[0], j, k] + \
                            state[i, (j - 1) % state.shape[1], k] + \
                            state[i, (j + 1) % state.shape[1], k] + \
                            state[i, j, (k - 1) % state.shape[2]] + \
                            state[i, j, (k + 1) % state.shape[2]]
                # 根据规则更新细胞状态
                if state[i, j, k] == 0 and neighbors == 3:
                    new_state[i, j, k] = 1  # 死细胞复活
                elif state[i, j, k] == 1 and (neighbors < 2 or neighbors > 3):
                    new_state[i, j, k] = 0  # 活细胞死亡
    return new_state


# 可视化函数，用颜色表示细胞状态
def visualize(state):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = np.where(state == 1)  # 找出活细胞的坐标
    ax.scatter(x, y, z, c='blue', s=10)  # 绘制散点图
    ax.set_xlim(0, state.shape[0])
    ax.set_ylim(0, state.shape[1])
    ax.set_zlim(0, state.shape[2])
    plt.show()


if __name__ == '__main__':
    while True:
        visualize(state)
        state = update(state)
        time.sleep(5)

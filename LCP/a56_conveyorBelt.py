# -*- coding: UTF-8 -*-
"""
title: 信物传送
欢迎各位勇者来到力扣城，本次试炼主题为「信物传送」。
本次试炼场地设有若干传送带，matrix[i][j] 表示第 i 行 j 列的传送带运作方向，"^","v","<",">" 这四种符号分别表示 上、下、左、右 四个方向。信物会随传送带的方向移动。勇者每一次施法操作，可临时变更一处传送带的方向，在物品经过后传送带恢复原方向。
通关信物初始位于坐标 start处，勇者需要将其移动到坐标 end 处，请返回勇者施法操作的最少次数。
注意：start 和 end 的格式均为 [i,j]


示例 1:
输入：matrix = [">>v","v^<","<><"], start = [0,1], end = [2,0]
输出：1
解释：
如上图所示
当信物移动到 [1,1] 时，勇者施法一次将 [1,1] 的传送方向 ^ 从变更为 <
从而信物移动到 [1,0]，后续到达 end 位置
因此勇者最少需要施法操作 1 次

示例 2:
输入：matrix = [">>v",">>v","^<<"], start = [0,0], end = [1,1]
输出：0
解释：勇者无需施法，信物将自动传送至 end 位置

示例 3:
输入：matrix = [">^^>","<^v>","^v^<"], start = [0,0], end = [1,3]
输出：3


提示：
matrix 中仅包含 '^'、'v'、'<'、'>'
0 < matrix.length <= 100
0 < matrix[i].length <= 100
0 <= start[0],end[0] < matrix.length
0 <= start[1],end[1] < matrix[i].length
"""
import heapq
from collections import deque
from typing import List


class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        """Dijkstra算法，使用优先队列。参考LeetCode题1368的方法一"""
        m, n = len(matrix), len(matrix[0])
        # 用于记录当前有哪些节点已经确定了到达start的最短路径长度及其相应的最短路径长度
        point2dist = {}
        # dist, i, j。按照每个节点到达start的最短路径长度dist进行升序
        queue = [(0, start[0], start[1])]
        # 每次while循环都能确定一个节点到达start的最短路径长度
        while queue:
            dist, i, j = heapq.heappop(queue)
            if [i, j] == end:
                return dist
            if (i, j) in point2dist:
                continue
            point2dist[(i, j)] = dist
            cur_dir = matrix[i][j]
            for x, y, dir in [(i - 1, j, '^'), (i + 1, j, 'v'), (i, j - 1, '<'), (i, j + 1, '>')]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in point2dist:
                    heapq.heappush(queue, (dist + (cur_dir != dir), x, y))

    def conveyorBelt_2(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        """0-1 BFS，使用双端队列。参考LeetCode题1368的方法二"""
        m, n = len(matrix), len(matrix[0])
        # 用于记录当前有哪些节点已经确定了到达start的最短路径长度及其相应的最短路径长度
        point2dist = {}
        # dist, i, j。
        queue = deque([(0, start[0], start[1])])
        # 每次while循环都能确定一个节点到达start的最短路径长度
        while queue:
            dist, i, j = queue.popleft()
            if [i, j] == end:
                return dist
            if (i, j) in point2dist:
                continue
            point2dist[(i, j)] = dist
            cur_dir = matrix[i][j]
            for x, y, dir in [(i - 1, j, '^'), (i + 1, j, 'v'), (i, j - 1, '<'), (i, j + 1, '>')]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in point2dist:
                    # 若移动到的位置与(i, j)处的箭头方向一致，则加入到双端队列的队首，否则加到队尾
                    if cur_dir == dir:
                        queue.appendleft((dist, x, y))
                    else:
                        queue.append((dist + 1, x, y))


if __name__ == '__main__':
    print(Solution().conveyorBelt(matrix=[">>v", "v^<", "<><"], start=[0, 1], end=[2, 0]))

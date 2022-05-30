# -*- coding: UTF-8 -*-
"""
title: 逃离火灾
You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:
    0 represents grass,
    1 represents fire,
    2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.
Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.
Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.
A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).


Example 1:
Input: grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
Output: 3
Explanation: The figure above shows the scenario where you stay in the initial position for 3 minutes.
You will still be able to safely reach the safehouse.
Staying for more than 3 minutes will not allow you to safely reach the safehouse.

Example 2:
Input: grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
Output: -1
Explanation: The figure above shows the scenario where you immediately move towards the safehouse.
Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse.
Thus, -1 is returned.

Example 3:
Input: grid = [[0,0,0],[2,2,0],[1,2,0]]
Output: 1000000000
Explanation: The figure above shows the initial grid.
Notice that the fire is contained by walls and you will always be able to safely reach the safehouse.
Thus, 109 is returned.


Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 300
4 <= m * n <= 2 * 10^4
grid[i][j] is either 0, 1, or 2.
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        """
        二分查找 + BFS
        总共 m * n 个单元格，无论火种从哪开始蔓延，只要火种如果没被围墙完全包围，那么就可以在m * n的时间内逐渐蔓延到起点(0,0)。
        因此可在0 ~ m * n 的范围内二分查找起始位置上的最长停留时间。
        火势蔓延 以及 人走向安全屋的过程，可分别使用BFS进行模拟。
        """
        m, n = len(grid), len(grid[0])

        def check(t: int) -> bool:
            """表示是否可在起始位置上停留时长t。若在时长t内会烧到起始位置，则返回False，表示不能停留这么长时间"""
            # cur_fires 表示当前这轮火势蔓延到的坐标，初始时，为所有火种的坐标
            cur_fires = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        cur_fires.append((i, j))
            all_fires = set(cur_fires)

            def fire_spread():
                nonlocal cur_fires
                tmp_fires = cur_fires
                cur_fires = []
                for i, j in tmp_fires:
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) not in all_fires and grid[x][y] != 2:
                            cur_fires.append((x, y))
                            all_fires.add((x, y))

            while t and cur_fires:
                # 先让火势蔓延t分钟。若在时间到达t之前，cur_fires就为[]，则表示火势被围墙完全包围了，不再蔓延了
                fire_spread()
                t -= 1
            if (0, 0) in all_fires or (m - 1, n - 1) in all_fires:
                return False
            # 即使火势在时长t内没有烧到起始位置，那还需判断等待时间t之后，还能否走到安全屋
            cur_person = [(0, 0)]
            all_person = set(cur_person)
            while cur_person:
                tmp_person = cur_person
                cur_person = []
                for i, j in tmp_person:
                    # 题目提示：如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。
                    # 除了安全屋以外的坐标，如果人到了，火势随之也到了，那么这个位置是不能走的，参考示例2
                    if (i, j) not in all_fires:
                        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            # 除了上面的判断条件，还需判断不能走回头路，因为没有意义
                            if 0 <= x < m and 0 <= y < n and (x, y) not in all_fires and grid[x][y] != 2 and (
                                    x, y) not in all_person:
                                if (x, y) == (m - 1, n - 1):
                                    return True
                                cur_person.append((x, y))
                                all_person.add((x, y))
                # 人每走一步，火势也会蔓延一步
                fire_spread()
            return False

        if not check(0):
            return -1
        left, right = 0, m * n
        while left < right:
            mid = (left + right + 1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left if left < m * n else 10 ** 9


if __name__ == '__main__':
    print(Solution().maximumMinutes(
        grid=[[0, 2, 0, 0, 1], [0, 2, 0, 2, 2], [0, 2, 0, 0, 0], [0, 0, 2, 2, 0], [0, 0, 0, 0, 0]]))

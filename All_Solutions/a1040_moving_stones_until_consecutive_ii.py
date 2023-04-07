# -*- coding: utf-8 -*-
# @date: 2023/4/7
# @author: liuquan
"""
title: 移动石子直到连续 II
There are some stones in different positions on the X-axis. You are given an integer array stones, the positions of the stones.
Call a stone an endpoint stone if it has the smallest or largest position. In one move, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.
    In particular, if the stones are at say, stones = [1,2,5], you cannot move the endpoint stone at position 5, since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.
The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).
Return an integer array answer of length 2 where:
    answer[0] is the minimum number of moves you can play, and
    answer[1] is the maximum number of moves you can play.


Example 1:
Input: stones = [7,4,9]
Output: [1,2]
Explanation: We can move 4 -> 8 for one move to finish the game.
Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.

Example 2:
Input: stones = [6,5,4,3,10]
Output: [2,3]
Explanation: We can move 3 -> 8 then 10 -> 7 to finish the game.
Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.


Constraints:
3 <= stones.length <= 10^4
1 <= stones[i] <= 10^9
All the values of stones are unique.
"""
from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        """
        思维题，类似于下跳棋。排序 + 数学 + 滑动窗口
        先对stones升序，假设stones的长度为n，stones[0]与stones[n-1]之间的空格数为 stones[n-1] - stones[0] + 1 - n
        最大操作数：
        1、若最先移动stones[0]，为了保证操作数最大，则应将stones[0]变为大于stones[1]的最小空格值，此时最左侧至少有两个元素是连续的，
        接下来，再将最左侧元素(即 stones[1])变为大于次左侧的最小空格值，即 从左侧逐个填满空格，直到所有元素变为 stones[n-1] - n + 1 ~ stones[n-1]，
        此时的总操作数为 stones[n-1] - stones[1] + 1 - (n-1)，即 将stones[1] ~ stones[n-1]之间的所有空格都走一次
        2、若最先移动stones[n-1]，则与上面同理，最终将所有元素变为 stones[0] ~ stones[0] + n - 1
        此时的总操作数为 stones[n-2] - stones[0] + 1 - (n-1)，即 将stones[n-2] ~ stones[0]之间的所有空格都走一次
        最终的最大操作数为 max(stones[n-1] - stones[1] + 1 - (n-1), stones[n-2] - stones[0] + 1 - (n-1))

        最小操作数：          # 以右侧为例进行分析，左侧同理
        1、若stones[n-1] - stones[n-2] == 2，则最少只需操作1次。例如：stones = [1,2,3,5]，即 stones[0] ——> 4
        2、若stones[n-1] - stones[n-2] > 2，则最少需要操作2次。例如：stones = [1,2,3,6]，即 stones[0] ——> 5，stones[-1] ——> 4
        用一个长度为n的滑动窗口，找到包含最多stone的那个窗口，假设该窗口内的stone个数为k，窗口外左侧的stone个数为a，
        窗口外右侧的stone个数为b，a + b == n - k
        先让该窗口向右移，使得左端点位于窗口内的第一个元素(该操作并不会使窗口内的stone个数变少, 依旧还是k)
        1、若此时右端点位于窗口内的最后一个元素，则可把窗口外右侧的b个元素从大到小依次填满窗口内右侧的b个空格，然后
        把窗口外左侧的a个元素从小到大依次填满窗口内左侧的a个空格，此时的总操作数为 n - k
        2、若此时右端点为空格
            2.1、若a + b > 1，则可先将左侧的最小元素或右侧的最大元素放到右端点，接下来就跟情况1一样了，此时的总操作数为 n - k
            2.2、若a + b == 1，此时说明窗口内的n-1个元素已连续排列在窗口内的左侧
                2.2.1、若stones[n-1] - stones[n-2] > 2 or stones[1] - stones[0] > 2，则此时的总操作数为 2，即 n - k + 1
                2.2.2、其余情况下，总操作数为 1，即 n - k
        综上，只有当 k == n-1 and 右端点为空格 and (stones[n-1] - stones[n-2] > 2 or stones[1] - stones[0] > 2) 时，
        最小操作数才会为n - k + 1，其余情况下，最小操作数均为n - k
        """
        stones.sort()
        n = len(stones)
        if stones[n - 1] - stones[0] + 1 == n:
            return [0, 0]
        max_moves = max(stones[n - 1] - stones[1] + 1 - (n - 1), stones[n - 2] - stones[0] + 1 - (n - 1))
        j, min_moves = 0, n
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 <= n:
                j += 1
            k = j - i + 1
            # 说明这n-1元素是连续的，窗口外面只有一个元素
            if k == n - 1 and stones[j] != stones[i] + n - 1 and \
                    (stones[n - 1] - stones[n - 2] > 2 or stones[1] - stones[0] > 2):
                min_moves = min(min_moves, n - k + 1)
            else:
                min_moves = min(min_moves, n - k)
        return [min_moves, max_moves]


if __name__ == '__main__':
    print(Solution().numMovesStonesII(stones=[6, 5, 4, 3, 10]))

# -*- coding: UTF-8 -*-
"""
title: 不可能得到的最短骰子序列
You are given an integer array rolls of length n and an integer k. You roll a k sided dice numbered from 1 to k, n times, where the result of the ith roll is rolls[i].
Return the length of the shortest sequence of rolls that cannot be taken from rolls.
A sequence of rolls of length len is the result of rolling a k sided dice len times.
Note that the sequence taken does not have to be consecutive as long as it is in order.


Example 1:
Input: rolls = [4,2,1,2,3,3,2,4,1], k = 4
Output: 3
Explanation: Every sequence of rolls of length 1, [1], [2], [3], [4], can be taken from rolls.
Every sequence of rolls of length 2, [1, 1], [1, 2], ..., [4, 4], can be taken from rolls.
The sequence [1, 4, 2] cannot be taken from rolls, so we return 3.
Note that there are other sequences that cannot be taken from rolls.

Example 2:
Input: rolls = [1,1,2,2], k = 2
Output: 2
Explanation: Every sequence of rolls of length 1, [1], [2], can be taken from rolls.
The sequence [2, 1] cannot be taken from rolls, so we return 2.
Note that there are other sequences that cannot be taken from rolls but [2, 1] is the shortest.

Example 3:
Input: rolls = [1,1,3,2,2,2,3,3], k = 4
Output: 1
Explanation: The sequence [4] cannot be taken from rolls, so we return 1.
Note that there are other sequences that cannot be taken from rolls but [4] is the shortest.


Constraints:
n == rolls.length
1 <= n <= 10^5
1 <= rolls[i] <= k <= 10^5
"""
from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        """
        脑筋急转弯
        假设可以找到的最长骰子子序列的长度为m，则说明这m个位置中的任意一个位置都可以取到1~k中的任一值，
        即 可以把原始数组rolls从前往后划分为m个子数组，每个子数组中都包含1~k中的任一值。
        因此，可根据上述方法来划分原始数组rolls，统计可以找到多少个那样的子数组，然后加1就是最终返回结果
        """
        cnt = 0
        roll_set = set()
        for roll in rolls:
            roll_set.add(roll)
            if len(roll_set) == k:
                roll_set.clear()
                cnt += 1
        return cnt + 1


if __name__ == '__main__':
    print(Solution().shortestSequence(rolls=[1, 1, 2, 2], k=2))

# -*- coding: UTF-8 -*-
"""
title: 你能构造出连续值的最大数目
You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.
Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.
Note that you may have multiple coins of the same value.


Example 1:
Input: coins = [1,3]
Output: 2
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.

Example 2:
Input: coins = [1,1,1,4]
Output: 8
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.

Example 3:
Input: nums = [1,4,10,3,1]
Output: 20


Constraints:
coins.length == n
1 <= n <= 4 * 10^4
1 <= coins[i] <= 4 * 10^4
"""
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        """
        排序 + 贪心
        假设数组中的若干个元素可以构造出 [0, x] 内的所有整数，此时再从剩余元素中选择一个y，则可构造出 [y, x + y] 内的所有整数。
        要使构造出的区间尽量大，就意味着要尽量让 [0, x] 与 [y, x + y] 可以连上，由题意可知，1 <= y，所以 x+1 <= x+y
        要使两个区间相连，就需要 y <= x+1，如果y > x+1，就意味着这个y对答案没有影响，所以需要从剩余元素中选择尽量小的元素y
        """
        coins.sort()
        pre_end = 0
        for coin in coins:
            if coin > pre_end + 1:
                break
            pre_end += coin
        return pre_end + 1


if __name__ == '__main__':
    print(Solution().getMaximumConsecutive(coins=[1, 1, 1, 4]))

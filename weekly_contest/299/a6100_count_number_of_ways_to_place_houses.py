# -*- coding: UTF-8 -*-
"""
title: 统计放置房子的方式数
There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are numbered from 1 to n. On each plot, a house can be placed.
Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it modulo 10^9 + 7.
Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street.


Example 1:
Input: n = 1
Output: 4
Explanation:
Possible arrangements:
1. All plots are empty.
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.

Example 2:
Input: n = 2
Output: 9
Explanation: The 9 possible arrangements are shown in the diagram above.


Constraints:
1 <= n <= 10^4
"""


class Solution:
    def countHousePlacements(self, n: int) -> int:
        """
        动态规划。
        因为两侧的房子互不影响，所以只需求解出一侧放置房子的方式数，便可根据乘法原理得到最终结果。
        dp[i] 表示前 i 个地块的放置方案数，其中第 i 个地块可以放置房子，也可以不放置房子。
        若第 i 个地块不放置房子，则 dp[i] = dp[i-1]；若第 i 个地块放置房子，则 dp[i] = dp[i-2]。
        所以状态转移方程为：dp[i] = dp[i-1] + dp[i-2]
        边界条件：
        dp[0] = 1，没有地块，只能选择不放置房子，所以只有1种方式
        dp[1] = 2，只有一个地块，既可选择放置一个房子，也可选择不放置房子，所以有2种方式
        """
        mod = 10 ** 9 + 7
        pre_2, pre_1 = 1, 2
        for i in range(2, n + 1):
            pre_2, pre_1 = pre_1, (pre_1 + pre_2) % mod
        return pre_1 * pre_1 % mod


if __name__ == '__main__':
    print(Solution().countHousePlacements(3))

# -*- coding: UTF-8 -*-
"""
title: 访问完所有房间的第一天
There are n rooms you need to visit, labeled from 0 to n - 1. Each day is labeled, starting from 0. You will go in and visit one room a day.
Initially on day 0, you visit room 0. The order you visit the rooms for the coming days is determined by the following rules and a given 0-indexed array nextVisit of length n:
Assuming that on a day, you visit room i,
if you have been in room i an odd number of times (including the current visit), on the next day you will visit the room specified by nextVisit[i] where 0 <= nextVisit[i] <= i;
if you have been in room i an even number of times (including the current visit), on the next day you will visit room (i + 1) mod n.
Return the label of the first day where you have been in all the rooms. It can be shown that such a day exists. Since the answer may be very large, return it modulo 10^9 + 7.


Example 1:
Input: nextVisit = [0,0]
Output: 2
Explanation:
- On day 0, you visit room 0. The total times you have been in room 0 is 1, which is odd.
  On the next day you will visit room nextVisit[0] = 0
- On day 1, you visit room 0, The total times you have been in room 0 is 2, which is even.
  On the next day you will visit room (0 + 1) mod 2 = 1
- On day 2, you visit room 1. This is the first day where you have been in all the rooms.

Example 2:
Input: nextVisit = [0,0,2]
Output: 6
Explanation:
Your room visiting order for each day is: [0,0,1,0,0,1,2,...].
Day 6 is the first day where you have been in all the rooms.

Example 3:
Input: nextVisit = [0,1,2,0]
Output: 6
Explanation:
Your room visiting order for each day is: [0,0,1,1,2,2,3,...].
Day 6 is the first day where you have been in all the rooms.


Constraints:
n == nextVisit.length
2 <= n <= 10^5
0 <= nextVisit[i] <= i
"""
from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        """
        动态规划。假设dp[i]表示访问完第 i 个房间所需的天数(即 首访房间i 到 可以离开房间i去访问房间i+1 之间的天数)。
        从题意可知，这个值一定是偶数，因为只有偶数次访问时，才可以访问下一个房间(i+1)；奇数次访问时，只能回访房间(j = nextVisit[i]，0 <= j <= i)。
        因此，dp[i]的计算公式为：首访房间i需要1天，完整回访完 j = nextVisit[i] ~ i-1 需要 dp[j] + dp[j+1] + …… + dp[i-1] 这么多天，
        最后第二次访问房间i还需要1天。所以，dp[i] = 1 + dp[j] + dp[j+1] + …… + dp[i-1] + 1 。
        对于每个dp[i]，都只是会在房间i待2天，其余时间都用来回访之前的房间，回访时用的总天数(dp[j] + dp[j+1] + …… + dp[i-1])可以用 前缀和 求解。
        可以省略dp数组，直接用 前缀和pre_sum 数组来记录访问完前 i-1 个房间所需的总天数。例如：pre_sum[i] 表示访问完第 0 个、第 1 个 …… 第 i-1 个房间所需的总天数，
        pre_sum[j] 表示访问完第 0 个、第 1 个 …… 第 j-1 个房间所需的总天数，所以，pre_sum[i] - pre_sum[j] = dp[j] + dp[j+1] + …… + dp[i-1]，
        所以，dp[i] = pre_sum[i] - pre_sum[j] + 2
        """
        n = len(nextVisit)
        mod = 10 ** 9 + 7
        # pre_sum[1] = dp_0、pre_sum[2] = dp_0 + dp_1、…… 、pre_sum[n-1] = dp_0 + dp_1 + …… + dp_n-2
        # 由于n个房间的最后一个房间号为n-1，而pre_sum[n-1]表示访问完前n-2个房间所需的总天数，再加1天就是首次访问房间n-1，即总共需要 pre_sum[n-1] + 1 这么多天。
        # 注意：题目问的是第几天可以访问完所有房间，而第几天是从0开始计算的，所以最终结果为 pre_sum[n-1] + 1 - 1 = pre_sum[n-1]
        pre_sum = [0 for _ in range(n)]
        for i in range(n - 1):
            # 需要保证pre_sum数组中的所有元素都小于mod。虽然在进行mod之前，pre_sum[i] 一定大于 pre_sum[j]，但对元素mod完以后，有可能pre_sum[i] < pre_sum[j]，
            # 所以pre_sum[i] - pre_sum[j]时，需要给pre_sum[i]先加上mod，以防pre_sum[i] - pre_sum[j]的结果为负数
            dp_i = (pre_sum[i] + mod - pre_sum[nextVisit[i]] + 2) % mod
            pre_sum[i + 1] = (pre_sum[i] + dp_i) % mod
        return pre_sum[-1]


if __name__ == '__main__':
    print(Solution().firstDayBeenInAllRooms([0, 1, 2, 0]))

# -*- coding: utf-8 -*-
# @date: 2023/4/26
# @author: liuquan
"""
title: 两个线段获得的最多奖品
There are some prizes on the X-axis. You are given an integer array prizePositions that is sorted in non-decreasing order, where prizePositions[i] is the position of the ith prize. There could be different prizes at the same position on the line. You are also given an integer k.
You are allowed to select two segments with integer endpoints. The length of each segment must be k. You will collect all prizes whose position falls within at least one of the two selected segments (including the endpoints of the segments). The two selected segments may intersect.
    For example if k = 2, you can choose segments [1, 3] and [2, 4], and you will win any prize i that satisfies 1 <= prizePositions[i] <= 3 or 2 <= prizePositions[i] <= 4.
Return the maximum number of prizes you can win if you choose the two segments optimally.


Example 1:
Input: prizePositions = [1,1,2,2,3,3,5], k = 2
Output: 7
Explanation: In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5].

Example 2:
Input: prizePositions = [1,2,3,4], k = 0
Output: 2
Explanation: For this example, one choice for the segments is [3, 3] and [4, 4], and you will be able to get 2 prizes.


Constraints:
1 <= prizePositions.length <= 10^5
1 <= prizePositions[i] <= 10^9
0 <= k <= 10^9
prizePositions is sorted in non-decreasing order.
"""
from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        """
        前缀和 + 双指针 + 枚举。参考LeetCode题1031
        注意：prizePositions中的元素值是指的奖品所在位置，并不是奖品数量。某个位置在prizePositions中出现了几次，
        就表示在该位置上有几个奖品
        """
        # 在prizePositions的前i个元素中长度至多为k的子数组的最大和
        pre_sum = [0]
        res = i = 0
        for j, pos in enumerate(prizePositions):
            while pos - prizePositions[i] > k:
                i += 1
            res = max(res, pre_sum[i] + j - i + 1)
            pre_sum.append(max(pre_sum[-1], j - i + 1))
        return res


if __name__ == '__main__':
    print(Solution().maximizeWin(prizePositions=[1, 1, 2, 2, 3, 3, 5], k=2))

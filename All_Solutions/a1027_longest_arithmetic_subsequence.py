# -*- coding: utf-8 -*-
# @date: 2023/4/22
# @author: liuquan
"""
title: 最长等差数列
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
Note that:
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).


Example 1:
Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].


Constraints:
2 <= nums.length <= 1000
0 <= nums[i] <= 500
"""
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        动态规划
        dp[i][j] 表示以nums[i]结尾且公差为j的等差数列的最大长度
        由于0 <= nums[i] <= 500，所以公差的取值范围为: [-500, 500]，为方便计算，将公差统一加500，使得公差的取值范围为: [0, 1000]
        状态转移方程：dp[i][j] = max(dp[i][j], dp[k][j] + 1)，其中，nums[k] = nums[i] - j + 500
        初始值：dp[i][*] = 1 每个元素都可看作是一个长度为1的公差为任意值的等差数列
        最终返回最大的 dp[i][j]
        """
        res, n = 0, len(nums)
        dp = [[1] * 1001 for _ in range(n)]
        for i in range(1, n):
            for k in range(i):
                j = nums[i] - nums[k] + 500
                dp[i][j] = max(dp[i][j], dp[k][j] + 1)
                res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    print(Solution().longestArithSeqLength(nums=[3, 6, 9, 12]))

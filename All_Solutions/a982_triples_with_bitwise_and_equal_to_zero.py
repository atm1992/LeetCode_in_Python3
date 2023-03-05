# -*- coding: UTF-8 -*-
"""
title: 按位与为零的三元组
Given an integer array nums, return the number of AND triples.
An AND triple is a triple of indices (i, j, k) such that:
    0 <= i < nums.length
    0 <= j < nums.length
    0 <= k < nums.length
    nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.


Example 1:
Input: nums = [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2

Example 2:
Input: nums = [0,0,0]
Output: 27


Constraints:
1 <= nums.length <= 1000
0 <= nums[i] < 2^16
"""
from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        """直接枚举"""
        ij2cnt = Counter(i & j for i in nums for j in nums)
        return sum(cnt for ij, cnt in ij2cnt.items() for k in nums if ij & k == 0)

    def countTriplets_2(self, nums: List[int]) -> int:
        """
        枚举 + 子集优化。
        在方法一的第二个二重循环中，在数据随机的情况下，哈希表ij2cnt中会包含 [0, 2^16) 中的大部分整数，即 第二个二重循环的时间复杂度为 O(2^16 * n)
        在第二个二重循环中，要想使ij & k == 0，就意味着若k的第t个二进制位为0，则ij二元组的第t个二进制位才可以为1，否则ij二元组的相应二进制位必须为0
        通过 k ^ 0xffff 将k中的所有0变为1，所有1变为0，即 得到k的补集m。然后通过 sub = (sub - 1) & m 从大到小枚举补集m的所有子集。
        补集m在平均情况下，会有8位1，即 第二个二重循环的时间复杂度降为 O(2^8 * n)
        """
        ij2cnt = Counter(i & j for i in nums for j in nums)
        res = 0
        for k in nums:
            sub = m = k ^ 0xffff
            while True:
                res += ij2cnt.get(sub, 0)
                if sub == 0:
                    break
                sub = (sub - 1) & m
        return res


if __name__ == '__main__':
    print(Solution().countTriplets(nums=[0, 0, 0]))

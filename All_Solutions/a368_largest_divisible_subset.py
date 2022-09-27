# -*- coding: UTF-8 -*-
"""
title: 最大整除子集
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.


Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
All the integers in nums are unique.
"""
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        排序 + 动态规划。参考LeetCode题300
        """
        sorted_nums = sorted(nums)
        subsets = []
        max_idx = -1
        for i, num in enumerate(sorted_nums):
            cur_subset = []
            for j in range(i - 1, -1, -1):
                if j + 1 <= len(cur_subset):
                    break
                if num % sorted_nums[j] == 0 and len(subsets[j]) > len(cur_subset):
                    cur_subset = subsets[j]
            subsets.append(cur_subset + [num])
            if max_idx == -1 or len(subsets[max_idx]) < len(subsets[-1]):
                max_idx = i
        return subsets[max_idx]


if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([1, 2, 3]))

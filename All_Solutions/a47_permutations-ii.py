# -*- coding: UTF-8 -*-
"""
title: 全排列 II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """回溯搜索。相比a46，此题重点在于如何解决重复问题，将重复的数字先排好序，然后在所有的全排列结果中都保持这个相对顺序，即可实现去重。
        先对原始数组nums排序，重复的数字会相邻，然后确保每次填入的数字都是这些重复数字中第一个未被标记的。
        假设原始数组nums中存在3个2，对应的标记数组初始状态为[False, False, False]，因为需要确保每次填入的数字都是这些重复数字中第一个未被标记的，
        所以对应的标记数组变化为：[False, False, False] ——> [True, False, False] ——> [True, True, False] ——> [True, True, True]"""

        def dfs(idx: int = 0, path: List[int] = [], visited: int = 0) -> None:
            if idx == n:
                res.append(path)
                return
            for i in range(n):
                if (visited >> i) & 1 or (i > 0 and nums[i] == nums[i - 1] and ((visited >> i - 1) & 1) == 0):
                    continue
                dfs(idx + 1, path + [nums[i]], visited | (1 << i))

        nums.sort()
        n = len(nums)
        res = []
        dfs()
        return res


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 2, 1, 3]))

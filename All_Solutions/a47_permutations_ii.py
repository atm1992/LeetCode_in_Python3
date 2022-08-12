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
        """回溯"""
        def dfs(path: List[int], visited: int) -> None:
            if len(path) == n:
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if visited & (1 << i) or (i > 0 and nums[i - 1] == num and visited & (1 << (i - 1)) == 0):
                    continue
                path.append(num)
                dfs(path, visited | (1 << i))
                path.pop()

        res = []
        n = len(nums)
        nums.sort()
        dfs([], 0)
        return res


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 2, 1, 3]))

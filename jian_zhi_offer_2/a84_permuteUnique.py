# -*- coding: UTF-8 -*-
"""
title: 含有重复元素集合的全排列
给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。


示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


提示：
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
    print(Solution().permuteUnique([1, 1, 2]))

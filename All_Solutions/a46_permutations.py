# -*- coding: UTF-8 -*-
"""
title: 全排列
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """基于填空的回溯。使用visited数组或二进制位来标记某个数字是否已使用过，可以让返回结果中数字的顺序与原始nums中的顺序一致"""

        def dfs(path: List[int], visited: int) -> None:
            if len(path) == n:
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if visited & (1 << i) == 0:
                    path.append(num)
                    dfs(path, visited | (1 << i))
                    path.pop()

        res = []
        n = len(nums)
        dfs([], 0)
        return res

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        """基于交换的回溯。省略visited数组或二进制位，不考虑返回结果中数字的顺序；也不使用path数组，直接修改原始nums中的顺序，降低空间复杂度"""

        def dfs(i: int) -> None:
            if i == n:
                res.append(nums[:])
                return
            # i 会依次指向子数组中的每个位置(下标为0 ~ n-1)，表示当前需要确定哪个位置上的元素
            for j in range(i, n):
                # 0 ~ i-1 是已确定位置的元素，i ~ n-1 是待确定位置的元素。从 i ~ n-1 中选择一个合适的元素j放到位置i上
                nums[i], nums[j] = nums[j], nums[i]
                # 确定位置i+1上的元素
                dfs(i + 1)
                # 回溯时，恢复元素的顺序
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        n = len(nums)
        dfs(0)
        return res


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))

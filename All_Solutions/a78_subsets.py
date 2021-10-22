# -*- coding: UTF-8 -*-
"""
title: 子集
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """回溯"""

        def dfs(idx: int = 0, path: list = []):
            if idx == n:
                res.append(path[:])
                return
            # 选择当前元素
            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()

            # 跳过当前元素
            dfs(idx + 1, path)

        n = len(nums)
        res = []
        dfs()
        return res

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        """使用二进制位进行枚举。n位全0，表示所有元素都不选，即 []；n位全1，表示全选所有元素，即 nums本身。
        n为数组nums的长度，从0遍历到2^n - 1，就可取到所有的子集。"""
        n = len(nums)
        res, tmp = [], []
        for mask in range(2 ** n):
            tmp.clear()
            idx = 0
            while mask > 0:
                if mask & 1:
                    tmp.append(nums[idx])
                mask >>= 1
                idx += 1
            res.append(tmp[:])
        return res


if __name__ == '__main__':
    print(Solution().subsets_2([1, 2, 3]))

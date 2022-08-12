# -*- coding: UTF-8 -*-
"""
title: 组合总和
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]


Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """回溯"""

        def dfs(i: int, path: List[int], total: int) -> None:
            if total == target:
                # 因为每次传入的path都是一个新的path，回溯时不会再修改这个path，所以无需 append(path[:])
                res.append(path)
                return
            if i == n or total + candidates[i] > target:
                return
            num = candidates[i]
            # 对于任意一个元素，最多可以加入max_cnt次到path中
            max_cnt = (target - total) // num
            # 最先考虑加入max_cnt次的情况，最后再考虑不加入的情况。这样做的好处是：最终返回结果是升序的（先按返回结果数组的第一个值升序，再按第二个值升序 ……）
            for cnt in range(max_cnt, -1, -1):
                dfs(i + 1, path + [num] * cnt, total + num * cnt)

        res = []
        candidates.sort()
        n = len(candidates)
        dfs(0, [], 0)
        return res

    def combinationSum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        """回溯"""

        def dfs(i: int, path: List[int], total: int) -> None:
            if total == target:
                res.append(path[:])
                return
            if i == n or total + candidates[i] > target:
                return
            path.append(candidates[i])
            # 当前元素允许被选多次
            dfs(i, path, total + candidates[i])
            path.pop()
            # 跳过当前元素
            dfs(i + 1, path, total)

        res = []
        candidates.sort()
        n = len(candidates)
        for i, num in enumerate(candidates):
            # 分别考虑以每个元素为起始元素的情况，固定起始元素，避免重复
            dfs(i, [num], num)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))

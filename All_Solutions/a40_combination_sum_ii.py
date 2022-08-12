# -*- coding: UTF-8 -*-
"""
title: 组合总和 II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.


Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """回溯"""
        def dfs(i: int, path: List[int], total: int) -> None:
            if total == target:
                # 因为每次传入的path都是一个新的path，回溯时不会再修改这个path，所以无需 append(path[:])
                res.append(path)
                return
            if i == n or total + num2cnt[i][0] > target:
                return
            num = num2cnt[i][0]
            # 对于任意一个元素，最多可以加入max_cnt次到path中
            max_cnt = min(num2cnt[i][1], (target - total) // num)
            # 最先考虑加入max_cnt次的情况，最后再考虑不加入的情况。这样做的好处是：最终返回结果是升序的（先按返回结果数组的第一个值升序，再按第二个值升序 ……）
            for cnt in range(max_cnt, -1, -1):
                dfs(i + 1, path + [num] * cnt, total + num * cnt)

        res = []
        num2cnt = sorted(Counter(candidates).items())
        n = len(num2cnt)
        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))

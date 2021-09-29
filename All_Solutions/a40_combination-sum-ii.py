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


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """递归回溯"""
        from collections import Counter

        def dfs(target: int, combination: List[int], idx: int) -> None:
            if target == 0:
                res.append(combination)
                return
            # 对idx == n的判断必须放在target == 0的判断之后，考虑特殊情况：把最后一个元素(n-1)加入combination之后，idx将变为n，
            # 如果最后一个元素(n-1)刚好是符合条件的，idx == n的判断会直接return，从而丢弃了该结果
            if idx == n or target < 0:
                return
            number = number_freq[idx][0]
            freq = number_freq[idx][1]
            # 对于任意一个元素，最多可以加入max_times次到combination中
            max_times = min(target // number, freq)
            # 最先考虑加入max_times次的情况，最后再考虑不加入的情况。这样做的好处是：最终返回结果是升序的（先按返回结果数组的第一个值升序，再按第二个值升序 ……）
            for i in range(max_times, -1, -1):
                # 因为这里没有直接修改combination，所以无需在回溯前记录combination长度，回溯后再恢复combination长度
                dfs(target - number * i, combination + [number] * i, idx + 1)

        number_freq = sorted(Counter(candidates).items())
        n = len(number_freq)
        res = []
        dfs(target, [], 0)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))

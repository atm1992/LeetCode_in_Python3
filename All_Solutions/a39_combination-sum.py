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
        """递归回溯"""

        def dfs(target: int, combination: List[int], idx: int) -> None:
            if target == 0:
                res.append(combination)
                return
            # 对idx == n的判断必须放在target == 0的判断之后，考虑特殊情况：把最后一个元素(n-1)加入combination之后，idx将变为n，
            # 如果最后一个元素(n-1)刚好是符合条件的，idx == n的判断会直接return，从而丢弃了该结果
            if idx == n or target < 0:
                return
            # 对于任意一个元素，最多可以加入max_times次到combination中
            number = candidates[idx]
            max_times = target // number
            # 最先考虑加入max_times次的情况，最后再考虑不加入的情况。这样做的好处是：最终返回结果是升序的（先按返回结果数组的第一个值升序，再按第二个值升序 ……）
            for i in range(max_times, -1, -1):
                # 因为这里没有直接修改combination，所以无需在回溯前记录combination长度，回溯后再恢复combination长度
                dfs(target - number * i, combination + [number] * i, idx + 1)

        candidates.sort()
        n = len(candidates)
        res = []
        # 从第0个元素开始选择。对于任意一个元素，都只有两种情况：加入到某个combination or 不加入某个combination
        dfs(target, [], 0)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))

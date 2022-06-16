# -*- coding: UTF-8 -*-
"""
title: 含有重复元素集合的组合
给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。 


示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5
输出:
[
[1,2,2],
[5]
]


提示:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from collections import Counter
from typing import List


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
    print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))

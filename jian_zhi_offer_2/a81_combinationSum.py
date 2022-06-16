# -*- coding: UTF-8 -*-
"""
title: 允许重复选择元素的组合
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的唯一组合数少于 150 个。


示例 1：
输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]

示例 2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []

示例 4：
输入: candidates = [1], target = 1
输出: [[1]]

示例 5：
输入: candidates = [1], target = 2
输出: [[1,1]]


提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
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
            # 如果最后一个元素(n-1)刚好是符合条件的，idx == n的判断会直接return，从而丢弃了该结果。
            # 使用target < candidates[idx]，相比使用target < 0，可以大大减少运行时间。要多注意剪枝
            if idx == n or target < candidates[idx]:
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

    def combinationSum_2(self, candidates: List[int], target: int) -> List[List[int]]:

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
    print(Solution().combinationSum(candidates=[2, 3, 5], target=8))

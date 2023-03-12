# -*- coding: UTF-8 -*-
"""
title: 获得分数的方法数
There is a test that has n types of questions. You are given an integer target and a 0-indexed 2D integer array types where types[i] = [counti, marksi] indicates that there are counti questions of the ith type, and each one of them is worth marksi points.
Return the number of ways you can earn exactly target points in the exam. Since the answer may be too large, return it modulo 10^9 + 7.
Note that questions of the same type are indistinguishable.
    For example, if there are 3 questions of the same type, then solving the 1st and 2nd questions is the same as solving the 1st and 3rd questions, or the 2nd and 3rd questions.


Example 1:
Input: target = 6, types = [[6,1],[3,2],[2,3]]
Output: 7
Explanation: You can earn 6 points in one of the seven ways:
- Solve 6 questions of the 0th type: 1 + 1 + 1 + 1 + 1 + 1 = 6
- Solve 4 questions of the 0th type and 1 question of the 1st type: 1 + 1 + 1 + 1 + 2 = 6
- Solve 2 questions of the 0th type and 2 questions of the 1st type: 1 + 1 + 2 + 2 = 6
- Solve 3 questions of the 0th type and 1 question of the 2nd type: 1 + 1 + 1 + 3 = 6
- Solve 1 question of the 0th type, 1 question of the 1st type and 1 question of the 2nd type: 1 + 2 + 3 = 6
- Solve 3 questions of the 1st type: 2 + 2 + 2 = 6
- Solve 2 questions of the 2nd type: 3 + 3 = 6

Example 2:
Input: target = 5, types = [[50,1],[50,2],[50,5]]
Output: 4
Explanation: You can earn 5 points in one of the four ways:
- Solve 5 questions of the 0th type: 1 + 1 + 1 + 1 + 1 = 5
- Solve 3 questions of the 0th type and 1 question of the 1st type: 1 + 1 + 1 + 2 = 5
- Solve 1 questions of the 0th type and 2 questions of the 1st type: 1 + 2 + 2 = 5
- Solve 1 question of the 2nd type: 5

Example 3:
Input: target = 18, types = [[6,1],[3,2],[2,3]]
Output: 1
Explanation: You can only earn 18 points by answering all questions.


Constraints:
1 <= target <= 1000
n == types.length
1 <= n <= 50
types[i].length == 2
1 <= counti, marksi <= 50
"""
from functools import lru_cache
from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        """排序 + DFS + 记忆化"""
        mod = 10 ** 9 + 7
        types.sort(key=lambda item: item[1])
        n = len(types)

        @lru_cache(None)
        def dfs(i: int, remain: int) -> int:
            if remain == 0:
                return 1
            if i == n or remain < types[i][1]:
                return 0
            cnt, mark = types[i]
            res = 0
            for c in range(cnt + 1):
                if remain < c * mark:
                    break
                res = (res + dfs(i + 1, remain - c * mark)) % mod
            return res

        return dfs(0, target)

    def waysToReachTarget_2(self, target: int, types: List[List[int]]) -> int:
        """
        动态规划。分组背包
        dp[i][j]表示使用前i种类型的题目恰好组成j分的方案数
        状态转移方程：dp[i][j] = sum(dp[i-1][j - k * mark_i])
        其中，j - k * mark_i >= 0 并且 0 <= k <= count_i
        因为dp[i]只与dp[i-1]有关，所以可使用滚动数组来优化空间复杂度
        """
        mod = 10 ** 9 + 7
        # 初始化。使用0种类型的题目时，只能组成0分，且只有一种方案
        dp = [1] + [0] * target
        for count, mark in types:
            # 组成0分只有一种方案，所以无需计算。必须逆序遍历
            for j in range(target, 0, -1):
                # k = 0时，就是dp[j]本身，因此无需计算
                for k in range(1, min(count, j // mark) + 1):
                    dp[j] = (dp[j] + dp[j - k * mark]) % mod
        return dp[-1]


if __name__ == '__main__':
    print(Solution().waysToReachTarget(target=6, types=[[6, 1], [3, 2], [2, 3]]))

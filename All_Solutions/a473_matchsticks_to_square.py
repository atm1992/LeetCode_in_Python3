# -*- coding: UTF-8 -*-
"""
title: 火柴拼正方形
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.


Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Constraints:
1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8
"""
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        回溯 + 贪心
        将给定数组划分为4个相等的子集，参考LeetCode题698
        """
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        n = len(matchsticks)
        # 贪心。优先使用长的火柴
        matchsticks.sort(reverse=True)
        edges = [total // 4] * 4

        def dfs(idx: int) -> bool:
            if idx == n:
                return True
            for i in range(4):
                edges[i] -= matchsticks[idx]
                if edges[i] >= 0 and dfs(idx + 1):
                    return True
                edges[i] += matchsticks[idx]
            return False

        return dfs(0)

    def makesquare_2(self, matchsticks: List[int]) -> bool:
        """
        状态压缩 + 动态规划
        对正方形的4条边进行编号，依次放满每条边，只有当前一条边放满后，才可以放下一条边。
        状态state表示已使用了哪些火柴，n = len(matchsticks)，总共有2^n种状态，0 表示未使用任何火柴，2^n - 1 表示使用了所有的火柴。
        dp[s] 表示正方形当前未放满的那条边的长度，当这条边的长度恰好等于total // 4时，就可以放下一条边了，此时dp[s]的值恢复为0
        """
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        edge = total // 4
        size = 1 << len(matchsticks)
        # dp[s] == -1 表示当前状态未计算过 或 当前状态下找不到合适的放置方案；dp[s] == 0 表示该状态下，恰好能放满m条边，m可取0、1、2、3、4。
        dp = [-1] * size
        # 未使用任何火柴的状态下，能放满0条边
        dp[0] = 0
        # 从状态1遍历到状态2^n - 1
        for s in range(1, size):
            # 对于每种状态，都需要遍历所有火柴，找到属于当前状态的火柴，并可将该火柴放入当前未放满的那条边中
            for idx, num in enumerate(matchsticks):
                # 先判断当前火柴是否属于当前状态s
                if s & (1 << idx) == 0:
                    continue
                # 除去当前火柴之外的前一个状态。状态转移：在状态pre_s的基础上，再放入当前火柴，就可得到当前状态s
                # 一个状态s有多少个状态pre_s，取决于状态s中有多少位1
                pre_s = s & ~(1 << idx)
                # 前一个状态需要是可行的，并且放入当前火柴后，长度必须小于等于edge
                # 因为s > pre_s，所以pre_s肯定已经被计算过了，但若dp[pre_s] == -1，则只能说明状态pre_s下找不到合适的放置方案
                if dp[pre_s] != -1 and dp[pre_s] + num <= edge:
                    # 对edge取模的原因：当dp[pre_s] + num == edge时，将dp[s]的值恢复为0，准备放下一条边
                    dp[s] = (dp[pre_s] + num) % edge
                    # 剪枝
                    # 找到一种符合要求的火柴放置方案后，就不用再继续计算当前状态了。
                    # 因为题目问的是能否找到一种放置方案，并没要求找到所有的放置方案，所以只要计算得到的当前状态符合要求就行了
                    break
        # 使用完所有的火柴之后，需要是恰好放满4条边。
        return dp[-1] == 0

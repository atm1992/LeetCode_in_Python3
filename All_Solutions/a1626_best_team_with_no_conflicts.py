# -*- coding: UTF-8 -*-
"""
title: 无矛盾的最佳球队
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.
However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.
Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.


Example 1:
Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.

Example 2:
Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

Example 3:
Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players.


Constraints:
1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 10^6
1 <= ages[i] <= 1000
"""
from collections import defaultdict
from typing import List


class BIT:
    def __init__(self, max_age: int):
        self.max_age = max_age
        self.age2max_dp = defaultdict(int)

    def low_bit(self, idx: int) -> int:
        # 负数的补码为其绝对值的原码按位取反(符号位除外)，然后加1
        return idx & -idx

    def update(self, age: int, max_dp: int) -> None:
        # 从子节点向父节点更新
        while age <= self.max_age:
            self.age2max_dp[age] = max(self.age2max_dp[age], max_dp)
            age += self.low_bit(age)

    def get_range_max(self, age: int) -> int:
        # 获取 [1, age] 范围内的最大dp值
        max_dp = 0
        while age >= 1:
            max_dp = max(max_dp, self.age2max_dp[age])
            age -= self.low_bit(age)
        return max_dp


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        排序 + 动态规划 + 哈希表
        dp[i]表示排序后以第i个球员结尾的无矛盾球队的分数
        先按scores升序，再按ages升序。然后从前往后遍历时，就无需考虑score，因为当前球员的score肯定大于等于之前所有球员的score，
        此时只需考虑age，找到之前分数最高的且age小于等于当前球员的dp[j]，然后 dp[i] = dp[j] + scores[i]
        只需记录各个age对应的最大dp值，所以可使用哈希表。最终结果为哈希表中的最大dp值
        """
        res = 0
        # 1 <= ages[i]
        age2max_dp = {0: 0}
        for score, age in sorted(zip(scores, ages)):
            cur = max(m for a, m in age2max_dp.items() if a <= age) + score
            # cur肯定会大于原来的age2max_dp[age]。因为cur是在小于等于当前age的最大dp值的基础上加score，并且题目已知 1 <= scores[i]
            age2max_dp[age] = cur
            res = max(res, cur)
        return res

    def bestTeamScore_2(self, scores: List[int], ages: List[int]) -> int:
        """
        排序 + 动态规划 + 树状数组。参考LeetCode题307
        方法一中查找[1, age]范围内的最大dp值，可使用线段树或树状数组来优化，将查找的时间复杂度从O(n)降到O(logn)
        """
        res = 0
        bit = BIT(max(ages))
        for score, age in sorted(zip(scores, ages)):
            cur = bit.get_range_max(age) + score
            bit.update(age, cur)
            res = max(res, cur)
        return res


if __name__ == '__main__':
    print(Solution().bestTeamScore_2(scores=[1, 2, 3, 5], ages=[8, 9, 10, 1]))

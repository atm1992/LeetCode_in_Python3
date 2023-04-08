# -*- coding: utf-8 -*-
# @date: 2023/4/8
# @author: liuquan
"""
title: 最小的必要团队
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.
Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.
    For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.
It is guaranteed an answer exists.


Example 1:
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]

Example 2:
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]


Constraints:
1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] consists of lowercase English letters.
All the strings of req_skills are unique.
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] consists of lowercase English letters.
All the strings of people[i] are unique.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
"""
from functools import lru_cache
from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """
        0-1背包 + 状态压缩 + 记忆化搜索
        dp[i][j]表示从前i个people中选出满足技能集合j的最小团队
        状态转移方程：
        1、若不选择people[i]，则 dp[i][j] = dp[i-1][j]
        2、若选择people[i]，则 dp[i][j] = dp[i-1][j - people[i]] ∪ {i}。j - people[i] 表示技能集合j中除去people[i]的技能后的技能子集，
        然后将people[i]加入到团队dp[i-1][j - people[i]]中
        综上，dp[i][j] = min(dp[i-1][j], dp[i-1][j - people[i]] ∪ {i})，选择人数更少的那个团队作为dp[i][j]
        代码实现上，可使用记忆化搜索
        """
        n, m = len(req_skills), len(people)
        target = (1 << n) - 1
        skill2r_idx = {s: i for i, s in enumerate(req_skills)}
        p2s = []
        for i, p in enumerate(people):
            state = 0
            for s in p:
                state |= 1 << skill2r_idx[s]
            if state == target:
                return [i]
            p2s.append(state)

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            """
            :param i: 在people[0:i+1]中选择人员
            :param j: 状态压缩后的所需技能集合
            :return: 满足上述技能集合的状态压缩后的最小团队
            """
            # 若所需技能集合为空，则无需选择任何人员
            if j == 0:
                return 0
            # 若没有可选人员，则无法满足所需的非空技能集合，因为最终结果是取较小值，所以这里可以返回一个最大值(选择所有people)
            if i < 0:
                return (1 << m) - 1
            r1 = dfs(i - 1, j)
            # j & ~p2s[i] 先将people[i]的技能按位取反，然后再和技能集合j进行按位与，得到技能集合j中除去people[i]的技能后的技能子集
            r2 = dfs(i - 1, j & ~p2s[i]) | (1 << i)
            return r1 if r1.bit_count() <= r2.bit_count() else r2

        tmp = dfs(m - 1, target)
        res, i = [], 0
        while tmp:
            if tmp & 1:
                res.append(i)
            i += 1
            tmp >>= 1
        return res


if __name__ == '__main__':
    print(Solution().smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                            people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
                                                    ["java", "csharp", "aws"], ["reactjs", "csharp"],
                                                    ["csharp", "math"], ["aws", "java"]]))

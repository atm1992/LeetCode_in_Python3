# -*- coding: UTF-8 -*-
"""
title: 搜寻名人
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) that tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.


Example 1:
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.


Constraints:
n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1

Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?
"""


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        """贪心算法。最多调用3n - 3次knows"""
        candidate = 0
        # 找到有可能为名人的那位，用candidate指向他
        for i in range(1, n):
            # 能从1走到i，就证明 1 ~ i-1，是candidate不知道的，也就意味着 1 ~ i-1 肯定不是名人
            # 现在candidate知道了 i，就说明candidate肯定也不是名人。现在唯一有可能是名人的就剩i了
            if knows(candidate, i):
                candidate = i
        # 最后验证candidate到底是不是名人
        for i in range(n):
            # 本人无需验证
            if i == candidate:
                continue
            # 如果有人不知道candidate，或者candidate知道其他人，那说明candidate也不是名人
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        return candidate

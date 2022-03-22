# -*- coding: UTF-8 -*-
"""
title: 分割回文串
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.


Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        动态规划预处理，避免使用双指针产生重复计算，状态转移方程为：f(i,j) 表示 s[i..j] 是否为回文串，i>=j时，f(i,j) = True；i<j时，f(i,j) = f(i+1,j-1) & (s[i] == s[j])。
        回溯：从 i 开始，从小到大依次枚举 j，判断当前的s[i..j]是否为回文串，若是，则加入子数组item，然后将j+1作为新的i进行下一层搜索，并在未来回溯时，将 s[i..j] 从子数组item中移除
        """
        n = len(s)
        dp = [[True] * n for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # dp[i+1][j-1] 是 dp[i][j] 左下角，所以i要从下往上计算，先计算出下面的行，再去计算上一行时，就可以直接使用之前的计算结果
                # 因为i>=j时，结果均为默认值True，所以只需计算(0,0) ——> (n-1,n-1)对角线以上的部分
                # 至于j是从前往后还是从后往前，其实无所谓
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
        res = []
        item = []

        def dfs(i: int = 0) -> None:
            if i == n:
                res.append(item[:])
                return
            # 注意：j是从i开始，因为单个字符也是回文
            for j in range(i, n):
                if dp[i][j]:
                    # res中的第一个item中一定都是单个字符；第二个item中的前面元素都是单个字符，只有最后一个元素是多字符组成的回文
                    item.append(s[i:j + 1])
                    dfs(j + 1)
                    # 回溯
                    item.pop()

        dfs()
        return res

    def partition_2(self, s: str) -> List[List[str]]:
        """
        使用记忆化搜索代替上面的动态规划预处理，然后再使用回溯得到所有结果
        """
        n = len(s)
        # 默认值0表示未搜索，1表示是回文串，-1表示不是回文串
        dp = [[0] * n for _ in range(n)]
        res = []
        item = []

        # 记忆化搜索
        def is_palindrome(i: int, j: int) -> int:
            # 不为0，说明已经搜索过
            if dp[i][j]:
                return dp[i][j]
            if i >= j:
                dp[i][j] = 1
            else:
                dp[i][j] = is_palindrome(i + 1, j - 1) if s[i] == s[j] else -1
            return dp[i][j]

        def dfs(i: int = 0) -> None:
            if i == n:
                res.append(item[:])
                return
            for j in range(i, n):
                if is_palindrome(i, j) == 1:
                    item.append(s[i:j + 1])
                    dfs(j + 1)
                    item.pop()

        dfs()
        return res


if __name__ == '__main__':
    print(Solution().partition_2("aab"))

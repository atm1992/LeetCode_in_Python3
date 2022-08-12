# -*- coding: UTF-8 -*-
"""
title: 编辑距离
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """动态规划。要将word1 转换为 word2，可理解为将word1和word2变为一样。假设dp[i][j]表示word1的前i个字符与word2的前j个字符之间的编辑距离(操作次数)。
        因为只有3种操作：一、在word1中插入一个字符(等同于在word2中删除一个字符)；二、在word1中删除一个字符(等同于在word2中插入一个字符)；
        三、在word1中替换一个字符。
        dp[i-1][j] ——> dp[i][j] 表示在word2的第j个字符后面插入一个与word1的第i个字符相同的字符，等同于在word1中删除一个字符；
        dp[i][j-1] ——> dp[i][j] 表示在word1的第i个字符后面插入一个与word2的第j个字符相同的字符；
        dp[i-1][j-1] ——> dp[i][j] 表示将word1的第i个字符替换为word2的第j个字符，注意：若word1的第i个字符与word2的第j个字符原本就相同，则无需替换。
        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        因为状态转移方程只涉及到 i-1、i 这两行，所以dp数组可以只保存两行。
        又因为最终结果是要让word1和word2变为一样，所以交换这两个word的位置，并不影响最终结果，可以选择将长度更小的那个作为word2，从而减小列数，进一步降低空间复杂度。
        """
        if len(word2) > len(word1):
            return self.minDistance(word2, word1)
        m, n = len(word1), len(word2)
        # 一个空字符串 与 一个非空字符串，它们之间的编辑距离为非空字符串的长度。所以row=0与col=0时，dp值无需计算。每次都只需更新dp数组第2行的值。
        # 因为m>=n，所以m=0时，n必为0，结果为0 = dp[0][0] = dp[-1][-1]。
        # m > 0时，会进入下面的for循环，结果为dp[-1][-1]。所以最后直接返回dp[-1][-1]即可
        dp = [list(range(n + 1)), [0] * (n + 1)]
        for row in range(1, m + 1):
            for col in range(n + 1):
                if col == 0:
                    dp[1][col] = row
                else:
                    dp[1][col] = min(dp[0][col] + 1, dp[1][col - 1] + 1,
                                     dp[0][col - 1] + int(word1[row - 1] != word2[col - 1]))
            dp[0] = dp[1][:]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance(word1="intention", word2="execution"))

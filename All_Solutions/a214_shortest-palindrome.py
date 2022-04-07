# -*- coding: UTF-8 -*-
"""
title: 最短回文串
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.


Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"


Constraints:
0 <= s.length <= 5 * 10^4
s consists of lowercase English letters only.
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        问题可转化为寻找以首字母开头的最长回文串。参考题5
        暴力枚举的时间复杂度为O(n^2)
        动态规划的时间复杂度为O(n^2)
        中心扩展算法的时间复杂度为O(n^2)
        由于s.length 最大可为 5 * 10^4，因此，O(n^2)的算法都会超时。
        Rabin-Karp字符串哈希算法的时间复杂度为O(n)，不过可能会产生哈希碰撞(概率很低)，从而导致错误的判断结果。在工程代码中，不建议这么做
        KMP算法的时间复杂度为O(n)。
        方法一：暴力枚举。实测可以通过
        """
        end = 0
        n = len(s)
        for i in range(n - 1, 0, -1):
            if s[:i + 1] == s[i::-1]:
                end = i
                break
        return s[:end:-1] + s


if __name__ == '__main__':
    print(Solution().shortestPalindrome("abcd"))

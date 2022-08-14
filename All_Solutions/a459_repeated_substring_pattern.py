# -*- coding: UTF-8 -*-
"""
title: 重复的子字符串
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.


Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        枚举
        假设原字符串的长度为n，子字符串的长度为m，则n必须是m的整数倍，倍数 > 1。即 1 <= m <= n//2
        枚举原字符串的所有前缀，前缀长度m的范围为：[1, n//2]
        """
        n = len(s)
        for m in range(1, n // 2 + 1):
            # n必须是m的整数倍
            if n % m != 0:
                continue
            if all(s[i] == s[i - m] for i in range(m, n)):
                return True
        return False

    def repeatedSubstringPattern_2(self, s: str) -> bool:
        """
        字符串匹配
        假设t = s + s，若在t中查找s的开始下标为i，且i不等于0和n（i等于0和n时，肯定能匹配到s），则认为s可由重复子串拼接而成。
        t中以下标i起始的字符串要等于s(长度为n)，则i必须满足：0 < i < n
        验证过程如下：
        s[0:n] == t[i:i+n] == t[i:n] + t[n:i+n] == s[i:n] + s[0:i]
        相当于把s的前缀s[0:i]移到了末尾，然后仍等于s
        即 在对n取模的情况下，s[j] == s[j+i]
        可得，s[j] == s[j+i] == s[j+i + i] == s[j+i + i * 2] == ……
        说明s可由子串s[0:i]重复拼接而成，s[0:i]是s中的最短重复子串
        """
        # 在t中从下标1开始查找s，查找结果不能是len(s)
        # find方法会返回第一次出现的下标，一定不会返回-1，因为起始下标为len(s)时，肯定能匹配到s
        return (s + s).find(s, 1) != len(s)

    def repeatedSubstringPattern_3(self, s: str) -> bool:
        """
        KMP算法
        KMP算法中的next数组可得到s中最长相等前后缀的长度，假设最长前缀(最长后缀)的长度为i，即 s[0:i] == s[n-i:n]
        当一个字符串是由重复子串拼接而成时，它的最短重复子串就是最长前缀(最长后缀)不包含的部分，即 s[i:n] == s[0:n-i]
        因为如果字符串是由a个重复子串拼接而成，那么最长前缀(最长后缀)必然是由 b = a-1 个重复子串拼接而成。
        所以当字符串的长度是最短重复子串长度的整数倍时，该字符串就可由这个最短重复子串拼接而成。
        """
        n = len(s)
        nxt = [0] * n
        cur = 0
        for i in range(1, n):
            while cur > 0 and s[cur] != s[i]:
                cur = nxt[cur - 1]
            if s[cur] == s[i]:
                cur += 1
                nxt[i] = cur
        return nxt[-1] > 0 and n % (n - nxt[-1]) == 0


if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern_3("abab"))

# -*- coding: UTF-8 -*-
"""
title: 字符串的总引力
The appeal of a string is the number of distinct characters found in the string.
    For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.
A substring is a contiguous sequence of characters within a string.


Example 1:
Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
The total sum is 5 + 7 + 7 + 6 + 3 = 28.

Example 2:
Input: s = "code"
Output: 20
Explanation: The following are the substrings of "code":
- Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
- Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
- Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 4: "code" has an appeal of 4. The sum is 4.
The total sum is 4 + 6 + 6 + 4 = 20.


Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


class Solution:
    def appealSum(self, s: str) -> int:
        """
        动态规划。
        假设 dp[i] 表示以字符s[i]结尾的子字符串(从0开始, 长度为i+1)的总引力，那么 dp[i-1] 就表示以字符s[i-1]结尾的子字符串(从0开始, 长度为i)的总引力。
        将字符s[i]添加到以字符s[i-1]结尾的子字符串(从0开始, 长度为i)之后，将会影响到所有以字符s[i-1]结尾的子字符串(不一定从0开始, 长度小于等于i)的引力。
        若字符s[i]在以字符s[i-1]结尾的子字符串(从0开始, 长度为i)中未曾出现过，那么增加的引力为：i + 1，以字符s[i-1]结尾的子字符串共有i个，最后加上字符s[i]单独组成的子字符串；
        若字符s[i]在以字符s[i-1]结尾的子字符串(从0开始, 长度为i)中最后一次出现的下标为j，那么增加的引力为：i - 1 - j + 1，以字符s[i-1]结尾的子字符串(当中不含字符s[i])共有i - 1 - j个，最后加上字符s[i]单独组成的子字符串。
        由上可知，dp[i] 仅与 dp[i-1] 有关。
        """
        # 记录26个小写字母各自最后出现的下标。若未出现过，则将下标看作 -1。从而将上述两种情况的表达式合并为 i - j，因为 i - (-1) == i + 1
        last_idx = [-1] * 26
        res = pre = 0
        for idx, ch in enumerate(s):
            ch_idx = ord(ch) - ord('a')
            pre += idx - last_idx[ch_idx]
            res += pre
            last_idx[ch_idx] = idx
        return res


if __name__ == '__main__':
    print(Solution().appealSum(s="aa"))

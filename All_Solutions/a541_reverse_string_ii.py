# -*- coding: UTF-8 -*-
"""
title: 反转字符串 II
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.


Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"


Constraints:
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^4
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """双指针"""
        s = list(s)
        i, n = 0, len(s)
        while i < n:
            left, right = i, min(i + k - 1, n - 1)
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            i += 2 * k
        return ''.join(s)


if __name__ == '__main__':
    print(Solution().reverseStr(s="abcdefg", k=2))

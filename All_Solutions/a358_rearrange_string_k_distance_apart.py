# -*- coding: UTF-8 -*-
"""
title: K 距离间隔重排字符串
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".


Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.

Example 3:
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.


Constraints:
1 <= s.length <= 3 * 10^5
s consists of only lowercase English letters.
0 <= k <= s.length
"""


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        pass

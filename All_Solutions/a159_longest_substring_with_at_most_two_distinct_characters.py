# -*- coding: UTF-8 -*-
"""
title: 至多包含两个不同字符的最长子串
Given a string s, return the length of the longest substring that contains at most two distinct characters.


Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.


Constraints:
1 <= s.length <= 10^5
s consists of English letters.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        滑动窗口。
        滑动窗口 .vs. 双指针
        1、滑动窗口：两个指针的移动方向相同
        2、双指针：两个指针的移动方向相反
        """
        n = len(s)
        left = right = 0
        ch2lastidx = {}
        res = 0
        while right < n:
            ch2lastidx[s[right]] = right
            if len(ch2lastidx) == 3:
                min_idx = min(ch2lastidx.values())
                ch2lastidx.pop(s[min_idx])
                left = min_idx + 1
            right += 1
            res = max(res, right - left)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringTwoDistinct(s="abcabcabc"))

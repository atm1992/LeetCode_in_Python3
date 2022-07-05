# -*- coding: UTF-8 -*-
"""
title: 替换后的最长重复字符
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        双指针(变长滑动窗口)。滑动窗口的长度要么保持(记录曾经的最大长度)，要么加1(right指向的字符属于max_cnt)。
        最终返回结果就是滑动窗口的长度。注意：最后一个滑动窗口内的所有字符未必是题目要求的最长重复字符。我们只是使用滑动窗口的长度来记录最终结果
        """
        ch2cnt = [0] * 26
        n = len(s)
        left = right = 0
        # 双指针范围内重复字符的最大出现次数，注意：这些重复字符不一定是连续的，因为可以通过k次替换来使这些非连续的重复字符变成连续的
        max_cnt = 0
        while right < n:
            idx = ord(s[right]) - ord('A')
            ch2cnt[idx] += 1
            max_cnt = max(max_cnt, ch2cnt[idx])
            # 注意：这里left只向右移动了一步，虽然删除的left字符可能会属于max_cnt，导致left右移一步后，依旧还是right - left + 1 - max_cnt == k + 1
            # 滑动窗口的长度能从初始值1(0-0+1)扩展到现在的(right - left + 1)，就说明曾经出现过的最长重复字符长度为right - left + 1，
            # 小于这个长度的字符串无需再考虑了，所以让滑动窗口维持曾经的最大长度。right - left + 1 - max_cnt 要么等于k+1，要么小于等于k
            if right - left + 1 - max_cnt == k + 1:
                ch2cnt[ord(s[left]) - ord('A')] -= 1
                left += 1
            right += 1
        # 因为退出上述while循环时，right == n，所以这里return的是right - left，而不是right - left + 1
        return right - left


if __name__ == '__main__':
    print(Solution().characterReplacement(s="AABABBA", k=1))

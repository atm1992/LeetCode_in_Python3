# -*- coding: UTF-8 -*-
"""
title: 字符串的排列
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.


Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """滑动窗口"""
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        # 26个小写字母
        diff_cnt = [0] * 26
        # 初始化一个长度为n1的滑动窗口
        for i in range(n1):
            diff_cnt[ord(s1[i]) - ord('a')] -= 1
            diff_cnt[ord(s2[i]) - ord('a')] += 1
        # 对于长度相等的两个字符串，只有完全相同，diff_cnt才会都为0，len才为1。否则diff_cnt中既有正数、又有负数
        if len(set(diff_cnt)) == 1:
            return True
        for i in range(n1, n2):
            diff_cnt[ord(s2[i]) - ord('a')] += 1
            diff_cnt[ord(s2[i - n1]) - ord('a')] -= 1
            if len(set(diff_cnt)) == 1:
                return True
        return False

    def checkInclusion_2(self, s1: str, s2: str) -> bool:
        """双指针"""
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        diff_cnt = [0] * 26
        for i in range(n1):
            diff_cnt[ord(s1[i]) - ord('a')] -= 1
        left = 0
        for right in range(n2):
            cnt_idx = ord(s2[right]) - ord('a')
            diff_cnt[cnt_idx] += 1
            while diff_cnt[cnt_idx] > 0:
                diff_cnt[ord(s2[left]) - ord('a')] -= 1
                left += 1
            # 不会存在 s1 = 'ara', s2 = 'aea' 返回True。因为在right指向s2的'e'时，就会通过上面的while循环来移动left指向'e'后面的'a'
            if right - left + 1 == n1:
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion_2(s1="ab", s2="eidbaooo"))

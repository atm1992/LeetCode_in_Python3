# -*- coding: UTF-8 -*-
"""
title: 至多包含 K 个不同字符的最长子串
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.


Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.


Constraints:
1 <= s.length <= 5 * 10^4
0 <= k <= 50
"""
from collections import defaultdict, OrderedDict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """滑动窗口 + 哈希表。使用哈希表记录各个字符最后出现的下标，而不是记录各个字符的出现次数"""
        if k == 0:
            return 0
        res = 0
        ch2idx = defaultdict(int)
        left = 0
        for i in range(len(s)):
            ch2idx[s[i]] = i
            if len(ch2idx) == k + 1:
                # 这里的时间复杂度为O(k)
                del_idx = min(ch2idx.values())
                ch2idx.pop(s[del_idx])
                left = del_idx + 1
            res = max(res, i - left + 1)
        return res

    def lengthOfLongestSubstringKDistinct_2(self, s: str, k: int) -> int:
        """滑动窗口 + 有序字典OrderedDict。有序字典可以记住插入时的顺序"""
        if k == 0:
            return 0
        res = 0
        ch2idx = OrderedDict()
        left = 0
        for i in range(len(s)):
            ch = s[i]
            # 先删除，再插入，是为了将新插入的ch放到有序字典的最右侧
            if ch in ch2idx:
                ch2idx.pop(ch)
            ch2idx[ch] = i
            if len(ch2idx) == k + 1:
                # 删除有序字典中最左侧的item。这里的时间复杂度为O(1)
                # popitem(last=False) 表示删除第一个加入的；popitem() 表示删除最后加入的
                _, del_idx = ch2idx.popitem(last=False)
                left = del_idx + 1
            res = max(res, i - left + 1)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringKDistinct(s="abaccc", k=2))

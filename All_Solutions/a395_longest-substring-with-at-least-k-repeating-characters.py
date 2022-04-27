# -*- coding: UTF-8 -*-
"""
title: 至少有 K 个重复字符的最长子串
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.


Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^5
"""
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """分治。先从s中找出一个出现次数小于k的字符，然后用该字符去分割s，因为所求的最长子串中不可能会包含该字符"""

        def dfs(s: str) -> int:
            split_ch = ''
            for ch, cnt in Counter(s).items():
                if cnt < k:
                    split_ch = ch
                    break
            if not split_ch:
                return len(s)
            tmp_res = 0
            for sub_s in s.split(split_ch):
                if len(sub_s) <= tmp_res:
                    continue
                tmp_res = max(tmp_res, dfs(sub_s))
            return tmp_res

        if len(s) < k:
            return 0
        return dfs(s)

    def longestSubstring_2(self, s: str, k: int) -> int:
        """滑动窗口。不如上面的方法"""
        n = len(s)
        res = 0
        if n < k:
            return res
        # limit_class 表示当前大循环查找的最长子串中最多允许出现的字符种类，最多26种不同的字符，因为小写字母只有26种
        for limit_class in range(1, 27):
            left, right = 0, 0
            cnt = [0] * 26
            # actual_class 表示实际出现的字符种类数量；less 表示出现次数小于k的字符数量
            actual_class = 0
            less = 0
            while right < n:
                cnt_idx_r = ord(s[right]) - ord('a')
                cnt[cnt_idx_r] += 1
                # 表示在滑动窗口中增加了一种新的字符
                if cnt[cnt_idx_r] == 1:
                    actual_class += 1
                    less += 1
                if cnt[cnt_idx_r] == k:
                    less -= 1
                while actual_class > limit_class:
                    cnt_idx_l = ord(s[left]) - ord('a')
                    cnt[cnt_idx_l] -= 1
                    if cnt[cnt_idx_l] == k - 1:
                        less += 1
                    # 表示在滑动窗口中减少了一种字符
                    if cnt[cnt_idx_l] == 0:
                        actual_class -= 1
                        less -= 1
                    left += 1
                if less == 0:
                    res = max(res, right - left + 1)
                right += 1
        return res


if __name__ == '__main__':
    print(Solution().longestSubstring_2(s="ababbc", k=2))

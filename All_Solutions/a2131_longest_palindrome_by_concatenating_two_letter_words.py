# -*- coding: UTF-8 -*-
"""
title: 连接两字母单词得到的最长回文串
You are given an array of strings words. Each element of words consists of two lowercase English letters.
Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
A palindrome is a string that reads the same forward and backward.


Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".


Constraints:
1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """贪心 + 哈希表"""
        word2cnt = Counter(words)
        res = 0
        add_center = False
        for word, cnt in word2cnt.items():
            # 叠词
            if word[0] == word[1]:
                # 因为每个word的长度均为2，所以最后需要乘以2
                res += (cnt // 2 * 2) * 2
                # 可以从奇数个的叠词中任选一个作为回文中心
                if not add_center and cnt & 1:
                    res += 2
                    add_center = True
            # 存在对称的非叠词
            elif word[1] + word[0] in word2cnt:
                # 之后遍历遇到word[1] + word[0]时，会再加一次。假设word都放在左侧，而word[1] + word[0]都放在右侧
                res += min(cnt, word2cnt[word[1] + word[0]]) * 2
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome(words=["lc", "cl", "gg"]))

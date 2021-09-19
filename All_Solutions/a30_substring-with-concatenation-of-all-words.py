# -*- coding: UTF-8 -*-
"""
title: 串联所有单词的子串
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
You can return the answer in any order.


Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:
1 <= s.length <= 10^4
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """滑动窗口"""
        res = []
        words_count = {}
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1
        n = len(s)
        m = len(words[0])
        cnt = len(words)
        if n < m * cnt:
            return res
        for i in range(m):
            # 滑动窗口的左右边界
            left = right = i
            tmp = {}
            # tmp中所有单词的次数累加。最后通过比较tmp_cnt和cnt来决定是否匹配，而不是比较words_count和tmp
            tmp_cnt = 0
            while left <= n - m * cnt and right <= n - m * (cnt - tmp_cnt):
                w = s[right:right + m]
                right += m
                if w not in words_count:
                    # 抛弃掉之前的所有结果
                    left = right
                    tmp = {}
                    tmp_cnt = 0
                else:
                    tmp[w] = tmp.get(w, 0) + 1
                    tmp_cnt += 1
                    # 移动left，从滑动窗口的左边逐个删除单词
                    while tmp[w] > words_count[w]:
                        left_w = s[left:left + m]
                        tmp[left_w] -= 1
                        tmp_cnt -= 1
                        left += m
                    if tmp_cnt == cnt:
                        res.append(left)
        return res


if __name__ == '__main__':
    print(Solution().findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))

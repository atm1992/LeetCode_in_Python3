# -*- coding: UTF-8 -*-
"""
title: 查找共用字符
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.


Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """计数"""
        ch2min_freq = None
        for word in words:
            # 注意：这里不能写成 if not ch2min_freq
            if ch2min_freq is None:
                ch2min_freq = Counter(word)
            elif not ch2min_freq:
                return []
            else:
                # 取交集
                ch2min_freq &= Counter(word)
        res = []
        for ch, cnt in ch2min_freq.items():
            res.extend([ch] * cnt)
        return res


if __name__ == '__main__':
    print(Solution().commonChars(words=["bella", "label", "roller"]))

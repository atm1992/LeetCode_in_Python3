# -*- coding: UTF-8 -*-
"""
title: 前K个高频单词
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.


Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


Constraints:
1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """哈希表 + 自定义排序"""

        def mycmp(a: str, b: str) -> int:
            if word2cnt[a] != word2cnt[b]:
                # 根据cnt降序
                return word2cnt[b] - word2cnt[a]
            for i in range(min(len(a), len(b))):
                # 按字典序升序
                if a[i] < b[i]:
                    return -1
                elif a[i] > b[i]:
                    return 1
            # 若一个字符串是另一个字符串的前缀，则按长度升序
            return len(a) - len(b)

        word2cnt = Counter(words)
        # res = sorted(word2cnt.keys(), key=cmp_to_key(mycmp))
        res = sorted(word2cnt.keys(), key=lambda word: (-word2cnt[word], word))
        return res[:k]


if __name__ == '__main__':
    print(Solution().topKFrequent(words=["i", "love", "cod", "i", "love", "coding"], k=3))

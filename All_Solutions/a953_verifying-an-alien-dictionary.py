# -*- coding: UTF-8 -*-
"""
title: 验证外星语词典
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.


Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ch2idx = {}
        for idx, ch in enumerate(order):
            ch2idx[ch] = idx
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            n1, n2 = len(w1), len(w2)
            flag = False
            for j in range(min(n1, n2)):
                ch1, ch2 = w1[j], w2[j]
                if ch1 != ch2:
                    if ch2idx[ch1] > ch2idx[ch2]:
                        return False
                    flag = True
                    break
            if not flag and n1 > n2:
                return False
        return True

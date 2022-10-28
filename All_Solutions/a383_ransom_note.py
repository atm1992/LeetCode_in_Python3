# -*- coding: UTF-8 -*-
"""
title: 赎金信
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:
1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ch2cnt = Counter(magazine)
        for ch in ransomNote:
            if ch not in ch2cnt:
                return False
            ch2cnt[ch] -= 1
            if ch2cnt[ch] == 0:
                ch2cnt.pop(ch)
        return True

    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not Counter(ransomNote) - Counter(magazine)


if __name__ == '__main__':
    print(Solution().canConstruct_2(ransomNote="aa", magazine="aab"))

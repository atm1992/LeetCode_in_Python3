# -*- coding: utf-8 -*-
# @date: 2023/4/29
# @author: liuquan
"""
title: 删除字符使频率相同
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
Note:
    The frequency of a letter x is the number of times it occurs in the string.
    You must remove exactly one letter and cannot chose to do nothing.


Example 1:
Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

Example 2:
Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.


Constraints:
2 <= word.length <= 100
word consists of lowercase English letters only.
"""
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        """
        哈希表 + 排序 + 分情况讨论
        满足题目条件的有以下3种情况：
        1、只有一种字母，例如：[2]、[3]
        2、有两种及以上字母，第一个字母的cnt为1，其余字母的cnt相等，例如：[1, 1]、[1, 3]、[1, 1, 1]、[1, 3, 3]
        3、有两种及以上字母，最后一个字母的cnt比其余字母的cnt大1，例如：[1, 1, 2]、[2, 3]
        """
        cnts = sorted(Counter(word).values())
        return len(cnts) == 1 or (cnts[0] == 1 and cnts[1] == cnts[-1]) or cnts[0] == cnts[-2] == cnts[-1] - 1


if __name__ == '__main__':
    print(Solution().equalFrequency(word="abcc"))

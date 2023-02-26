# -*- coding: UTF-8 -*-
"""
title: 得分最高的单词集合
Given a list of words, list of single letters (might be repeating) and score of every character.
Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.


Example 1:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

Example 2:
Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.

Example 3:
Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.


Constraints:
1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
"""
from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        二进制枚举(状态压缩)
        因为单词数目不超过14，所以可以直接枚举所有的单词子集。用一个整数 state 来表示一个单词子集，若state的第k位二进制为1，则表示当前子集包含了words[k]。
        """
        n, res = len(words), 0
        ch2cnt = Counter(letters)
        word2cnt = [Counter(word) for word in words]
        # 总共有2^n个单词子集，不过无需考虑为空的那个子集
        for state in range(1, 1 << n):
            cur = Counter()
            for i in range(n):
                if (state >> i) & 1:
                    cur += word2cnt[i]
            if all(cnt <= ch2cnt.get(ch, 0) for ch, cnt in cur.items()):
                res = max(res, sum(score[ord(ch) - ord('a')] * cnt for ch, cnt in cur.items()))
        return res

    def maxScoreWords_2(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """回溯。执行效率远高于方法一"""
        from typing import Counter as Typing_Counter
        n, res = len(words), 0
        word2cnt = [Counter(word) for word in words]

        def dfs(i: int, ch2cnt: Typing_Counter) -> int:
            if i == n:
                return 0
            # 不选word[i]
            res = dfs(i + 1, ch2cnt)
            # 选择word[i]
            # 若word[i]可以被选择
            if all(cnt <= ch2cnt.get(ch, 0) for ch, cnt in word2cnt[i].items()):
                res = max(res, sum(score[ord(ch) - ord('a')] * cnt for ch, cnt in word2cnt[i].items())
                          + dfs(i + 1, ch2cnt - word2cnt[i]))
            return res

        return dfs(0, Counter(letters))


if __name__ == '__main__':
    print(Solution().maxScoreWords_2(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"],
                                     score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
                                            10]))

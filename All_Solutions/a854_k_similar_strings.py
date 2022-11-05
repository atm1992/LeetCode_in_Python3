# -*- coding: UTF-8 -*-
"""
title: 相似度为 K 的字符串
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.
Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.


Example 1:
Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".

Example 2:
Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".


Constraints:
1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.
"""


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        """BFS + 剪枝。枚举所有可能的交换方案"""
        if s1 == s2:
            return 0
        res, n = 1, len(s1)
        queue, visited = [(s1, 0)], {s1}
        while True:
            tmp = queue
            queue = []
            for cur, i in tmp:
                while i < n and cur[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    # 剪枝。若cur[j] == s2[j]，则说明下标j的字符已经在最终位置了，因此就不要使用它进行交换了，使用它只会让交换次数变多
                    if cur[j] == s2[i] and cur[j] != s2[j]:
                        nxt = list(cur)
                        nxt[i], nxt[j] = nxt[j], nxt[i]
                        nxt = ''.join(nxt)
                        if nxt == s2:
                            return res
                        if nxt not in visited:
                            visited.add(nxt)
                            # 下一次从下标i+1开始交换nxt中的字符
                            queue.append((nxt, i + 1))
            res += 1


if __name__ == '__main__':
    print(Solution().kSimilarity(s1="abc", s2="bca"))

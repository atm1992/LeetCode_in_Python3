# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        words2 = words.copy()
        deleted = set()
        for i in range(n):
            words2[i] = ''.join(sorted(words2[i]))
            if i > 0 and words2[i] == words2[i-1]:
                deleted.add(i)
        res = []
        for i in range(n):
            if i not in deleted:
                res.append(words[i])
        return res


if __name__ == '__main__':
    print(Solution().removeAnagrams(words = ["a","b","c","d","e"]))







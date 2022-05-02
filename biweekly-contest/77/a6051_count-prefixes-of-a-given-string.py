# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for word in words:
            if s.startswith(word):
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countPrefixes(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))

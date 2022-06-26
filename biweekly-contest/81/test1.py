# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        for i, item in enumerate(s.split('|')):
            if i & 1 == 0:
                res += item.count('*')
        return res


if __name__ == '__main__':
    print(Solution().countAsterisks(s = "yo|uar|e**|b|e***au|tifu|l"))

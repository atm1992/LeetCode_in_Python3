# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        tmp = {}
        for item in rectangles:
            key = item[0] / item[1]
            tmp[key] = tmp.get(key, 0) + 1
        res = 0
        for item in tmp.values():
            res += sum(range(item))
        return res


if __name__ == '__main__':
    print(Solution().interchangeableRectangles([[4, 5], [7, 8]]))

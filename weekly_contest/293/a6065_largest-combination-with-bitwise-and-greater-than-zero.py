# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = [0] * 31
        for num in candidates:
            idx = 0
            while idx < 31 and num > 0:
                if num & 1:
                    res[idx] += 1
                num >>= 1
                idx += 1
        return max(res)


if __name__ == '__main__':
    print(Solution().largestCombination([8,8]))

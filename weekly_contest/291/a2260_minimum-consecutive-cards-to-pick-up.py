# -*- coding: UTF-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # 记录每个num最后出现的index
        num2idx = defaultdict(int)
        n = len(cards)
        res = n + 1
        for idx, num in enumerate(cards):
            if num in num2idx:
                tmp = idx - num2idx[num] + 1
                if tmp < res:
                    res = tmp
                if tmp == 2:
                    break
            num2idx[num] = idx
        return -1 if res == n + 1 else res


if __name__ == '__main__':
    print(Solution().minimumCardPickup(cards=[3, 4, 2, 3, 4, 7]))

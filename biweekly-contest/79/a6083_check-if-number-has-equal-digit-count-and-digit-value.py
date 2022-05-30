# -*- coding: UTF-8 -*-
from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        num2cnt = defaultdict(int)
        for ch in num:
            num2cnt[int(ch)] += 1
        for i in range(len(num)):
            if int(num[i]) != num2cnt[i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().digitCount('030'))

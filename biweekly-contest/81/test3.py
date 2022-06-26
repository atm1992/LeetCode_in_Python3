# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        max_num = max(nums)
        n = len(bin(max_num)) - 2
        cnt = [0] * n
        for num in nums:
            for i in range(n):
                if num & (1<<i):
                    cnt[i] += 1
        res = 2 ** n - 1
        for i in range(n):
            if cnt[i] == 0:
                res ^= 1 << i
        return res


if __name__ == '__main__':
    print(Solution().maximumXOR(nums = [1,2,3,9,2]))






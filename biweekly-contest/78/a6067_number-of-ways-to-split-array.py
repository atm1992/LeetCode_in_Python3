# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = nums.copy()
        for i in range(1, n):
            pre_sum[i] += pre_sum[i - 1]
        res = 0
        for i in range(n - 1):
            if pre_sum[i] >= pre_sum[n - 1] - pre_sum[i]:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().waysToSplitArray([2, 3, 1, 0]))
